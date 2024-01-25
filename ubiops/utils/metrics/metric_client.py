import hashlib
import logging
import os
import queue
import random
import threading
import time
import ubiops

from ubiops.exceptions import ApiException, UbiOpsException
from threading import Event

from .metric_utils import Metric, TimeSeries

logger = logging.getLogger("MetricClient")


class MetricClient(threading.Thread):
    """
    Thread for periodically pushing metrics to the API. The thread collects all new data points with the specified
    frequency and sends them to the API.
    """

    def __init__(self, project_name, api_client=None, insert_frequency=60, debug=False):
        """
        Initialize the metrics client.

        If no api_client is provided it will be inferred from the environment variables INT_API_URL and INT_API_TOKEN.

        :param str project_name: the name of the project to insert metrics to
        :param ApiClient api_client: a UbiOps ApiClient
        :param int insert_frequency: how often metrics are inserted via the UbiOps API in seconds
        :param bool debug: whether to log how many timeseries/data points are successfully inserted to the UbiOps API
        """

        # Configuring the thread as daemon ensures it won't prevent the process from shutting down.
        # It's recommended to stop the thread using metric_client.stop()
        threading.Thread.__init__(self, daemon=True)

        self.project_name = project_name
        self.api_client = api_client
        self.insert_frequency = insert_frequency
        self.debug = debug

        # Pick a random moment during every insert interval to avoid all clients inserting metrics at the same time
        self.insert_second = random.randint(0, insert_frequency)

        # Stop event
        self.stop_metrics = Event()

        # Initialize the client library
        if self.api_client is None:
            self._initialize_client()
        self.core_api = ubiops.CoreApi(api_client=self.api_client)

        self.timeseries = {}

        self.metrics_queue = queue.Queue()

    def _initialize_client(self):
        """
        Infer api_url and api_token from environment variables and initialize the client library with them
        """

        configuration = ubiops.Configuration()
        api_url = os.environ.get("INT_API_URL", "")
        api_token = os.environ.get("INT_API_TOKEN", "")

        if not api_url or not api_token:
            raise UbiOpsException(
                "Either an api_client or environment variables INT_API_URL and INT_API_TOKEN need to be provided"
            )

        # Configure API token authorization
        configuration.api_key["Authorization"] = api_token
        # Defining host is optional and default to "https://api.ubiops.com/v2.1"
        configuration.host = api_url

        self.api_client = ubiops.ApiClient(configuration=configuration)

    def stop(self, timeout=None):
        """
        Stop the thread

        :param int timeout: how many seconds to wait for the MetricClient time to insert the last metrics
        """

        self.stop_metrics.set()
        if timeout:
            self.join(timeout=timeout)
        else:
            # By default, wait for an entire interval with some additional delay for inserting the metrics
            self.join(timeout=self.insert_frequency + 5)

    def run(self):
        """
        Every <insert_frequency> seconds push available data points to the API
        """

        while not self.stop_metrics.is_set():
            current_time = int(time.time())
            sleep_until = (
                current_time + self.insert_frequency + self.insert_second - (current_time % self.insert_frequency)
            )

            # Wait till the event is set or the sleep expires
            self.stop_metrics.wait(timeout=max(sleep_until - int(time.time()), 0))

            # Process logged metrics and store them per timeseries
            while not self.metrics_queue.empty():
                metric = self.metrics_queue.get(block=False)
                timeseries = self.get_timeseries(metric=metric)
                timeseries.insert(metric=metric)

            # Process existing timeseries and convert them into a format suitable for the API
            data = []
            data_count = 0
            timeseries_names = []
            for identifier in list(self.timeseries.keys()):
                timeseries = self.timeseries.get(identifier)
                timeseries_values = timeseries.get_values_formatted()
                if timeseries_values:
                    data_count += len(timeseries_values.get("data", []))
                    data.append(timeseries_values)
                    timeseries_names.append(timeseries.get_name())
                else:
                    # Garbage collect unused timeseries
                    del self.timeseries[identifier]

            # Send timeseries data to the API
            if len(data) > 0:
                try:
                    self.core_api.time_series_data_aggregate(project_name=self.project_name, data=data)
                    if self.debug:
                        logger.info(
                            f"Logged {data_count} data point{'' if data_count == 1 else 's'} in total "
                            f"for metrics {timeseries_names}"
                        )

                except ApiException as e:
                    logger.warning(
                        f"Failed to log {data_count} data point{'' if data_count == 1 else 's'} in total "
                        f"for metrics {timeseries_names}: {e}"
                    )

    def get_timeseries(self, metric):
        """
        Get the timeseries for the given metric. Create a new timeseries if necessary

        :param Metric metric: the metric to use
        """

        timeseries = None
        identifier = self._get_timeseries_identifier(metric=metric)
        if identifier:
            timeseries = self.timeseries.get(identifier)
        if not timeseries:
            timeseries = TimeSeries(metric_name=metric.name, labels=metric.labels)
            self.timeseries[identifier] = timeseries
        return timeseries

    @staticmethod
    def _get_timeseries_identifier(metric):
        """
        Get a unique identifier for the timeseries. 'metric.name' may not be unique and exist for different labels.

        :param Metric metric: the metric to use

        :returns str the md5sum of the metric_name + labels
        """

        hash_string = metric.name
        for key in sorted(metric.labels):
            hash_string += f"{key}:{metric.labels[key]}"

        return hashlib.md5(string=hash_string.encode(encoding="utf-8")).hexdigest()

    def log_metric(self, metric_name, labels, value):
        """
        Method to insert metrics.

        Example
        ```
        metric_client = MetricClient(project_name="<my-project-name>")
        metric_client.start()

        metric_client.log_metric(metric_name="my-delta", labels={"version_id": "<version_id>"}, value=1.0)
        metric_client.stop()
        ```

        :param str metric_name: the name of the metric to use
        :param dict labels: the labels of the training run or inference request
        :param float value: the value to insert
        """

        self.metrics_queue.put(Metric(metric_name=metric_name, labels=labels, value=value))

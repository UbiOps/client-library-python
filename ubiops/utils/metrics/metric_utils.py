import datetime


class Metric:
    """
    The metric class represents a single measurement

    :param str metric_name: the name of the metric to be tracked
    :param dict labels: the labels to store the metric with
    :param float value: the value observed

    """

    def __init__(self, metric_name, labels, value):
        self.name = metric_name
        self.labels = labels
        self.timestamp = datetime.datetime.utcnow()
        self.value = value

    @property
    def name(self):
        """
        Get the metric name
        """

        return self._name

    @name.setter
    def name(self, metric_name):
        """
        Set the metric name
        """

        self._name = metric_name

    @property
    def labels(self):
        """
        Get the labels
        """

        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Set the labels

        :param dict labels: a dict of labels
        """

        if not isinstance(labels, dict):
            raise ValueError("'labels' must be a dictionary of key value pairs")

        for label_name, label_value in labels.items():
            self._validate_label(label_name=label_name, label_value=label_value)
        self._labels = labels

    @staticmethod
    def _validate_label(label_name, label_value):
        """
        Validate a single label

        :param str label_name: the name of the label
        :param str label_value: the value of the label
        :return: labels if valid
        """

        if not isinstance(label_name, str) or not isinstance(label_value, str):
            raise ValueError("Label name and value must be of type string")

    @property
    def timestamp(self):
        """
        Get the timestamp of the metric
        """

        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Set the timestamp of the metric
        """

        self._timestamp = timestamp

    @property
    def value(self):
        """
        Get the value of the metric
        """

        return self._value

    @value.setter
    def value(self, value):
        """
        Set the value of the metric
        """

        self._value = float(value)


class TimeSeries:
    """
    TimeSeries class defines a single TimeSeries that is being tracked.
    """

    def __init__(self, metric_name, labels):
        """
        The TimeSeries class stores metrics for the same metric_name, labels combination.

        :param str metric_name: the name of the metric to be tracked
        :param dict labels: the labels to store the metric with
        """

        self.metric_name = metric_name
        self.labels = labels

        self.metrics = []

    def get_name(self):
        """
        Get the name of the timeseries. It contains the metric name + labels.
        """

        return f"{self.metric_name} {self.labels}"

    def get_values(self):
        """
        Get value(s) from the metrics stored in memory

        :returns list[dict] in the shape
        ```
        [{
            "date": "2023-09-15T20:00:00.000+00:00",
            "value": 182
        },
        {
            "date": "2023-09-15T21:00:00.000+00:00",
            "value": 1
        }]
        ```
        """

        values = [{"date": metric.timestamp, "value": metric.value} for metric in self.metrics]
        self.metrics.clear()
        return values

    def get_values_formatted(self):
        """
        Get averaged value(s) from the metrics stored in memory in a format accepted by the UbiOps API

        :returns dict in the shape
        ```
        {
            "metric": "custom.my_metric",
            "labels": {},
            "data": [
                {
                    "date": "2023-09-15T20:00:00.000+00:00",
                    "value": 182
                },
                {
                    "date": "2023-09-15T21:00:00.000+00:00",
                    "value": 1
                }
            ]
        ```
        """

        values = self.get_values()
        if values:
            return {"metric": self.metric_name, "labels": self.labels, "data": values}
        return None

    def insert(self, metric):
        """
        The default method for inserting metric values

        :param Metric metric: the metric to insert
        """

        self.metrics.append(metric)

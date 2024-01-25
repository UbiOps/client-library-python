# MetricClient

Helper class for inserting (custom) metrics

| Method                                         | Description                   |
|------------------------------------------------|-------------------------------|
| [**log_metric**](./MetricClient.md#log_metric) | Method to insert metrics      |
| [**start**](./MetricClient.md#start)           | Start the MetricClient thread |
| [**stop**](./MetricClient.md#stop)             | Stop the MetricClient thread  |

# **log_metric**
> log_metric(self, metric_name, labels, value)

Log a metric to the UbiOps API

## Description
Method to insert metrics.

### Example

Example with explicitly creating an api_client.

```python
import ubiops

from ubiops.utils.metrics import MetricClient
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

project_name = 'project_name_example' # str

metric_client = MetricClient(project_name=project_name, api_client=api_client)
metric_client.start()

metric_client.log_metric(metric_name="custom.metric", labels={"test": "test"}, value=1.0)

metric_client.stop()
```

Example using with environment variables

```python
import os

from ubiops.utils.metrics import MetricClient

os.environ["INT_API_URL"] = 'https://api.ubiops.com/v2.1'
os.environ["INT_API_TOKEN"] = 'Token <YOUR_API_TOKEN>'

project_name = 'project_name_example' # str

metric_client = MetricClient(project_name=project_name)
metric_client.start()

metric_client.log_metric(metric_name="custom.metric", labels={"test": "test"}, value=1.0)

metric_client.stop()
```

### Parameters

| Name            | Type      | Notes                                              |
|-----------------|-----------|----------------------------------------------------|
| **metric_name** | **str**   |                                                    |
| **labels**      | **dict**  |                                                    |
| **value**       | **float** |                                                    |

[[Back to top]](#)


# **start**
> start()

Start the MetricClient thread

## Description
The MetricClient will run as a daemon tread and periodically send inserted metrics to the UbiOps API.

[[Back to top]](#)

# **stop**
> stop()

Stop the MetricClient thread

## Description
The MetricClient will terminate gracefully and send any remaining metrics to the UbiOps API.

[[Back to top]](#)

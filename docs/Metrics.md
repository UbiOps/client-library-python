# Metrics

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metrics_create**](./Metrics.md#metrics_create) | **POST** /projects/{project_name}/metrics | Create metrics
[**metrics_delete**](./Metrics.md#metrics_delete) | **DELETE** /projects/{project_name}/metrics/{metric_name} | Delete metric
[**metrics_get**](./Metrics.md#metrics_get) | **GET** /projects/{project_name}/metrics/{metric_name} | Get metric
[**metrics_list**](./Metrics.md#metrics_list) | **GET** /projects/{project_name}/metrics | List metrics
[**metrics_update**](./Metrics.md#metrics_update) | **PATCH** /projects/{project_name}/metrics/{metric_name} | Update metric
[**time_series_data_aggregate**](./Metrics.md#time_series_data_aggregate) | **POST** /projects/{project_name}/time-series/aggregate | Aggregate metric data
[**time_series_data_create**](./Metrics.md#time_series_data_create) | **POST** /projects/{project_name}/time-series/data | Create metric data
[**time_series_data_list**](./Metrics.md#time_series_data_list) | **GET** /projects/{project_name}/time-series/data | List time series data
[**time_series_delete**](./Metrics.md#time_series_delete) | **DELETE** /projects/{project_name}/time-series/{time_series_id} | Delete time series
[**time_series_search**](./Metrics.md#time_series_search) | **GET** /projects/{project_name}/time-series/search | Search time series


# **metrics_create**
> MetricDetail metrics_create(project_name, data)

Create metrics

## Description
Create a custom metric. The name must start with *custom.*.

### Required Parameters

- `name`: Name of the metric
- `metric_type`: Type of the metric. It can be either 'delta' or 'gauge'.

### Optional Parameters

- `description`: Description of the metric
- `unit`: Unit of the metric
- `labels`: A list of labels that can be used to get data points containing the metric. For example, if the metric is defined for a deployment version and will be queried later with the ID of the deployment version, the labels list should contain 'deployment_version_id'.

## Request Examples

```
{
  "name": "custom.metric-1",
  "metric_type": "delta",
  "unit": "seconds",
  "labels": ["deployment_version_id"]
}
```

### Response Structure
Details of the created metric

- `id`: Unique identifier for the metric
- `name`: Name of the metric
- `description`: Description of the metric
- `creation_date`: The date when the metric was created
- `last_updated`: The date when the metric was last updated
- `custom`: A boolean indicating whether the metric is custom
- `metric_type`: Type of the metric
- `unit`: Unit of the metric
- `labels`: A list of labels that can be used to get data points containing the metric

## Response Examples

```
{
  "id": 10,
  "name": "custom.metric-1",
  "description": "My custom metric",
  "creation_date": "2023-09-01T08:32:14.876451Z",
  "last_updated": "2023-09-01T10:52:23.124784Z",
  "custom": true,
  "metric_type": "delta",
  "unit": "seconds",
  "labels": ["deployment_version_id"]
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
data = ubiops.MetricCreate() # MetricCreate

# Create metrics
api_response = core_api.metrics_create(project_name, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**MetricCreate**](./models/MetricCreate.md) | 

### Return type

[**MetricDetail**](./models/MetricDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **metrics_delete**
> metrics_delete(project_name, metric_name)

Delete metric

## Description
Delete a metric. Only custom metrics can be deleted.

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
metric_name = 'metric_name_example' # str

# Delete metric
core_api.metrics_delete(project_name, metric_name)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **metric_name** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **metrics_get**
> MetricDetail metrics_get(project_name, metric_name)

Get metric

## Description
Retrieve details of a metric

### Response Structure
Details of a metric

- `id`: Unique identifier for the metric
- `name`: Name of the metric
- `description`: Description of the metric
- `creation_date`: The date when the metric was created
- `last_updated`: The date when the metric was last updated
- `custom`: A boolean indicating whether the metric is custom
- `metric_type`: Type of the metric
- `unit`: Unit of the metric
- `labels`: A list of labels that can be used to get data points containing the metric

## Response Examples

```
{
  "id": 10,
  "name": "custom.metric-1",
  "description": "My custom metric",
  "creation_date": "2023-09-01T08:32:14.876451Z",
  "last_updated": "2023-09-01T10:52:23.124784Z",
  "custom": true,
  "metric_type": "delta",
  "unit": "seconds",
  "labels": ["deployment_version_id"]
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
metric_name = 'metric_name_example' # str

# Get metric
api_response = core_api.metrics_get(project_name, metric_name)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **metric_name** | **str** | 

### Return type

[**MetricDetail**](./models/MetricDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **metrics_list**
> list[MetricDetail] metrics_list(project_name, custom=custom)

List metrics

## Description
List available metrics in the project

### Optional Parameters

- `custom`: A boolean indicating whether to list default or custom metrics for the project

### Response Structure
A list of details of metrics

- `id`: Unique identifier for the metric
- `name`: Name of the metric
- `description`: Description of the metric
- `creation_date`: The date when the metric was created
- `last_updated`: The date when the metric was last updated
- `custom`: A boolean indicating whether the metric is custom
- `metric_type`: Type of the metric
- `unit`: Unit of the metric
- `labels`: A list of labels that can be used to get data points containing the metric

## Response Examples

```
[
  {
    "id": 1,
    "name": "deployments.requests",
    "description": "Requests to a deployment version",
    "creation_date": "2023-09-01T08:32:14.876451Z",
    "last_updated": "2023-09-01T10:52:23.124784Z",
    "custom": false,
    "metric_type": "delta",
    "unit": "requests",
    "labels": ["deployment_version_id", "user_id"]
  },
  {
    "id": 2,
    "name": "deployments.credits",
    "description": "Credits usage",
    "creation_date": "2023-09-02T10:12:51.195381Z",
    "last_updated": "2023-09-02T10:12:51.195381Z",
    "custom": false,
    "metric_type": "delta",
    "unit": "credits",
    "labels": ["deployment_version_id"]
  },
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
custom = True # bool (optional)

# List metrics
api_response = core_api.metrics_list(project_name, custom=custom)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **custom** | **bool** | [optional] 

### Return type

[**list[MetricDetail]**](./models/MetricDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **metrics_update**
> MetricDetail metrics_update(project_name, metric_name, data)

Update metric

## Description
Update a metric. Only custom metrics can be updated.

### Optional Parameters

- `name`: Name of the metric
- `description`: Description of the metric
- `unit`: Unit of the metric
- `labels`: A list of labels that can be used to get data points containing the metric. For example, if the metric is defined for a deployment version and will be queried later with the ID of the deployment version, the labels list should contain 'deployment_version_id'.

## Request Examples

```
{
  "name": "custom.metric-2"
}
```

### Response Structure
Details of the updated metric

- `id`: Unique identifier for the metric
- `name`: Name of the metric
- `description`: Description of the metric
- `creation_date`: The date when the metric was created
- `last_updated`: The date when the metric was last updated
- `custom`: A boolean indicating whether the metric is custom
- `metric_type`: Type of the metric
- `unit`: Unit of the metric
- `labels`: A list of labels that can be used to get data points containing the metric

## Response Examples

```
{
  "id": 10,
  "name": "custom.metric-2",
  "description": "My custom metric",
  "creation_date": "2023-09-01T08:32:14.876451Z",
  "last_updated": "2023-09-01T10:52:23.124784Z",
  "custom": true,
  "metric_type": "delta",
  "unit": "seconds",
  "labels": ["deployment_version_id"]
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
metric_name = 'metric_name_example' # str
data = ubiops.MetricUpdate() # MetricUpdate

# Update metric
api_response = core_api.metrics_update(project_name, metric_name, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **metric_name** | **str** | 
 **data** | [**MetricUpdate**](./models/MetricUpdate.md) | 

### Return type

[**MetricDetail**](./models/MetricDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **time_series_data_aggregate**
> object time_series_data_aggregate(project_name, data)

Aggregate metric data

## Description
Aggregate metric data for given date, metrics and labels. Only data up to 2 minutes ago is accepted.

### Required Parameters

- `metric`: Name of the metric
- `labels`: Dictionary containing key/value pairs where key indicates the string that can be used to query this metric later and value is the corresponding value of that
- `data`: A list of dictionaries containing 'date' and 'value' fields to indicate the value of the metric for a specific date

## Request Examples

```
[
  {
    "metric": "deployments.requests",
    "labels": {
      "deployment_version_id": "056efa9e-67eb-45e3-a49a-0742b3f08aee"
    },
    "data": [
      {
        "date": "2023-09-15T20:12:33.210+00:00",
        "value": 182
      },
      {
        "date": "2023-09-15T21:41:12.532+00:00",
        "value": 1
      }
    ]
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
data = ubiops.TimeSeriesDataCreate() # TimeSeriesDataCreate

# Aggregate metric data
api_response = core_api.time_series_data_aggregate(project_name, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**TimeSeriesDataCreate**](./models/TimeSeriesDataCreate.md) | 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **time_series_data_create**
> object time_series_data_create(project_name, data)

Create metric data

## Description
Insert data points for a metric. Multiple metrics for different types is supported.

### Required Parameters

- `metric`: Name of the metric
- `labels`: Dictionary containing key/value pairs where key indicates the string that can be used to query this metric later and value is the corresponding value of that
- `data`: A list of dictionaries containing 'date' and 'value' fields to indicate the value of the metric for a specific date. The value is inserted for the minute provided in the date field.

## Request Examples

```
[
  {
    "metric": "deployments.requests",
    "labels": {
      "deployment_version_id": "056efa9e-67eb-45e3-a49a-0742b3f08aee"
    },
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
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
data = ubiops.TimeSeriesDataCreate() # TimeSeriesDataCreate

# Create metric data
api_response = core_api.time_series_data_create(project_name, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**TimeSeriesDataCreate**](./models/TimeSeriesDataCreate.md) | 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **time_series_data_list**
> TimeSeriesDataList time_series_data_list(project_name, metric=metric, start_date=start_date, end_date=end_date, aggregation_period=aggregation_period, labels=labels, unit_period=unit_period)

List time series data

## Description
List data points for a metric

Available metrics for deployments:

- `deployments.requests`: Number of requests to a deployment version
- `deployments.failed_requests`: Number of failed requests to a deployment version
- `deployments.request_duration`: Average time in seconds for a deployment request to complete
- `deployments.input_volume`: Volume of incoming data in bytes
- `deployments.output_volume`: Volume of outgoing data in bytes
- `deployments.network_in`: Volume of inbound data traffic in bytes
- `deployments.network_out`: Volume of outbound data traffic in bytes
- `deployments.queue_size`: Average number of queued requests
- `deployments.queue_time`: Average time in seconds for a request to start processing
- `deployments.memory_utilization`: Average memory used during a request
- `deployments.instances`: Number of active deployment instances
- `deployments.credits`: Usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours the deployments are running

Available metrics for pipelines:

- `pipelines.requests`: Number of requests to a pipeline version
- `pipelines.failed_requests`: Number of failed requests to a pipeline version
- `pipelines.request_duration`: Average time in seconds for a pipeline request to complete
- `pipelines.input_volume`: Volume of incoming data in bytes
- `pipelines.output_volume`: Volume of outgoing data in bytes
- `pipelines.object_requests`: Number of object requests in a pipeline version
- `pipelines.object_failed_requests`: Number of failed object requests in a pipeline version

### Required Parameters

- `metric`: Name of the metric
- `start_date`: Start date for metric data points
- `end_date`: End date for metric data points

### Optional Parameters

- `aggregation_period`: Time period in seconds in which data points are grouped. It defaults to the highest resolution possible given the provided date range. Available values are: 60, 300, 900, 3600, 7200, 21600 and 86400.
Start and end dates are adjusted according to the aggregation period. For example, if aggregation period is 3600, start date is rounded down to the previous full hour and end date is rounded up to the next full hour.
- `labels`: Comma-separated values for labels to filter on data points. It must be in the format: key-1:value-1,key-2:value-2.

## Request Examples
With aggregation period 60, to get the credits usage of a deployment version per minute

```
{
  "metric": "deployments.credits",
  "start_date": "2024-05-01T10:00:00Z",
  "end_date": "2024-05-01T10:30:12Z",
  "labels": "deployment_version_id:dbcc9de3-1dcb-48ad-8197-3b2ac99f5e94"
}
```

With aggregation period 3600, to get the credits usage of a deployment version per hour

```
{
  "metric": "deployments.credits",
  "start_date": "2024-05-01T10:00:00Z",
  "end_date": "2024-05-01T16:30:12Z",
  "labels": "deployment_version_id:dbcc9de3-1dcb-48ad-8197-3b2ac99f5e94"
}
```

### Response Structure

- `metric`: Name of the metric
- `metric_type`: Type of the metric
- `unit`: Unit of the metric
- `start_date`: Start date for metric data points
- `end_date`: End date for metric data points
- `aggregation_period`: Time period in seconds in which data points are grouped
- `labels`: Labels to filter on data points
- `data`: A list of dictionaries containing the data points

## Response Examples

```
{
  "metric": "deployments.requests",
  "metric_type": "delta",
  "unit": "requests/s",
  "start_date": "2023-01-01T10:00:00Z",
  "end_date": 2023-01-01T12:00:00Z",
  "aggregation_period": 3600,
  "labels": {
    "deployment_version_id": "8935a589-8686-4ce7-8c9e-8b5e529c6b47"
  },
  "data": [
    {
      "start_date": "2023-01-01T10:00:00Z",
      "end_date": 2023-01-01T11:00:00Z",
      "value": 3
    },
    {
      "start_date": "2023-01-01T11:00:00Z",
      "end_date": 2023-01-01T12:00:00Z",
      "value": 10
    }
  ]
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
metric = 'metric_example' # str (optional)
start_date = 'start_date_example' # str (optional)
end_date = 'end_date_example' # str (optional)
aggregation_period = 56 # int (optional)
labels = "label1:value1,label2:value2" # str (optional)
unit_period = 56 # int (optional)

# List time series data
api_response = core_api.time_series_data_list(project_name, metric=metric, start_date=start_date, end_date=end_date, aggregation_period=aggregation_period, labels=labels, unit_period=unit_period)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **metric** | **str** | [optional] 
 **start_date** | **str** | [optional] 
 **end_date** | **str** | [optional] 
 **aggregation_period** | **int** | [optional] 
 **labels** | **str** | [optional] 
 **unit_period** | **int** | [optional] 

### Return type

[**TimeSeriesDataList**](./models/TimeSeriesDataList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **time_series_delete**
> time_series_delete(project_name, time_series_id)

Delete time series

## Description
Delete a time series

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
time_series_id = 'time_series_id_example' # str

# Delete time series
core_api.time_series_delete(project_name, time_series_id)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **time_series_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **time_series_search**
> list[TimeSeriesSearch] time_series_search(project_name, metric=metric, labels=labels, custom=custom, exact_match=exact_match, limit=limit, offset=offset)

Search time series

## Description
Search through time series

### Optional Parameters

- `metric`: Name of the metric
- `labels`: Comma-separated values for labels to filter on data points. It must be in the format: key-1:value-1,key-2:value-2.
- `custom`: A boolean indicating whether only default or custom metrics should be returned. If this parameter is not provided, both types are returned.
- `exact_match`: A boolean indicating whether the provided labels should match exactly or whether matching a subset is allowed. Defaults to false (matching a subset is allowed).
- `limit`: The maximum number of time series to return. It defaults to 500.
- `offset`: The number that indicates the starting point of the time series to return. It defaults to 0.

### Response Structure
A list of time series

- `metric`: Name of the metric
- `labels`: Labels that the time series has
- `resolution`: Metric resolution in seconds

## Response Examples

```
[
  {
    "metric": "deployments.requests",
    "labels": {
      "deployment_version_id": "8935a589-8686-4ce7-8c9e-8b5e529c6b47",
      "user_id": "5bb50513-2b4e-466a-ab88-e5be70d63f75"
    },
    "resolution": 60
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
metric = 'metric_example' # str (optional)
labels = "label1:value1,label2:value2" # str (optional)
custom = True # bool (optional)
exact_match = True # bool (optional)
limit = 56 # int (optional)
offset = 56 # int (optional)

# Search time series
api_response = core_api.time_series_search(project_name, metric=metric, labels=labels, custom=custom, exact_match=exact_match, limit=limit, offset=offset)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **metric** | **str** | [optional] 
 **labels** | **str** | [optional] 
 **custom** | **bool** | [optional] 
 **exact_match** | **bool** | [optional] 
 **limit** | **int** | [optional] 
 **offset** | **int** | [optional] 

### Return type

[**list[TimeSeriesSearch]**](./models/TimeSeriesSearch.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


# Pipeline_Requests

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_pipeline_requests_create**](PipelineRequests.md#batch_pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/batch | Create a batch pipeline request
[**batch_pipeline_version_requests_create**](PipelineRequests.md#batch_pipeline_version_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/batch | Create a batch pipeline version request
[**pipeline_requests_batch_delete**](PipelineRequests.md#pipeline_requests_batch_delete) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/delete | Delete multiple pipeline requests
[**pipeline_requests_batch_get**](PipelineRequests.md#pipeline_requests_batch_get) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/collect | Retrieve multiple pipeline requests
[**pipeline_requests_create**](PipelineRequests.md#pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests | Create a pipeline request
[**pipeline_requests_delete**](PipelineRequests.md#pipeline_requests_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/requests/{request_id} | Delete a pipeline request
[**pipeline_requests_get**](PipelineRequests.md#pipeline_requests_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/requests/{request_id} | Get a pipeline request
[**pipeline_requests_list**](PipelineRequests.md#pipeline_requests_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/requests | List pipeline requests
[**pipeline_version_object_requests_get**](PipelineRequests.md#pipeline_version_object_requests_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/object-requests/{request_id} | Get an operator request
[**pipeline_version_requests_batch_delete**](PipelineRequests.md#pipeline_version_requests_batch_delete) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/delete | Delete multiple pipeline version requests
[**pipeline_version_requests_batch_get**](PipelineRequests.md#pipeline_version_requests_batch_get) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/collect | Retrieve multiple pipeline version requests
[**pipeline_version_requests_create**](PipelineRequests.md#pipeline_version_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests | Create a pipeline version request
[**pipeline_version_requests_delete**](PipelineRequests.md#pipeline_version_requests_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/{request_id} | Delete a pipeline version request
[**pipeline_version_requests_get**](PipelineRequests.md#pipeline_version_requests_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/{request_id} | Get a pipeline version request
[**pipeline_version_requests_list**](PipelineRequests.md#pipeline_version_requests_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests | List pipeline version requests


# **batch_pipeline_requests_create**
> list[PipelineRequestBatchCreateResponse] batch_pipeline_requests_create(project_name, pipeline_name, data, timeout=timeout, notification_group=notification_group)

Create a batch pipeline request

## Description
Make a batch request to the default version of a pipeline. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the pipeline request collect methods.

The maximum number of requests that can be created per batch is 100.

### Required Parameters
In case of structured input pipeline: A list of dictionaries, where each dictionary contains the input fields of the pipeline as keys. It is also possible to send a single dictionary as input.
In case of plain input pipeline: A list of strings. It is also possible to send a single string as input.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the entire pipeline request in seconds. The maximum allowed value is 172800 (48 hours) and the default value is 14400 (4 hours).
The deployment request timeouts default to 14400 seconds for deployments in the pipeline.
- `notification_group`: Name of a notification group to send notifications (e.g., emails) when the request is completed

## Request Examples
Multiple structured batch pipeline requests

```
[
  {
    "pipeline-input-field-1": 5.0,
    "pipeline-input-field-2": "N",
    "pipeline-input-field-3": [0.25, 0.25, 2.1, 16.3]
  },
  {
    "pipeline-input-field-1": 3.0,
    "pipeline-input-field-2": "S",
    "pipeline-input-field-3": [4.23, 3.27, 2.41, 12.4]
  }
]
```

Multiple plain batch pipeline requests

```
[
  "plain-data-goes-here", "plain-example-data"
]
```

### Response Structure
A list of dictionaries containing the details of the created pipeline requests with the following fields:

- `id`: Unique identifier for the pipeline request, which can be used to collect the result
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request is made
- `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
- `time_created`: Server time that the request was made (current time)

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  }
]
```

### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
data = [{'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'}] # list[str or dict()] 
timeout = 56 # int  (optional)
notification_group = 'notification_group_example' # str  (optional)

# Create a batch pipeline request
api_response = api.batch_pipeline_requests_create(project_name, pipeline_name, data, timeout=timeout, notification_group=notification_group)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **data** | **list[str or dict()]** | 
 **timeout** | **int** | [optional] 
 **notification_group** | **str** | [optional] 

### Return type

[**list[PipelineRequestBatchCreateResponse]**](./models/PipelineRequestBatchCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **batch_pipeline_version_requests_create**
> list[PipelineRequestBatchCreateResponse] batch_pipeline_version_requests_create(project_name, pipeline_name, version, data, timeout=timeout, notification_group=notification_group)

Create a batch pipeline version request

## Description
Make a batch request to a pipeline version. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the pipeline version request collect methods.

The maximum number of requests that can be created per batch is 100.

### Required Parameters
In case of structured input pipeline: A list of dictionaries, where each dictionary contains the input fields of the pipeline as keys. It is also possible to send a single dictionary as input.
In case of plain input pipeline: A list of strings. It is also possible to send a single string as input.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the entire pipeline request in seconds. The maximum allowed value is 172800 (48 hours) and the default value is 14400 (4 hours).
The deployment request timeouts default to 14400 seconds for deployments in the pipeline.
- `notification_group`: Name of a notification group to send notifications (e.g., emails) when the request is completed

## Request Examples
Multiple structured batch pipeline requests

```
[
  {
    "pipeline-input-field-1": 5.0,
    "pipeline-input-field-2": "N",
    "pipeline-input-field-3": [0.25, 0.25, 2.1, 16.3]
  },
  {
    "pipeline-input-field-1": 3.0,
    "pipeline-input-field-2": "S",
    "pipeline-input-field-3": [4.23, 3.27, 2.41, 12.4]
  }
]
```

Multiple plain batch pipeline requests

```
[
  "plain-data-goes-here", "plain-example-data"
]
```

### Response Structure
A list of dictionaries containing the details of the created pipeline version requests with the following fields:

- `id`: Unique identifier for the pipeline version request, which can be used to collect the result
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request is made
- `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
- `time_created`: Server time that the request was made (current time)

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  }
]
```

### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
version = 'version_example' # str 
data = [{'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'}] # list[str or dict()] 
timeout = 56 # int  (optional)
notification_group = 'notification_group_example' # str  (optional)

# Create a batch pipeline version request
api_response = api.batch_pipeline_version_requests_create(project_name, pipeline_name, version, data, timeout=timeout, notification_group=notification_group)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 
 **data** | **list[str or dict()]** | 
 **timeout** | **int** | [optional] 
 **notification_group** | **str** | [optional] 

### Return type

[**list[PipelineRequestBatchCreateResponse]**](./models/PipelineRequestBatchCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_batch_delete**
> object pipeline_requests_batch_delete(project_name, pipeline_name, data)

Delete multiple pipeline requests

## Description
Delete multiple pipeline requests for the default version of a pipeline. If one of the given pipeline requests does not exist, an error message is given and no request is deleted. A maximum of 100 pipeline requests can be deleted with this method.

### Required Parameters
A list of ids of the requests

## Request Examples

```
["2521378e-263e-4e2e-85e9-a96254b36536", "69eca481-8576-49e8-8e20-ea56f2005bcb"]
```

### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
data = ['request_id_1', 'request_id_2'] # list[str] 

# Delete multiple pipeline requests
api_response = api.pipeline_requests_batch_delete(project_name, pipeline_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **data** | **list[str]** | 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_batch_get**
> list[PipelineRequestDetail] pipeline_requests_batch_get(project_name, pipeline_name, data)

Retrieve multiple pipeline requests

## Description
Retrieve multiple pipeline requests for the default version of a pipeline. If one of the given pipeline requests does not exist, an error message is given and no request is returned. A maximum of 100 pipeline requests can be retrieved with this method. The pipeline requests are NOT returned in the order they are given in.

### Required Parameters
A list of ids of the requests

## Request Examples

```
["2521378e-263e-4e2e-85e9-a96254b36536", "69eca481-8576-49e8-8e20-ea56f2005bcb"]
```

### Response Structure
A list of dictionaries containing the details of the retrieved pipeline requests with the following fields:

- `id`: Unique identifier for the pipeline request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request was made
- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'.
- `success`: A boolean value that indicates whether the pipeline request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed
- `request_data`: A dictionary (structured input type) or string (plain input type) containing the data that was sent when the request was created
- `result`: A dictionary (structured output type) or string (plain output type) containing the data connected to the pipeline end
- `deployment_requests`: A list of requests to the deployments in the pipeline. With the deployment request ids provided in this list, it's possible to collect the results of the deployment requests separately.
- `operator_requests`: A list of requests of the operators in the pipeline. With the operator request ids provided in this list, it's possible to collect the results of the operator requests separately.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-063-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {
      "input_field": 23.5
    },
    "deployment_requests": [
      {
        "id": "4b9c8a81-b3ef-437a-8d35-187490eda3e4",
        "pipeline_object": "deployment-1-v1-object",
        "deployment": "deployment-1",
        "version": "v1",
        "sequence_id": "16699092560130860",
        "success": true,
        "error_message": null
      }
    ],
    "operator_requests": [
      {
        "id": "bd6d6ce5-ba9d-4c91-af61-0cf16f1f5452",
        "pipeline_object": "function-1",
        "operator": "function",
        "sequence_id": "16699092560130861",
        "success": true,
        "error_message": null
      }
    ],
    "result": {
      "output_field": 23.5
    },
    "error_message": null
  },
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-063-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {
      "input_field": 23.5
    },
    "deployment_requests": [
      {
        "id": "5fa86ad1-7949-48f5-8e2c-210cce78f427",
        "pipeline_object": "deployment-1-v1-object",
        "deployment": "deployment-1",
        "version": "v1"
      }
    ],
    "result": {
      "output_field": 23.5
    },
    "error_message": null
  }
]
```

### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
data = ['request_id_1', 'request_id_2'] # list[str] 

# Retrieve multiple pipeline requests
api_response = api.pipeline_requests_batch_get(project_name, pipeline_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **data** | **list[str]** | 

### Return type

[**list[PipelineRequestDetail]**](./models/PipelineRequestDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_create**
> PipelineRequestCreateResponse pipeline_requests_create(project_name, pipeline_name, data, pipeline_timeout=pipeline_timeout, deployment_timeout=deployment_timeout)

Create a pipeline request

## Description
Make a direct request to the default version of a pipeline. This method returns all the results of the deployment requests made within the pipeline version.

### Required Parameters
The input for the request. In case of a structured pipeline, this is a dictionary which contains the input fields of the pipeline as keys. In case of a plain pipeline, give a string or list of strings.

### Optional Parameters
The following parameters should be given as query parameters:

- `pipeline_timeout`: Timeout for the entire pipeline request in seconds. The maximum allowed value is 7200 (2 hours) and the default value is 3600 (1 hour).
- `deployment_timeout`: Timeout for each deployment request in the pipeline in seconds. The maximum allowed value is 3600 (1 hour) and the default value is 300  (5 minutes).

## Request Examples
A structured pipeline request

```
{
  "pipeline-input-field-1": 5.0,
  "pipeline-input-field-2": "N"
}
```

A plain pipeline request

```
example-plain-data
```

### Response Structure

- `id`: Unique identifier for the pipeline request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request is made
- `success`: A boolean value that indicates whether the pipeline request was successful
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `deployment_requests`: A list of dictionaries containing the results of the deployment requests made for the version objects in the pipeline. The dictionaries contain the following fields:
    - `id`: Unique identifier for the deployment request
    - `pipeline_object`: Name of the object in the pipeline
    - `deployment`: Name of the deployment the request was made to
    - `version`: Name of the version the request was made to
    - `success`: A boolean value that indicates whether the deployment request was successful
    - `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `result`: A dictionary (structured output type) or string (plain output type) containing the data connected to the pipeline end

## Response Examples

```
{
  "id": "286f771b-6617-4985-ab49-12ed720e62b1",
  "pipeline": "pipeline-1",
  "version": "v1",
  "success": false,
  "error_message": "Error while processing a deployment request",
  "deployment_requests": [
    {
      "id": "a7524614-bdb7-41e1-b4c1-653bb72c30b4",
      "pipeline_object": "deployment-object-1",
      "sequence_id": "16699092560130860",
      "success": true,
      "error_message": null
    },
    {
      "id": "fe322c50-58f8-4e67-b7d6-cba14273874e",
      "pipeline_object": "deployment-object-2",
      "sequence_id": "16699092560130861",
      "success": false,
      "error_message": "Invalid message format"
    }
  ],
  "operator_requests": [
    {
      "id": "bd6d6ce5-ba9d-4c91-af61-0cf16f1f5452",
      "pipeline_object": "function-1",
      "operator": "function",
      "sequence_id": "16699092560130860",
      "success": true,
      "error_message": null
    }
  ],
  "result": {
    "output_field": 23.5
  }
}
```

### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
data = {'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'} # str or dict() 
pipeline_timeout = 56 # int  (optional)
deployment_timeout = 56 # int  (optional)

# Create a pipeline request
api_response = api.pipeline_requests_create(project_name, pipeline_name, data, pipeline_timeout=pipeline_timeout, deployment_timeout=deployment_timeout)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **data** | **str or dict()** | 
 **pipeline_timeout** | **int** | [optional] 
 **deployment_timeout** | **int** | [optional] 

### Return type

[**PipelineRequestCreateResponse**](./models/PipelineRequestCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_delete**
> pipeline_requests_delete(project_name, pipeline_name, request_id)

Delete a pipeline request

## Description
Delete a request for the default version of a pipeline. This action deletes all the deployment requests in the pipeline.

### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
request_id = 'request_id_example' # str 

# Delete a pipeline request
api.pipeline_requests_delete(project_name, pipeline_name, request_id)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_get**
> PipelineRequestSingleDetail pipeline_requests_get(project_name, pipeline_name, request_id, metadata_only=metadata_only)

Get a pipeline request

## Description
Get a request for the default version of a pipeline. With this method, the result of the request may be retrieved.

### Optional Parameters
The following parameters should be given as query parameters:

- `metadata_only`: A boolean value that indicates whether the response should include the request data and result. The default value is False.

### Response Structure
A dictionary containing the details of the pipeline request with the following fields:

- `id`: Unique identifier for the pipeline request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request was made
- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'.
- `success`: A boolean value that indicates whether the pipeline request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed
- `request_data`: A dictionary (structured input type) or string (plain input type) containing the data that was sent when the request was created
- `deployment_requests`: A list of requests of the deployments in the pipeline. With the deployment request ids provided in this list, it's possible to collect the results of the deployment requests separately.
- `operator_requests`: A list of requests of the operators in the pipeline. With the operator request ids provided in this list, it's possible to collect the results of the operator requests separately.
- `result`: A dictionary (structured output type) or string (plain output type) containing the data connected to the pipeline end
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `created_by`: The email of the user that created the request. In case the request is created by a service, the field will have a "UbiOps" value.
- `notification_group`: Name of a notification group to send notifications (e.g., emails) when the request is completed
- `origin`: A dictionary containing the information on where the request originated from. It contains:
   - the pipeline (and version) names if the request is directly made to the pipeline
   - the request schedule name if the request is created via a request schedule

## Response Examples

```
{
  "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
  "pipeline": "pipeline-1",
  "version": "v1",
  "status": "pending",
  "success": true,
  "time_created": "2020-03-28T20:00:26.613+00:00",
  "time_started": "2020-03-28T20:00:41.276+00:00",
  "time_completed": "2020-03-28T20:00:42.241+00:00",
  "request_data": {
    "input_field": 23.5
  },
  "deployment_requests": [
    {
      "id": "4b9c8a81-b3ef-437a-8d35-187490eda3e4",
      "pipeline_object": "deployment-1-v1-object",
      "deployment": "deployment-1",
      "version": "v1",
      "sequence_id": "16699092560130860",
      "success": true,
      "error_message": null
    }
  ],
  "operator_requests": [
    {
      "id": "bd6d6ce5-ba9d-4c91-af61-0cf16f1f5452",
      "pipeline_object": "function-1",
      "operator": "function",
      "sequence_id": "16699092560130861",
      "success": true,
      "error_message": null
    }
  ],
  "result": {
    "output_field": 23.5
  },
  "error_message": null,
  "created_by": "my.example.user@ubiops.com",
  "notification_group": "notification-group-1",
  "origin": {
    "pipeline": "pipeline-1",
    "pipeline"_version": "v1"
  }
}
```

### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
request_id = 'request_id_example' # str 
metadata_only = True # bool  (optional)

# Get a pipeline request
api_response = api.pipeline_requests_get(project_name, pipeline_name, request_id, metadata_only=metadata_only)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 
 **metadata_only** | **bool** | [optional] 

### Return type

[**PipelineRequestSingleDetail**](./models/PipelineRequestSingleDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_list**
> list[PipelineRequestList] pipeline_requests_list(project_name, pipeline_name, status=status, success=success, limit=limit, offset=offset, sort=sort, request_schedule=request_schedule, start_date=start_date, end_date=end_date, search_id=search_id)

List pipeline requests

## Description
List all requests for the default version of a pipeline

### Optional Parameters
The following parameters should be given as query parameters:

- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'.
- `success`: A boolean value that indicates whether the pipeline request was successful
- `limit`: The maximum number of requests given back, default is 50
- `offset`: The number which forms the starting point of the requests given back. If offset equals 2, then the first 2 requests will be omitted from the list.
- `sort`: Direction of sorting according to the creation date of the request, can be 'asc' or 'desc'. The default sorting is done in descending order.
- `request_schedule`: The name of a request schedule that created requests
- `start_date`: Start date of the interval for which the requests are retrieved, looking at the creation date of the request
- `end_date`: End date of the interval for which the requests are retrieved, looking at the creation date of the request
- `search_id`: A string to search inside request ids. It will filter all request ids that contain this string

If no start or end date is provided, the most recent requests are returned.

### Response Structure
A list of dictionaries containing the details of the pipeline requests with the following fields:

- `id`: Unique identifier for the pipeline request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request was made
- `status`: Status of the request
- `success`: A boolean value that indicates whether the pipeline request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  }
]
```

### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
status = 'status_example' # str  (optional)
success = True # bool  (optional)
limit = 56 # int  (optional)
offset = 56 # int  (optional)
sort = 'sort_example' # str  (optional)
request_schedule = 'request_schedule_example' # str  (optional)
start_date = 'start_date_example' # str  (optional)
end_date = 'end_date_example' # str  (optional)
search_id = 'search_id_example' # str  (optional)

# List pipeline requests
api_response = api.pipeline_requests_list(project_name, pipeline_name, status=status, success=success, limit=limit, offset=offset, sort=sort, request_schedule=request_schedule, start_date=start_date, end_date=end_date, search_id=search_id)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **status** | **str** | [optional] 
 **success** | **bool** | [optional] 
 **limit** | **int** | [optional] 
 **offset** | **int** | [optional] 
 **sort** | **str** | [optional] 
 **request_schedule** | **str** | [optional] 
 **start_date** | **str** | [optional] 
 **end_date** | **str** | [optional] 
 **search_id** | **str** | [optional] 

### Return type

[**list[PipelineRequestList]**](./models/PipelineRequestList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_object_requests_get**
> OperatorRequestDetail pipeline_version_object_requests_get(project_name, pipeline_name, request_id, version, metadata_only=metadata_only)

Get an operator request

## Description
Get a request for an operator object of a version of a pipeline. With this method, the result of the request may be retrieved.

### Optional Parameters
The following parameters should be given as query parameters:

- `metadata_only`: A boolean value that indicates whether the response should include the request data and result. The default value is False.

### Response Structure
A dictionary containing the details of the operator request with the following fields:

- `id`: Unique identifier for the pipeline version object request
- `pipeline_request_id`: Unique identifier for the pipeline request to which the object request belongs
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request was made
- `object`: Name of the pipeline version object for which the request was made
- `operator`: Name of the pipeline operator for which the request was made
- `status`: Status of the request. Can be 'failed' or 'completed'.
- `success`: A boolean value that indicates whether the request was successful
- `time_created`: Server time that the request was made
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed
- `request_data`: A dictionary containing the data that was sent when the request was created
- `result`: Request result value. NULL if the request failed.
- `error_message`: An error message explaining why the request has failed

## Response Examples

```
{
  "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
  "pipeline_request_id": "ce488fed-04c2-4ce5-a839-f6e5580ad40f",
  "pipeline": "pipeline-1",
  "version": "v1",
  "object": "function-1",
  "operator": "function",
  "status": "completed",
  "success": true,
  "time_created": "2020-03-28T20:00:26.613+00:00",
  "time_started": "2020-03-28T20:00:41.276+00:00",
  "time_completed": "2020-03-28T20:00:42.241+00:00",
  "request_data": {
    "input_field": 23.5
  },
  "result": {
    "output": 23.5
  },
  "error_message": ""
}
```

### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
request_id = 'request_id_example' # str 
version = 'version_example' # str 
metadata_only = True # bool  (optional)

# Get an operator request
api_response = api.pipeline_version_object_requests_get(project_name, pipeline_name, request_id, version, metadata_only=metadata_only)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 
 **version** | **str** | 
 **metadata_only** | **bool** | [optional] 

### Return type

[**OperatorRequestDetail**](./models/OperatorRequestDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_batch_delete**
> object pipeline_version_requests_batch_delete(project_name, pipeline_name, version, data)

Delete multiple pipeline version requests

## Description
Delete multiple requests for a pipeline version. If one of the given pipeline requests does not exist, an error message is given and no request is deleted. A maximum of 100 pipeline requests can be deleted with this method.

### Required Parameters
A list of ids of the requests

## Request Examples

```
["2521378e-263e-4e2e-85e9-a96254b36536", "69eca481-8576-49e8-8e20-ea56f2005bcb"]
```

### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
version = 'version_example' # str 
data = ['request_id_1', 'request_id_2'] # list[str] 

# Delete multiple pipeline version requests
api_response = api.pipeline_version_requests_batch_delete(project_name, pipeline_name, version, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 
 **data** | **list[str]** | 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_batch_get**
> list[PipelineRequestDetail] pipeline_version_requests_batch_get(project_name, pipeline_name, version, data)

Retrieve multiple pipeline version requests

## Description
Retrieve multiple requests for a pipeline version. If one of the given pipeline requests does not exist, an error message is given and no request is returned. A maximum of 100 pipeline version requests can be retrieved with this method. The pipeline version requests are NOT returned in the order they are given in.

### Required Parameters
A list of ids of the requests

## Request Examples

```
["2521378e-263e-4e2e-85e9-a96254b36536", "69eca481-8576-49e8-8e20-ea56f2005bcb"]
```

### Response Structure
A list of dictionaries containing the details of the retrieved pipeline requests with the following fields:

- `id`: Unique identifier for the pipeline request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request was made
- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'.
- `success`: A boolean value that indicates whether the pipeline request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed
- `request_data`: A dictionary (structured input type) or string (plain input type) containing the data that was sent when the request was created
- `result`: A dictionary (structured output type) or string (plain output type) containing the data connected to the pipeline end
- `deployment_requests`: A list of requests to the deployments in the pipeline. With the deployment request ids provided in this list, it's possible to collect the results of the deployment requests separately.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-063-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {
      "input_field": 23.5
    },
    "deployment_requests": [
      {
        "id": "4b9c8a81-b3ef-437a-8d35-187490eda3e4",
        "pipeline_object": "deployment-1-v1-object",
        "deployment": "deployment-1",
        "version": "v1"
      }
    ],
    "result": {
      "output_field": 23.5
    },
    "error_message": null
  },
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-063-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {
      "input_field": 23.5
    },
    "deployment_requests": [
      {
        "id": "5fa86ad1-7949-48f5-8e2c-210cce78f427",
        "pipeline_object": "deployment-1-v1-object",
        "deployment": "deployment-1",
        "version": "v1"
      }
    ],
    "result": {
      "output_field": 23.5
    },
    "error_message": null
  }
]
```

### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
version = 'version_example' # str 
data = ['request_id_1', 'request_id_2'] # list[str] 

# Retrieve multiple pipeline version requests
api_response = api.pipeline_version_requests_batch_get(project_name, pipeline_name, version, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 
 **data** | **list[str]** | 

### Return type

[**list[PipelineRequestDetail]**](./models/PipelineRequestDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_create**
> PipelineRequestCreateResponse pipeline_version_requests_create(project_name, pipeline_name, version, data, pipeline_timeout=pipeline_timeout, deployment_timeout=deployment_timeout)

Create a pipeline version request

## Description
Make a direct request to a pipeline version. This method returns all the results of the deployment requests made within the pipeline version.

### Required Parameters
The input for the request. In case of a structured pipeline, this is a dictionary which contains the input fields of the pipeline as keys. In case of a plain pipeline, give a string or list of strings.

### Optional Parameters
The following parameters should be given as query parameters:

- `pipeline_timeout`: Timeout for the entire pipeline request in seconds. The maximum allowed value is 7200 (2 hours) and the default value is 3600 (1 hour).
- `deployment_timeout`: Timeout for each deployment request in the pipeline in seconds. The maximum allowed value is 3600 (1 hour) and the default value is 300 (5 minutes).

## Request Examples
A structured pipeline request

```
{
  "pipeline-input-field-1": 5.0,
  "pipeline-input-field-2": "N"
}
```

A plain pipeline request

```
example-plain-data
```

### Response Structure

- `id`: Unique identifier for the pipeline request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request is made
- `success`: A boolean value that indicates whether the pipeline request was successful
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `deployment_requests`: A list of dictionaries containing the results of the deployment requests made for the version objects in the pipeline. The dictionaries contain the following fields:
    - `id`: Unique identifier for the deployment request
    - `pipeline_object`: Name of the object in the pipeline
    - `deployment`: Name of the deployment the request was made to
    - `version`: Name of the version the request was made to
    - `success`: A boolean value that indicates whether the deployment request was successful
    - `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `result`: A dictionary (structured output type) or string (plain output type) containing the data connected to the pipeline end

## Response Examples

```
{
  "id": "286f771b-6617-4985-ab49-12ed720e62b1",
  "project": "project-1",
  "pipeline": "pipeline-1",
  "version": "v1",
  "success": false,
  "error_message": "Error while processing a deployment request",
  "deployment_requests": [
    {
      "id": "a7524614-bdb7-41e1-b4c1-653bb72c30b4",
      "pipeline_object": "deployment-object-1",
      "success": true,
      "error_message": null
    },
    {
      "id": "fe322c50-58f8-4e67-b7d6-cba14273874e",
      "pipeline_object": "deployment-object-2",
      "success": false,
      "error_message": "Invalid message format"
    }
  ],
  "result": {
    "output_field": 23.5
  }
}
```

### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
version = 'version_example' # str 
data = {'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'} # str or dict() 
pipeline_timeout = 56 # int  (optional)
deployment_timeout = 56 # int  (optional)

# Create a pipeline version request
api_response = api.pipeline_version_requests_create(project_name, pipeline_name, version, data, pipeline_timeout=pipeline_timeout, deployment_timeout=deployment_timeout)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 
 **data** | **str or dict()** | 
 **pipeline_timeout** | **int** | [optional] 
 **deployment_timeout** | **int** | [optional] 

### Return type

[**PipelineRequestCreateResponse**](./models/PipelineRequestCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_delete**
> pipeline_version_requests_delete(project_name, pipeline_name, request_id, version)

Delete a pipeline version request

## Description
Delete a request for a pipeline version. This action deletes all the deployment requests in the pipeline.

### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
request_id = 'request_id_example' # str 
version = 'version_example' # str 

# Delete a pipeline version request
api.pipeline_version_requests_delete(project_name, pipeline_name, request_id, version)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 
 **version** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_get**
> PipelineRequestSingleDetail pipeline_version_requests_get(project_name, pipeline_name, request_id, version, metadata_only=metadata_only)

Get a pipeline version request

## Description
Get a request for a pipeline version. With this method, the result of a request may be retrieved.

### Optional Parameters
The following parameters should be given as query parameters:

- `metadata_only`: A boolean value that indicates whether the response should include the request data and result. The default value is False.

### Response Structure
A dictionary containing the details of the pipeline version request with the following fields:

- `id`: Unique identifier for the pipeline version request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request was made
- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'.
- `success`: A boolean value that indicates whether the pipeline version request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed
- `request_data`: A dictionary (structured input type) or string (plain input type) containing the data that was sent when the request was created
- `deployment_requests`: A list of requests of the deployments in the pipeline. With the deployment request ids provided in this list, it's possible to collect the results of the deployment requests separately.
- `result`: A dictionary (structured output type) or string (plain output type) containing the data connected to the pipeline end
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `created_by`: The email of the user that created the request. In case the request is created by a service, the field will have a "UbiOps" value.
- `notification_group`: Name of a notification group to send notifications (e.g., emails) when the request is completed

## Response Examples

```
{
  "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
  "pipeline": "pipeline-1",
  "version": "v1",
  "status": "pending",
  "success": true,
  "time_created": "2020-03-28T20:00:26.613+00:00",
  "time_started": "2020-03-28T20:00:41.276+00:00",
  "time_completed": "2020-03-28T20:00:42.241+00:00",
  "request_data": {
    "input_field": 23.5
  },
  "deployment_requests": [
    {
      "id": "4b9c8a81-b3ef-437a-8d35-187490eda3e4",
      "pipeline_object": "deployment-1-v1-object",
      "deployment": "deployment-1",
      "version": "v1"
    }
  ],
  "result": {
    "output_field": 23.5
  },
  "error_message": null,
  "created_by": "my.example.user@ubiops.com",
  "notification_group": "notification-group-1"
}
```

### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
request_id = 'request_id_example' # str 
version = 'version_example' # str 
metadata_only = True # bool  (optional)

# Get a pipeline version request
api_response = api.pipeline_version_requests_get(project_name, pipeline_name, request_id, version, metadata_only=metadata_only)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 
 **version** | **str** | 
 **metadata_only** | **bool** | [optional] 

### Return type

[**PipelineRequestSingleDetail**](./models/PipelineRequestSingleDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_list**
> list[PipelineRequestList] pipeline_version_requests_list(project_name, pipeline_name, version, status=status, success=success, limit=limit, offset=offset, sort=sort, request_schedule=request_schedule, start_date=start_date, end_date=end_date, search_id=search_id)

List pipeline version requests

## Description
List all requests for a pipeline version

### Optional Parameters
The following parameters should be given as query parameters:

- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'.
- `success`: A boolean value that indicates whether the pipeline version request was successful
- `limit`: The maximum number of requests given back, default is 50
- `offset`: The number which forms the starting point of the requests given back. If offset equals 2, then the first 2 requests will be omitted from the list.
- `sort`: Direction of sorting according to the creation date of the request, can be 'asc' or 'desc'. The default sorting is done in descending order.
- `request_schedule`: The name of a request schedule that created requests
- `start_date`: Start date of the interval for which the requests are retrieved, looking at the creation date of the request
- `end_date`: End date of the interval for which the requests are retrieved, looking at the creation date of the request
- `search_id`: A string to search inside request ids. It will filter all request ids that contain this string

If no start or end date is provided, the most recent requests are returned.

### Response Structure
A list of dictionaries containing the details of the pipeline version requests with the following fields:

- `id`: Unique identifier for the pipeline version request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request was made
- `status`: Status of the request
- `success`: A boolean value that indicates whether the pipeline version request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  }
]
```

### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

# Create an instance of the API class
api = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
version = 'version_example' # str 
status = 'status_example' # str  (optional)
success = True # bool  (optional)
limit = 56 # int  (optional)
offset = 56 # int  (optional)
sort = 'sort_example' # str  (optional)
request_schedule = 'request_schedule_example' # str  (optional)
start_date = 'start_date_example' # str  (optional)
end_date = 'end_date_example' # str  (optional)
search_id = 'search_id_example' # str  (optional)

# List pipeline version requests
api_response = api.pipeline_version_requests_list(project_name, pipeline_name, version, status=status, success=success, limit=limit, offset=offset, sort=sort, request_schedule=request_schedule, start_date=start_date, end_date=end_date, search_id=search_id)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 
 **status** | **str** | [optional] 
 **success** | **bool** | [optional] 
 **limit** | **int** | [optional] 
 **offset** | **int** | [optional] 
 **sort** | **str** | [optional] 
 **request_schedule** | **str** | [optional] 
 **start_date** | **str** | [optional] 
 **end_date** | **str** | [optional] 
 **search_id** | **str** | [optional] 

### Return type

[**list[PipelineRequestList]**](./models/PipelineRequestList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


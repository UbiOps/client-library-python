# Pipeline_Requests

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_pipeline_requests_create**](./PipelineRequests.md#batch_pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/batch | Create a batch pipeline request
[**batch_pipeline_version_requests_create**](./PipelineRequests.md#batch_pipeline_version_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/batch | Create a batch pipeline version request
[**pipeline_requests_batch_cancel**](./PipelineRequests.md#pipeline_requests_batch_cancel) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/cancel | Cancel multiple pipeline requests
[**pipeline_requests_batch_delete**](./PipelineRequests.md#pipeline_requests_batch_delete) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/delete | Delete multiple pipeline requests
[**pipeline_requests_batch_get**](./PipelineRequests.md#pipeline_requests_batch_get) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/collect | Retrieve multiple pipeline requests
[**pipeline_requests_create**](./PipelineRequests.md#pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests | Create a pipeline request
[**pipeline_requests_delete**](./PipelineRequests.md#pipeline_requests_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/requests/{request_id} | Delete a pipeline request
[**pipeline_requests_get**](./PipelineRequests.md#pipeline_requests_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/requests/{request_id} | Get a pipeline request
[**pipeline_requests_input_get**](./PipelineRequests.md#pipeline_requests_input_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/requests/{request_id}/input | Get a pipeline request input
[**pipeline_requests_list**](./PipelineRequests.md#pipeline_requests_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/requests | List pipeline requests
[**pipeline_requests_output_get**](./PipelineRequests.md#pipeline_requests_output_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/requests/{request_id}/output | Get a pipeline request output
[**pipeline_requests_update**](./PipelineRequests.md#pipeline_requests_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name}/requests/{request_id} | Update a pipeline request
[**pipeline_version_object_requests_get**](./PipelineRequests.md#pipeline_version_object_requests_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/object-requests/{request_id} | Get an operator request
[**pipeline_version_object_requests_input_get**](./PipelineRequests.md#pipeline_version_object_requests_input_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/object-requests/{request_id}/input | Get an operator request input
[**pipeline_version_object_requests_output_get**](./PipelineRequests.md#pipeline_version_object_requests_output_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/object-requests/{request_id}/output | Get an operator request output
[**pipeline_version_requests_batch_cancel**](./PipelineRequests.md#pipeline_version_requests_batch_cancel) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/cancel | Cancel multiple pipeline version requests
[**pipeline_version_requests_batch_delete**](./PipelineRequests.md#pipeline_version_requests_batch_delete) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/delete | Delete multiple pipeline version requests
[**pipeline_version_requests_batch_get**](./PipelineRequests.md#pipeline_version_requests_batch_get) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/collect | Retrieve multiple pipeline version requests
[**pipeline_version_requests_create**](./PipelineRequests.md#pipeline_version_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests | Create a pipeline version request
[**pipeline_version_requests_delete**](./PipelineRequests.md#pipeline_version_requests_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/{request_id} | Delete a pipeline version request
[**pipeline_version_requests_get**](./PipelineRequests.md#pipeline_version_requests_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/{request_id} | Get a pipeline version request
[**pipeline_version_requests_input_get**](./PipelineRequests.md#pipeline_version_requests_input_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/{request_id}/input | Get a pipeline request input
[**pipeline_version_requests_list**](./PipelineRequests.md#pipeline_version_requests_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests | List pipeline version requests
[**pipeline_version_requests_output_get**](./PipelineRequests.md#pipeline_version_requests_output_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/{request_id}/output | Get a pipeline request output
[**pipeline_version_requests_update**](./PipelineRequests.md#pipeline_version_requests_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/{request_id} | Update a pipeline version request


# **batch_pipeline_requests_create**
> list[PipelineRequestBatchCreateResponse] batch_pipeline_requests_create(project_name, pipeline_name, data, timeout=timeout, priority=priority)

Create a batch pipeline request

## Description
Make a batch request to the default version of a pipeline. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the pipeline request collect methods.

The maximum number of requests that can be created per batch is 250.

### Required Parameters
In case of structured input pipeline: A list of dictionaries, where each dictionary contains the input fields of the pipeline as keys. It is also possible to send a single dictionary as input.
In case of plain input pipeline: A list of strings. It is also possible to send a single string as input.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the entire pipeline request in seconds. The maximum allowed value is 172800 (48 hours) and the default value is 14400 (4 hours).
The deployment request timeouts are calculated at each step with the remaining timeout for the pipeline request.
- `priority`: Priority level of the request. O: high priority, 1: standard priority.

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

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
data = [{'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'}] # list[str or dict()]
timeout = 56 # int (optional)
priority = 56 # int (optional)

# Create a batch pipeline request
api_response = core_api.batch_pipeline_requests_create(project_name, pipeline_name, data, timeout=timeout, priority=priority)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **data** | **list[str or dict()]** | 
 **timeout** | **int** | [optional] 
 **priority** | **int** | [optional] 

### Return type

[**list[PipelineRequestBatchCreateResponse]**](./models/PipelineRequestBatchCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **batch_pipeline_version_requests_create**
> list[PipelineRequestBatchCreateResponse] batch_pipeline_version_requests_create(project_name, pipeline_name, version, data, timeout=timeout, priority=priority)

Create a batch pipeline version request

## Description
Make a batch request to a pipeline version. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the pipeline version request collect methods.

The maximum number of requests that can be created per batch is 250.

### Required Parameters
In case of structured input pipeline: A list of dictionaries, where each dictionary contains the input fields of the pipeline as keys. It is also possible to send a single dictionary as input.
In case of plain input pipeline: A list of strings. It is also possible to send a single string as input.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the entire pipeline request in seconds. The maximum allowed value is 172800 (48 hours) and the default value is 14400 (4 hours).
The deployment request timeouts are calculated at each step with the remaining timeout for the pipeline request.
- `priority`: Priority level of the request. O: high priority, 1: standard priority.

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

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
version = 'version_example' # str
data = [{'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'}] # list[str or dict()]
timeout = 56 # int (optional)
priority = 56 # int (optional)

# Create a batch pipeline version request
api_response = core_api.batch_pipeline_version_requests_create(project_name, pipeline_name, version, data, timeout=timeout, priority=priority)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 
 **data** | **list[str or dict()]** | 
 **timeout** | **int** | [optional] 
 **priority** | **int** | [optional] 

### Return type

[**list[PipelineRequestBatchCreateResponse]**](./models/PipelineRequestBatchCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_batch_cancel**
> object pipeline_requests_batch_cancel(project_name, pipeline_name, data, status=status)

Cancel multiple pipeline requests

## Description
Cancel multiple pipeline requests for the default version of a pipeline. A maximum of 250 pipeline requests can be cancelled with this method.

To cancel all pending or processing requests, use the query parameter `status`, with the value 'pending' or 'processing', with an empty request body.

### Required Parameters
A list of ids for the requests

## Request Examples

```
["2521378e-263e-4e2e-85e9-a96254b36536", "69eca481-8576-49e8-8e20-ea56f2005bcb"]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
data = ['request_id_1', 'request_id_2'] # list[str]
status = 'status_example' # str (optional)

# Cancel multiple pipeline requests
api_response = core_api.pipeline_requests_batch_cancel(project_name, pipeline_name, data, status=status)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **data** | **list[str]** | 
 **status** | **str** | [optional] 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_batch_delete**
> object pipeline_requests_batch_delete(project_name, pipeline_name, data)

Delete multiple pipeline requests

## Description
Delete multiple pipeline requests for the default version of a pipeline. If one of the given pipeline requests does not exist, an error message is given and no request is deleted. A maximum of 250 pipeline requests can be deleted with this method.

### Required Parameters
A list of ids of the requests

## Request Examples

```
["2521378e-263e-4e2e-85e9-a96254b36536", "69eca481-8576-49e8-8e20-ea56f2005bcb"]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
data = ['request_id_1', 'request_id_2'] # list[str]

# Delete multiple pipeline requests
api_response = core_api.pipeline_requests_batch_delete(project_name, pipeline_name, data)
print(api_response)
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
Retrieve multiple pipeline requests for the default version of a pipeline. If one of the given pipeline requests does not exist, an error message is given and no request is returned. A maximum of 250 pipeline requests can be retrieved with this method. The pipeline requests are NOT returned in the order they are given in.

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
- `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
- `time_created`: Datetime when the request is created
- `time_started`: Datetime when the request starts to be processed
- `time_completed`: Datetime when the request is completed
- `request_data`: [DEPRECATED] Input of the request. This field is deprecated, use '/input' to download the input data of the request.
- `result`: [DEPRECATED] Output of the request. This field is deprecated, use '/output' to download the result of the request.
- `error_message`: An error message explaining why the request has failed. It is set to null if the request was successful.
- `pipeline_timeout`: Timeout of the pipeline request in seconds
- `deployment_timeout`: Timeout for each deployment request in this pipeline request in seconds
- `input_size`: Size of the request data
- `output_size`: Size of the result
- `deployment_requests`: A list of requests to the deployments in the pipeline. With the request ids provided in this list, it's possible to collect the results of the deployment requests separately.
- `operator_requests`: A list of requests of the operators in the pipeline. With the request ids provided in this list, it's possible to collect the results of the operator requests separately.
- `pipeline_requests`: A list of requests to the sub-pipelines in the pipeline. With the request ids provided in this list, it's possible to collect the results of the sub-pipeline requests separately.

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-063-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {"input_field": 23.5},
    "result": {"output_field": 23.5},
    "error_message": null,
    "pipeline_timeout": 300,
    "deployment_timeout": 300,
    "input_size": 20,
    "output_size": 21,
    "deployment_requests": [
      {
        "id": "4b9c8a81-b3ef-437a-8d35-187490eda3e4",
        "time_created": "2025-12-01T20:00:00.000+00:00",
        "time_started": "2025-12-01T20:00:05.000+00:00",
        "time_completed": "2025-12-01T20:00:10.000+00:00",
        "pipeline_object": "deployment-1-v1-object",
        "deployment": "deployment-1",
        "version": "v1",
        "sequence_id": "16699092560130860",
        "status": "completed",
        "success": true,
        "error_message": null,
        "input_size": 10,
        "output_size": 10
      }
    ],
    "operator_requests": [
      {
        "id": "bd6d6ce5-ba9d-4c91-af61-0cf16f1f5452",
        "time_created": "2025-12-01T20:01:00.000+00:00",
        "time_started": "2025-12-01T20:01:05.000+00:00",
        "time_completed": "2025-12-01T20:01:10.000+00:00",
        "pipeline_object": "function-1",
        "operator": "function",
        "sequence_id": "16699092560130861",
        "status": "completed",
        "success": true,
        "error_message": null,
        "input_size": 10,
        "output_size": 10
      }
    ],
    "pipeline_requests": [
      {
        "id": "73d673b3-79e0-466e-af44-d841087a5c15",
        "time_created": "2025-12-01T20:02:00.000+00:00",
        "time_started": "2025-12-01T20:02:05.000+00:00",
        "time_completed": "2025-12-01T20:02:10.000+00:00",
        "pipeline_object": "sub-pipeline-1-v1-object",
        "pipeline": "pipeline-1",
        "version": "v1",
        "sequence_id": "16699092560130890",
        "status": "completed",
        "success": true,
        "error_message": null,
        "input_size": 10,
        "output_size": 10
      }
    ]
  },
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "processing",
    "success": false,
    "time_created": "2020-063-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": null,
    "request_data": {"input_field": 23.5},
    "result": null,
    "error_message": null,
    "pipeline_timeout": 300,
    "deployment_timeout": 300,
    "input_size": 20,
    "output_size": null,
    "deployment_requests": [
      {
        "id": "5fa86ad1-7949-48f5-8e2c-210cce78f427",
        "time_created": "2025-12-01T20:00:00.000+00:00",
        "time_started": "2025-12-01T20:00:05.000+00:00",
        "time_completed": "2025-12-01T20:00:10.000+00:00",
        "pipeline_object": "deployment-1-v1-object",
        "deployment": "deployment-1",
        "version": "v1",
        "sequence_id": "16699092560130860",
        "status": "processing",
        "success": false,
        "error_message": null,
        "input_size": 10,
        "output_size": null
      }
    ],
    "operator_requests": [],
    "pipeline_requests": []
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
data = ['request_id_1', 'request_id_2'] # list[str]

# Retrieve multiple pipeline requests
api_response = core_api.pipeline_requests_batch_get(project_name, pipeline_name, data)
print(api_response)
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
> PipelineRequestCreateResponse pipeline_requests_create(project_name, pipeline_name, data, timeout=timeout, priority=priority, pipeline_timeout=pipeline_timeout)

Create a pipeline request

## Description
Make a direct request to the default version of a pipeline. This method returns the request ids for each pipeline object, with which the result can be retrieved separately.

### Required Parameters
The input for the request. In case of a structured pipeline, this is a dictionary which contains the input fields of the pipeline as keys. In case of a plain pipeline, give a string or list of strings.

### Optional Parameters
The following parameters should be given as query parameters:

- `timeout`: Timeout for the entire pipeline request in seconds. The maximum allowed value is 7200 (2 hours) and the default value is 3600 (1 hour).
The deployment request timeouts are calculated at each step with the remaining timeout for the pipeline request.
- `priority`: Priority level of the request. O: high priority, 1: standard priority.

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
- `status`: Status of the pipeline request. It can be 'completed' or 'failed'.
- `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `deployment_requests`: A list of dictionaries containing the results of the deployment requests made for the deployment objects in the pipeline. The dictionaries contain the following fields:
    - `id`: Unique identifier for the deployment request
    - `time_created`: Server time that the request was created
    - `time_started`: Server time that the request was started
    - `time_completed`: Server time that the request was completed
    - `pipeline_object`: Name of the object in the pipeline
    - `deployment`: Name of the deployment the request was made to
    - `version`: Name of the version the request was made to
    - `status`: Status of the request. It can be 'completed' or 'failed'.
    - `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
    - `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
    - `sequence_id`: The sequence id based on creation date and index of bulk creation, used for sorting
- `operator_requests`: A list of dictionaries containing the results of the operator requests made for the operator objects in the pipeline. The dictionaries contain the following fields:
    - `id`: Unique identifier for the operator request
    - `time_created`: Server time that the request was created
    - `time_started`: Server time that the request was started
    - `time_completed`: Server time that the request was completed
    - `pipeline_object`: Name of the object in the pipeline
    - `operator`: Name of the operator the request was made to
    - `status`: Status of the request. It can be 'completed' or 'failed'.
    - `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
    - `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
    - `sequence_id`: The sequence id based on creation date and index of bulk creation, used for sorting
- `pipeline_requests`: A list of dictionaries containing the results of the sub-pipeline requests made for the sub-pipeline objects in the pipeline. The dictionaries contain the following fields:
    - `id`: Unique identifier for the sub-pipeline request
    - `time_created`: Server time that the request was created
    - `time_started`: Server time that the request was started
    - `time_completed`: Server time that the request was completed
    - `pipeline_object`: Name of the object in the pipeline
    - `pipeline`: Name of the sub-pipeline the request was made to
    - `version`: Name of the version the request was made to
    - `status`: Status of the request. It can be 'completed' or 'failed'.
    - `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
    - `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
    - `sequence_id`: The sequence id based on creation date and index of bulk creation, used for sorting
- `result`: A dictionary (structured output type) or string (plain output type) containing the data connected to the pipeline end
- `pipeline_timeout`: Timeout of the pipeline request in seconds
- `deployment_timeout`: Timeout for each deployment request in this pipeline request in seconds

## Response Examples

```
{
  "id": "286f771b-6617-4985-ab49-12ed720e62b1",
  "pipeline": "pipeline-1",
  "version": "v1",
  "status": "failed",
  "success": false,
  "error_message": "Error while processing a deployment request",
  "deployment_requests": [
    {
      "id": "a7524614-bdb7-41e1-b4c1-653bb72c30b4",
      "time_created": "2025-12-01T20:00:00.000+00:00",
      "time_started": "2025-12-01T20:00:05.000+00:00",
      "time_completed": "2025-12-01T20:00:10.000+00:00",
      "pipeline_object": "deployment-object-1",
      "deployment": "deployment-1",
      "version": "v1",
      "sequence_id": "16699092560130860",
      "status": "completed",
      "success": true,
      "error_message": null
    },
    {
      "id": "fe322c50-58f8-4e67-b7d6-cba14273874e",
      "time_created": "2025-12-01T20:01:00.000+00:00",
      "time_started": "2025-12-01T20:01:05.000+00:00",
      "time_completed": "2025-12-01T20:01:10.000+00:00",
      "pipeline_object": "deployment-object-2",
      "deployment": "deployment-2",
      "version": "v1",
      "sequence_id": "16699092560130861",
      "status": "failed",
      "success": false,
      "error_message": "Invalid message format"
    }
  ],
  "operator_requests": [
    {
      "id": "bd6d6ce5-ba9d-4c91-af61-0cf16f1f5452",
      "time_created": "2025-12-01T20:02:00.000+00:00",
      "time_started": "2025-12-01T20:02:05.000+00:00",
      "time_completed": "2025-12-01T20:02:10.000+00:00",
      "pipeline_object": "function-1",
      "operator": "function",
      "sequence_id": "16699092560130860",
      "status": "completed",
      "success": true,
      "error_message": null
    }
  ],
  "pipeline_requests": [
    {
      "id": "dd307a3e-6eb0-4a55-981b-52e277529df1",
      "time_created": "2025-12-01T20:03:00.000+00:00",
      "time_started": "2025-12-01T20:03:05.000+00:00",
      "time_completed": "2025-12-01T20:03:10.000+00:00",
      "pipeline_object": "sub-pipeline-object-1",
      "pipeline": "pipeline-1",
      "version": "v1",
      "sequence_id": "16699092560130890",
      "status": "completed",
      "success": true,
      "error_message": null
    },
    {
      "id": "411aa6f8-7706-45e7-9438-892e399947a1",
      "time_created": "2025-12-01T20:04:00.000+00:00",
      "time_started": "2025-12-01T20:04:05.000+00:00",
      "time_completed": "2025-12-01T20:04:10.000+00:00",
      "pipeline_object": "sub-pipeline-object-2",
      "pipeline": "pipeline-2",
      "version": "v1",
      "sequence_id": "16699092560130891",
      "status": "failed",
      "success": false,
      "error_message": "Invalid message format"
    }
  ],
  "result": {"output_field": 23.5},
  "pipeline_timeout": 300,
  "deployment_timeout": 300
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
data = {'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'} # str or dict()
timeout = 56 # int (optional)
priority = 56 # int (optional)
pipeline_timeout = 56 # int (optional)

# Create a pipeline request
api_response = core_api.pipeline_requests_create(project_name, pipeline_name, data, timeout=timeout, priority=priority, pipeline_timeout=pipeline_timeout)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **data** | **str or dict()** | 
 **timeout** | **int** | [optional] 
 **priority** | **int** | [optional] 
 **pipeline_timeout** | **int** | [optional] 

### Return type

[**PipelineRequestCreateResponse**](./models/PipelineRequestCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_delete**
> pipeline_requests_delete(project_name, pipeline_name, request_id)

Delete a pipeline request

## Description
Delete a request for the default version of a pipeline. This action deletes all the subrequests in the pipeline.

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
request_id = 'request_id_example' # str

# Delete a pipeline request
core_api.pipeline_requests_delete(project_name, pipeline_name, request_id)
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
Get the details of a request for the default version of a pipeline

### Optional Parameters
The following parameters should be given as query parameters:

- `metadata_only`: [DEPRECATED] A boolean value that indicates whether the response should include the request data and result, defaults to False

### Response Structure
A dictionary containing the details of the pipeline request with the following fields:

- `id`: Unique identifier for the pipeline request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request was made
- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'.
- `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
- `time_created`: Datetime when the request is created
- `time_started`: Datetime when the request starts to be processed
- `time_completed`: Datetime when the request is completed
- `request_data`: [DEPRECATED] Input of the request. This field is deprecated, use '/input' to download the input data of the request.
- `result`: [DEPRECATED] Output of the request. This field is deprecated, use '/output' to download the result of the request.
- `error_message`: An error message explaining why the request has failed. It is set to null if the request was successful.
- `pipeline_timeout`: Timeout of the pipeline request in seconds
- `deployment_timeout`: Timeout for each deployment request in this pipeline request in seconds
- `origin`: A dictionary containing the information on where the request originated from. It contains:
    - a `created_by` field with the email of the user that created the request. In case the request is created by a service, the field will have a "UbiOps" value.
- `input_size`: Size of the request data
- `output_size`: Size of the result
- `deployment_requests`: A list of requests of the deployments in the pipeline. With the request ids provided in this list, it's possible to collect the results of the deployment requests separately.
- `operator_requests`: A list of requests of the operators in the pipeline. With the request ids provided in this list, it's possible to collect the results of the operator requests separately.
- `pipeline_requests`: A list of requests of the sub-pipelines in the pipeline. With the request ids provided in this list, it's possible to collect the results of the sub-pipeline requests separately.

## Response Examples

```
{
  "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
  "pipeline": "pipeline-1",
  "version": "v1",
  "status": "completed",
  "success": true,
  "time_created": "2020-03-28T20:00:26.613+00:00",
  "time_started": "2020-03-28T20:00:41.276+00:00",
  "time_completed": "2020-03-28T20:00:42.241+00:00",
  "request_data": {"input_field": 23.5},
  "result": {"output_field": 23.5},
  "error_message": null,
  "pipeline_timeout": 300,
  "deployment_timeout": 300,
  "origin": {
    "created_by": "my.example.user@ubiops.com"
  },
  "input_size": 20,
  "output_size": 21,
  "deployment_requests": [
    {
      "id": "4b9c8a81-b3ef-437a-8d35-187490eda3e4",
      "time_created": "2025-12-01T20:00:00.000+00:00",
      "time_started": "2025-12-01T20:00:05.000+00:00",
      "time_completed": "2025-12-01T20:00:10.000+00:00",
      "pipeline_object": "deployment-1-v1-object",
      "deployment": "deployment-1",
      "version": "v1",
      "sequence_id": "16699092560130860",
      "status": "completed",
      "success": true,
      "error_message": null,
      "input_size": 10,
      "output_size": 10
    }
  ],
  "operator_requests": [
    {
      "id": "bd6d6ce5-ba9d-4c91-af61-0cf16f1f5452",
      "time_created": "2025-12-01T20:01:00.000+00:00",
      "time_started": "2025-12-01T20:01:05.000+00:00",
      "time_completed": "2025-12-01T20:01:10.000+00:00",
      "pipeline_object": "function-1",
      "operator": "function",
      "sequence_id": "16699092560130861",
      "status": "completed",
      "success": true,
      "error_message": null,
      "input_size": 10,
      "output_size": 10
    }
  ],
  "pipeline_requests": [
    {
      "id": "a152612e-b5d1-4f44-a04b-fe4a26849b02",
      "time_created": "2025-12-01T20:02:00.000+00:00",
      "time_started": "2025-12-01T20:02:05.000+00:00",
      "time_completed": "2025-12-01T20:02:10.000+00:00",
      "pipeline_object": "sub-pipeline-1-v1-object",
      "pipeline": "pipeline-1",
      "version": "v1",
      "sequence_id": "1669909256013090",
      "status": "completed",
      "success": true,
      "error_message": null,
      "input_size": 10,
      "output_size": 10
    }
  ]
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
request_id = 'request_id_example' # str
metadata_only = True # bool (optional)

# Get a pipeline request
api_response = core_api.pipeline_requests_get(project_name, pipeline_name, request_id, metadata_only=metadata_only)
print(api_response)
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

# **pipeline_requests_input_get**
> file pipeline_requests_input_get(project_name, pipeline_name, request_id)

Get a pipeline request input

## Description
Get the input of a request for the default version of a pipeline

### Response Structure
Input of the pipeline request as a file

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
request_id = 'request_id_example' # str

# Get a pipeline request input
api_response = core_api.pipeline_requests_input_get(project_name, pipeline_name, request_id)
result = api_response.json()
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 

### Return type

**file**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_list**
> list[PipelineRequestList] pipeline_requests_list(project_name, pipeline_name, status=status, limit=limit, offset=offset, start_date=start_date, end_date=end_date, search_id=search_id)

List pipeline requests

## Description
List all requests for the default version of a pipeline

### Optional Parameters
The following parameters should be given as query parameters:

- `status`: Status of the request, one of the following 'pending', 'processing', 'failed', 'completed' or 'cancelled', defaults to 'completed'. A combination of statuses can also be requested. 'pending' and 'processing' requests cannot be combined with other statuses.
- `limit`: The maximum number of requests given back, default is 50
- `offset`: The number which forms the starting point of the requests given back. If offset equals 2, then the first 2 requests will be omitted from the list.
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
- `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
- `time_created`: Datetime when the request is created
- `time_started`: Datetime when the request starts to be processed
- `time_completed`: Datetime when the request is completed
- `input_size`: Size of the request data
- `output_size`: Size of the result

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
    "time_started": null,
    "time_completed": null,
    "input_size": 10,
    "output_size": null
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": null,
    "time_completed": null,
    "input_size": 10,
    "output_size": null
  }
]
```

With start_date="2020-03-28T20:00:26+00:00" and end_date="2020-03-28T22:00:26+00:00":

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T20:00:43.613+00:00",
    "time_started": "2020-03-28T20:00:50.276+00:00",
    "time_completed": "2020-03-28T20:00:55.241+00:00",
    "input_size": 10,
    "output_size": 10
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T21:12:45.613+00:00",
    "time_started": "2020-03-28T21:13:00.276+00:00",
    "time_completed": "2020-03-28T21:13:05.241+00:00",
    "input_size": 10,
    "output_size": 10
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
status = 'status_example' # str (optional)
limit = 56 # int (optional)
offset = 56 # int (optional)
start_date = 'start_date_example' # str (optional)
end_date = 'end_date_example' # str (optional)
search_id = 'search_id_example' # str (optional)

# List pipeline requests
api_response = core_api.pipeline_requests_list(project_name, pipeline_name, status=status, limit=limit, offset=offset, start_date=start_date, end_date=end_date, search_id=search_id)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **status** | **str** | [optional] 
 **limit** | **int** | [optional] 
 **offset** | **int** | [optional] 
 **start_date** | **str** | [optional] 
 **end_date** | **str** | [optional] 
 **search_id** | **str** | [optional] 

### Return type

[**list[PipelineRequestList]**](./models/PipelineRequestList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_output_get**
> file pipeline_requests_output_get(project_name, pipeline_name, request_id)

Get a pipeline request output

## Description
Get the output of a request for the default version of a pipeline

### Response Structure
Output of the pipeline request as a file

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
request_id = 'request_id_example' # str

# Get a pipeline request output
api_response = core_api.pipeline_requests_output_get(project_name, pipeline_name, request_id)
result = api_response.json()
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 

### Return type

**file**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_update**
> object pipeline_requests_update(project_name, pipeline_name, request_id, data)

Update a pipeline request

## Description
Cancel a pipeline request for the default version of a pipeline

### Required Parameters

- `status`: Status that the request will be updated to. It can only be `cancelled`.

## Request Examples

```
{
"status": "cancelled"
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
request_id = 'request_id_example' # str
data = ubiops.PipelineRequestUpdate() # PipelineRequestUpdate

# Update a pipeline request
api_response = core_api.pipeline_requests_update(project_name, pipeline_name, request_id, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 
 **data** | [**PipelineRequestUpdate**](./models/PipelineRequestUpdate.md) | 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_object_requests_get**
> OperatorRequestDetail pipeline_version_object_requests_get(project_name, pipeline_name, request_id, version, metadata_only=metadata_only, pipeline_request_id=pipeline_request_id, pipeline_object_id=pipeline_object_id)

Get an operator request

## Description
Get a request for an operator object of a version of a pipeline. With this method, the result of the request may be retrieved.

### Optional Parameters
The following parameters should be given as query parameters:

- `metadata_only`: [DEPRECATED] A boolean value that indicates whether the response should include the request data and result, defaults to False
- `pipeline_request_id`: ID of pipeline request to which the operator request belongs
- `pipeline_object_id`: ID of pipeline object for which the operator request is created

### Response Structure
A dictionary containing the details of the operator request with the following fields:

- `id`: Unique identifier for the pipeline version object request
- `pipeline_request_id`: Unique identifier for the pipeline request to which the object request belongs
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request was made
- `object`: Name of the pipeline version object for which the request was made
- `operator`: Name of the pipeline operator for which the request was made
- `status`: Status of the request. Can be 'failed' or 'completed'.
- `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
- `time_created`: Datetime when the request is created
- `time_started`: Datetime when the request starts to be processed
- `time_completed`: Datetime when the request is completed
- `request_data`: [DEPRECATED] A dictionary containing the data that was sent when the request was created. This field is deprecated, use '/input' to download the input data of the request.
- `result`: [DEPRECATED] Request result value. This field is deprecated, use '/output' to download the result of the request.
- `error_message`: An error message explaining why the request has failed
- `input_size`: Size of the request data
- `output_size`: Size of the result

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
  "request_data": {"input_field": 23.5},
  "result": {"output": 23.5},
  "error_message": "",
  "input_size": 20,
  "output_size": 15
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
request_id = 'request_id_example' # str
version = 'version_example' # str
metadata_only = True # bool (optional)
pipeline_request_id = 'pipeline_request_id_example' # str (optional)
pipeline_object_id = 'pipeline_object_id_example' # str (optional)

# Get an operator request
api_response = core_api.pipeline_version_object_requests_get(project_name, pipeline_name, request_id, version, metadata_only=metadata_only, pipeline_request_id=pipeline_request_id, pipeline_object_id=pipeline_object_id)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 
 **version** | **str** | 
 **metadata_only** | **bool** | [optional] 
 **pipeline_request_id** | **str** | [optional] 
 **pipeline_object_id** | **str** | [optional] 

### Return type

[**OperatorRequestDetail**](./models/OperatorRequestDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_object_requests_input_get**
> file pipeline_version_object_requests_input_get(project_name, pipeline_name, request_id, version)

Get an operator request input

## Description
Get the input of an operator request of a version of a pipeline

### Response Structure
Input of the operator request as a file

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
request_id = 'request_id_example' # str
version = 'version_example' # str

# Get an operator request input
api_response = core_api.pipeline_version_object_requests_input_get(project_name, pipeline_name, request_id, version)
result = api_response.json()
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 
 **version** | **str** | 

### Return type

**file**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_object_requests_output_get**
> file pipeline_version_object_requests_output_get(project_name, pipeline_name, request_id, version)

Get an operator request output

## Description
Get the output of an operator request of a version of a pipeline

### Response Structure
Output of the operator request as a file

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
request_id = 'request_id_example' # str
version = 'version_example' # str

# Get an operator request output
api_response = core_api.pipeline_version_object_requests_output_get(project_name, pipeline_name, request_id, version)
result = api_response.json()
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 
 **version** | **str** | 

### Return type

**file**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_batch_cancel**
> object pipeline_version_requests_batch_cancel(project_name, pipeline_name, version, data, status=status)

Cancel multiple pipeline version requests

## Description
Cancel multiple requests for a pipeline version. A maximum of 250 pipeline requests can be deleted with this method.

To cancel all pending or processing requests, use the query parameter `status`, with the value 'pending' or 'processing', with an empty request body.

### Required Parameters
A list of ids for the requests

## Request Examples

```
["2521378e-263e-4e2e-85e9-a96254b36536", "69eca481-8576-49e8-8e20-ea56f2005bcb"]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
version = 'version_example' # str
data = ['request_id_1', 'request_id_2'] # list[str]
status = 'status_example' # str (optional)

# Cancel multiple pipeline version requests
api_response = core_api.pipeline_version_requests_batch_cancel(project_name, pipeline_name, version, data, status=status)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 
 **data** | **list[str]** | 
 **status** | **str** | [optional] 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_batch_delete**
> object pipeline_version_requests_batch_delete(project_name, pipeline_name, version, data)

Delete multiple pipeline version requests

## Description
Delete multiple requests for a pipeline version. If one of the given pipeline requests does not exist, an error message is given and no request is deleted. A maximum of 250 pipeline requests can be deleted with this method.

### Required Parameters
A list of ids of the requests

## Request Examples

```
["2521378e-263e-4e2e-85e9-a96254b36536", "69eca481-8576-49e8-8e20-ea56f2005bcb"]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
version = 'version_example' # str
data = ['request_id_1', 'request_id_2'] # list[str]

# Delete multiple pipeline version requests
api_response = core_api.pipeline_version_requests_batch_delete(project_name, pipeline_name, version, data)
print(api_response)
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
Retrieve multiple requests for a pipeline version. If one of the given pipeline requests does not exist, an error message is given and no request is returned. A maximum of 250 pipeline version requests can be retrieved with this method. The pipeline version requests are NOT returned in the order they are given in.

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
- `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
- `time_created`: Datetime when the request is created
- `time_started`: Datetime when the request starts to be processed
- `time_completed`: Datetime when the request is completed
- `request_data`: [DEPRECATED] Input of the request. This field is deprecated, use '/input' to download the input data of the request.
- `result`: [DEPRECATED] Output of the request. This field is deprecated, use '/output' to download the result of the request.
- `error_message`: An error message explaining why the request has failed. It is set to null if the request was successful.
- `pipeline_timeout`: Timeout of the pipeline request in seconds
- `deployment_timeout`: Timeout for each deployment request in this pipeline request in seconds
- `input_size`: Size of the request data
- `output_size`: Size of the result
- `deployment_requests`: A list of requests to the deployments in the pipeline. With the request ids provided in this list, it's possible to collect the results of the deployment requests separately.
- `operator_requests`: A list of requests of the operators in the pipeline. With the request ids provided in this list, it's possible to collect the results of the operator requests separately.
- `pipeline_requests`: A list of requests to the sub-pipelines in the pipeline. With the request ids provided in this list, it's possible to collect the results of the sub-pipeline requests separately.

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-063-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {"input_field": 23.5},
    "result": {"output_field": 23.5},
    "error_message": null,
    "pipeline_timeout": 300,
    "deployment_timeout": 300,
    "input_size": 20,
    "output_size": 21,
    "deployment_requests": [
      {
        "id": "4b9c8a81-b3ef-437a-8d35-187490eda3e4",
        "time_created": "2025-12-01T20:00:00.000+00:00",
        "time_started": "2025-12-01T20:00:05.000+00:00",
        "time_completed": "2025-12-01T20:00:10.000+00:00",
        "pipeline_object": "deployment-1-v1-object",
        "deployment": "deployment-1",
        "version": "v1",
        "sequence_id": "16699092560130860",
        "status": "completed",
        "success": true,
        "error_message": null,
        "input_size": 10,
        "output_size": 10
      }
    ],
    "operator_requests": [
      {
        "id": "bd6d6ce5-ba9d-4c91-af61-0cf16f1f5452",
        "time_created": "2025-12-01T20:01:00.000+00:00",
        "time_started": "2025-12-01T20:01:05.000+00:00",
        "time_completed": "2025-12-01T20:01:10.000+00:00",
        "pipeline_object": "function-1",
        "operator": "function",
        "sequence_id": "16699092560130861",
        "status": "completed",
        "success": true,
        "error_message": null,
        "input_size": 10,
        "output_size": 10
      }
    ],
    "pipeline_requests": [
      {
        "id": "73d673b3-79e0-466e-af44-d841087a5c15",
        "time_created": "2025-12-01T20:02:00.000+00:00",
        "time_started": "2025-12-01T20:02:05.000+00:00",
        "time_completed": "2025-12-01T20:02:10.000+00:00",
        "pipeline_object": "sub-pipeline-1-v1-object",
        "pipeline": "pipeline-1",
        "version": "v1",
        "sequence_id": "16699092560130890",
        "status": "completed",
        "success": true,
        "error_message": null,
        "input_size": 10,
        "output_size": 10
      }
    ]
  },
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "processing",
    "success": false,
    "time_created": "2020-063-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": null,
    "request_data": {"input_field": 23.5},
    "result": null,
    "error_message": null,
    "pipeline_timeout": 300,
    "deployment_timeout": 300,
    "input_size": 20,
    "output_size": null,
    "deployment_requests": [
      {
        "id": "5fa86ad1-7949-48f5-8e2c-210cce78f427",
        "time_created": "2025-12-01T20:00:00.000+00:00",
        "time_started": "2025-12-01T20:00:05.000+00:00",
        "time_completed": "2025-12-01T20:00:10.000+00:00",
        "pipeline_object": "deployment-1-v1-object",
        "deployment": "deployment-1",
        "version": "v1",
        "sequence_id": "16699092560130860",
        "status": "processing",
        "success": false,
        "error_message": null,
        "input_size": 10,
        "output_size": null
      }
    ],
    "operator_requests": [],
    "pipeline_requests": []
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
version = 'version_example' # str
data = ['request_id_1', 'request_id_2'] # list[str]

# Retrieve multiple pipeline version requests
api_response = core_api.pipeline_version_requests_batch_get(project_name, pipeline_name, version, data)
print(api_response)
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
> PipelineRequestCreateResponse pipeline_version_requests_create(project_name, pipeline_name, version, data, timeout=timeout, priority=priority, pipeline_timeout=pipeline_timeout)

Create a pipeline version request

## Description
Make a direct request to a pipeline version. This method returns the request ids for each pipeline object, with which the result can be retrieved separately.

### Required Parameters
The input for the request. In case of a structured pipeline, this is a dictionary which contains the input fields of the pipeline as keys. In case of a plain pipeline, give a string or list of strings.

### Optional Parameters
The following parameters should be given as query parameters:

- `timeout`: Timeout for the entire pipeline request in seconds. The maximum allowed value is 7200 (2 hours) and the default value is 3600 (1 hour).
The deployment request timeouts are calculated at each step with the remaining timeout for the pipeline request.
- `priority`: Priority level of the request. O: high priority, 1: standard priority.

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
- `status`: Status of the pipeline request. It can be 'completed' or 'failed'.
- `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `deployment_requests`: A list of dictionaries containing the results of the deployment requests made for the deployment objects in the pipeline. The dictionaries contain the following fields:
    - `id`: Unique identifier for the deployment request
    - `time_created`: Server time that the request was created
    - `time_started`: Server time that the request was started
    - `time_completed`: Server time that the request was completed
    - `pipeline_object`: Name of the object in the pipeline
    - `deployment`: Name of the deployment the request was made to
    - `version`: Name of the version the request was made to
    - `status`: Status of the request. It can be 'completed' or 'failed'.
    - `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
    - `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
    - `sequence_id`: The sequence id based on creation date and index of bulk creation, used for sorting
- `operator_requests`: A list of dictionaries containing the results of the operator requests made for the operator objects in the pipeline. The dictionaries contain the following fields:
    - `id`: Unique identifier for the operator request
    - `time_created`: Server time that the request was created
    - `time_started`: Server time that the request was started
    - `time_completed`: Server time that the request was completed
    - `pipeline_object`: Name of the object in the pipeline
    - `operator`: Name of the operator the request was made to
    - `status`: Status of the request. It can be 'completed' or 'failed'.
    - `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
    - `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
    - `sequence_id`: The sequence id based on creation date and index of bulk creation, used for sorting
- `pipeline_requests`: A list of dictionaries containing the results of the sub-pipeline requests made for the sub-pipeline objects in the pipeline. The dictionaries contain the following fields:
    - `id`: Unique identifier for the sub-pipeline request
    - `time_created`: Server time that the request was created
    - `time_started`: Server time that the request was started
    - `time_completed`: Server time that the request was completed
    - `pipeline_object`: Name of the object in the pipeline
    - `pipeline`: Name of the sub-pipeline the request was made to
    - `version`: Name of the version the request was made to
    - `status`: Status of the request. It can be 'completed' or 'failed'.
    - `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
    - `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
    - `sequence_id`: The sequence id based on creation date and index of bulk creation, used for sorting
- `result`: A dictionary (structured output type) or string (plain output type) containing the data connected to the pipeline end
- `pipeline_timeout`: Timeout of the pipeline request in seconds
- `deployment_timeout`: Timeout for each deployment request in this pipeline request in seconds

## Response Examples

```
{
  "id": "286f771b-6617-4985-ab49-12ed720e62b1",
  "project": "project-1",
  "pipeline": "pipeline-1",
  "version": "v1",
  "status": "failed",
  "success": false,
  "error_message": "Error while processing a deployment request",
  "deployment_requests": [
    {
      "id": "a7524614-bdb7-41e1-b4c1-653bb72c30b4",
      "time_created": "2025-12-01T20:00:00.000+00:00",
      "time_started": "2025-12-01T20:00:05.000+00:00",
      "time_completed": "2025-12-01T20:00:10.000+00:00",
      "pipeline_object": "deployment-object-1",
      "deployment": "deployment-1",
      "version": "v1",
      "sequence_id": "16699092560130860",
      "status": "completed",
      "success": true,
      "error_message": null
    },
    {
      "id": "fe322c50-58f8-4e67-b7d6-cba14273874e",
      "time_created": "2025-12-01T20:01:00.000+00:00",
      "time_started": "2025-12-01T20:01:05.000+00:00",
      "time_completed": "2025-12-01T20:01:10.000+00:00",
      "pipeline_object": "deployment-object-2",
      "deployment": "deployment-2",
      "version": "v1",
      "sequence_id": "16699092560130861",
      "status": "failed",
      "success": false,
      "error_message": "Invalid message format"
    }
  ],
  "operator_requests": [
    {
      "id": "bd6d6ce5-ba9d-4c91-af61-0cf16f1f5452",
      "time_created": "2025-12-01T20:02:00.000+00:00",
      "time_started": "2025-12-01T20:02:05.000+00:00",
      "time_completed": "2025-12-01T20:02:10.000+00:00",
      "pipeline_object": "function-1",
      "operator": "function",
      "sequence_id": "16699092560130860",
      "status": "completed",
      "success": true,
      "error_message": null
    }
  ],
  "pipeline_requests": [
    {
      "id": "dd307a3e-6eb0-4a55-981b-52e277529df1",
      "time_created": "2025-12-01T20:03:00.000+00:00",
      "time_started": "2025-12-01T20:03:05.000+00:00",
      "time_completed": "2025-12-01T20:03:10.000+00:00",
      "pipeline_object": "sub-pipeline-object-1",
      "pipeline": "pipeline-1",
      "version": "v1",
      "sequence_id": "16699092560130890",
      "status": "completed",
      "success": true,
      "error_message": null
    },
    {
      "id": "411aa6f8-7706-45e7-9438-892e399947a1",
      "time_created": "2025-12-01T20:04:00.000+00:00",
      "time_started": "2025-12-01T20:04:05.000+00:00",
      "time_completed": "2025-12-01T20:04:10.000+00:00",
      "pipeline_object": "sub-pipeline-object-2",
      "pipeline": "pipeline-2",
      "version": "v1",
      "sequence_id": "16699092560130891",
      "status": "failed",
      "success": false,
      "error_message": "Invalid message format"
    }
  ],
  "result": {"output_field": 23.5},
  "pipeline_timeout": 300,
  "deployment_timeout": 300
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
version = 'version_example' # str
data = {'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'} # str or dict()
timeout = 56 # int (optional)
priority = 56 # int (optional)
pipeline_timeout = 56 # int (optional)

# Create a pipeline version request
api_response = core_api.pipeline_version_requests_create(project_name, pipeline_name, version, data, timeout=timeout, priority=priority, pipeline_timeout=pipeline_timeout)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 
 **data** | **str or dict()** | 
 **timeout** | **int** | [optional] 
 **priority** | **int** | [optional] 
 **pipeline_timeout** | **int** | [optional] 

### Return type

[**PipelineRequestCreateResponse**](./models/PipelineRequestCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_delete**
> pipeline_version_requests_delete(project_name, pipeline_name, request_id, version)

Delete a pipeline version request

## Description
Delete a request for a pipeline version. This action deletes all the subrequests in the pipeline.

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
request_id = 'request_id_example' # str
version = 'version_example' # str

# Delete a pipeline version request
core_api.pipeline_version_requests_delete(project_name, pipeline_name, request_id, version)
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
Get the details of a request for a pipeline version

### Optional Parameters
The following parameters should be given as query parameters:

- `metadata_only`: [DEPRECATED] A boolean value that indicates whether the response should include the request data and result, defaults to False

### Response Structure
A dictionary containing the details of the pipeline request with the following fields:

- `id`: Unique identifier for the pipeline request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request was made
- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'.
- `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
- `time_created`: Datetime when the request is created
- `time_started`: Datetime when the request starts to be processed
- `time_completed`: Datetime when the request is completed
- `request_data`: [DEPRECATED] Input of the request. This field is deprecated, use '/input' to download the input data of the request.
- `result`: [DEPRECATED] Output of the request. This field is deprecated, use '/output' to download the result of the request.
- `error_message`: An error message explaining why the request has failed. It is set to null if the request was successful.
- `pipeline_timeout`: Timeout of the pipeline request in seconds
- `deployment_timeout`: Timeout for each deployment request in this pipeline request in seconds
- `origin`: A dictionary containing the information on where the request originated from. It contains:
    - a `created_by` field with the email of the user that created the request. In case the request is created by a service, the field will have a "UbiOps" value.
- `input_size`: Size of the request data
- `output_size`: Size of the result
- `deployment_requests`: A list of requests of the deployments in the pipeline. With the request ids provided in this list, it's possible to collect the results of the deployment requests separately.
- `operator_requests`: A list of requests of the operators in the pipeline. With the request ids provided in this list, it's possible to collect the results of the operator requests separately.
- `pipeline_requests`: A list of requests of the sub-pipelines in the pipeline. With the request ids provided in this list, it's possible to collect the results of the sub-pipeline requests separately.

## Response Examples

```
{
  "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
  "pipeline": "pipeline-1",
  "version": "v1",
  "status": "completed",
  "success": true,
  "time_created": "2020-03-28T20:00:26.613+00:00",
  "time_started": "2020-03-28T20:00:41.276+00:00",
  "time_completed": "2020-03-28T20:00:42.241+00:00",
  "request_data": {"input_field": 23.5},
  "result": {"output_field": 23.5},
  "error_message": null,
  "pipeline_timeout": 300,
  "deployment_timeout": 300,
  "origin": {
    "created_by": "my.example.user@ubiops.com"
  },
  "input_size": 20,
  "output_size": 21,
  "deployment_requests": [
    {
      "id": "4b9c8a81-b3ef-437a-8d35-187490eda3e4",
      "time_created": "2025-12-01T20:00:00.000+00:00",
      "time_started": "2025-12-01T20:00:05.000+00:00",
      "time_completed": "2025-12-01T20:00:10.000+00:00",
      "pipeline_object": "deployment-1-v1-object",
      "deployment": "deployment-1",
      "version": "v1",
      "sequence_id": "16699092560130860",
      "status": "completed",
      "success": true,
      "error_message": null,
      "input_size": 10,
      "output_size": 10
    }
  ],
  "operator_requests": [
    {
      "id": "bd6d6ce5-ba9d-4c91-af61-0cf16f1f5452",
      "time_created": "2025-12-01T20:01:00.000+00:00",
      "time_started": "2025-12-01T20:01:05.000+00:00",
      "time_completed": "2025-12-01T20:01:10.000+00:00",
      "pipeline_object": "function-1",
      "operator": "function",
      "sequence_id": "16699092560130861",
      "status": "completed",
      "success": true,
      "error_message": null,
      "input_size": 10,
      "output_size": 10
    }
  ],
  "pipeline_requests": [
    {
      "id": "a152612e-b5d1-4f44-a04b-fe4a26849b02",
      "time_created": "2025-12-01T20:02:00.000+00:00",
      "time_started": "2025-12-01T20:02:05.000+00:00",
      "time_completed": "2025-12-01T20:02:10.000+00:00",
      "pipeline_object": "sub-pipeline-1-v1-object",
      "pipeline": "pipeline-1",
      "version": "v1",
      "sequence_id": "1669909256013090",
      "status": "completed",
      "success": true,
      "error_message": null,
      "input_size": 10,
      "output_size": 10
    }
  ]
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
request_id = 'request_id_example' # str
version = 'version_example' # str
metadata_only = True # bool (optional)

# Get a pipeline version request
api_response = core_api.pipeline_version_requests_get(project_name, pipeline_name, request_id, version, metadata_only=metadata_only)
print(api_response)
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

# **pipeline_version_requests_input_get**
> file pipeline_version_requests_input_get(project_name, pipeline_name, request_id, version)

Get a pipeline request input

## Description
Get the input of a request for a pipeline version

### Response Structure
Input of the pipeline request as a file

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
request_id = 'request_id_example' # str
version = 'version_example' # str

# Get a pipeline request input
api_response = core_api.pipeline_version_requests_input_get(project_name, pipeline_name, request_id, version)
result = api_response.json()
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 
 **version** | **str** | 

### Return type

**file**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_list**
> list[PipelineRequestList] pipeline_version_requests_list(project_name, pipeline_name, version, status=status, limit=limit, offset=offset, start_date=start_date, end_date=end_date, search_id=search_id)

List pipeline version requests

## Description
List all requests for a pipeline version

### Optional Parameters
The following parameters should be given as query parameters:

- `status`: Status of the request, one of the following 'pending', 'processing', 'failed', 'completed' or 'cancelled', defaults to 'completed'. A combination of statuses can also be requested. 'pending' and 'processing' requests cannot be combined with other statuses.
- `limit`: The maximum number of requests given back, default is 50
- `offset`: The number which forms the starting point of the requests given back. If offset equals 2, then the first 2 requests will be omitted from the list.
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
- `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
- `time_created`: Datetime when the request is created
- `time_started`: Datetime when the request starts to be processed
- `time_completed`: Datetime when the request is completed
- `input_size`: Size of the request data
- `output_size`: Size of the result

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
    "time_started": null,
    "time_completed": null,
    "input_size": 10,
    "output_size": null
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": null,
    "time_completed": null,
    "input_size": 10,
    "output_size": null
  }
]
```

With start_date="2020-03-28T20:00:26+00:00" and end_date="2020-03-28T22:00:26+00:00":

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T20:00:43.613+00:00",
    "time_started": "2020-03-28T20:00:50.276+00:00",
    "time_completed": "2020-03-28T20:00:55.241+00:00",
    "input_size": 10,
    "output_size": 10
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T21:12:45.613+00:00",
    "time_started": "2020-03-28T21:13:00.276+00:00",
    "time_completed": "2020-03-28T21:13:05.241+00:00",
    "input_size": 10,
    "output_size": 10
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
version = 'version_example' # str
status = 'status_example' # str (optional)
limit = 56 # int (optional)
offset = 56 # int (optional)
start_date = 'start_date_example' # str (optional)
end_date = 'end_date_example' # str (optional)
search_id = 'search_id_example' # str (optional)

# List pipeline version requests
api_response = core_api.pipeline_version_requests_list(project_name, pipeline_name, version, status=status, limit=limit, offset=offset, start_date=start_date, end_date=end_date, search_id=search_id)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 
 **status** | **str** | [optional] 
 **limit** | **int** | [optional] 
 **offset** | **int** | [optional] 
 **start_date** | **str** | [optional] 
 **end_date** | **str** | [optional] 
 **search_id** | **str** | [optional] 

### Return type

[**list[PipelineRequestList]**](./models/PipelineRequestList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_output_get**
> file pipeline_version_requests_output_get(project_name, pipeline_name, request_id, version)

Get a pipeline request output

## Description
Get the output of a request for a pipeline version

### Response Structure
Output of the pipeline request as a file

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
request_id = 'request_id_example' # str
version = 'version_example' # str

# Get a pipeline request output
api_response = core_api.pipeline_version_requests_output_get(project_name, pipeline_name, request_id, version)
result = api_response.json()
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 
 **version** | **str** | 

### Return type

**file**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_update**
> object pipeline_version_requests_update(project_name, pipeline_name, request_id, version, data)

Update a pipeline version request

## Description
Cancel a pipeline request for a pipeline version

### Required Parameters

- `status`: Status that the request will be updated to. It can only be `cancelled`.

## Request Examples

```
{
"status": "cancelled"
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
pipeline_name = 'pipeline_name_example' # str
request_id = 'request_id_example' # str
version = 'version_example' # str
data = ubiops.PipelineRequestUpdate() # PipelineRequestUpdate

# Update a pipeline version request
api_response = core_api.pipeline_version_requests_update(project_name, pipeline_name, request_id, version, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 
 **version** | **str** | 
 **data** | [**PipelineRequestUpdate**](./models/PipelineRequestUpdate.md) | 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


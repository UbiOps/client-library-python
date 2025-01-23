# Deployment_Requests

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_deployment_requests_create**](./DeploymentRequests.md#batch_deployment_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/batch | Create a batch deployment request
[**batch_deployment_version_requests_create**](./DeploymentRequests.md#batch_deployment_version_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/batch | Create a batch deployment version request
[**deployment_requests_batch_cancel**](./DeploymentRequests.md#deployment_requests_batch_cancel) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/cancel | Cancel multiple deployment requests
[**deployment_requests_batch_delete**](./DeploymentRequests.md#deployment_requests_batch_delete) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/delete | Delete multiple deployment requests
[**deployment_requests_batch_get**](./DeploymentRequests.md#deployment_requests_batch_get) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/collect | Retrieve multiple deployment requests
[**deployment_requests_create**](./DeploymentRequests.md#deployment_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests | Create a direct deployment request
[**deployment_requests_delete**](./DeploymentRequests.md#deployment_requests_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Delete a deployment request
[**deployment_requests_get**](./DeploymentRequests.md#deployment_requests_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Get a deployment request
[**deployment_requests_list**](./DeploymentRequests.md#deployment_requests_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/requests | List deployment requests
[**deployment_requests_update**](./DeploymentRequests.md#deployment_requests_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Update a deployment request
[**deployment_version_requests_batch_cancel**](./DeploymentRequests.md#deployment_version_requests_batch_cancel) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/cancel | Delete multiple deployment version requests
[**deployment_version_requests_batch_delete**](./DeploymentRequests.md#deployment_version_requests_batch_delete) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/delete | Delete multiple deployment version requests
[**deployment_version_requests_batch_get**](./DeploymentRequests.md#deployment_version_requests_batch_get) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/collect | Retrieve multiple deployment version requests
[**deployment_version_requests_create**](./DeploymentRequests.md#deployment_version_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests | Create a direct deployment version request
[**deployment_version_requests_delete**](./DeploymentRequests.md#deployment_version_requests_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Delete a deployment version request
[**deployment_version_requests_get**](./DeploymentRequests.md#deployment_version_requests_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Get a deployment version request
[**deployment_version_requests_list**](./DeploymentRequests.md#deployment_version_requests_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests | List deployment version requests
[**deployment_version_requests_update**](./DeploymentRequests.md#deployment_version_requests_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Update a deployment version request


# **batch_deployment_requests_create**
> list[DeploymentRequestBatchCreateResponse] batch_deployment_requests_create(project_name, deployment_name, data, timeout=timeout)

Create a batch deployment request

## Description
Request multiple predictions from the default version of a deployment. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the deployment request collect methods.

If one of the requests is faulty, all requests are denied. The maximum number of requests per batch call is 250.

### Required Parameters
In case of structured input deployment: A list of dictionaries, where each dictionary contains the input fields of the deployment as keys. It is also possible to send a single dictionary as input.
In case of plain input deployment: A list of strings. It is also possible to send a single string as input.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the batch deployment request in seconds. The maximum allowed value is 172800 (48 hours) and the default value is 14400 (4 hours).

## Request Examples
Multiple structured batch deployment requests

```
[
  {
    "input-field-1": 5.0,
    "input-field-2": "N",
    "input-field-3": [0.25, 0.25, 2.1, 16.3]
  },
  {
    "input-field-1": 3.0,
    "input-field-2": "S",
    "input-field-3": [4.23, 3.27, 2.41, 12.4]
  }
]
```

Multiple plain batch deployment requests

```
[
  "plain-data-goes-here", "plain-example-data"
]
```

### Response Structure
A list of dictionaries containing the details of the created deployment requests with the following fields:

- `id`: Unique identifier for the deployment request, which can be used to collect the result
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `time_created`: Server time that the request was made (current time)

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  }
]
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    data = [{'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'}] # list[str or dict()]
    timeout = 56 # int (optional)

    # Create a batch deployment request
    api_response = core_api.batch_deployment_requests_create(project_name, deployment_name, data, timeout=timeout)
    print(api_response)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    data = [{'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'}] # list[str or dict()]
    timeout = 56 # int (optional)

    # Create a batch deployment request
    api_response = core_api.batch_deployment_requests_create(project_name, deployment_name, data, timeout=timeout)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **data** | **list[str or dict()]** | 
 **timeout** | **int** | [optional] 

### Return type

[**list[DeploymentRequestBatchCreateResponse]**](./models/DeploymentRequestBatchCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **batch_deployment_version_requests_create**
> list[DeploymentRequestBatchCreateResponse] batch_deployment_version_requests_create(project_name, deployment_name, version, data, timeout=timeout)

Create a batch deployment version request

## Description
Request multiple predictions from a deployment version. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the deployment request collect methods. It is only possible to make a request if a deployment file is uploaded for that version and the deployment build has succeeded (meaning that the version is in available state).

If one of the requests is faulty, all requests are denied. The maximum number of requests per batch call is 250.

### Required Parameters
In case of structured input deployment: A list of dictionaries, where each dictionary contains the input fields of the deployment as keys. It is also possible to send a single dictionary as input.
In case of plain input deployment: A list of strings. It is also possible to send a single string as input.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the batch deployment request in seconds. The maximum allowed value is 172800 (48 hours) and the default value is 14400 (4 hours).

## Request Examples
Multiple structured batch deployment requests

```
[
  {
    "input-field-1": 5.0,
    "input-field-2": "N",
    "input-field-3": [0.25, 0.25, 2.1, 16.3]
  },
  {
    "input-field-1": 3.0,
    "input-field-2": "S",
    "input-field-3": [4.23, 3.27, 2.41, 12.4]
  }
]
```

Multiple plain batch deployment requests

```
[
  "plain-data-goes-here", "plain-example-data"
]
```

### Response Structure
A list of dictionaries containing the details of the created deployment requests with the following fields:

- `id`: Unique identifier for the deployment request, which can be used to collect the result
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `time_created`: Server time that the request was made (current time)

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  }
]
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    version = 'version_example' # str
    data = [{'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'}] # list[str or dict()]
    timeout = 56 # int (optional)

    # Create a batch deployment version request
    api_response = core_api.batch_deployment_version_requests_create(project_name, deployment_name, version, data, timeout=timeout)
    print(api_response)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    version = 'version_example' # str
    data = [{'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'}] # list[str or dict()]
    timeout = 56 # int (optional)

    # Create a batch deployment version request
    api_response = core_api.batch_deployment_version_requests_create(project_name, deployment_name, version, data, timeout=timeout)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 
 **data** | **list[str or dict()]** | 
 **timeout** | **int** | [optional] 

### Return type

[**list[DeploymentRequestBatchCreateResponse]**](./models/DeploymentRequestBatchCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_requests_batch_cancel**
> object deployment_requests_batch_cancel(project_name, deployment_name, data, status=status)

Cancel multiple deployment requests

## Description
Cancel multiple deployment requests for the default version of a deployment. A maximum of 250 deployment requests can be cancelled with this method.

To cancel all pending or processing requests, use the query parameter `status`, with the value 'pending' or 'processing', with an empty request body.

### Required Parameters
A list of ids for the requests

## Request Examples

```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    data = ['request_id_1', 'request_id_2'] # list[str]
    status = 'status_example' # str (optional)

    # Cancel multiple deployment requests
    api_response = core_api.deployment_requests_batch_cancel(project_name, deployment_name, data, status=status)
    print(api_response)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    data = ['request_id_1', 'request_id_2'] # list[str]
    status = 'status_example' # str (optional)

    # Cancel multiple deployment requests
    api_response = core_api.deployment_requests_batch_cancel(project_name, deployment_name, data, status=status)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **data** | **list[str]** | 
 **status** | **str** | [optional] 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_requests_batch_delete**
> object deployment_requests_batch_delete(project_name, deployment_name, data)

Delete multiple deployment requests

## Description
Delete multiple deployment requests for the default version of a deployment. If one of the given deployment requests does not exist, an error message is given and no request is deleted. A maximum of 250 deployment requests can be deleted with this method.

### Required Parameters
A list of ids for the requests

## Request Examples

```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    data = ['request_id_1', 'request_id_2'] # list[str]

    # Delete multiple deployment requests
    api_response = core_api.deployment_requests_batch_delete(project_name, deployment_name, data)
    print(api_response)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    data = ['request_id_1', 'request_id_2'] # list[str]

    # Delete multiple deployment requests
    api_response = core_api.deployment_requests_batch_delete(project_name, deployment_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **data** | **list[str]** | 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_requests_batch_get**
> list[DeploymentRequestDetail] deployment_requests_batch_get(project_name, deployment_name, data)

Retrieve multiple deployment requests

## Description
Retrieve multiple deployment requests for the default version of a deployment. If one of the given deployment requests does not exist, an error message is given and no request is returned. A maximum of 250 deployment requests can be retrieved with this method. The deployment requests are NOT returned in the order they are given in.

### Required Parameters
A list of ids for the requests

## Request Examples

```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```

### Response Structure
A list of dictionaries containing the details of the retrieved deployment requests with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request, one of the following 'pending', 'processing', 'failed', 'completed' or 'cancelled'
- `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
- `time_created`: Datetime when the request is created
- `time_started`: Datetime when the request starts to be processed
- `time_completed`: Datetime when the request is completed
- `timeout`: Timeout in seconds for the request
- `request_data`: Input of the request
- `result`: Output of the request. It is set to null if the request is in pending/processing/failed statuses.
- `error_message`: An error message explaining why the request has failed. It is set to null if the request was successful.
- `input_size`: Size of the request data
- `output_size`: Size of the result

## Response Examples

```
[
  {
    "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-29T08:09:10.729+00:00",
    "time_started": null,
    "time_completed": null,
    "timeout": 300,
    "request_data": {"input": 82.2},
    "result": null,
    "error_message": null,
    "input_size": 14,
    "output_size": null
  },
  {
    "id": "85711124-54db-4794-b83d-24492247c6e1",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-06-25T09:37:17.765+00:00",
    "timeout": 300,
    "time_started": null,
    "time_completed": null,
    "request_data": {"input": 52.4},
    "result": null,
    "error_message": null,
    "input_size": 14,
    "output_size": null
  }
]
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    data = ['request_id_1', 'request_id_2'] # list[str]

    # Retrieve multiple deployment requests
    api_response = core_api.deployment_requests_batch_get(project_name, deployment_name, data)
    print(api_response)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    data = ['request_id_1', 'request_id_2'] # list[str]

    # Retrieve multiple deployment requests
    api_response = core_api.deployment_requests_batch_get(project_name, deployment_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **data** | **list[str]** | 

### Return type

[**list[DeploymentRequestDetail]**](./models/DeploymentRequestDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_requests_create**
> DeploymentRequestCreateResponse deployment_requests_create(project_name, deployment_name, data, timeout=timeout)

Create a direct deployment request

## Description
Request a prediction from a deployment. Deployment requests are made for the default version of a deployment.
When using the 'requests' function of a deployment a list should be provided as input, see the example below.

### Required Parameters
The input for the request. In case of a structured deployment, this is a dictionary which contains the input fields of the deployment as keys. In case of a plain deployment, give a string or list of strings.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the deployment request in seconds. The maximum allowed value is 3600 (1 hour) and the default value is 300 (5 minutes).

## Request Examples
A structured deployment request

```
{
  "input-field-1": 5.0,
  "input-field-2": "N",
  "input-field-3": [0.25, 0.25, 2.1, 16.3]
}
```

A structured deployment request with a file field

```
{
  "input-field-1": 5.0,
  "file-input-field": "ubiops-file://my-bucket/file-1.jpg"
}
```

A plain deployment request

```
"example-plain-data"
```

Multiple structured deployment requests using the 'requests' function of a deployment
```
[
    {
        "input-field-1": 5.0
    },
    {
        "input-field-1": 10.0
    }
]
```

### Response Structure
Details of the created deployment request

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request. It can be 'completed' or 'failed'.
- `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
- `result`: Deployment request result value. NULL if the request failed.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `timeout`: Timeout of the request in seconds

## Response Examples
A failed deployment request

```
{
  "id": "85ae32a7-fe3a-4a55-be27-9db88ae68501",
  "deployment": "deployment-1",
  "version": "v1",
  "status": "failed",
  "success": false,
  "result": None,
  "error_message": "Asset ID not supported"
  "timeout": 300
}
```

A successful deployment request

```
{
  "id": "ffce45da-1562-419a-89a0-0a0837e55392",
  "deployment": "deployment-1",
  "version": "v2",
  "status": "completed",
  "success": true,
  "result": {
    "output-field-1": "2.1369",
    "output-field-2": "5.5832",
  },
  "error_message": null,
  "timeout": 300
}
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    data = {'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'} # str or dict()
    timeout = 56 # int (optional)

    # Create a direct deployment request
    api_response = core_api.deployment_requests_create(project_name, deployment_name, data, timeout=timeout)
    print(api_response)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    data = {'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'} # str or dict()
    timeout = 56 # int (optional)

    # Create a direct deployment request
    api_response = core_api.deployment_requests_create(project_name, deployment_name, data, timeout=timeout)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **data** | **str or dict()** | 
 **timeout** | **int** | [optional] 

### Return type

[**DeploymentRequestCreateResponse**](./models/DeploymentRequestCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_requests_delete**
> deployment_requests_delete(project_name, deployment_name, request_id)

Delete a deployment request

## Description
Delete a deployment request for the default version of a deployment

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    request_id = 'request_id_example' # str

    # Delete a deployment request
    core_api.deployment_requests_delete(project_name, deployment_name, request_id)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    request_id = 'request_id_example' # str

    # Delete a deployment request
    core_api.deployment_requests_delete(project_name, deployment_name, request_id)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **request_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_requests_get**
> DeploymentRequestSingleDetail deployment_requests_get(project_name, deployment_name, request_id, metadata_only=metadata_only)

Get a deployment request

## Description
Get the details of a request for the default version of a deployment

### Optional Parameters

- `metadata_only`: A boolean value that indicates whether the response should include the request data and result, defaults to False

### Response Structure
A dictionary containing the details of the deployment request with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request, one of the following 'pending', 'processing', 'failed', 'completed' or 'cancelled'
- `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
- `time_created`: Datetime when the request is created
- `time_started`: Datetime when the request starts to be processed
- `time_completed`: Datetime when the request is completed
- `timeout`: Timeout in seconds for the request
- `request_data`: Input of the request
- `result`: Output of the request. It is set to null if the request is in pending/processing/failed statuses.
- `error_message`: An error message explaining why the request has failed. It is set to null if the request was successful.
- `origin`: A dictionary containing the information on where the request originated from. It contains:
    - `created_by` field with the email of the user that created the request. In case the request is created by a service, the field will have a "UbiOps" value.
- `input_size`: Size of the request data
- `output_size`: Size of the result

## Response Examples

```
{
  "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
  "deployment": "deployment-1",
  "version": "v1",
  "status": "pending",
  "success": false,
  "time_created": "2020-03-29T08:09:10.729+00:00",
  "time_started": null,
  "time_completed": null,
  "timeout": 300,
  "request_data": {"input": 82.3},
  "result": null,
  "error_message": null,
  "origin": {
    "created_by": "my.example.user@ubiops.com"
  },
  "input_size": 14,
  "output_size": null
}
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    request_id = 'request_id_example' # str
    metadata_only = True # bool (optional)

    # Get a deployment request
    api_response = core_api.deployment_requests_get(project_name, deployment_name, request_id, metadata_only=metadata_only)
    print(api_response)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    request_id = 'request_id_example' # str
    metadata_only = True # bool (optional)

    # Get a deployment request
    api_response = core_api.deployment_requests_get(project_name, deployment_name, request_id, metadata_only=metadata_only)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **request_id** | **str** | 
 **metadata_only** | **bool** | [optional] 

### Return type

[**DeploymentRequestSingleDetail**](./models/DeploymentRequestSingleDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_requests_list**
> list[DeploymentRequestList] deployment_requests_list(project_name, deployment_name, status=status, limit=limit, offset=offset, start_date=start_date, end_date=end_date, search_id=search_id)

List deployment requests

## Description
List all requests for the default version of a deployment

### Optional Parameters

- `status`: Status of the request, one of the following 'pending', 'processing', 'failed', 'completed' or 'cancelled', defaults to 'completed'. A combination of statuses can also be requested. 'pending' and 'processing' requests cannot be combined with other statuses.
- `limit`: The maximum number of requests given back, defaults to 50
- `offset`: The number which forms the starting point of the requests given back, defaults to 0. If offset equals 2, then the first 2 requests will be omitted from the list.
- `start_date`: Start date of the interval for which the requests are retrieved, looking at the creation date of the request. *Only available* for completed/failed/cancelled requests.
- `end_date`: End date of the interval for which the requests are retrieved, looking at the creation date of the request. *Only available* for completed/failed/cancelled requests.
- `search_id`: A string to search inside request ids. It will filter all request ids that contain this string. *Only available* for completed/failed/cancelled requests.

If no start or end date is provided, the most recent requests are returned.

### Response Structure
A list of dictionaries containing the details of the deployment requests with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
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
    "deployment": "deployment-1",
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
    "deployment": "deployment-1",
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

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    status = 'status_example' # str (optional)
    limit = 56 # int (optional)
    offset = 56 # int (optional)
    start_date = 'start_date_example' # str (optional)
    end_date = 'end_date_example' # str (optional)
    search_id = 'search_id_example' # str (optional)

    # List deployment requests
    api_response = core_api.deployment_requests_list(project_name, deployment_name, status=status, limit=limit, offset=offset, start_date=start_date, end_date=end_date, search_id=search_id)
    print(api_response)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    status = 'status_example' # str (optional)
    limit = 56 # int (optional)
    offset = 56 # int (optional)
    start_date = 'start_date_example' # str (optional)
    end_date = 'end_date_example' # str (optional)
    search_id = 'search_id_example' # str (optional)

    # List deployment requests
    api_response = core_api.deployment_requests_list(project_name, deployment_name, status=status, limit=limit, offset=offset, start_date=start_date, end_date=end_date, search_id=search_id)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **status** | **str** | [optional] 
 **limit** | **int** | [optional] 
 **offset** | **int** | [optional] 
 **start_date** | **str** | [optional] 
 **end_date** | **str** | [optional] 
 **search_id** | **str** | [optional] 

### Return type

[**list[DeploymentRequestList]**](./models/DeploymentRequestList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_requests_update**
> object deployment_requests_update(project_name, deployment_name, request_id, data)

Update a deployment request

## Description
Cancel a deployment request for the default version of a deployment

### Required Parameters

- `status`: Status that the request will be updated to. It can only be `cancelled`.

## Request Examples

```
{
"status": "cancelled"
}
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    request_id = 'request_id_example' # str
    data = ubiops.DeploymentRequestUpdate() # DeploymentRequestUpdate

    # Update a deployment request
    api_response = core_api.deployment_requests_update(project_name, deployment_name, request_id, data)
    print(api_response)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    request_id = 'request_id_example' # str
    data = ubiops.DeploymentRequestUpdate() # DeploymentRequestUpdate

    # Update a deployment request
    api_response = core_api.deployment_requests_update(project_name, deployment_name, request_id, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **request_id** | **str** | 
 **data** | [**DeploymentRequestUpdate**](./models/DeploymentRequestUpdate.md) | 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_requests_batch_cancel**
> object deployment_version_requests_batch_cancel(project_name, deployment_name, version, data, status=status)

Delete multiple deployment version requests

## Description
Cancel multiple deployment requests for a deployment version. A maximum of 250 deployment requests can be deleted with this method.

To cancel all pending or processing requests, use the query parameter `status`, with the value 'pending' or 'processing', with an empty request body.

### Required Parameters
A list of ids for the requests

## Request Examples

```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    version = 'version_example' # str
    data = ['request_id_1', 'request_id_2'] # list[str]
    status = 'status_example' # str (optional)

    # Delete multiple deployment version requests
    api_response = core_api.deployment_version_requests_batch_cancel(project_name, deployment_name, version, data, status=status)
    print(api_response)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    version = 'version_example' # str
    data = ['request_id_1', 'request_id_2'] # list[str]
    status = 'status_example' # str (optional)

    # Delete multiple deployment version requests
    api_response = core_api.deployment_version_requests_batch_cancel(project_name, deployment_name, version, data, status=status)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 
 **data** | **list[str]** | 
 **status** | **str** | [optional] 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_requests_batch_delete**
> object deployment_version_requests_batch_delete(project_name, deployment_name, version, data)

Delete multiple deployment version requests

## Description
Delete multiple deployment requests for a deployment version. If one of the given deployment requests does not exist, an error message is given and no request is deleted. A maximum of 250 deployment requests can be deleted with this method.

### Required Parameters
A list of ids for the requests

## Request Examples

```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    version = 'version_example' # str
    data = ['request_id_1', 'request_id_2'] # list[str]

    # Delete multiple deployment version requests
    api_response = core_api.deployment_version_requests_batch_delete(project_name, deployment_name, version, data)
    print(api_response)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    version = 'version_example' # str
    data = ['request_id_1', 'request_id_2'] # list[str]

    # Delete multiple deployment version requests
    api_response = core_api.deployment_version_requests_batch_delete(project_name, deployment_name, version, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 
 **data** | **list[str]** | 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_requests_batch_get**
> list[DeploymentRequestDetail] deployment_version_requests_batch_get(project_name, deployment_name, version, data)

Retrieve multiple deployment version requests

## Description
Retrieve multiple deployment requests for a deployment version. If one of the given deployment requests does not exist, an error message is given and no request is returned. A maximum of 250 deployment requests can be retrieved with this method. The deployment requests are NOT returned in the order they are given in.

### Required Parameters
A list of ids for the requests

## Request Examples

```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```

### Response Structure
A list of dictionaries containing the details of the retrieved deployment requests with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request, one of the following 'pending', 'processing', 'failed', 'completed' or 'cancelled'
- `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
- `time_created`: Datetime when the request is created
- `time_started`: Datetime when the request starts to be processed
- `time_completed`: Datetime when the request is completed
- `timeout`: Timeout in seconds for the request
- `request_data`: Input of the request
- `result`: Output of the request. It is set to null if the request is in pending/processing/failed statuses.
- `error_message`: An error message explaining why the request has failed. It is set to null if the request was successful.
- `input_size`: Size of the request data
- `output_size`: Size of the result

## Response Examples

```
[
  {
    "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-29T08:09:10.729+00:00",
    "time_started": null,
    "time_completed": null,
    "timeout": 300,
    "request_data": {"input": 82.2},
    "result": null,
    "error_message": null,
    "input_size": 14,
    "output_size": null
  },
  {
    "id": "85711124-54db-4794-b83d-24492247c6e1",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-06-25T09:37:17.765+00:00",
    "time_started": null,
    "time_completed": null,
    "timeout": 300,
    "request_data": {"input": 52.4},
    "result": null,
    "error_message": null,
    "input_size": 14,
    "output_size": null
  }
]
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    version = 'version_example' # str
    data = ['request_id_1', 'request_id_2'] # list[str]

    # Retrieve multiple deployment version requests
    api_response = core_api.deployment_version_requests_batch_get(project_name, deployment_name, version, data)
    print(api_response)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    version = 'version_example' # str
    data = ['request_id_1', 'request_id_2'] # list[str]

    # Retrieve multiple deployment version requests
    api_response = core_api.deployment_version_requests_batch_get(project_name, deployment_name, version, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 
 **data** | **list[str]** | 

### Return type

[**list[DeploymentRequestDetail]**](./models/DeploymentRequestDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_requests_create**
> DeploymentRequestCreateResponse deployment_version_requests_create(project_name, deployment_name, version, data, timeout=timeout)

Create a direct deployment version request

## Description
Request a prediction from a deployment version. It is only possible to make a request if a deployment file is uploaded for that version and the deployment build has succeeded (meaning that the version is in available state).
When using the 'requests' function of a deployment a list should be provided as input, see the example below.

### Required Parameters
The input for the request. In case of a structured deployment, this is a dictionary which contains the input fields of the deployment as keys. In case of a plain deployment, give a string or list of strings.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the deployment request in seconds. The maximum allowed value is 3600 (1 hour) and the default value is 300 (5 minutes).

## Request Examples
A structured deployment request

```
{
  "input-field-1": 5.0,
  "input-field-2": "N",
  "input-field-3": [0.25, 0.25, 2.1, 16.3]
}
```

A structured deployment request with a file field

```
{
  "input-field-1": 5.0,
  "file-input-field": "ubiops-file://my-bucket/file-1.jpg"
}
```

A plain deployment request

```
"example-plain-data"
```

Multiple structured deployment requests using the 'requests' function of a deployment version
```
[
    {
        "input-field-1": 5.0
    },
    {
        "input-field-1": 10.0
    }
]
```

### Response Structure
Details of the created deployment request

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request. It can be 'completed' or 'failed'.
- `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
- `result`: Deployment request result value. NULL if the request failed.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `timeout`: Timeout of the request in seconds

## Response Examples
A failed deployment request

```
{
  "id": "85ae32a7-fe3a-4a55-be27-9db88ae68501",
  "deployment": "deployment-1",
  "version": "v1",
  "status": "failed",
  "success": false,
  "result": None,
  "error_message": "Asset ID not supported",
  "timeout": 300
}
```

A successful deployment request

```
{
  "id": "ffce45da-1562-419a-89a0-0a0837e55392",
  "deployment": "deployment-1",
  "version": "v2",
  "status": "completed",
  "success": true,
  "result": {
    "output-field-1": "2.1369",
    "output-field-2": "5.5832",
  },
  "error_message": None,
  "timeout": 300
}
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    version = 'version_example' # str
    data = {'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'} # str or dict()
    timeout = 56 # int (optional)

    # Create a direct deployment version request
    api_response = core_api.deployment_version_requests_create(project_name, deployment_name, version, data, timeout=timeout)
    print(api_response)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    version = 'version_example' # str
    data = {'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'} # str or dict()
    timeout = 56 # int (optional)

    # Create a direct deployment version request
    api_response = core_api.deployment_version_requests_create(project_name, deployment_name, version, data, timeout=timeout)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 
 **data** | **str or dict()** | 
 **timeout** | **int** | [optional] 

### Return type

[**DeploymentRequestCreateResponse**](./models/DeploymentRequestCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_requests_delete**
> deployment_version_requests_delete(project_name, deployment_name, request_id, version)

Delete a deployment version request

## Description
Delete a deployment request for a deployment version

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    request_id = 'request_id_example' # str
    version = 'version_example' # str

    # Delete a deployment version request
    core_api.deployment_version_requests_delete(project_name, deployment_name, request_id, version)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    request_id = 'request_id_example' # str
    version = 'version_example' # str

    # Delete a deployment version request
    core_api.deployment_version_requests_delete(project_name, deployment_name, request_id, version)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **request_id** | **str** | 
 **version** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_requests_get**
> DeploymentRequestSingleDetail deployment_version_requests_get(project_name, deployment_name, request_id, version, metadata_only=metadata_only)

Get a deployment version request

## Description
Get the details of a request for a deployment version

### Optional Parameters

- `metadata_only`: A boolean value that indicates whether the response should include the request data and result, defaults to False

### Response Structure
A dictionary containing the details of the deployment request with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request, one of the following 'pending', 'processing', 'failed', 'completed' or 'cancelled'
- `success`: [DEPRECATED] A boolean value that indicates whether the request was successful. This field is deprecated, use 'status' instead.
- `time_created`: Datetime when the request is created
- `time_started`: Datetime when the request starts to be processed
- `time_completed`: Datetime when the request is completed
- `timeout`: Timeout in seconds for the request
- `request_data`: Input of the request
- `result`: Output of the request. It is set to null if the request is in pending/processing/failed statuses.
- `error_message`: An error message explaining why the request has failed. It is set to null if the request was successful.
- `origin`: A dictionary containing the information on where the request originated from. It contains:
    - `created_by` field with the email of the user that created the request. In case the request is created by a service, the field will have a "UbiOps" value.
- `input_size`: Size of the request data
- `output_size`: Size of the result

## Response Examples

```
{
  "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
  "deployment": "deployment-1",
  "version": "v1",
  "status": "pending",
  "success": false,
  "time_created": "2020-03-29T08:09:10.729+00:00",
  "time_started": null,
  "time_completed": null,
  "timeout": 300,
  "request_data": {"input": 82.3},
  "result": null,
  "error_message": null,
  "origin": {
    "created_by": "my.example.user@ubiops.com"
  },
  "input_size": 14,
  "output_size": null
}
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    request_id = 'request_id_example' # str
    version = 'version_example' # str
    metadata_only = True # bool (optional)

    # Get a deployment version request
    api_response = core_api.deployment_version_requests_get(project_name, deployment_name, request_id, version, metadata_only=metadata_only)
    print(api_response)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    request_id = 'request_id_example' # str
    version = 'version_example' # str
    metadata_only = True # bool (optional)

    # Get a deployment version request
    api_response = core_api.deployment_version_requests_get(project_name, deployment_name, request_id, version, metadata_only=metadata_only)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **request_id** | **str** | 
 **version** | **str** | 
 **metadata_only** | **bool** | [optional] 

### Return type

[**DeploymentRequestSingleDetail**](./models/DeploymentRequestSingleDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_requests_list**
> list[DeploymentRequestList] deployment_version_requests_list(project_name, deployment_name, version, status=status, limit=limit, offset=offset, start_date=start_date, end_date=end_date, search_id=search_id)

List deployment version requests

## Description
List all requests for a deployment version

### Optional Parameters

- `status`: Status of the request, one of the following 'pending', 'processing', 'failed', 'completed' or 'cancelled', defaults to 'completed'. A combination of statuses can also be requested. 'pending' and 'processing' requests cannot be combined with other statuses.
- `limit`: The maximum number of requests given back, defaults to 50
- `offset`: The number which forms the starting point of the requests given back, defaults to 0. If offset equals 2, then the first 2 requests will be omitted from the list.
- `start_date`: Start date of the interval for which the requests are retrieved, looking at the creation date of the request. *Only available* for completed/failed/cancelled requests.
- `end_date`: End date of the interval for which the requests are retrieved, looking at the creation date of the request. *Only available* for completed/failed/cancelled requests.
- `search_id`: A string to search inside request ids. It will filter all request ids that contain this string. *Only available* for completed/failed/cancelled requests.

If no start or end date is provided, the most recent requests are returned.

### Response Structure
A list of dictionaries containing the details of the deployment requests with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
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
    "deployment": "deployment-1",
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
    "deployment": "deployment-1",
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

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    version = 'version_example' # str
    status = 'status_example' # str (optional)
    limit = 56 # int (optional)
    offset = 56 # int (optional)
    start_date = 'start_date_example' # str (optional)
    end_date = 'end_date_example' # str (optional)
    search_id = 'search_id_example' # str (optional)

    # List deployment version requests
    api_response = core_api.deployment_version_requests_list(project_name, deployment_name, version, status=status, limit=limit, offset=offset, start_date=start_date, end_date=end_date, search_id=search_id)
    print(api_response)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    version = 'version_example' # str
    status = 'status_example' # str (optional)
    limit = 56 # int (optional)
    offset = 56 # int (optional)
    start_date = 'start_date_example' # str (optional)
    end_date = 'end_date_example' # str (optional)
    search_id = 'search_id_example' # str (optional)

    # List deployment version requests
    api_response = core_api.deployment_version_requests_list(project_name, deployment_name, version, status=status, limit=limit, offset=offset, start_date=start_date, end_date=end_date, search_id=search_id)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 
 **status** | **str** | [optional] 
 **limit** | **int** | [optional] 
 **offset** | **int** | [optional] 
 **start_date** | **str** | [optional] 
 **end_date** | **str** | [optional] 
 **search_id** | **str** | [optional] 

### Return type

[**list[DeploymentRequestList]**](./models/DeploymentRequestList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_requests_update**
> object deployment_version_requests_update(project_name, deployment_name, request_id, version, data)

Update a deployment version request

## Description
Cancel a deployment request for the default version of a deployment

### Required Parameters

- `status`: Status that the request will be updated to. It can only be `cancelled`.

## Request Examples

```
{
"status": "cancelled"
}
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    request_id = 'request_id_example' # str
    version = 'version_example' # str
    data = ubiops.DeploymentRequestUpdate() # DeploymentRequestUpdate

    # Update a deployment version request
    api_response = core_api.deployment_version_requests_update(project_name, deployment_name, request_id, version, data)
    print(api_response)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = 'project_name_example' # str
    deployment_name = 'deployment_name_example' # str
    request_id = 'request_id_example' # str
    version = 'version_example' # str
    data = ubiops.DeploymentRequestUpdate() # DeploymentRequestUpdate

    # Update a deployment version request
    api_response = core_api.deployment_version_requests_update(project_name, deployment_name, request_id, version, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **request_id** | **str** | 
 **version** | **str** | 
 **data** | [**DeploymentRequestUpdate**](./models/DeploymentRequestUpdate.md) | 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


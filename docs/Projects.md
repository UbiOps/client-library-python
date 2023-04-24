# Projects

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instance_types_list**](Projects.md#instance_types_list) | **GET** /projects/{project_name}/instance-types | List instance types
[**metrics_get**](Projects.md#metrics_get) | **GET** /projects/{project_name}/metrics/{metric} | Get metrics
[**project_audit_events_list**](Projects.md#project_audit_events_list) | **GET** /projects/{project_name}/audit | List audit events in a project
[**project_environment_variables_create**](Projects.md#project_environment_variables_create) | **POST** /projects/{project_name}/environment-variables | Create project environment variable
[**project_environment_variables_delete**](Projects.md#project_environment_variables_delete) | **DELETE** /projects/{project_name}/environment-variables/{id} | Delete project environment variable
[**project_environment_variables_get**](Projects.md#project_environment_variables_get) | **GET** /projects/{project_name}/environment-variables/{id} | Get project environment variable
[**project_environment_variables_list**](Projects.md#project_environment_variables_list) | **GET** /projects/{project_name}/environment-variables | List project environment variables
[**project_environment_variables_update**](Projects.md#project_environment_variables_update) | **PATCH** /projects/{project_name}/environment-variables/{id} | Update project environment variable
[**project_requests_list**](Projects.md#project_requests_list) | **GET** /projects/{project_name}/requests | List requests in project
[**project_users_create**](Projects.md#project_users_create) | **POST** /projects/{project_name}/users | Add user to a project
[**project_users_delete**](Projects.md#project_users_delete) | **DELETE** /projects/{project_name}/users/{user_id} | Delete user from a project
[**project_users_get**](Projects.md#project_users_get) | **GET** /projects/{project_name}/users/{user_id} | Get user in a project
[**project_users_list**](Projects.md#project_users_list) | **GET** /projects/{project_name}/users | List users in a project
[**projects_create**](Projects.md#projects_create) | **POST** /projects | Create projects
[**projects_delete**](Projects.md#projects_delete) | **DELETE** /projects/{project_name} | Delete a project
[**projects_get**](Projects.md#projects_get) | **GET** /projects/{project_name} | Get details of a project
[**projects_list**](Projects.md#projects_list) | **GET** /projects | List projects
[**projects_log_list**](Projects.md#projects_log_list) | **POST** /projects/{project_name}/logs | List logs for a project
[**projects_resource_usage**](Projects.md#projects_resource_usage) | **GET** /projects/{project_name}/resources | List resource usage of a project
[**projects_update**](Projects.md#projects_update) | **PATCH** /projects/{project_name} | Update a project
[**projects_usage_get**](Projects.md#projects_usage_get) | **GET** /projects/{project_name}/usage | Get resource usage
[**quotas_list**](Projects.md#quotas_list) | **GET** /projects/{project_name}/quotas | List quotas


# **instance_types_list**
> list[DeploymentInstanceType] instance_types_list(project_name)

List instance types

## Description
Get list of available deployment instance types for a project

### Response Structure
Details of the instance type

- `id`: Unique identifier for the instance type (UUID)

- `name`: Name of the deployment instance type

- `display_name`: Readable name of the deployment instance type

- `memory_allocation`: Integer indicating memory allocation for this instance type (Mi)

- `cpu_allocation`: Integer indicating CPU allocation for this instance type (milliCPU)

- `gpu_allocation`: Integer indicating number of GPU cores for this instance type

- `storage_allocation`: Integer indicating the maximum storage that can be used by this instance type (MB)

## Response Examples

```
[
  {
    "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
    "name": "512mb",
    "display_name": "512 MB",
    "memory_allocation": 512,
    "cpu_allocation": 125,
    "gpu_allocation": 0,
    "storage_allocation": 2048
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

    # List instance types
    api_response = core_api.instance_types_list(project_name)
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

    # List instance types
    api_response = core_api.instance_types_list(project_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 

### Return type

[**list[DeploymentInstanceType]**](./models/DeploymentInstanceType.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **metrics_get**
> list[Metrics] metrics_get(project_name, metric, start_date, end_date, object_type, interval=interval, object_id=object_id, user_id=user_id)

Get metrics

## Description
Get metrics for the project or a specified object. The following metrics are available:

Metrics on pipeline version level:
- `requests`: Number of requests made to the object
- `failed_requests`: Number of failed requests made to the object
- `request_duration`: Average time in seconds for a pipeline request to complete
- `input_volume`: Volume of incoming data in bytes
- `object_requests`: Number of requests made to objects in the pipeline version
- `object_failed_requests`: Number of failed requests made to deployments in a pipeline

Metrics on deployment version level:
- `requests`: Number of requests made to the object
- `failed_requests`: Number of failed requests made to the object
- `input_volume`: Volume of incoming data in bytes
- `output_volume`: Volume of outgoing data in bytes
- `outputs`: Number of outgoing data items
- `compute`: Average time in seconds for a request to complete
- `memory_peak`: Peak memory used during a request
- `instances`: Number of active deployment instances
- `credits`: Usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours the deployments are running
- `active_time`: Time in seconds that the deployment is active
- `express_queue_size`: Average number of queued express requests
- `batch_queue_size`: Average number of queued batch requests
- `express_queue_time`: Average time in seconds for an express request to start processing
- `batch_queue_time`: Average time in seconds for a batch request to start processing

### Required Parameters

- `start_date`: Starting date for the metric values to be returned. It should be provided in datetime isoformat.
- `end_date`: Ending date for the metric values to be returned. It should be provided in datetime isoformat.
- `object_type`: The type of the object for which the metrics are requested. It can be either `deployment_version` or `pipeline_version`.

### Optional Parameters

- `interval`: Interval for the metric value. It can be minute, hour, day or month. The metric values will be aggregated according to this interval. The default value is hour.
- `object_id`: Uuid of the specific object for which the metrics are requested. When it is not provided, the metrics are aggregated for the given `object_type`.
- `user_id`: Uuid of the user for which the metrics are requested. When it is not provided, the metrics are aggregated for the given `object_type` generated by all users.

### Response Structure

- `start_date`: Timestamp denoting the start of the period over which the metric was measured
- `end_date`: Timestamp denoting the end of the period over which the metric was measured
- `value`: Aggregated metric value for the given interval

## Response Examples
With interval as minute, start_date as 2019-11-13 12:00:00 and end_date as 2019-11-13 12:03:00

```
[
  {
    "start_date": "2019-11-13T12:00:00+00:00",
    "end_date": "2019-11-13T12:01:00+00:00",
    "value": 100
  },
  {
    "start_date": "2019-11-13T12:01:00+00:00",
    "end_date": "2019-11-13T12:02:00+00:00",
    "value": 134
  },
  {
    "start_date": "2019-11-13T12:02:00+00:00",
    "end_date": "2019-11-13T12:03:00+00:00",
    "value": 112
  }
]

```

With interval as hour, start_date as 2019-11-13 12:00:00 and end_date as 2019-11-13 14:00:00

```
[
  {
   "start_date": "2019-11-13T12:00:00+00:00",
   "end_date": "2019-11-13T13:00:00+00:00",
   "value": 92
  },
  {
    "start_date": "2019-11-13T13:00:00+00:00",
    "end_date": "2019-11-13T14:00:00+00:00",
    "value": 120
  },
  {
    "start_date": "2019-11-13T14:00:00+00:00",
    "end_date": "2019-11-13T15:00:00+00:00",
    "value": 0
  }
]
```

With interval as day, start_date as 2019-11-13 12:00:00 and end_date as 2019-11-14 12:00:00

```
[
  {
   "start_date": "2019-11-13T00:00:00+00:00",
   "end_date": "2019-11-14T00:00:00+00:00",
   "value": 528
  },
  {
    "start_date": "2019-11-14T00:00:00+00:00",
    "end_date": "2019-11-15T00:00:00+00:00",
    "value": 342
  }
]
```

With interval as month, start_date as 2019-11-13 12:00:00 and end_date as 2019-12-13 12:00:00
```
[
  {
   "start_date": "2019-11-01T00:00:00+00:00",
   "end_date": "2019-12-01T00:00:00+00:00",
   "value": 1983
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
    metric = 'metric_example' # str
    start_date = 'start_date_example' # str
    end_date = 'end_date_example' # str
    object_type = 'object_type_example' # str
    interval = 'interval_example' # str (optional)
    object_id = 'object_id_example' # str (optional)
    user_id = 'user_id_example' # str (optional)

    # Get metrics
    api_response = core_api.metrics_get(project_name, metric, start_date, end_date, object_type, interval=interval, object_id=object_id, user_id=user_id)
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
    metric = 'metric_example' # str
    start_date = 'start_date_example' # str
    end_date = 'end_date_example' # str
    object_type = 'object_type_example' # str
    interval = 'interval_example' # str (optional)
    object_id = 'object_id_example' # str (optional)
    user_id = 'user_id_example' # str (optional)

    # Get metrics
    api_response = core_api.metrics_get(project_name, metric, start_date, end_date, object_type, interval=interval, object_id=object_id, user_id=user_id)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **metric** | **str** | 
 **start_date** | **str** | 
 **end_date** | **str** | 
 **object_type** | **str** | 
 **interval** | **str** | [optional] 
 **object_id** | **str** | [optional] 
 **user_id** | **str** | [optional] 

### Return type

[**list[Metrics]**](./models/Metrics.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_audit_events_list**
> list[AuditList] project_audit_events_list(project_name, action=action, limit=limit, offset=offset)

List audit events in a project

## Description
List all audit events in a project including all objects

### Optional Parameters
The following parameters should be given as query parameters:

- `action`: Type of action. It can be one of: create, update, delete, info.
- `limit`: The maximum number of audit events given back, default is 50
- `offset`: The number which forms the starting point of the audit events given back. If offset equals 2, then the first 2 events will be omitted from the list.

### Response Structure
A list of details of the audit events in the project

- `id`: Unique identifier for the audit event (UUID)
- `date`: The date when the action was performed
- `action`: Type of action. It can be one of: create, update, delete, info. *info* action denotes that the action does not fall into create, update or delete categories.
- `user`: Email of the user who performed the action
- `event`: Description of the event
- `object_type`: Type of the object on which the action was performed
- `object_name`: Name of the object on which the action was performed. If the object is deleted at the time of listing audit events, this field is empty.

## Response Examples

```
[
  {
    "id": "54c1ea23-5773-4821-8fd7-1b577cc301bc",
    "date": "2020-05-23T11:53:02.873+00:00",
    "action": "create",
    "user": "user@example.com",
    "event": "Created project test-project",
    "object_type": "project",
    "object_name": "test-project"
  },
  {
    "id": "764e254c-7402-4445-ac79-009d08b21caa",
    "date": "2020-05-23T11:57:20.072+00:00",
    "action": "create",
    "user": "user@example.com",
    "event": "Created deployment deployment-1",
    "object_type": "deployment",
    "object_name": "deployment-1"
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
    action = 'action_example' # str (optional)
    limit = 56 # int (optional)
    offset = 56 # int (optional)

    # List audit events in a project
    api_response = core_api.project_audit_events_list(project_name, action=action, limit=limit, offset=offset)
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
    action = 'action_example' # str (optional)
    limit = 56 # int (optional)
    offset = 56 # int (optional)

    # List audit events in a project
    api_response = core_api.project_audit_events_list(project_name, action=action, limit=limit, offset=offset)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **action** | **str** | [optional] 
 **limit** | **int** | [optional] 
 **offset** | **int** | [optional] 

### Return type

[**list[AuditList]**](./models/AuditList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_environment_variables_create**
> EnvironmentVariableList project_environment_variables_create(project_name, data)

Create project environment variable

## Description
Create an environment variable for the project. This variable will be inherited by all deployments in this project.

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users.

## Request Examples

```
{
  "name": "database_schema",
  "value": "public",
  "secret": false
}
```


```
{
  "name": "database_password",
  "value": "password",
  "secret": true
}
```

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

```
{
  "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
  "name": "database_schema",
  "value": "public",
  "secret": false
}
```


```
{
  "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
  "name": "database_password",
  "value": null,
  "secret": true
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
    data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate

    # Create project environment variable
    api_response = core_api.project_environment_variables_create(project_name, data)
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
    data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate

    # Create project environment variable
    api_response = core_api.project_environment_variables_create(project_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**EnvironmentVariableCreate**](./models/EnvironmentVariableCreate.md) | 

### Return type

[**EnvironmentVariableList**](./models/EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_environment_variables_delete**
> project_environment_variables_delete(project_name, id)

Delete project environment variable

## Description
Delete an environment variable of the project

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    id = 'id_example' # str

    # Delete project environment variable
    core_api.project_environment_variables_delete(project_name, id)

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
    id = 'id_example' # str

    # Delete project environment variable
    core_api.project_environment_variables_delete(project_name, id)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_environment_variables_get**
> EnvironmentVariableList project_environment_variables_get(project_name, id)

Get project environment variable

## Description
Retrieve details of a project environment variable.

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
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
    id = 'id_example' # str

    # Get project environment variable
    api_response = core_api.project_environment_variables_get(project_name, id)
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
    id = 'id_example' # str

    # Get project environment variable
    api_response = core_api.project_environment_variables_get(project_name, id)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **id** | **str** | 

### Return type

[**EnvironmentVariableList**](./models/EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_environment_variables_list**
> list[EnvironmentVariableList] project_environment_variables_list(project_name)

List project environment variables

## Description
List the environment variables defined for the project. These are the variables that are inherited by all deployments in this project.

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true
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

    # List project environment variables
    api_response = core_api.project_environment_variables_list(project_name)
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

    # List project environment variables
    api_response = core_api.project_environment_variables_list(project_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 

### Return type

[**list[EnvironmentVariableList]**](./models/EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_environment_variables_update**
> EnvironmentVariableList project_environment_variables_update(project_name, id, data)

Update project environment variable

## Description
Update an environment variable for the projects

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string.
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users. Can be updated from false to true, but not from true to false (i.e. secrets will stay secrets).

## Request Examples

```
{
  "name": "database_schema",
  "value": "new+schema",
  "secret": false
}
```

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

```
{
  "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
  "name": "database_schema",
  "value": "new_schema",
  "secret": false
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
    id = 'id_example' # str
    data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate

    # Update project environment variable
    api_response = core_api.project_environment_variables_update(project_name, id, data)
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
    id = 'id_example' # str
    data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate

    # Update project environment variable
    api_response = core_api.project_environment_variables_update(project_name, id, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **id** | **str** | 
 **data** | [**EnvironmentVariableCreate**](./models/EnvironmentVariableCreate.md) | 

### Return type

[**EnvironmentVariableList**](./models/EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_requests_list**
> list[RequestsOverview] project_requests_list(project_name, object_type, status=status, success=success, limit=limit, offset=offset, sort=sort, pipeline=pipeline, request_schedule=request_schedule, start_date=start_date, end_date=end_date, search_id=search_id)

List requests in project

## Description
List the deployment/pipeline requests of the given project

### Required Parameters

- `object_type`: The type of the object. It can be either deployment or pipeline.

### Optional Parameters

- `status`: Status of the request. Can be 'pending', 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `success`: A boolean value that indicates whether the deployment request was successful
- `limit`: The maximum number of requests given back, default is 50
- `offset`: The number which forms the starting point of the requests given back. If offset equals 2, then the first 2 requests will be omitted from the list.
- `sort`: Direction of sorting according to the creation date of the request, can be 'asc' or 'desc'. The default sorting is done in descending order.
- `pipeline`: A boolean value that indicates whether the deployment request was part of a pipeline request
- `request_schedule`: The name of a request schedule that created requests
- `start_date`: Start date of the interval for which the requests are retrieved, looking at the creation date of the request
- `end_date`: End date of the interval for which the requests are retrieved, looking at the creation date of the request
- `search_id`: A string to search inside request ids. It will filter all request ids that contain this string

### Response Structure
A list of dictionaries containing the metadata of the deployment/pipeline requests with the following fields:

- `id`: The UUID of the object
- `deployment`: Name of the deployment the request was made to (Optional: in case it's a deployment request. Else NULL)
- `pipeline`: Name of the pipeline the request was made to (Optional: in case it's a pipeline request. Else NULL)
- `version`: Name of the version the request was made to
- `status`: Status of the request
- `success`: A boolean value that indicates whether the deployment/pipeline request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "deployment": "deployment-1",
    "pipeline": null,
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "deployment": null,
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

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    object_type = 'object_type_example' # str
    status = 'status_example' # str (optional)
    success = True # bool (optional)
    limit = 56 # int (optional)
    offset = 56 # int (optional)
    sort = 'sort_example' # str (optional)
    pipeline = True # bool (optional)
    request_schedule = 'request_schedule_example' # str (optional)
    start_date = 'start_date_example' # str (optional)
    end_date = 'end_date_example' # str (optional)
    search_id = 'search_id_example' # str (optional)

    # List requests in project
    api_response = core_api.project_requests_list(project_name, object_type, status=status, success=success, limit=limit, offset=offset, sort=sort, pipeline=pipeline, request_schedule=request_schedule, start_date=start_date, end_date=end_date, search_id=search_id)
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
    object_type = 'object_type_example' # str
    status = 'status_example' # str (optional)
    success = True # bool (optional)
    limit = 56 # int (optional)
    offset = 56 # int (optional)
    sort = 'sort_example' # str (optional)
    pipeline = True # bool (optional)
    request_schedule = 'request_schedule_example' # str (optional)
    start_date = 'start_date_example' # str (optional)
    end_date = 'end_date_example' # str (optional)
    search_id = 'search_id_example' # str (optional)

    # List requests in project
    api_response = core_api.project_requests_list(project_name, object_type, status=status, success=success, limit=limit, offset=offset, sort=sort, pipeline=pipeline, request_schedule=request_schedule, start_date=start_date, end_date=end_date, search_id=search_id)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **object_type** | **str** | 
 **status** | **str** | [optional] 
 **success** | **bool** | [optional] 
 **limit** | **int** | [optional] 
 **offset** | **int** | [optional] 
 **sort** | **str** | [optional] 
 **pipeline** | **bool** | [optional] 
 **request_schedule** | **str** | [optional] 
 **start_date** | **str** | [optional] 
 **end_date** | **str** | [optional] 
 **search_id** | **str** | [optional] 

### Return type

[**list[RequestsOverview]**](./models/RequestsOverview.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_users_create**
> ProjectUserList project_users_create(project_name, data)

Add user to a project

## Description
Add a user to a project. The user making the request must be admin of the organization. The user can later be assigned roles in the project, such as project-admin, project-viewer etc.

### Required Parameters

- `user_id`: UUID of the user

## Request Examples

```
{
  "user_id": "bd3e25a3-f77a-4cb5-92df-a7e614106e95"
}
```

### Response Structure
Details of the added user

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

## Response Examples

```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name"
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
    data = ubiops.ProjectUserCreate() # ProjectUserCreate

    # Add user to a project
    api_response = core_api.project_users_create(project_name, data)
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
    data = ubiops.ProjectUserCreate() # ProjectUserCreate

    # Add user to a project
    api_response = core_api.project_users_create(project_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**ProjectUserCreate**](./models/ProjectUserCreate.md) | 

### Return type

[**ProjectUserList**](./models/ProjectUserList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_users_delete**
> project_users_delete(project_name, user_id)

Delete user from a project

## Description
Delete a user from a project. The user making the request must be admin of the organization.

**When a user is deleted from a project, all his roles defined in the scope of the project are also deleted.**

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    user_id = 'user_id_example' # str

    # Delete user from a project
    core_api.project_users_delete(project_name, user_id)

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
    user_id = 'user_id_example' # str

    # Delete user from a project
    core_api.project_users_delete(project_name, user_id)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **user_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_users_get**
> ProjectUserList project_users_get(project_name, user_id)

Get user in a project

## Description
Get the details of a user in a project. The user making the request must also be a project user.

### Response Structure
Details of the user

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

## Response Examples

```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name"
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
    user_id = 'user_id_example' # str

    # Get user in a project
    api_response = core_api.project_users_get(project_name, user_id)
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
    user_id = 'user_id_example' # str

    # Get user in a project
    api_response = core_api.project_users_get(project_name, user_id)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **user_id** | **str** | 

### Return type

[**ProjectUserList**](./models/ProjectUserList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_users_list**
> list[ProjectUserList] project_users_list(project_name, user_type=user_type)

List users in a project

## Description
List users and their details in a project. The user making the request must also be a project user.

### Response Structure
List of users

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

## Response Examples

```
[
  {
    "id": "54977bc3-2c3b-4d8f-97c7-aff89a95bf21",
    "email": "user@example.com",
    "name": "user",
    "surname": "name"
  },
  {
    "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
    "email": "user2@example.com",
    "name": "user",
    "surname": "name"
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
    user_type = 'user_type_example' # str (optional)

    # List users in a project
    api_response = core_api.project_users_list(project_name, user_type=user_type)
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
    user_type = 'user_type_example' # str (optional)

    # List users in a project
    api_response = core_api.project_users_list(project_name, user_type=user_type)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **user_type** | **str** | [optional] 

### Return type

[**list[ProjectUserList]**](./models/ProjectUserList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **projects_create**
> ProjectDetail projects_create(data)

Create projects

## Description
Create a new project with the provided name.
**Only the organization admins have permission to make this request.** When a new project is created, the current organization admins are assigned project-admin role for the created project.

### Required Parameters

- `name`: Name of the project. The name is globally unique. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter.
- `organization_name`: Name of the organization in which the project is going to be created

### Optional Parameters

- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project. It defaults to False.
- `credits`: Maximum usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours they are running. It defaults to null, meaning that there are no limits.

## Request Examples

```
{
  "name": "project-1",
  "organization_name": "organization-1"
}
```

### Response Structure
Details of the created project

- `id`: Unique identifier for the project (UUID)
- `name`: Name of the project
- `creation_date`: Time the project was created
- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project
- `organization_name`: Name of the organization in which the project is created
- `credits`: Maximum usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours they are running
- `suspended`: A boolean indicating whether the project is suspended due to going over the credits limit
- `suspended_reason`: Description explaining why the project is suspended

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "advanced_permissions": false,
  "organization_name": "organization-1",
  "credits": null,
  "suspended": false,
  "suspended_reason": null
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

    data = ubiops.ProjectCreate() # ProjectCreate

    # Create projects
    api_response = core_api.projects_create(data)
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

    data = ubiops.ProjectCreate() # ProjectCreate

    # Create projects
    api_response = core_api.projects_create(data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **data** | [**ProjectCreate**](./models/ProjectCreate.md) | 

### Return type

[**ProjectDetail**](./models/ProjectDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **projects_delete**
> projects_delete(project_name)

Delete a project

## Description
Delete a project. The user making the request must have appropriate permissions.
**When project is deleted, all the deployments and pipelines defined in it are also deleted.**

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str

    # Delete a project
    core_api.projects_delete(project_name)

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

    # Delete a project
    core_api.projects_delete(project_name)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **projects_get**
> ProjectDetail projects_get(project_name)

Get details of a project

## Description
Get the details of a single project. The user making the request must have appropriate permissions.

### Response Structure
Details of a project

- `id`: Unique identifier for the project (UUID)
- `name`: Name of the project
- `creation_date`: Time the project was created
- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project
- `organization_name`: Name of the organization in which the project is created
- `credits`: Maximum usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours they are running
- `suspended`: A boolean indicating whether the project is suspended due to going over the credits limit
- `suspended_reason`: Description explaining why the project is suspended

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "advanced_permissions": false,
  "organization_name": "organization-1",
  "credits": 10000,
  "suspended": false,
  "suspended_reason": null
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

    # Get details of a project
    api_response = core_api.projects_get(project_name)
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

    # Get details of a project
    api_response = core_api.projects_get(project_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 

### Return type

[**ProjectDetail**](./models/ProjectDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **projects_list**
> list[ProjectList] projects_list(organization=organization)

List projects

## Description
List all projects to which the user making request has access. The projects in organizations to which the user belongs are shown.

### Response Structure
A list of details of the projects

- `id`: Unique identifier for the project (UUID)

- `name`: Name of the project

- `creation_date`: Time the project was created

- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project

- `organization_name`: Name of the organization in which the project is created

### Optional Parameters
These parameters should be given as query parameters

- `organization`: Name of the organization whose projects should be obtained

## Response Examples

```
[
  {
    "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
    "name": "project-1",
    "creation_date": "2018-10-26",
    "advanced_permissions": false,
    "organization_name": "organization-1"
  },
  {
    "id": "e6a85cd7-94cc-44cf-9fa0-4b462d5a71ab",
    "name": "project-2",
    "creation_date": "2019-06-20",
    "advanced_permissions": false,
    "organization_name": "organization-2"
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

    organization = 'organization_example' # str (optional)

    # List projects
    api_response = core_api.projects_list(organization=organization)
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

    organization = 'organization_example' # str (optional)

    # List projects
    api_response = core_api.projects_list(organization=organization)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization** | **str** | [optional] 

### Return type

[**list[ProjectList]**](./models/ProjectList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **projects_log_list**
> list[Logs] projects_log_list(project_name, data=data)

List logs for a project

## Description
Retrieve the logs of all objects in a project, including deployments, pipelines and requests. Using filters you can filter the logs on the objects and information of your choice.

### Optional Parameters

- `filters`: A dictionary containing information to filter logs on. It may contain zero or more of the following fields:

    - `deployment_name`: name of a deployment

    - `deployment_version`: name of a deployment version. If this field is present in the request, deployment_name must also be given. The deployment versions are only meaningful in combination with the deployments they are defined for.

    - `deployment_version_revision_id`: the UUID of a deployment version revision. It does not have to be given in combination with the deployment and version name.

    - `environment_name`: name of an environment

    - `environment_build_id`: the UUID of an environment build. It does not have to be given in combination with the environment name.

    - `pipeline_name`: name of a pipeline

    - `pipeline_version`: name of a pipeline version. If this field is present in the request, pipeline_name must also be given. The pipeline versions are only meaningful in combination with the pipelines they are defined for.

    - `pipeline_object_name`: name of a pipeline object. If this field is present in the request, pipeline_name and pipeline_version must also be given. The pipeline objects are only meaningful in combination with the pipeline versions they are defined in.

    - `deployment_request_id`: the UUID of a deployment request

    - `pipeline_request_id`: the UUID of a pipeline request

    - `system`: whether the log was generated by the system or user code (true / false)

    - `level`: the level of the log (info / error)


Any combination of filters may be given in the request. For example, if only a deployment_name is provided, all logs for that deployment are returned. These logs can contain information from all the pipelines that deployment is referenced in. If the filters dictionary is empty, all logs for all objects in the project are returned.
Either `date` or `id` should be provided, as they both refer to a starting point of the logs. If no `date` or `id` is specified, the API will use the current time as a starting point and try to fetch the logs starting from now minus date range seconds into the past.

- `date`: Starting date for the logs. If it is not provided and the `id` parameter is not set, the most recent logs are returned. It should be provided in ISO 8601 format. The results are inclusive of the given date.

- `id`: identifier for log lines. If specified, it will act as a starting point for the interval in which to query the logs. This can be useful when making multiple queries to obtain consecutive logs

    It will include the log having the log id equal to the id value in the response, regardless of whether the date_range is positive or negative.
- `limit`: Limit for the logs response. If specified, it will limit the total number of logs returned from the query to the specified number. Defaults to 50, the maximum is 500.

- `date_range`: The date range parameter sets the interval of time in which to query the logs, specified in seconds. It may be a positive or a negative value.

    If it is positive, logs starting from the specified date / log id (both inclusive) plus date range seconds towards the present time are returned.

    Otherwise, logs starting from the specified date / log id (both inclusive) minus date range seconds towards the past are returned.

    The default value is -21600 (6 hours). The maximum value is -/+ 86400 seconds (24 hours).

## Request Examples

```
{
  "filters": {
    "deployment_name": "deployment-1",
    "deployment_version": "v1"
  },
  "date": "2020-01-01T00:00:00.000000Z"
}
```


```
{
  "filters": {
    "pipeline_name": "pipeline-1",
    "pipeline_version": "v1"
  },
  "id": "41d7a7c5cd025e3501a00000",
  "date_range": -100
}
```


```
{
  "filters": {
    "pipeline_name": "pipeline-1",
    "pipeline_version": "v1",
    "deployment_name": "deployment-1",
    "deployment_version": "v1"
  },
  "date": "2020-01-01T00:00:00.000000Z",
  "date_range": -86400,
  "limit": 5
}
```

### Response Structure
A list of log details

- `id`: Unique UUID of the log line

- `log`: Log line text

- `date`: Time the log line was created

The following fields will be returned on response if they are set for the log line:
- `deployment_name`:  The deployment which the log is related to

- `deployment_version`:  The deployment version which the log is related to

- `deployment_version_revision_id`: The UUID of the deployment version revision

- `environment_name`:  The environment which the log is related to

- `environment_build_id`: The UUID of the environment build

- `pipeline_name`: The pipeline which the log is related to

- `pipeline_version`: The pipeline version which the log is related to

- `pipeline_object_name`: The pipeline object which the log is related to

- `deployment_request_id`:  The deployment request the log is related to

- `pipeline_request_id`:  The pipeline request the log is related to

- `system`:  Whether the log was generated by the system (true / false)

- `level`: The level of the log (info / error)

## Response Examples
Logs for a specific deployment and version

```
[
  {
    "id": "5dcad12ba76a2c6e4331f180",
    "deployment_name": "deployment-1",
    "deployment_version": "v1",
    "date": "2020-01-01T00:00:00.000000Z",
    "log": "[Info] Prediction result 0.14981"
  },
  {
    "id": "5dcad12ba76a2c6e4331f181",
    "deployment_name": "deployment-1",
    "deployment_version": "v1",
    "deployment_request_id": "ee63f938-ba81-438e-8482-9ac76037895f",
    "pipeline_name": "pipeline-2",
    "pipeline_version": "v2",
    "pipeline_object_name": "deployment-1-v1-object",
    "pipeline_request_id": "8bb6ed79-8606-4acf-acd2-90507130523c",
    "date": "2020-01-01T00:00:01.000000Z",
    "log": "[Error] Deployment call result (failed)"
  }
]
```

Logs for a specific pipeline

```
[
  {
    "id": "5dcad12ba76a2c6e4331f192",
    "deployment_name": "deployment-2",
    "deployment_version": "v2",
    "deployment_request_id": "6ee941d3-9905-49f5-95b4-cd9c4c23bb03",
    "pipeline_name": "pipeline-1",
    "pipeline_version": "v1",
    "pipeline_object_name": "deployment-2-v2-object",
    "pipeline_request_id": "4f75b10d-6012-47ab-ae68-cc9e69f35841",
    "date": "2020-01-01T00:00:00.000000Z",
    "log": "[Info] Deployment call result (success): 0.2316"
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
    data = ubiops.LogsCreate() # LogsCreate (optional)

    # List logs for a project
    api_response = core_api.projects_log_list(project_name, data=data)
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
    data = ubiops.LogsCreate() # LogsCreate (optional)

    # List logs for a project
    api_response = core_api.projects_log_list(project_name, data=data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**LogsCreate**](./models/LogsCreate.md) | [optional] 

### Return type

[**list[Logs]**](./models/Logs.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **projects_resource_usage**
> ProjectResourceUsage projects_resource_usage(project_name)

List resource usage of a project

## Description
List the total number of resources used in a project

### Response Structure
A list containing the number of

- deployments

- deployment_versions

- pipelines

- pipeline_versions

currently defined in the project.

## Response Examples

```
{
  "deployments": 30,
  "deployment_versions": 47,
  "pipelines": 2,
  "pipeline_versions": 4
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

    # List resource usage of a project
    api_response = core_api.projects_resource_usage(project_name)
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

    # List resource usage of a project
    api_response = core_api.projects_resource_usage(project_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 

### Return type

[**ProjectResourceUsage**](./models/ProjectResourceUsage.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **projects_update**
> ProjectDetail projects_update(project_name, data)

Update a project

## Description
Update the name of a single project. The user making the request must have appropriate permissions.

### Optional Parameters

- `name`: New project name
- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project
- `credits`: Maximum usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours they are running
- `suspend`: A boolean to suspend and activate projects. If the project is already suspended by UbiOps, it is not possible to suspend/activate the project.

## Request Examples

```
{
  "name": "project-name-example"
}
```

### Response Structure
Details of a project

- `id`: Unique identifier for the project (UUID)
- `name`: Name of the project
- `creation_date`: Time the project was created
- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project
- `organization_name`: Name of the organization in which the project is created
- `credits`: Maximum usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours they are running
- `suspended`: A boolean indicating whether the project is suspended due to going over the credits limit
- `suspended_reason`: Description explaining why the project is suspended

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "advanced_permissions": false,
  "organization_name": "organization-1",
  "credits": 10000,
  "suspended": false,
  "suspended_reason": null
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
    data = ubiops.ProjectUpdate() # ProjectUpdate

    # Update a project
    api_response = core_api.projects_update(project_name, data)
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
    data = ubiops.ProjectUpdate() # ProjectUpdate

    # Update a project
    api_response = core_api.projects_update(project_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**ProjectUpdate**](./models/ProjectUpdate.md) | 

### Return type

[**ProjectDetail**](./models/ProjectDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **projects_usage_get**
> list[Usage] projects_usage_get(project_name, start_date=start_date, end_date=end_date, interval=interval)

Get resource usage

## Description
Get resource usage for the project. It contains **the details of each metric aggregated per month.**

### Optional Parameters

- `start_date`: date indicating the start date to fetch usage data from. If omitted, results are generated for current subscription period.
- `end_date`: date indicating the end date to fetch usage data until. If omitted, results are generated for current subscription period.
- `interval`: interval for which the usage data is fetched. It can be 'day' or 'month'. It defaults to 'month'.

If no **start_date** or **end_date** is given, the current subscription period is used, e.g. if the usage details are requested on 01-12-2020 and the subscription started on 20-11-2020, the results will contain data from 20-11-2020 to 20-12-2020.
When **start_date** and **end_date** are given, this month period is used, e.g. if 12-11-2020 is given as start date and 12-12-2020 as end date, the results will contain data from 12-11-2020 to 12-12-2020.

### Response Structure

- `metric`: Metric name
- `object_type`: Type of object the metric was measured for (deployment_version or pipeline_version)
- `usage`: an array of objects each containing the following:
  - `start_date`: Timestamp denoting the start of the current subscription period or the provided date
  - `end_date`: Timestamp denoting the end of the current subscription period or the provided date
  - `value`: Aggregated metric value for the given unit over the given month

## Response Examples
2019-08-01 as start date and 2019-09-01 as end date

```
[
  {
    "object_type": "deployment_version",
    "metric": "credits",
    "usage": [
      {
        "start_date": "2019-08-01T00:00:00Z",
        "end_date": "2019-09-01T00:00:00Z",
        "value": 13543
      } 
    ]
  },
  {
    "object_type": "deployment_version",
    "metric": "input_volume",
    "usage": [
      {
        "start_date": "2019-08-01T00:00:00Z",
        "end_date": "2019-09-01T00:00:00Z",
        "value": 136
      } 
    ]
  },
  {
    "object_type": "deployment_version",
    "metric": "output_volume",
    "usage": [
      {
        "start_date": "2019-08-01T00:00:00Z",
        "end_date": "2019-09-01T00:00:00Z",
        "value": 468
      } 
    ]
  },
  {
    "object_type": "pipeline_version",
    "metric": "input_volume",
    "usage": [
      {
        "start_date": "2019-08-01T00:00:00Z",
        "end_date": "2019-09-01T00:00:00Z",
        "value": 125
      } 
    ]
  },
  {
    "object_type": "pipeline_version",
    "metric": "output_volume",
    "usage": [
      {
        "start_date": "2019-08-01T00:00:00Z",
        "end_date": "2019-09-01T00:00:00Z",
        "value": 135
      } 
    ]
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
    start_date = str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')) # datetime (optional)
    end_date = str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')) # datetime (optional)
    interval = 'month' # str (optional) (default to 'month')

    # Get resource usage
    api_response = core_api.projects_usage_get(project_name, start_date=start_date, end_date=end_date, interval=interval)
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
    start_date = str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')) # datetime (optional)
    end_date = str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')) # datetime (optional)
    interval = 'month' # str (optional) (default to 'month')

    # Get resource usage
    api_response = core_api.projects_usage_get(project_name, start_date=start_date, end_date=end_date, interval=interval)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **start_date** | **datetime** | [optional] 
 **end_date** | **datetime** | [optional] 
 **interval** | **str** | [optional] [default to &#39;month&#39;]

### Return type

[**list[Usage]**](./models/Usage.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **quotas_list**
> list[QuotaDetail] quotas_list(project_name)

List quotas

## Description
List the quotas defined for a project. Project members can see quotas.

### Response Structure

- `resource`: The resource for the quota
- `quota`: Limit of how much the resource can be used in the project

## Response Examples

```
[
  {
    "resource": "memory_standard",
    "quota": 274877906944
  },
  {
    "resource": "cpu_standard",
    "quota": 62
  },
  {
    "resource": "gpu_standard",
    "quota": 0
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

    # List quotas
    api_response = core_api.quotas_list(project_name)
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

    # List quotas
    api_response = core_api.quotas_list(project_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 

### Return type

[**list[QuotaDetail]**](./models/QuotaDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

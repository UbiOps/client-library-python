# Request_Schedules

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_schedules_create**](RequestSchedules.md#request_schedules_create) | **POST** /projects/{project_name}/schedules | Create request schedules
[**request_schedules_delete**](RequestSchedules.md#request_schedules_delete) | **DELETE** /projects/{project_name}/schedules/{schedule_name} | Delete a request schedule
[**request_schedules_get**](RequestSchedules.md#request_schedules_get) | **GET** /projects/{project_name}/schedules/{schedule_name} | Get details of a request schedule
[**request_schedules_list**](RequestSchedules.md#request_schedules_list) | **GET** /projects/{project_name}/schedules | List request schedules
[**request_schedules_update**](RequestSchedules.md#request_schedules_update) | **PATCH** /projects/{project_name}/schedules/{schedule_name} | Update a request schedule


# **request_schedules_create**
> ScheduleList request_schedules_create(project_name, data)

Create request schedules

## Description
Create a new request schedule with the provided name

### Required Parameters

- `name`: Name of the request. The name is unique per project. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter.
- `object_type`: Type of object for which the request is made. Can be either 'deployment' or 'pipeline'.
- `object_name`: Name of deployment or pipeline for which the request is made
- `schedule`: Schedule in crontab format

### Optional Parameters

- `version`: Name of version for which the request schedule is made. If not provided, default version of the deployment/pipeline will be used.
- `request_data`: Input data for the request schedule. For structured deployments/pipelines, it must be a dictionary.
- `timeout`: Timeout of the request in seconds
- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled. Default is 'True'.
- `description`: Description of the request schedule
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Request Examples

```
{
  "name": "test-request",
  "object_type": "deployment",
  "object_name": "test-deployment",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "timeout": 300,
  "enabled": true,
  "description": "Daily request schedule",
  "labels": {
    "type": "daily"
  }
}
```

### Response Structure
Details of the created request schedule

- `name`: Name of the request
- `object_type`: Type of object for which the request is made
- `object_name`: Name of deployment/pipeline for which the request schedule is made
- `schedule`: Schedule in crontab format
- `version`: Name of version for which the request schedule is made
- `request_data`: Input data for the request schedule
- `timeout`: Timeout of the request in seconds
- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled
- `creation_date`: The date when the request schedule was created
- `description`: Description of the request schedule
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Response Examples

```
{
  "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
  "name": "test-request",
  "object_type": "deployment",
  "object_name": "test-deployment",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "timeout": 300,
  "enabled": true,
  "creation_date": "2020-09-16T08:06:34.457679Z",
  "description": "Daily request schedule",
  "labels": {
    "type": "daily"
  }
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
    data = ubiops.ScheduleCreate() # ScheduleCreate

    # Create request schedules
    api_response = core_api.request_schedules_create(project_name, data)
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
    data = ubiops.ScheduleCreate() # ScheduleCreate

    # Create request schedules
    api_response = core_api.request_schedules_create(project_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**ScheduleCreate**](./models/ScheduleCreate.md) | 

### Return type

[**ScheduleList**](./models/ScheduleList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **request_schedules_delete**
> request_schedules_delete(project_name, schedule_name)

Delete a request schedule

## Description
Delete the request schedule from the project.

If you want to temporarily disable a request schedule, update the request with `enabled` set to False.

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    schedule_name = 'schedule_name_example' # str

    # Delete a request schedule
    core_api.request_schedules_delete(project_name, schedule_name)

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
    schedule_name = 'schedule_name_example' # str

    # Delete a request schedule
    core_api.request_schedules_delete(project_name, schedule_name)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **schedule_name** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **request_schedules_get**
> ScheduleList request_schedules_get(project_name, schedule_name)

Get details of a request schedule

## Description
Retrieve details of a single request schedule

### Response Structure
Details of a request schedule

- `name`: Name of the request
- `object_type`: Type of object for which the request is made
- `object_name`: Name of deployment/pipeline for which the request is made
- `schedule`: Schedule in crontab format
- `version`: Name of version for which the request schedule is made
- `request_data`: Input data for the request schedule
- `timeout`: Timeout of the request in seconds
- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled
- `creation_date`: The date when the request schedule was created
- `description`: Description of the request schedule
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Response Examples

```
{
  "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
  "name": "test-request",
  "object_type": "deployment",
  "object_name": "test-deployment",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "timeout": 200,
  "enabled": true,
  "creation_date": "2020-09-16T08:06:34.457679Z",
  "description": "Daily request schedule",
  "labels": {
    "type": "daily"
  }
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
    schedule_name = 'schedule_name_example' # str

    # Get details of a request schedule
    api_response = core_api.request_schedules_get(project_name, schedule_name)
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
    schedule_name = 'schedule_name_example' # str

    # Get details of a request schedule
    api_response = core_api.request_schedules_get(project_name, schedule_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **schedule_name** | **str** | 

### Return type

[**ScheduleList**](./models/ScheduleList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **request_schedules_list**
> list[ScheduleList] request_schedules_list(project_name, labels=labels)

List request schedules

## Description
List the request schedules in a project. The user has to have 'requests.list' permission on either 'deployments.versions' or 'pipelines.versions' to list the request schedules.

### Optional Parameters

- `labels`: Filter on labels of the request schedules. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.

### Response Structure
A list of details of all request schedules in a project

- `name`: Name of the request
- `object_type`: Type of object for which the request is made
- `object_name`: Name of deployment/pipeline for which the request is made
- `schedule`: Schedule in crontab format
- `version`: Name of version for which the request schedule is made
- `request_data`: Input data for the request schedule
- `timeout`: Timeout of the request in seconds
- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled
- `creation_date`: The date when the request schedule was created
- `description`: Description of the request schedule
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Response Examples

```
[
  {
    "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
    "name": "test-request",
    "object_type": "deployment",
    "object_name": "test-deployment",
    "version": "v1",
    "schedule": "0 * 3 * *",
    "request_data": {
      "input_field_1": 2345,
      "input_field_2": 8765
    },
    "timeout": 200,
    "enabled": true,
    "creation_date": "2020-09-16T08:06:34.457679Z",
    "description": "Daily request schedule",
    "labels": {
      "type": "daily"
    }
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
    labels = 'labels_example' # str (optional)

    # List request schedules
    api_response = core_api.request_schedules_list(project_name, labels=labels)
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
    labels = 'labels_example' # str (optional)

    # List request schedules
    api_response = core_api.request_schedules_list(project_name, labels=labels)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **labels** | **str** | [optional] 

### Return type

[**list[ScheduleList]**](./models/ScheduleList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **request_schedules_update**
> ScheduleList request_schedules_update(project_name, schedule_name, data)

Update a request schedule

## Description
Update a request schedule in a project

### Optional Parameters

- `name`: Name of the request. The name is unique per project. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter.
- `schedule`: Schedule in crontab format
- `request_data`: Input data for the request schedule. For structured deployments/pipelines, it must be a dictionary.
- `timeout`: Timeout of the request in seconds
- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled. Default is 'True'.
- `description`: Description of the request schedule
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Request Examples

```
{
  "name": "test-request",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "timeout": 360,
  "enabled": false
}
```

### Response Structure
Details of the updated request schedule

- `name`: Name of the request
- `object_type`: Type of object for which the request is made
- `object_name`: Name of deployment/pipeline for which the request is made
- `schedule`: Schedule in crontab format
- `version`: Name of version for which the request schedule is made
- `request_data`: Input data for the request schedule
- `timeout`: Timeout of the request in seconds
- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled
- `creation_date`: The date when the request schedule was created
- `description`: Description of the request schedule
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Response Examples

```
{
  "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
  "name": "test-request",
  "object_type": "deployment",
  "object_name": "test-deployment",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "timeout": 360,
  "enabled": true,
  "creation_date": "2020-09-16T08:06:34.457679Z",
  "description": "Daily request schedule",
  "labels": {
    "type": "daily"
  }
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
    schedule_name = 'schedule_name_example' # str
    data = ubiops.ScheduleUpdate() # ScheduleUpdate

    # Update a request schedule
    api_response = core_api.request_schedules_update(project_name, schedule_name, data)
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
    schedule_name = 'schedule_name_example' # str
    data = ubiops.ScheduleUpdate() # ScheduleUpdate

    # Update a request schedule
    api_response = core_api.request_schedules_update(project_name, schedule_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **schedule_name** | **str** | 
 **data** | [**ScheduleUpdate**](./models/ScheduleUpdate.md) | 

### Return type

[**ScheduleList**](./models/ScheduleList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


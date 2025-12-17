# Services

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**services_create**](./Services.md#services_create) | **POST** /projects/{project_name}/services | Create service
[**services_delete**](./Services.md#services_delete) | **DELETE** /projects/{project_name}/services/{service_name} | Delete service
[**services_get**](./Services.md#services_get) | **GET** /projects/{project_name}/services/{service_name} | Get service
[**services_list**](./Services.md#services_list) | **GET** /projects/{project_name}/services | List services
[**services_update**](./Services.md#services_update) | **PATCH** /projects/{project_name}/services/{service_name} | Update service


# **services_create**
> ServiceDetail services_create(project_name, data)

Create service

## Description
Create a service in a project

### Required Parameters

- `name`: Name of the service
- `deployment`: Deployment of the service
- `version`: Version of the service. If not provided, the default version of the deployment is used.
- `port`: Port in the instances that are exposed

### Optional Parameters

- `description`: Description of the service
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `authentication_required`: Whether authentication is required on this service
- `authentication_method_token_enabled`: Whether authentication with a token is enabled
- `request_logging_excluded_paths`: A regex to exclude paths when storing requests
- `request_logging_excluded_extensions`: A list of file extensions to exclude when storing requests
- `health_check`: A dictionary containing the health check details
  - `path`: Path for the health check, it should start with a `/`
  - `interval`: (Optional) How often to check the service in seconds
  - `timeout`: (Optional) The number of seconds after which the health check times out
  - `failure_threshold`: (Optional) The number of times that the health check can fail before the service is considered failed
- `rate_limit_token`: Rate limit for the service per authentication token

## Request Examples

```
{
  "name": "service-1",
  "deployment": "deployment-1",
  "version": "v1",
  "port": 8080,
  "description": "",
  "labels": {},
  "authentication_required": true,
  "authentication_method_token_enabled": true,
  "request_logging_excluded_paths": "(health|status)$",
  "request_logging_excluded_extensions": ["svg", "tar"],
  "health_check": {"path": "/status"},
  "rate_limit_token": 300
}
```

### Response Structure

- `id`: Unique identifier for the service (UUID)
- `name`: Name of the service
- `deployment`: Deployment of the service
- `version`: Version of the service. If null, the default version of the deployment is used.
- `port`: Deployment port to use
- `time_created`: The date when the service was created
- `time_updated`: The date when the service was last updated
- `description`: Description of the service
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `authentication_required`: Whether authentication is required on this service
- `authentication_method_token_enabled`: Whether authentication with a token is enabled
- `request_logging_excluded_paths`: A regex to exclude paths when storing requests
- `request_logging_excluded_extensions`: A list of file extensions to exclude when storing requests
- `health_check`: A dictionary containing the health check details
- `rate_limit_token`: Rate limit for the service per authentication token
- `endpoint`: Service endpoint URL

## Response Examples

```
{
  "id": "4d13288f-9ac1-4dff-85da-fe48238a4dff",
  "name": "service-1",
  "deployment": "deployment-1",
  "version": "v1",
  "port": 8080,
  "time_created": "2025-10-09T12:38:10.060537Z",
  "time_updated": "2025-10-09T12:38:10.060537Z",
  "description": "",
  "labels": {},
  "authentication_required": true,
  "authentication_method_token_enabled": true,
  "request_logging_excluded_paths": "(health|status)$",
  "request_logging_excluded_extensions": ["svg", "tar"],
  "health_check": {"path": "/status"},
  "rate_limit_token": 300,
  "endpoint": "https://4d13288f-9ac1-4dff-85da-fe48238a4dff.services.ubiops.com"
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
data = ubiops.ServiceCreate() # ServiceCreate

# Create service
api_response = core_api.services_create(project_name, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**ServiceCreate**](./models/ServiceCreate.md) | 

### Return type

[**ServiceDetail**](./models/ServiceDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **services_delete**
> services_delete(project_name, service_name)

Delete service

## Description
Delete a service

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
service_name = 'service_name_example' # str

# Delete service
core_api.services_delete(project_name, service_name)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_name** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **services_get**
> ServiceDetail services_get(project_name, service_name)

Get service

## Description
Get the details of a service

### Response Structure

- `id`: Unique identifier for the service (UUID)
- `name`: Name of the service
- `deployment`: Deployment of the service
- `version`: Version of the service. If null, the default version of the deployment is used.
- `port`: Deployment port to use
- `time_created`: The date when the service was created
- `time_updated`: The date when the service was last updated
- `description`: Description of the service
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `authentication_required`: Whether authentication is required on this service
- `authentication_method_token_enabled`: Whether authentication with a token is enabled
- `request_logging_excluded_paths`: A regex to exclude paths when storing requests
- `request_logging_excluded_extensions`: A list of file extensions to exclude when storing requests
- `health_check`: A dictionary containing the health check details
- `rate_limit_token`: Rate limit for the service per authentication token
- `endpoint`: Service endpoint URL

## Response Examples

```
{
  "id": "4d13288f-9ac1-4dff-85da-fe48238a4dff",
  "name": "service-1",
  "deployment": "deployment-1",
  "version": "v1",
  "port": 8080,
  "time_created": "2025-10-09T12:38:10.060537Z",
  "time_updated": "2025-10-09T12:38:10.060537Z",
  "description": "",
  "labels": {},
  "authentication_required": true,
  "authentication_method_token_enabled": true,
  "request_logging_excluded_paths": "(health|status)$",
  "request_logging_excluded_extensions": ["svg", "tar"],
  "health_check": {"path": "/status"},
  "rate_limit_token": 300,
  "endpoint": "https://4d13288f-9ac1-4dff-85da-fe48238a4dff.services.ubiops.com"
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
service_name = 'service_name_example' # str

# Get service
api_response = core_api.services_get(project_name, service_name)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_name** | **str** | 

### Return type

[**ServiceDetail**](./models/ServiceDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **services_list**
> list[ServiceList] services_list(project_name, labels=labels, deployment_version_ids=deployment_version_ids)

List services

## Description
List services in a project

### Optional Parameters

- `labels`: Filter on labels of the services. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). Services that have at least one of the labels in the filter are returned. This parameter should be given as query parameter.
- `deployment_version_ids`: Filter on deployment version of the services. Separate multiple deployment version IDs with a comma (,). This parameter should be given as query parameter.

### Response Structure
A list of services   

- `id`: Unique identifier for the service (UUID)
- `name`: Name of the service
- `deployment`: Deployment of the service
- `version`: Version of the service. If null, the default version of the deployment is used.
- `port`: Port in the instances that are exposed
- `time_created`: Date when the service was created
- `time_updated`: Date when the service was last updated
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `authentication_required`: Whether authentication is required on this service

## Response Examples

```
[
  {
    "id": "4d13288f-9ac1-4dff-85da-fe48238a4dff",
    "name": "service-1",
    "deployment": "deployment-1",
    "version": "v1",
    "port": 8080,
    "time_created": "2025-10-09T12:38:10.060537Z",
    "time_updated": "2025-10-09T12:38:10.060537Z",
    "labels": {},
    "authentication_required": true
  },
  {
    "id": "3fe73d04-b0d8-4701-acf9-73525591fe1b",
    "name": "service-2",
    "deployment": "deployment-2",
    "version": "v1",
    "port": 3000,
    "time_created": "2025-10-10T08:01:24.010482Z",
    "time_updated": "2025-10-10T08:01:24.010482Z",
    "labels": {"type": "service"},
    "authentication_required": true
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
labels = "label1:value1,label2:value2" # str (optional)
deployment_version_ids = 'deployment_version_ids_example' # str (optional)

# List services
api_response = core_api.services_list(project_name, labels=labels, deployment_version_ids=deployment_version_ids)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **labels** | **str** | [optional] 
 **deployment_version_ids** | **str** | [optional] 

### Return type

[**list[ServiceList]**](./models/ServiceList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **services_update**
> ServiceDetail services_update(project_name, service_name, data)

Update service

## Description
Update a service in a project

### Optional Parameters

- `name`: Name of the service
- `deployment`: Deployment of the service
- `version`: Version of the service. If null, the default version of the deployment is used.
- `port`: Port in the instances that are exposed
- `description`: Description of the service
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `authentication_required`: Whether authentication is required on this service
- `authentication_method_token_enabled`: Whether authentication with a token is enabled
- `request_logging_excluded_paths`: A regex to exclude paths when storing requests
- `request_logging_excluded_extensions`: A list of file extensions to exclude when storing requests
- `health_check`: A dictionary containing the health check details
  - `path`: Path for the health check, it should start with a `/`
  - `interval`: (Optional) How often to check the service in seconds
  - `timeout`: (Optional) The number of seconds after which the health check times out
  - `failure_threshold`: (Optional) The number of times that the health check can fail before the service is considered failed
- `rate_limit_token`: Rate limit for the service per authentication token

## Request Examples

```
{
  "name": "service-1",
  "deployment": "deployment-1",
  "version": "v1",
  "port": 8080,
  "description": "",
  "labels": {},
  "authentication_required": true,
  "authentication_method_token_enabled": true,
  "request_logging_excluded_paths": "(health|status)$",
  "request_logging_excluded_extensions": ["svg", "tar"],
  "health_check": {"path": "/status"},
  "rate_limit_token": 300
}
```

### Response Structure

- `id`: Unique identifier for the service (UUID)
- `name`: Name of the service
- `deployment`: Deployment of the service
- `version`: Version of the service. If null, the default version of the deployment is used.
- `port`: Deployment port to use
- `time_created`: The date when the service was created
- `time_updated`: The date when the service was last updated
- `description`: Description of the service
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `authentication_required`: Whether authentication is required on this service
- `authentication_method_token_enabled`: Whether authentication with a token is enabled
- `request_logging_excluded_paths`: A regex to exclude paths when storing requests
- `request_logging_excluded_extensions`: A list of file extensions to exclude when storing requests
- `health_check`: A dictionary containing the health check details
- `rate_limit_token`: Rate limit for the service per authentication token
- `endpoint`: Service endpoint URL

## Response Examples

```
{
  "id": "4d13288f-9ac1-4dff-85da-fe48238a4dff",
  "name": "service-1",
  "deployment": "deployment-1",
  "version": "v1",
  "port": 8080,
  "time_created": "2025-10-09T12:38:10.060537Z",
  "time_updated": "2025-10-09T12:38:10.060537Z",
  "description": "",
  "labels": {},
  "authentication_required": true,
  "authentication_method_token_enabled": true,
  "request_logging_excluded_paths": "(health|status)$",
  "request_logging_excluded_extensions": ["svg", "tar"],
  "health_check": {"path": "/status"},
  "rate_limit_token": 300,
  "endpoint": "https://4d13288f-9ac1-4dff-85da-fe48238a4dff.services.ubiops.com"
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
service_name = 'service_name_example' # str
data = ubiops.ServiceUpdate() # ServiceUpdate

# Update service
api_response = core_api.services_update(project_name, service_name, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_name** | **str** | 
 **data** | [**ServiceUpdate**](./models/ServiceUpdate.md) | 

### Return type

[**ServiceDetail**](./models/ServiceDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


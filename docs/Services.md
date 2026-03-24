# Services

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**services_create**](./Services.md#services_create) | **POST** /projects/{project_name}/services | Create service
[**services_delete**](./Services.md#services_delete) | **DELETE** /projects/{project_name}/services/{service_name} | Delete service
[**services_get**](./Services.md#services_get) | **GET** /projects/{project_name}/services/{service_name} | Get service
[**services_list**](./Services.md#services_list) | **GET** /projects/{project_name}/services | List services
[**services_status_get**](./Services.md#services_status_get) | **GET** /projects/{project_name}/services/{service_name}/status | Get the service status
[**services_update**](./Services.md#services_update) | **PATCH** /projects/{project_name}/services/{service_name} | Update service
[**services_user_concurrency_limit_create**](./Services.md#services_user_concurrency_limit_create) | **POST** /projects/{project_name}/services/{service_name}/user-concurrency-limits | Create services user concurrency limit
[**services_user_concurrency_limit_delete**](./Services.md#services_user_concurrency_limit_delete) | **DELETE** /projects/{project_name}/services/{service_name}/user-concurrency-limits/{user_id} | Delete services user concurrency limit
[**services_user_concurrency_limit_get**](./Services.md#services_user_concurrency_limit_get) | **GET** /projects/{project_name}/services/{service_name}/user-concurrency-limits/{user_id} | Get services user concurrency limit
[**services_user_concurrency_limit_list**](./Services.md#services_user_concurrency_limit_list) | **GET** /projects/{project_name}/services/{service_name}/user-concurrency-limits | List services user concurrency limits
[**services_user_concurrency_limit_update**](./Services.md#services_user_concurrency_limit_update) | **PATCH** /projects/{project_name}/services/{service_name}/user-concurrency-limits/{user_id} | Update services user concurrency limit
[**services_user_rate_limit_create**](./Services.md#services_user_rate_limit_create) | **POST** /projects/{project_name}/services/{service_name}/user-rate-limits | Create services user rate limit
[**services_user_rate_limit_delete**](./Services.md#services_user_rate_limit_delete) | **DELETE** /projects/{project_name}/services/{service_name}/user-rate-limits/{user_id} | Delete services user rate limit
[**services_user_rate_limit_get**](./Services.md#services_user_rate_limit_get) | **GET** /projects/{project_name}/services/{service_name}/user-rate-limits/{user_id} | Get services user rate limit
[**services_user_rate_limit_list**](./Services.md#services_user_rate_limit_list) | **GET** /projects/{project_name}/services/{service_name}/user-rate-limits | List services user rate limits
[**services_user_rate_limit_update**](./Services.md#services_user_rate_limit_update) | **PATCH** /projects/{project_name}/services/{service_name}/user-rate-limits/{user_id} | Update services user rate limit


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
- `rate_limit`: Rate limit per minute for the entire service
- `rate_limit_user_default`: Default rate limit per minute for the service per user
- `concurrency_limit`: Concurrency limit for the entire service
- `concurrency_limit_user_default`: Default concurrency limit for the service per user

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
  "rate_limit": 3000,
  "rate_limit_user_default": 1000,
  "concurrency_limit": 100,
  "concurrency_limit_user_default": 50
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
- `rate_limit`: Rate limit per minute for the entire service
- `rate_limit_user_default`: Default rate limit per minute for the service per user
- `concurrency_limit`: Concurrency limit for the entire service
- `concurrency_limit_user_default`: Default concurrency limit for the service per user
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
  "rate_limit": 3000,
  "rate_limit_user_default": 1000,
  "concurrency_limit": 100,
  "concurrency_limit_user_default": 50,
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
- `rate_limit`: Rate limit per minute for the entire service
- `rate_limit_user_default`: Default rate limit per minute for the service per user
- `concurrency_limit`: Concurrency limit for the entire service
- `concurrency_limit_user_default`: Default concurrency limit for the service per user
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
  "rate_limit": 3000,
  "rate_limit_user_default": 1000,
  "concurrency_limit": 100,
  "concurrency_limit_user_default": 50,
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

# **services_status_get**
> ServiceStatus services_status_get(project_name, service_name)

Get the service status

## Description
Get the status of a service

### Response Structure

- `id`: Unique identifier for the service (UUID)
- `ready`: Boolean indicating if the service is ready or not
- `instances_ready`: Number of ready instances

## Response Examples

```
{
  "id": "4d13288f-9ac1-4dff-85da-fe48238a4dff",
  "ready": true,
  "instances_ready": 2
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
service_name = 'service_name_example' # str

# Get the service status
api_response = core_api.services_status_get(project_name, service_name)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_name** | **str** | 

### Return type

[**ServiceStatus**](./models/ServiceStatus.md)

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
- `rate_limit`: Rate limit per minute for the entire service
- `rate_limit_user_default`: Default rate limit per minute for the service per user
- `concurrency_limit`: Concurrency limit for the entire service
- `concurrency_limit_user_default`: Default concurrency limit for the service per user

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
  "rate_limit": 3000,
  "rate_limit_user_default": 1000,
  "concurrency_limit": 100,
  "concurrency_limit_user_default": 50
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
- `rate_limit`: Rate limit per minute for the entire service
- `rate_limit_user_default`: Default rate limit per minute for the service per user
- `concurrency_limit`: Concurrency limit for the entire service
- `concurrency_limit_user_default`: Default concurrency limit for the service per user
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
  "rate_limit": 3000,
  "rate_limit_user_default": 1000,
  "concurrency_limit": 100,
  "concurrency_limit_user_default": 50,
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

# **services_user_concurrency_limit_create**
> ServicesUserConcurrencyLimitList services_user_concurrency_limit_create(project_name, service_name, data)

Create services user concurrency limit

## Description
Create a concurrency limit for a user for a service

### Required Parameters

- `user_id`: Unique identifier for the user (UUID)
- `limit`: Concurrency limit

## Request Examples

```
{
  "user_id": "9294f470-ef0c-4778-ad81-6c54e93b3533",
  "limit": 20
}
```

### Response Structure

- `id`: Unique identifier for the user concurrency limit (UUID)
- `user_id`: Unique identifier for the user (UUID)
- `user_email`: Email of the user
- `limit`: Concurrency limit

## Response Examples

```
{
  "id": "03af4bed-3819-45b8-b161-56f6afd2353e",
  "user_id": "9294f470-ef0c-4778-ad81-6c54e93b3533",
  "user_email": "user@example.com",
  "limit": 20
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
service_name = 'service_name_example' # str
data = ubiops.ServicesUserConcurrencyLimitCreate() # ServicesUserConcurrencyLimitCreate

# Create services user concurrency limit
api_response = core_api.services_user_concurrency_limit_create(project_name, service_name, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_name** | **str** | 
 **data** | [**ServicesUserConcurrencyLimitCreate**](./models/ServicesUserConcurrencyLimitCreate.md) | 

### Return type

[**ServicesUserConcurrencyLimitList**](./models/ServicesUserConcurrencyLimitList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **services_user_concurrency_limit_delete**
> services_user_concurrency_limit_delete(project_name, service_name, user_id)

Delete services user concurrency limit

## Description
Delete the concurrency limit for a user for a service

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
service_name = 'service_name_example' # str
user_id = 'user_id_example' # str

# Delete services user concurrency limit
core_api.services_user_concurrency_limit_delete(project_name, service_name, user_id)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_name** | **str** | 
 **user_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **services_user_concurrency_limit_get**
> ServicesUserConcurrencyLimitList services_user_concurrency_limit_get(project_name, service_name, user_id)

Get services user concurrency limit

## Description
Get the concurrency limit for a user for a service

### Response Structure

- `id`: Unique identifier for the user concurrency limit (UUID)
- `user_id`: Unique identifier for the user (UUID)
- `user_email`: Email of the user
- `limit`: Concurrency limit

## Response Examples

```
{
  "id": "03af4bed-3819-45b8-b161-56f6afd2353e",
  "user_id": "9294f470-ef0c-4778-ad81-6c54e93b3533",
  "user_email": "user@example.com",
  "limit": 20
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
service_name = 'service_name_example' # str
user_id = 'user_id_example' # str

# Get services user concurrency limit
api_response = core_api.services_user_concurrency_limit_get(project_name, service_name, user_id)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_name** | **str** | 
 **user_id** | **str** | 

### Return type

[**ServicesUserConcurrencyLimitList**](./models/ServicesUserConcurrencyLimitList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **services_user_concurrency_limit_list**
> list[ServicesUserConcurrencyLimitList] services_user_concurrency_limit_list(project_name, service_name)

List services user concurrency limits

## Description
List user concurrency limits for a service in a project

### Response Structure
A list of user concurrency limits

- `id`: Unique identifier for the user concurrency limit (UUID)
- `user_id`: Unique identifier for the user (UUID)
- `user_email`: Email of the user
- `limit`: Concurrency limit

## Response Examples

```
[
  {
    "id": "03af4bed-3819-45b8-b161-56f6afd2353e",
    "user_id": "9294f470-ef0c-4778-ad81-6c54e93b3533",
    "user_email": "user@example.com",
    "limit": 20
  },
  {
    "id": "d43e4594-cb34-411c-92c3-3118373862f4",
    "user_id": "6d77c15f-c147-4262-9437-130d02c26a47",
    "user_email": "user2@example.com",
    "limit": 300
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
service_name = 'service_name_example' # str

# List services user concurrency limits
api_response = core_api.services_user_concurrency_limit_list(project_name, service_name)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_name** | **str** | 

### Return type

[**list[ServicesUserConcurrencyLimitList]**](./models/ServicesUserConcurrencyLimitList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **services_user_concurrency_limit_update**
> ServicesUserConcurrencyLimitList services_user_concurrency_limit_update(project_name, service_name, user_id, data)

Update services user concurrency limit

## Description
Update the concurrency limit for a user for a service

### Optional Parameters

- `limit`: Concurrency limit

## Request Examples

```
{
  "limit": 20
}
```

### Response Structure

- `id`: Unique identifier for the user concurrency limit (UUID)
- `user_id`: Unique identifier for the user (UUID)
- `user_email`: Email of the user
- `limit`: Concurrency limit

## Response Examples

```
{
  "id": "03af4bed-3819-45b8-b161-56f6afd2353e",
  "user_id": "9294f470-ef0c-4778-ad81-6c54e93b3533",
  "user_email": "user@example.com",
  "limit": 20
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
service_name = 'service_name_example' # str
user_id = 'user_id_example' # str
data = ubiops.ServicesUserConcurrencyLimitUpdate() # ServicesUserConcurrencyLimitUpdate

# Update services user concurrency limit
api_response = core_api.services_user_concurrency_limit_update(project_name, service_name, user_id, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_name** | **str** | 
 **user_id** | **str** | 
 **data** | [**ServicesUserConcurrencyLimitUpdate**](./models/ServicesUserConcurrencyLimitUpdate.md) | 

### Return type

[**ServicesUserConcurrencyLimitList**](./models/ServicesUserConcurrencyLimitList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **services_user_rate_limit_create**
> ServicesUserRateLimitList services_user_rate_limit_create(project_name, service_name, data)

Create services user rate limit

## Description
Create a rate limit for a user for a service

### Required Parameters

- `user_id`: Unique identifier for the user (UUID)
- `limit`: Rate limit per minute

## Request Examples

```
{
  "user_id": "9294f470-ef0c-4778-ad81-6c54e93b3533",
  "limit": 2000
}
```

### Response Structure

- `id`: Unique identifier for the user rate limit (UUID)
- `user_id`: Unique identifier for the user (UUID)
- `user_email`: Email of the user
- `limit`: Rate limit per minute

## Response Examples

```
{
  "id": "03af4bed-3819-45b8-b161-56f6afd2353e",
  "user_id": "9294f470-ef0c-4778-ad81-6c54e93b3533",
  "user_email": "user@example.com",
  "limit": 2000
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
service_name = 'service_name_example' # str
data = ubiops.ServicesUserRateLimitCreate() # ServicesUserRateLimitCreate

# Create services user rate limit
api_response = core_api.services_user_rate_limit_create(project_name, service_name, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_name** | **str** | 
 **data** | [**ServicesUserRateLimitCreate**](./models/ServicesUserRateLimitCreate.md) | 

### Return type

[**ServicesUserRateLimitList**](./models/ServicesUserRateLimitList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **services_user_rate_limit_delete**
> services_user_rate_limit_delete(project_name, service_name, user_id)

Delete services user rate limit

## Description
Delete the rate limit for a user for a service

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
service_name = 'service_name_example' # str
user_id = 'user_id_example' # str

# Delete services user rate limit
core_api.services_user_rate_limit_delete(project_name, service_name, user_id)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_name** | **str** | 
 **user_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **services_user_rate_limit_get**
> ServicesUserRateLimitList services_user_rate_limit_get(project_name, service_name, user_id)

Get services user rate limit

## Description
Get the rate limit for a user for a service

### Response Structure

- `id`: Unique identifier for the user rate limit (UUID)
- `user_id`: Unique identifier for the user (UUID)
- `user_email`: Email of the user
- `limit`: Rate limit per minute

## Response Examples

```
{
  "id": "03af4bed-3819-45b8-b161-56f6afd2353e",
  "user_id": "9294f470-ef0c-4778-ad81-6c54e93b3533",
  "user_email": "user@example.com",
  "limit": 2000
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
service_name = 'service_name_example' # str
user_id = 'user_id_example' # str

# Get services user rate limit
api_response = core_api.services_user_rate_limit_get(project_name, service_name, user_id)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_name** | **str** | 
 **user_id** | **str** | 

### Return type

[**ServicesUserRateLimitList**](./models/ServicesUserRateLimitList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **services_user_rate_limit_list**
> list[ServicesUserRateLimitList] services_user_rate_limit_list(project_name, service_name)

List services user rate limits

## Description
List user rate limits for a service in a project

### Response Structure
A list of user rate limits

- `id`: Unique identifier for the user rate limit (UUID)
- `user_id`: Unique identifier for the user (UUID)
- `user_email`: Email of the user
- `limit`: Rate limit per minute

## Response Examples

```
[
  {
    "id": "03af4bed-3819-45b8-b161-56f6afd2353e",
    "user_id": "9294f470-ef0c-4778-ad81-6c54e93b3533",
    "user_email": "user@example.com",
    "limit": 2000
  },
  {
    "id": "d43e4594-cb34-411c-92c3-3118373862f4",
    "user_id": "6d77c15f-c147-4262-9437-130d02c26a47",
    "user_email": "user2@example.com",
    "limit": 3000
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
service_name = 'service_name_example' # str

# List services user rate limits
api_response = core_api.services_user_rate_limit_list(project_name, service_name)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_name** | **str** | 

### Return type

[**list[ServicesUserRateLimitList]**](./models/ServicesUserRateLimitList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **services_user_rate_limit_update**
> ServicesUserRateLimitList services_user_rate_limit_update(project_name, service_name, user_id, data)

Update services user rate limit

## Description
Update the rate limit for a user for a service

### Optional Parameters

- `limit`: Rate limit per minute

## Request Examples

```
{
  "limit": 2000
}
```

### Response Structure

- `id`: Unique identifier for the user rate limit (UUID)
- `user_id`: Unique identifier for the user (UUID)
- `user_email`: Email of the user
- `limit`: Rate limit per minute

## Response Examples

```
{
  "id": "03af4bed-3819-45b8-b161-56f6afd2353e",
  "user_id": "9294f470-ef0c-4778-ad81-6c54e93b3533",
  "user_email": "user@example.com",
  "limit": 2000
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
service_name = 'service_name_example' # str
user_id = 'user_id_example' # str
data = ubiops.ServicesUserRateLimitUpdate() # ServicesUserRateLimitUpdate

# Update services user rate limit
api_response = core_api.services_user_rate_limit_update(project_name, service_name, user_id, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_name** | **str** | 
 **user_id** | **str** | 
 **data** | [**ServicesUserRateLimitUpdate**](./models/ServicesUserRateLimitUpdate.md) | 

### Return type

[**ServicesUserRateLimitList**](./models/ServicesUserRateLimitList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


# Service_Users

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_users_create**](./ServiceUsers.md#service_users_create) | **POST** /projects/{project_name}/service-users | Create a new service user
[**service_users_delete**](./ServiceUsers.md#service_users_delete) | **DELETE** /projects/{project_name}/service-users/{service_user_id} | Delete service user
[**service_users_get**](./ServiceUsers.md#service_users_get) | **GET** /projects/{project_name}/service-users/{service_user_id} | Retrieve details of a service user
[**service_users_list**](./ServiceUsers.md#service_users_list) | **GET** /projects/{project_name}/service-users | List service users
[**service_users_token**](./ServiceUsers.md#service_users_token) | **PUT** /projects/{project_name}/service-users/{service_user_id}/token | Reset the token of a service user
[**service_users_update**](./ServiceUsers.md#service_users_update) | **PATCH** /projects/{project_name}/service-users/{service_user_id} | Update service user details


# **service_users_create**
> ServiceUserTokenDetail service_users_create(project_name, data)

Create a new service user

## Description
Create a new service user. A unique email is generated for the service user. Additionally, a token for this service user is generated. This token can be used to authorize requests sent to our API. It is possible to set an expiry date for this token.
In addition, allowed cors origins can be configured for the service user. The service user will be allowed to make a deployment or pipeline request from these origins.

The token is **ONLY** returned on creation and will not be accessible afterwards.

### Optional Parameters

- `name`: Name of the service user

- `expiry_date`: Date when the service user account expires (UTC). If null is passed, the account will never expire.

## Request Examples

```
{
  "name": "service-user-1"
}
```


```
{
  "name": "service-user-1",
  "expiry_date": "2020-01-01T00:00:00.000Z"
}
```

### Response Structure
Details of the created service user

- `id`: Unique identifier for the service user (UUID)

- `email`: Email of the service user 

- `token`: The API token for the created service user 

- `name`: Name of the service user

- `creation_date`: Date when the service user was created

- `expiry_date`: Date when the service user account will expire (UTC)

## Response Examples

```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
  "token": "e962d9190348af7fa8d233d75cff7385b4335f81",
  "name": "service-user-1",
  "creation_date": "2020-03-24T09:16:27.504+00:00",
  "expiry_date": "2021-03-24T00:00:00.000+00:00"
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
    data = ubiops.ServiceUserCreate() # ServiceUserCreate

    # Create a new service user
    api_response = core_api.service_users_create(project_name, data)
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
    data = ubiops.ServiceUserCreate() # ServiceUserCreate

    # Create a new service user
    api_response = core_api.service_users_create(project_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**ServiceUserCreate**](./models/ServiceUserCreate.md) | 

### Return type

[**ServiceUserTokenDetail**](./models/ServiceUserTokenDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **service_users_delete**
> service_users_delete(project_name, service_user_id)

Delete service user

## Description
Delete a service user from a project

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    service_user_id = 'service_user_id_example' # str

    # Delete service user
    core_api.service_users_delete(project_name, service_user_id)

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
    service_user_id = 'service_user_id_example' # str

    # Delete service user
    core_api.service_users_delete(project_name, service_user_id)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_user_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **service_users_get**
> ServiceUserList service_users_get(project_name, service_user_id)

Retrieve details of a service user

## Description
Retrieve details of a service user

### Response Structure
Details of the service user

- `id`: Unique identifier for the service user (UUID)

- `email`: Email of the service user 

- `name`: Name of the service user

- `creation_date`: Date when the service user was created

- `expiry_date`: Date when the service user account will expire (UTC)

## Response Examples

```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
  "name": "new-service-user-name",
  "creation_date": "2020-03-26T12:18:43.123+00:00",
  "expiry_date": null
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
    service_user_id = 'service_user_id_example' # str

    # Retrieve details of a service user
    api_response = core_api.service_users_get(project_name, service_user_id)
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
    service_user_id = 'service_user_id_example' # str

    # Retrieve details of a service user
    api_response = core_api.service_users_get(project_name, service_user_id)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_user_id** | **str** | 

### Return type

[**ServiceUserList**](./models/ServiceUserList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **service_users_list**
> list[ServiceUserList] service_users_list(project_name)

List service users

## Description
List service users defined in a project

### Response Structure
List of details of the service users:

- `id`: Unique identifier for the service user (UUID)

- `email`: Email of the service user

- `name`: Name of the service user

- `creation_date`: Date when the service user was created

- `expiry_date`: Date when the service user account will expire (UTC)

## Response Examples

```
[
  {
    "id": "537bca64-5ab6-43eb-a7ef-1638bc30b6ed",
    "email": "537bca64-5ab6-43eb-a7ef-1638bc30b6ed.project1@serviceuser.ubiops.com",
    "name": "service-user-1",
    "creation_date": "2020-03-24T09:16:27.504+00:00",
    "expiry_date": "2021-03-24T00:00:00.000+00:00"
  },
  {
    "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
    "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
    "name": "service-user-2",
    "creation_date": "2020-03-26T12:18:43.123+00:00",
    "expiry_date": null
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

    # List service users
    api_response = core_api.service_users_list(project_name)
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

    # List service users
    api_response = core_api.service_users_list(project_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 

### Return type

[**list[ServiceUserList]**](./models/ServiceUserList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **service_users_token**
> ServiceUserTokenList service_users_token(project_name, service_user_id, data=data)

Reset the token of a service user

## Description
Reset the token of a service user. The old token will be deleted and a new one will be created for the service user. No data should be sent in the body of the request.

It is not possible to reset the token of a service user whose expiry date has been reached.

### Response Structure
Details of the new token for the service user

- `token`: The new API token for the service user

## Response Examples

```
{
  "token": "e962d9190348af7fa8d233d75cff7385b4335f81"
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
    service_user_id = 'service_user_id_example' # str
    data = None # object (optional)

    # Reset the token of a service user
    api_response = core_api.service_users_token(project_name, service_user_id, data=data)
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
    service_user_id = 'service_user_id_example' # str
    data = None # object (optional)

    # Reset the token of a service user
    api_response = core_api.service_users_token(project_name, service_user_id, data=data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_user_id** | **str** | 
 **data** | **object** | [optional] 

### Return type

[**ServiceUserTokenList**](./models/ServiceUserTokenList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **service_users_update**
> ServiceUserList service_users_update(project_name, service_user_id, data)

Update service user details

## Description
Update the name, expiry date and cors allowed origins of a service user. The new value for the cors_allowed_origin will replace the old value.
Leave as an empty list to remove the previous list of allowed origins.

It is not possible to update a service user whose expiry date has been reached.

### Optional Parameters

- `name`: Name of the service user

- `expiry_date`: Date when the service user account will expire (UTC). If null is passed, the account will never expire.

## Request Examples


```
{
  "name": "new-service-user-name",
}
```


```
{
  "expiry_date": "2020-01-01T00:00:00.000Z"
}
```

### Response Structure
Details of the updated service user

- `id`: Unique identifier for the service user (UUID)

- `email`: Email of the service user 

- `name`: Name of the service user

- `creation_date`: Date when the service user was created

- `expiry_date`: Date when the service user account will expire (UTC)

## Response Examples

```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
  "name": "new-service-user-name",
  "creation_date": "2020-03-26T12:18:43.123+00:00",
  "expiry_date": null
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
    service_user_id = 'service_user_id_example' # str
    data = ubiops.ServiceUserCreate() # ServiceUserCreate

    # Update service user details
    api_response = core_api.service_users_update(project_name, service_user_id, data)
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
    service_user_id = 'service_user_id_example' # str
    data = ubiops.ServiceUserCreate() # ServiceUserCreate

    # Update service user details
    api_response = core_api.service_users_update(project_name, service_user_id, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_user_id** | **str** | 
 **data** | [**ServiceUserCreate**](./models/ServiceUserCreate.md) | 

### Return type

[**ServiceUserList**](./models/ServiceUserList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


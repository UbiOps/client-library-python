# Organizations

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organization_users_create**](./Organizations.md#organization_users_create) | **POST** /organizations/{organization_name}/users | Add a user to an organization
[**organization_users_delete**](./Organizations.md#organization_users_delete) | **DELETE** /organizations/{organization_name}/users/{user_id} | Delete a user from an organization
[**organization_users_get**](./Organizations.md#organization_users_get) | **GET** /organizations/{organization_name}/users/{user_id} | Get details of a user in an organization
[**organization_users_list**](./Organizations.md#organization_users_list) | **GET** /organizations/{organization_name}/users | List the users in an organization
[**organization_users_update**](./Organizations.md#organization_users_update) | **PATCH** /organizations/{organization_name}/users/{user_id} | Update details of a user in an organization
[**organizations_create**](./Organizations.md#organizations_create) | **POST** /organizations | Create organizations
[**organizations_get**](./Organizations.md#organizations_get) | **GET** /organizations/{organization_name} | Get details of an organization
[**organizations_list**](./Organizations.md#organizations_list) | **GET** /organizations | List organizations
[**organizations_resource_usage**](./Organizations.md#organizations_resource_usage) | **GET** /organizations/{organization_name}/resources | Get resource usage
[**organizations_update**](./Organizations.md#organizations_update) | **PATCH** /organizations/{organization_name} | Update details of an organization
[**organizations_usage_get**](./Organizations.md#organizations_usage_get) | **GET** /organizations/{organization_name}/usage | Get organization usage


# **organization_users_create**
> OrganizationUserDetail organization_users_create(organization_name, data)

Add a user to an organization

## Description
Add a user to an organization as admin or normal user. The user making the request must be admin of the organization.
The user can later be assigned roles in the projects defined in the scope the organization, such as project-admin, project-viewer etc.

### Required Parameters

- `email`: Email of the user

- `admin`: Boolean value indicating whether the user is added as an admin of the organization or not

## Request Examples

```
{
  "email": "test@example.com",
  "admin": false
}
```

### Response Structure
Details of the added user

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

- `admin`: Boolean value indicating whether the user is an admin of the organization or not

## Response Examples

```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": false
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

    organization_name = 'organization_name_example' # str
    data = ubiops.OrganizationUserCreate() # OrganizationUserCreate

    # Add a user to an organization
    api_response = core_api.organization_users_create(organization_name, data)
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

    organization_name = 'organization_name_example' # str
    data = ubiops.OrganizationUserCreate() # OrganizationUserCreate

    # Add a user to an organization
    api_response = core_api.organization_users_create(organization_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 
 **data** | [**OrganizationUserCreate**](./models/OrganizationUserCreate.md) | 

### Return type

[**OrganizationUserDetail**](./models/OrganizationUserDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organization_users_delete**
> organization_users_delete(organization_name, user_id)

Delete a user from an organization

## Description
Delete a user from an organization. The user making the request must be admin of the organization.
It is not possible to delete the last admin of an organization.

**When a user is deleted from an organization, all his roles from all projects defined in the scope of the organization are also deleted.**

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    organization_name = 'organization_name_example' # str
    user_id = 'user_id_example' # str

    # Delete a user from an organization
    core_api.organization_users_delete(organization_name, user_id)

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

    organization_name = 'organization_name_example' # str
    user_id = 'user_id_example' # str

    # Delete a user from an organization
    core_api.organization_users_delete(organization_name, user_id)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 
 **user_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organization_users_get**
> OrganizationUserDetail organization_users_get(organization_name, user_id)

Get details of a user in an organization

## Description
Get the details of a user in an organization. The user making the request must be admin of the organization.

### Response Structure
Details of the user

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

- `admin`: Boolean value indicating whether the user is an admin of the organization or not

## Response Examples

```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": false
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

    organization_name = 'organization_name_example' # str
    user_id = 'user_id_example' # str

    # Get details of a user in an organization
    api_response = core_api.organization_users_get(organization_name, user_id)
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

    organization_name = 'organization_name_example' # str
    user_id = 'user_id_example' # str

    # Get details of a user in an organization
    api_response = core_api.organization_users_get(organization_name, user_id)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 
 **user_id** | **str** | 

### Return type

[**OrganizationUserDetail**](./models/OrganizationUserDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organization_users_list**
> list[OrganizationUserDetail] organization_users_list(organization_name)

List the users in an organization

## Description
List users and their details in an organization

### Response Structure
List of details of users

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

- `admin`: Boolean value indicating whether the user is an admin of the organization or not

## Response Examples

```
[
  {
    "id": "54977bc3-2c3b-4d8f-97c7-aff89a95bf21",
    "email": "user@example.com",
    "name": "user",
    "surname": "name",
    "admin": true
  },
  {
    "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
    "email": "user2@example.com",
    "name": "user",
    "surname": "name",
    "admin": false
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

    organization_name = 'organization_name_example' # str

    # List the users in an organization
    api_response = core_api.organization_users_list(organization_name)
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

    organization_name = 'organization_name_example' # str

    # List the users in an organization
    api_response = core_api.organization_users_list(organization_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 

### Return type

[**list[OrganizationUserDetail]**](./models/OrganizationUserDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organization_users_update**
> OrganizationUserDetail organization_users_update(organization_name, user_id, data)

Update details of a user in an organization

## Description
Update the admin status of a user in an organization. The user making the request must be admin of the organization.
It is not possible to change the last admin of an organization to a regular user.

### Required Parameters

- `admin`: Boolean value indicating whether the user is added as an admin of the organization or not

## Request Examples

```
{
  "admin": true
}
```

### Response Structure
Details of the user

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

- `admin`: Boolean value indicating whether the user is an admin of the organization or not

## Response Examples

```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": true
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

    organization_name = 'organization_name_example' # str
    user_id = 'user_id_example' # str
    data = ubiops.OrganizationUserUpdate() # OrganizationUserUpdate

    # Update details of a user in an organization
    api_response = core_api.organization_users_update(organization_name, user_id, data)
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

    organization_name = 'organization_name_example' # str
    user_id = 'user_id_example' # str
    data = ubiops.OrganizationUserUpdate() # OrganizationUserUpdate

    # Update details of a user in an organization
    api_response = core_api.organization_users_update(organization_name, user_id, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 
 **user_id** | **str** | 
 **data** | [**OrganizationUserUpdate**](./models/OrganizationUserUpdate.md) | 

### Return type

[**OrganizationUserDetail**](./models/OrganizationUserDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organizations_create**
> OrganizationList organizations_create(data)

Create organizations

## Description
Create a new organization. When a user creates an organization, s/he will automatically become an organization admin.

### Required Parameters

- `name`: Name of the organization. The name is globally unique. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter.

- `subscription`: Name of the subscription for the organization

### Optional Parameters

- `subscription_end_date`: End date of the subscription. The subscription will be cancelled on this date. A 'free' subscription cannot have a custom end_date as this subscription is always valid for a year.
If you are going to use a subscription other than the free subscription, you should provide the end date.

## Request Examples

```
{
  "name": "test-organization",
  "subscription": "premium",
  "subscription_end_date": "2021-03-25"
}
```


```
{
  "name": "test-organization",
  "subscription": "premium",
  "subscription_end_date": "2021-03-25"
}
```

### Response Structure
Details of the created organization

- `id`: Unique identifier for the organization (UUID)

- `name`: Name of the organization

- `creation_date`: Date and time the organization was created

## Response Examples

```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z"
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

    data = ubiops.OrganizationCreate() # OrganizationCreate

    # Create organizations
    api_response = core_api.organizations_create(data)
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

    data = ubiops.OrganizationCreate() # OrganizationCreate

    # Create organizations
    api_response = core_api.organizations_create(data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **data** | [**OrganizationCreate**](./models/OrganizationCreate.md) | 

### Return type

[**OrganizationList**](./models/OrganizationList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organizations_get**
> OrganizationDetail organizations_get(organization_name)

Get details of an organization

## Description
Get the details of an organization

### Response Structure
Details of the organization

- `id`: Unique identifier for the organization (UUID)

- `name`: Name of the organization

- `creation_date`: Time the organization was created

- `subscription`: Name of the subscription of the organization

- `subscription_self_service`: Boolean indicating if the organization subscription is self service

## Response Examples

```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z",
  "subscription": "free",
  "subscription_self_service": true
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

    organization_name = 'organization_name_example' # str

    # Get details of an organization
    api_response = core_api.organizations_get(organization_name)
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

    organization_name = 'organization_name_example' # str

    # Get details of an organization
    api_response = core_api.organizations_get(organization_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 

### Return type

[**OrganizationDetail**](./models/OrganizationDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organizations_list**
> list[OrganizationList] organizations_list()

List organizations

## Description
List all organizations where the user making the request is a member

### Response Structure
A list of details of the organizations

- `id`: Unique identifier for the organization (UUID)

- `name`: Name of the organization

- `creation_date`: Date and time the organization was created

## Response Examples

```
[
  {
    "id": "45a1f903-4146-4f15-be4a-302455cd6f7e",
    "name": "organization-name",
    "creation_date": "2020-03-23T11:47:15.436240Z"
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


    # List organizations
    api_response = core_api.organizations_list()
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


    # List organizations
    api_response = core_api.organizations_list()
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters

This endpoint does not need any parameter.

### Return type

[**list[OrganizationList]**](./models/OrganizationList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organizations_resource_usage**
> ResourceUsage organizations_resource_usage(organization_name)

Get resource usage

## Description
List the total number of resources used by this organization

### Response Structure
A list containing the number of

- projects
- users
- deployments
- deployment_versions
- pipelines
- pipeline_versions
- buckets
- environments
currently used by the organization.

## Response Examples

```
{
  "projects": 5,
  "users": 3,
  "deployments": 30,
  "deployment_versions": 47,
  "pipelines": 2,
  "pipeline_versions": 4,
  "buckets": 2,
  "environments": 2
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

    organization_name = 'organization_name_example' # str

    # Get resource usage
    api_response = core_api.organizations_resource_usage(organization_name)
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

    organization_name = 'organization_name_example' # str

    # Get resource usage
    api_response = core_api.organizations_resource_usage(organization_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 

### Return type

[**ResourceUsage**](./models/ResourceUsage.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organizations_update**
> OrganizationDetail organizations_update(organization_name, data)

Update details of an organization

## Description
Update an organization. The user making the request must be admin of the organization. Users are able to update the name of the organization, but changes to the subscription can only be done by Dutch Analytics.
To delete the end date of the current subscription, give the 'subscription_end_date' parameter with value null.

### Optional Parameters

- `name`: New organization name
- `subscription`: New subscription
- `subscription_end_date`: End date of the new subscription. The required format is `YYYY-MM-DD`. The subscription will be cancelled on this date. If you are going to update the subscription plan of the organization to a subscription other than free, you have to provide the end date.
- `subscription_start_date`: Start date of the new subscription. The required format is `YYYY-MM-DD`. The subscription will start from the provided date. If you are going to update the subscription of the organization or schedule a subscription for a time in future, you have to provide the start date.

## Request Examples



```
{
  "name": "new-organization-name"
}
```

```
{
  "subscription": "premium",
  "subscription_end_date": "2020-08-30",
  "subscription_start_date": "2020-07-30"
}
```

```
{
  "subscription_end_date": "2020-08-30",
  "subscription_start_date": "2020-07-30"
}
```

### Response Structure
Details of the organization

- `id`: Unique identifier for the organization (UUID)

- `name`: Name of the organization

- `creation_date`: Time the organization was created

- `subscription`: Name of the subscription

## Response Examples

```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z",
  "subscription": "free"
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

    organization_name = 'organization_name_example' # str
    data = ubiops.OrganizationUpdate() # OrganizationUpdate

    # Update details of an organization
    api_response = core_api.organizations_update(organization_name, data)
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

    organization_name = 'organization_name_example' # str
    data = ubiops.OrganizationUpdate() # OrganizationUpdate

    # Update details of an organization
    api_response = core_api.organizations_update(organization_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 
 **data** | [**OrganizationUpdate**](./models/OrganizationUpdate.md) | 

### Return type

[**OrganizationDetail**](./models/OrganizationDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organizations_usage_get**
> OrganizationUsage organizations_usage_get(organization_name, start_date=start_date, end_date=end_date, interval=interval)

Get organization usage

## Description
Get credits usage for the organization

### Optional Parameters

- `start_date`: Start date for the usage data to be returned. If omitted, results are generated for current subscription period.
- `end_date`: End date for the usage data to be returned. If omitted, results are generated for current subscription period.
- `interval`: Interval for the usage data. It can be 'day' or 'month'. It defaults to 'month'.

If no **start_date** or **end_date** is given, the current subscription period is used, e.g. if the usage details are requested on 01-12-2020 and the subscription started on 20-11-2020, the results will contain data from 20-11-2020 to 20-12-2020.
When **start_date** and **end_date** are given, this month period is used, e.g. if 12-11-2020 is given as start date and 12-12-2020 as end date, the results will contain data from 12-11-2020 to 12-12-2020.

### Response Structure

- `interval`: Interval for the usage data
- `data_organization`: A list of dictionaries containing the organization usage for the given date range
- `data_projects`: A list of dictionaries containing the usage of each project in the organization for the given date range
- `data_projects_deleted`: A list of dictionaries containing the usage corresponds to deleted projects in the organization for the given date range

## Response Examples
2019-08-01 as start date and 2019-09-01 as end date

```
{
  "interval": "month",
  "data_organization": [
    {
      "start_date": "2019-08-01T00:00:00Z",
      "end_date": "2019-09-01T00:00:00Z",
      "value": 600
    } 
  ],
  "data_projects": [
    {
      "project_id": "4aa10f82-24f3-4872-8883-f7a40e3a0733",
      "project_name": "project-1",
      "data": [
        {
          "start_date": "2019-08-01T00:00:00Z",
          "end_date": "2019-09-01T00:00:00Z",
          "value": 200
        }
      ]
    },
    {
      "project_id": "7e6238f3-d2c7-4d7d-a003-3e06a1c7a348",
      "project_name": "project-2",
      "data": [
        {
          "start_date": "2019-08-01T00:00:00Z",
          "end_date": "2019-09-01T00:00:00Z",
          "value": 300
        }
      ]
    }
  ],
  "data_deleted_projects": [
    {
      "start_date": "2019-08-01T00:00:00Z",
      "end_date": "2019-09-01T00:00:00Z",
      "value": 100
    }
  ]
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

    organization_name = 'organization_name_example' # str
    start_date = 'start_date_example' # str (optional)
    end_date = 'end_date_example' # str (optional)
    interval = 'month' # str (optional) (default to 'month')

    # Get organization usage
    api_response = core_api.organizations_usage_get(organization_name, start_date=start_date, end_date=end_date, interval=interval)
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

    organization_name = 'organization_name_example' # str
    start_date = 'start_date_example' # str (optional)
    end_date = 'end_date_example' # str (optional)
    interval = 'month' # str (optional) (default to 'month')

    # Get organization usage
    api_response = core_api.organizations_usage_get(organization_name, start_date=start_date, end_date=end_date, interval=interval)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 
 **start_date** | **str** | [optional] 
 **end_date** | **str** | [optional] 
 **interval** | **str** | [optional] [default to &#39;month&#39;]

### Return type

[**OrganizationUsage**](./models/OrganizationUsage.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


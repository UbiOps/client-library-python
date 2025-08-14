# User

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_create**](./User.md#user_create) | **POST** /user | Create a new user
[**user_delete**](./User.md#user_delete) | **DELETE** /user | Delete user


# **user_create**
> UserPendingDetail user_create(data)

Create a new user

## Description
Create a new user with the given details. After creation, an email is send to the email address to activate the account. The password needs to be at least 8 characters long.

### Required Parameters

- `email`: Email of the user
- `password`: Password of the user

### Optional Parameters

- `name`: Name of the user
- `surname`: Surname of the user

## Request Examples

```
{
  "email": "test@example.com",
  "password": "secret-password",
  "name": "User name",
  "surname": "User surname",
}
```


```
{
  "email": "test@example.com",
  "password": "secret-password"
}
```

### Response Structure
Details of the created user

- `email`: Email of the user
- `name`: Name of the user
- `surname`: Surname of the user

## Response Examples

```
{
  "email": "test@example.com",
  "name": "User name",
  "surname": "User surname",
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

    data = ubiops.UserPendingCreate() # UserPendingCreate

    # Create a new user
    api_response = core_api.user_create(data)
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

    data = ubiops.UserPendingCreate() # UserPendingCreate

    # Create a new user
    api_response = core_api.user_create(data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **data** | [**UserPendingCreate**](./models/UserPendingCreate.md) | 

### Return type

[**UserPendingDetail**](./models/UserPendingDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **user_delete**
> user_delete()

Delete user

## Description
Delete the user that makes the request

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()


    # Delete user
    core_api.user_delete()

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


    # Delete user
    core_api.user_delete()

    # Close the connection
    api_client.close()
    ```


### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


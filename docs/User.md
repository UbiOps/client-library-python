# User

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_create**](./User.md#user_create) | **POST** /user | Create a new user
[**user_delete**](./User.md#user_delete) | **DELETE** /user | Delete user
[**user_get**](./User.md#user_get) | **GET** /user | Get user details


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
  "surname": "User surname"
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
  "surname": "User surname"
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
data = ubiops.UserPendingCreate() # UserPendingCreate

# Create a new user
api_response = core_api.user_create(data)
print(api_response)
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

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python

# Delete user
core_api.user_delete()
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **user_get**
> UserDetail user_get()

Get user details

## Description
Get the details of the user that makes the request

### Response Structure
Details of the user

- `id`: Unique identifier for the user (UUID)
- `email`: Email of the user
- `name`: Name of the user
- `surname`: Surname of the user
- `registration_date`: Date when the user was registered
- `authentication`: Authentication method of the user. It can be 'google', 'microsoft' or 'ubiops'.

## Response Examples

```
{
  "id": "4740a13a-70ae-4b7a-a461-8231eb2c0594",
  "email": "test@example.com",
  "name": "User name",
  "surname": "User surname",
  "registration_date": "2020-01-10 10:06:25.632+00:00",
  "authentication": "ubiops"
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python

# Get user details
api_response = core_api.user_get()
print(api_response)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**UserDetail**](./models/UserDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


# Monitoring

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notification_groups_create**](Monitoring.md#notification_groups_create) | **POST** /projects/{project_name}/monitoring/notification-groups | Create notification groups
[**notification_groups_delete**](Monitoring.md#notification_groups_delete) | **DELETE** /projects/{project_name}/monitoring/notification-groups/{notification_group_name} | Delete notification group
[**notification_groups_get**](Monitoring.md#notification_groups_get) | **GET** /projects/{project_name}/monitoring/notification-groups/{notification_group_name} | Get notification group
[**notification_groups_list**](Monitoring.md#notification_groups_list) | **GET** /projects/{project_name}/monitoring/notification-groups | List notification groups
[**notification_groups_update**](Monitoring.md#notification_groups_update) | **PATCH** /projects/{project_name}/monitoring/notification-groups/{notification_group_name} | Update notification group


# **notification_groups_create**
> NotificationGroupList notification_groups_create(project_name, data)

Create notification groups

## Description
Create a notification group by defining a name and a list of contacts

### Required Parameters

- `name`: Name of the notification group. It is unique within a project.

### Optional Parameters

- `contacts`: A list of dictionaries containing the following keys:
  - `type`: Type of the contact. It can be `email`.
  - `configuration`: A custom dictionary that contains required information for the type. For `email` type, it should contain the key `email_address`.

## Request Examples

```
{
  "name": "notification-group-1",
  "contacts": [
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user@ubiops.com"
      }
    },
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user.2@ubiops.com"
      }
    }
  ]
}
```

### Response Structure
Details of the created notification group

- `id`: Unique identifier for the notification group (UUID)
- `name`: Name of the notification group
- `contacts`: A list of contacts in the notification group

## Response Examples

```
{
  "id": "dc083d2a-74aa-4c49-8806-8adbeadca8a8",
  "name": "notification-group-1",
  "contacts": [
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user@ubiops.com"
      }
    },
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user.2@ubiops.com"
      }
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

    project_name = 'project_name_example' # str
    data = ubiops.NotificationGroupCreate() # NotificationGroupCreate

    # Create notification groups
    api_response = core_api.notification_groups_create(project_name, data)
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
    data = ubiops.NotificationGroupCreate() # NotificationGroupCreate

    # Create notification groups
    api_response = core_api.notification_groups_create(project_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**NotificationGroupCreate**](./models/NotificationGroupCreate.md) | 

### Return type

[**NotificationGroupList**](./models/NotificationGroupList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **notification_groups_delete**
> notification_groups_delete(project_name, notification_group_name)

Delete notification group

## Description
Delete a notification group

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    notification_group_name = 'notification_group_name_example' # str

    # Delete notification group
    core_api.notification_groups_delete(project_name, notification_group_name)

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
    notification_group_name = 'notification_group_name_example' # str

    # Delete notification group
    core_api.notification_groups_delete(project_name, notification_group_name)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **notification_group_name** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **notification_groups_get**
> NotificationGroupList notification_groups_get(project_name, notification_group_name)

Get notification group

## Description
Retrieve details of a single notification group in a project

### Response Structure
Details of a notification group

- `id`: Unique identifier for the notification group (UUID)
- `name`: Name of the notification group
- `contacts`: A list of contacts in the notification group

## Response Examples

```
{
  "id": "dc083d2a-74aa-4c49-8806-8adbeadca8a8",
  "name": "notification-group-1",
  "contacts": [
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user@ubiops.com"
      }
    },
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user.2@ubiops.com"
      }
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

    project_name = 'project_name_example' # str
    notification_group_name = 'notification_group_name_example' # str

    # Get notification group
    api_response = core_api.notification_groups_get(project_name, notification_group_name)
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
    notification_group_name = 'notification_group_name_example' # str

    # Get notification group
    api_response = core_api.notification_groups_get(project_name, notification_group_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **notification_group_name** | **str** | 

### Return type

[**NotificationGroupList**](./models/NotificationGroupList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **notification_groups_list**
> list[NotificationGroupList] notification_groups_list(project_name)

List notification groups

## Description
List the notification groups in a project

### Response Structure
A list of details of the notification groups in the project

- `id`: Unique identifier for the notification group (UUID)
- `name`: Name of the notification group
- `contacts`: A list of contacts in the notification group

## Response Examples

```
[
  {
    "id": "dc083d2a-74aa-4c49-8806-8adbeadca8a8",
    "name": "notification-group-1",
    "contacts": [
      {
        "type": "email",
        "configuration": {
          "email_address": "my.example.user@ubiops.com"
        }
      },
      {
        "type": "email",
        "configuration": {
          "email_address": "my.example.user.2@ubiops.com"
        }
      }
    ],
  },
  {
    "id": "7193ca09-d28b-4fce-a15a-11e0bc9f7f6f",
    "name": "notification-group-2",
     "contacts": [
      {
        "type": "email",
        "configuration": {
          "email_address": "my.example.user.3@ubiops.com"
        }
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

    # List notification groups
    api_response = core_api.notification_groups_list(project_name)
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

    # List notification groups
    api_response = core_api.notification_groups_list(project_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 

### Return type

[**list[NotificationGroupList]**](./models/NotificationGroupList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **notification_groups_update**
> NotificationGroupList notification_groups_update(project_name, notification_group_name, data)

Update notification group

## Description
Update a notification group

### Optional Parameters

- `name`: New name for the deployment
- `contacts`: A list of dictionaries containing the following keys:
- `type`: Type of the contact. It can be `email`.
- `configuration`: A custom dictionary that contains required information for the type. For `email` type, it should contain the key `email_address`.

## Request Examples

```
{
  "name": "new-notification-group-name"
}
```

### Response Structure
Details of the updated notification group

- `id`: Unique identifier for the notification group (UUID)
- `name`: Name of the notification group
- `contacts`: A list of contacts in the notification group

## Response Examples

```
{
  "id": "dc083d2a-74aa-4c49-8806-8adbeadca8a8",
  "name": "new-notification-group-name",
  "contacts": [
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user@ubiops.com"
      }
    },
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user.2@ubiops.com"
      }
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

    project_name = 'project_name_example' # str
    notification_group_name = 'notification_group_name_example' # str
    data = ubiops.NotificationGroupUpdate() # NotificationGroupUpdate

    # Update notification group
    api_response = core_api.notification_groups_update(project_name, notification_group_name, data)
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
    notification_group_name = 'notification_group_name_example' # str
    data = ubiops.NotificationGroupUpdate() # NotificationGroupUpdate

    # Update notification group
    api_response = core_api.notification_groups_update(project_name, notification_group_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **notification_group_name** | **str** | 
 **data** | [**NotificationGroupUpdate**](./models/NotificationGroupUpdate.md) | 

### Return type

[**NotificationGroupList**](./models/NotificationGroupList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


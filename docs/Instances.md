# Instances

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instance_events_list**](./Instances.md#instance_events_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/instances/{instance_id}/events | List events for instances
[**instance_type_groups_create**](./Instances.md#instance_type_groups_create) | **POST** /projects/{project_name}/instance-type-groups | Create instance type group
[**instance_type_groups_delete**](./Instances.md#instance_type_groups_delete) | **DELETE** /projects/{project_name}/instance-type-groups/{instance_type_group_id} | Delete instance type group
[**instance_type_groups_get**](./Instances.md#instance_type_groups_get) | **GET** /projects/{project_name}/instance-type-groups/{instance_type_group_id} | Get instance type group
[**instance_type_groups_list**](./Instances.md#instance_type_groups_list) | **GET** /projects/{project_name}/instance-type-groups | List instance type groups
[**instance_type_groups_update**](./Instances.md#instance_type_groups_update) | **PATCH** /projects/{project_name}/instance-type-groups/{instance_type_group_id} | Update instance type group
[**instance_types_list**](./Instances.md#instance_types_list) | **GET** /projects/{project_name}/instance-types | List instance types
[**instances_get**](./Instances.md#instances_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/instances/{instance_id} | Get instance for deployment versions
[**instances_list**](./Instances.md#instances_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/instances | List instances for deployment versions
[**project_instances_get**](./Instances.md#project_instances_get) | **GET** /projects/{project_name}/instances/{instance_id} | Get instance for projects
[**project_instances_list**](./Instances.md#project_instances_list) | **GET** /projects/{project_name}/instances | List instances for projects


# **instance_events_list**
> InstanceEventPaginated instance_events_list(project_name, deployment_name, instance_id, version, cursor=cursor, limit=limit)

List events for instances

## Description
List the events for an instance. The results are paginated, use `cursor` and `limit` parameters to go between pages.

### Response Structure
A list of event details

- `id`: Unique identifier for the event (UUID)
- `time_created`: The date when the event was created
- `description`: Description of the event

## Response Examples

```
{
  "previous": null,
  "next": null,
  "results": [
    {
      "id": "d2727027-b681-43f1-be84-5f7bc7cbec4f",
      "time_created": "2023-05-01T16:25:11.195716Z",
      "description": "Instance status changed to initialising"
    },
    {
      "id": "36489db5-0fa8-467a-b2d3-8edcb7479726",
      "time_created": "2023-05-01T16:25:05.987451Z",
      "description": "Deployed on node pool 'Google CPU'"
    },
    {
      "id": "08c8bf93-4ece-4d99-9ecf-4f19d6703a58",
      "time_created": "2023-05-01T16:24:03.987451Z",
      "description": "Attempting to deploy with instance type '2048mb' on node pool 'Google CPU' (GCP cluster)"
    },
    {
      "id": "63ef2820-71ba-4a90-ba4e-a57035d1350f",
      "time_created": "2023-05-01T16:23:15.456812Z",
      "description": "Instance created"
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
    deployment_name = 'deployment_name_example' # str
    instance_id = 'instance_id_example' # str
    version = 'version_example' # str
    cursor = 'cursor_example' # str (optional)
    limit = 56 # int (optional)

    # List events for instances
    api_response = core_api.instance_events_list(project_name, deployment_name, instance_id, version, cursor=cursor, limit=limit)
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
    instance_id = 'instance_id_example' # str
    version = 'version_example' # str
    cursor = 'cursor_example' # str (optional)
    limit = 56 # int (optional)

    # List events for instances
    api_response = core_api.instance_events_list(project_name, deployment_name, instance_id, version, cursor=cursor, limit=limit)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **instance_id** | **str** | 
 **version** | **str** | 
 **cursor** | **str** | [optional] 
 **limit** | **int** | [optional] 

### Return type

[**InstanceEventPaginated**](./models/InstanceEventPaginated.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **instance_type_groups_create**
> InstanceTypeGroupList instance_type_groups_create(project_name, data)

Create instance type group

## Description
Create an instance type group in a project

### Required Parameters

- `name`: Name of the instance type group
- `instance_types`: A list of dictionaries containing the instance types that should be in the group
  - `id`: ID of the instance type
  - `priority`: Priority of the instance type. The lower the value, the more priority the instance type has.

## Request Examples

```
{
  "name": "instance-type-group-1",
  "instance_types": [
    {
      "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
      "priority": 0
    },
    {
      "id": "64dfc63d-a1fd-41b6-a01f-90caa74a270b",
      "priority": 1
    }
  ]
}
```

### Response Structure

- `id`: Unique identifier for the created instance type group (UUID)
- `name`: Name of the instance type group
- `time_created`: The date when the instance type group was created
- `time_updated`: The date when the instance type group was last updated
- `instance_types`: A list of instance types that are in this group
  - `id`: Unique identifier for the instance type (UUID)
  - `time_created`: The date when the instance type was created
  - `name`: Name of the instance type
  - `display_name`: Readable name of the instance type
  - `cpu`: Float indicating vCPU allocation
  - `memory`: Float indicating memory allocation (Mi)
  - `storage`: Float indicating the maximum storage that can be used (MB)
  - `accelerator`: Float indicating number of GPU cores
  - `credit_rate`: Credits used per hour
  - `dedicated_node`: A boolean indicating whether an entire node is dedicated to this instance type
  - `node_pool`: A dictionary containing the node pool details of the instance type
    - `cluster`: A dictionary containing the cluster details of the node pool
      - `type`: Type of the cluster
  - `priority`: Priority of the instance type in the group. The lower the value, the more priority the instance type has.
  - `schedule_timeout`: Timeout in seconds that indicates how long to wait until the instance type is scheduled.

## Response Examples

```
{
  "id": "6e1b5dcb-cb35-4fa6-9120-cfc1ba0c5f07",
  "name": "instance-type-group-1",
  "time_created": "2024-05-05T12:14:12.081753Z",
  "time_updated": "2024-05-05T12:14:12.081753Z",
  "instance_types": [
    {
      "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
      "time_created": "2024-05-01T08:32:14.876451Z",
      "name": "16384mb",
      "display_name": "16384 MB",
      "cpu": 4,
      "memory": 16384,
      "accelerator": 0,
      "storage": 65536,
      "credit_rate": 16,
      "dedicated_node": false,
      "node_pool": {
        "cluster": {
          "type": "gcp"
        }
      },
      "priority": 0,
      "schedule_timeout": 3600
    },
    {
      "id": "64dfc63d-a1fd-41b6-a01f-90caa74a270b",
      "time_created": "2024-05-01T08:32:14.876451Z",
      "name": "8192mb",
      "display_name": "8192 MB",
      "cpu": 2,
      "memory": 8192,
      "accelerator": 0,
      "storage": 32768,
      "credit_rate": 8,
      "dedicated_node": false,
      "node_pool": {
        "cluster": {
          "type": "aws"
        }
      },
      "priority": 1,
      "schedule_timeout": 3600
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
    data = ubiops.InstanceTypeGroupCreate() # InstanceTypeGroupCreate

    # Create instance type group
    api_response = core_api.instance_type_groups_create(project_name, data)
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
    data = ubiops.InstanceTypeGroupCreate() # InstanceTypeGroupCreate

    # Create instance type group
    api_response = core_api.instance_type_groups_create(project_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**InstanceTypeGroupCreate**](./models/InstanceTypeGroupCreate.md) | 

### Return type

[**InstanceTypeGroupList**](./models/InstanceTypeGroupList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **instance_type_groups_delete**
> instance_type_groups_delete(project_name, instance_type_group_id)

Delete instance type group

## Description
Delete an instance type group. If the instance type group is referenced by any deployment versions, it cannot be deleted.

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    instance_type_group_id = 'instance_type_group_id_example' # str

    # Delete instance type group
    core_api.instance_type_groups_delete(project_name, instance_type_group_id)

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
    instance_type_group_id = 'instance_type_group_id_example' # str

    # Delete instance type group
    core_api.instance_type_groups_delete(project_name, instance_type_group_id)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **instance_type_group_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **instance_type_groups_get**
> InstanceTypeGroupList instance_type_groups_get(project_name, instance_type_group_id)

Get instance type group

## Description
Get the details of an instance type group

### Response Structure

- `id`: Unique identifier for the instance type group (UUID)
- `name`: Name of the instance type group
- `time_created`: The date when the instance type group was created
- `time_updated`: The date when the instance type group was last updated
- `instance_types`: A list of instance types that are in this group
  - `id`: Unique identifier for the instance type (UUID)
  - `time_created`: The date when the instance type was created
  - `name`: Name of the instance type
  - `display_name`: Readable name of the instance type
  - `cpu`: Float indicating vCPU allocation
  - `memory`: Float indicating memory allocation (Mi)
  - `storage`: Float indicating the maximum storage that can be used (MB)
  - `accelerator`: Float indicating number of GPU cores
  - `credit_rate`: Credits used per hour
  - `dedicated_node`: A boolean indicating whether an entire node is dedicated to this instance type
  - `node_pool`: A dictionary containing the node pool details of the instance type
    - `cluster`: A dictionary containing the cluster details of the node pool
      - `type`: Type of the cluster
  - `priority`: Priority of the instance type in the group. The lower the value, the more priority the instance type has.
  - `schedule_timeout`: Timeout in seconds that indicates how long to wait until the instance type is scheduled.

## Response Examples

```
{
  "id": "6e1b5dcb-cb35-4fa6-9120-cfc1ba0c5f07",
  "name": "high-memory-instance-type-group",
  "time_created": "2024-05-05T12:14:12.081753Z",
  "time_updated": "2024-05-05T12:14:12.081753Z",
  "instance_types": [
    {
      "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
      "time_created": "2024-05-01T08:32:14.876451Z",
      "name": "16384mb",
      "display_name": "16384 MB",
      "cpu": 4,
      "memory": 16384,
      "accelerator": 0,
      "storage": 65536,
      "credit_rate": 16,
      "dedicated_node": false,
      "node_pool": {
        "cluster": {
          "type": "gcp"
        }
      },
      "priority": 0,
      "schedule_timeout": 3600
    },
    {
      "id": "64dfc63d-a1fd-41b6-a01f-90caa74a270b",
      "time_created": "2024-05-01T08:32:14.876451Z",
      "name": "8192mb",
      "display_name": "8192 MB",
      "cpu": 2,
      "memory": 8192,
      "accelerator": 0,
      "storage": 32768,
      "credit_rate": 8,
      "dedicated_node": false,
      "node_pool": {
        "cluster": {
          "type": "aws"
        }
      },
      "priority": 1,
      "schedule_timeout": 3600
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
    instance_type_group_id = 'instance_type_group_id_example' # str

    # Get instance type group
    api_response = core_api.instance_type_groups_get(project_name, instance_type_group_id)
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
    instance_type_group_id = 'instance_type_group_id_example' # str

    # Get instance type group
    api_response = core_api.instance_type_groups_get(project_name, instance_type_group_id)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **instance_type_group_id** | **str** | 

### Return type

[**InstanceTypeGroupList**](./models/InstanceTypeGroupList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **instance_type_groups_list**
> InstanceTypeGroupListPaginated instance_type_groups_list(project_name, cursor=cursor, limit=limit)

List instance type groups

## Description
List instance type groups in a project. The results are paginated, use `cursor` and `limit` parameters to go between pages.

### Response Structure
A list of instance type groups

- `id`: Unique identifier for the instance type group (UUID)
- `name`: Name of the instance type group
- `time_created`: The date when the instance type group was created
- `time_updated`: The date when the instance type group was last updated
- `instance_types`: A list of instance types that are in this group
  - `id`: Unique identifier for the instance type (UUID)
  - `time_created`: The date when the instance type was created
  - `name`: Name of the instance type
  - `display_name`: Readable name of the instance type
  - `cpu`: Float indicating vCPU allocation
  - `memory`: Float indicating memory allocation (Mi)
  - `storage`: Float indicating the maximum storage that can be used (MB)
  - `accelerator`: Float indicating number of GPU cores
  - `credit_rate`: Credits used per hour
  - `dedicated_node`: A boolean indicating whether an entire node is dedicated to this instance type
  - `node_pool`: A dictionary containing the node pool details of the instance type
    - `cluster`: A dictionary containing the cluster details of the node pool
      - `type`: Type of the cluster
  - `priority`: Priority of the instance type in the group. The lower the value, the more priority the instance type has.
  - `schedule_timeout`: Timeout in seconds that indicates how long to wait until the instance type is scheduled.

## Response Examples

```
{
  "previous": null,
  "next": null,
  "results": [
    {
      "id": "6e1b5dcb-cb35-4fa6-9120-cfc1ba0c5f07",
      "name": "high-memory-instance-type-group",
      "time_created": "2024-05-05T12:14:12.081753Z",
      "time_updated": "2024-05-05T12:14:12.081753Z",
      "instance_types": [
        {
          "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
          "time_created": "2024-05-01T08:32:14.876451Z",
          "name": "16384mb",
          "display_name": "16384 MB",
          "cpu": 4,
          "memory": 16384,
          "accelerator": 0,
          "storage": 65536,
          "credit_rate": 16,
          "dedicated_node": false,
          "node_pool": {
            "cluster": {
              "type": "gcp"
            }
          },
          "priority": 0,
          "schedule_timeout": 3600
        },
        {
          "id": "64dfc63d-a1fd-41b6-a01f-90caa74a270b",
          "time_created": "2024-05-01T08:32:14.876451Z",
          "name": "8192mb",
          "display_name": "8192 MB",
          "cpu": 2,
          "memory": 8192,
          "accelerator": 0,
          "storage": 32768,
          "credit_rate": 8,
          "dedicated_node": false,
          "node_pool": {
            "cluster": {
              "type": "aws"
            }
          },
          "priority": 1,
          "schedule_timeout": 3600
        }
      ]
    },
    {
      "id": "4bb1a7d8-24b4-49e3-9b63-34fbbf604c35",
      "name": "low-memory-instance-type-group",
      "time_created": "2024-05-06T15:32:49.916572Z",
      "time_updated": "2024-05-06T15:32:49.916572Z",
      "instance_types": [
        {
          "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
          "time_created": "2024-05-01T08:32:14.876451Z",
          "name": "256mb",
          "display_name": "256 MB",
          "cpu": 0.0625,
          "memory": 256,
          "accelerator": 0,
          "storage": 1024,
          "credit_rate": 0.25,
          "dedicated_node": false,
          "node_pool": {
            "cluster": {
              "type": "gcp"
            }
          },
          "priority": 0,
          "schedule_timeout": 3600
        }
      ]
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
    cursor = 'cursor_example' # str (optional)
    limit = 56 # int (optional)

    # List instance type groups
    api_response = core_api.instance_type_groups_list(project_name, cursor=cursor, limit=limit)
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
    cursor = 'cursor_example' # str (optional)
    limit = 56 # int (optional)

    # List instance type groups
    api_response = core_api.instance_type_groups_list(project_name, cursor=cursor, limit=limit)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **cursor** | **str** | [optional] 
 **limit** | **int** | [optional] 

### Return type

[**InstanceTypeGroupListPaginated**](./models/InstanceTypeGroupListPaginated.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **instance_type_groups_update**
> InstanceTypeGroupList instance_type_groups_update(project_name, instance_type_group_id, data)

Update instance type group

## Description
Update an instance type group in a project

### Optional Parameters

- `name`: Name of the instance type group
- `instance_types`: A list of dictionaries containing the instance types that should be in the group. Previously added instance types will be removed.
  - `id`: ID of the instance type
  - `priority`: Priority of the instance type. The lower the value, the more priority the instance type has.

## Request Examples

```
{
  "name": "instance-type-group-1",
  "instance_types": [
    {
      "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
      "priority": 0
    },
    {
      "id": "64dfc63d-a1fd-41b6-a01f-90caa74a270b",
      "priority": 1
    }
  ]
}
```

### Response Structure

- `id`: Unique identifier for the created instance type group (UUID)
- `name`: Name of the instance type group
- `time_created`: The date when the instance type group was created
- `time_updated`: The date when the instance type group was last updated
- `instance_types`: A list of instance types that are in this group
  - `id`: Unique identifier for the instance type (UUID)
  - `time_created`: The date when the instance type was created
  - `name`: Name of the instance type
  - `display_name`: Readable name of the instance type
  - `cpu`: Float indicating vCPU allocation
  - `memory`: Float indicating memory allocation (Mi)
  - `storage`: Float indicating the maximum storage that can be used (MB)
  - `accelerator`: Float indicating number of GPU cores
  - `credit_rate`: Credits used per hour
  - `dedicated_node`: A boolean indicating whether an entire node is dedicated to this instance type
  - `node_pool`: A dictionary containing the node pool details of the instance type
    - `cluster`: A dictionary containing the cluster details of the node pool
      - `type`: Type of the cluster
  - `priority`: Priority of the instance type in the group. The lower the value, the more priority the instance type has.
  - `schedule_timeout`: Timeout in seconds that indicates how long to wait until the instance type is scheduled.

## Response Examples

```
{
  "id": "6e1b5dcb-cb35-4fa6-9120-cfc1ba0c5f07",
  "name": "instance-type-group-1",
  "time_created": "2024-05-05T12:14:12.081753Z",
  "time_updated": "2024-05-05T12:14:12.081753Z",
  "instance_types": [
    {
      "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
      "time_created": "2024-05-01T08:32:14.876451Z",
      "name": "16384mb",
      "display_name": "16384 MB",
      "cpu": 4,
      "memory": 16384,
      "accelerator": 0,
      "storage": 65536,
      "credit_rate": 16,
      "dedicated_node": false,
      "node_pool": {
        "cluster": {
          "type": "gcp"
      },
      "priority": 0,
      "schedule_timeout": 3600
    },
    {
      "id": "64dfc63d-a1fd-41b6-a01f-90caa74a270b",
      "time_created": "2024-05-01T08:32:14.876451Z",
      "name": "8192mb",
      "display_name": "8192 MB",
      "cpu": 2,
      "memory": 8192,
      "accelerator": 0,
      "storage": 32768,
      "credit_rate": 8,
      "dedicated_node": false,
      "node_pool": {
        "cluster": {
          "type": "aws"
        }
      },
      "priority": 1,
      "schedule_timeout": 3600
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
    instance_type_group_id = 'instance_type_group_id_example' # str
    data = ubiops.InstanceTypeGroupCreate() # InstanceTypeGroupCreate

    # Update instance type group
    api_response = core_api.instance_type_groups_update(project_name, instance_type_group_id, data)
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
    instance_type_group_id = 'instance_type_group_id_example' # str
    data = ubiops.InstanceTypeGroupCreate() # InstanceTypeGroupCreate

    # Update instance type group
    api_response = core_api.instance_type_groups_update(project_name, instance_type_group_id, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **instance_type_group_id** | **str** | 
 **data** | [**InstanceTypeGroupCreate**](./models/InstanceTypeGroupCreate.md) | 

### Return type

[**InstanceTypeGroupList**](./models/InstanceTypeGroupList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **instance_types_list**
> InstanceTypeListPaginated instance_types_list(project_name, cursor=cursor, limit=limit)

List instance types

## Description
List available instance types in a project. The results are paginated, use `cursor` and `limit` parameters to go between pages.

### Response Structure
A list of instance types

- `id`: Unique identifier for the instance type (UUID)
- `time_created`: The date when the instance type was created
- `name`: Name of the instance type
- `display_name`: Readable name of the instance type
- `cpu`: Float indicating vCPU allocation
- `memory`: Float indicating memory allocation (Mi)
- `storage`: Float indicating the maximum storage that can be used (MB)
- `accelerator`: Float indicating number of GPU cores
- `credit_rate`: Credits used per hour
- `dedicated_node`: A boolean indicating whether an entire node is dedicated to this instance type
- `node_pool`: A dictionary containing the node pool details of the instance type
  - `cluster`: A dictionary containing the cluster details of the node pool
    - `type`: Type of the cluster

## Response Examples

```
{
  "previous": null,
  "next": null,
  "results": [
    {
      "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
      "time_created": "2024-05-01T08:32:14.876451Z",
      "name": "512mb",
      "display_name": "512 MB",
      "cpu": 0.125,
      "memory": 512.0,
      "storage": 2048.0,
      "accelerator": 0,
      "credit_rate": 0.5,
      "dedicated_node": false,
      "node_pool": {
        "cluster": {
          "type": "gcp"
        }
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
    cursor = 'cursor_example' # str (optional)
    limit = 56 # int (optional)

    # List instance types
    api_response = core_api.instance_types_list(project_name, cursor=cursor, limit=limit)
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
    cursor = 'cursor_example' # str (optional)
    limit = 56 # int (optional)

    # List instance types
    api_response = core_api.instance_types_list(project_name, cursor=cursor, limit=limit)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **cursor** | **str** | [optional] 
 **limit** | **int** | [optional] 

### Return type

[**InstanceTypeListPaginated**](./models/InstanceTypeListPaginated.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **instances_get**
> InstanceDetail instances_get(project_name, deployment_name, instance_id, version)

Get instance for deployment versions

## Description
Get the details of an instance running for a deployment version

### Response Structure

- `id`: Unique identifier for the instance (UUID)
- `status`: Status of the instance. It can be one of the following: pending, initialising, running, stopping.
- `time_created`: The date when the instance was created
- `time_updated`: The date when the instance was last updated
- `instance_type`: A dictionary containing instance type details of the instance. If the instance has no instance type set yet, it is null.
  - `id`: UUID of the instance type
  - `name`: Name of the instance type
  - `display_name`: Display name of the instance type
- `node`: A dictionary containing the node details of the instance
  - `ipv4_address`: IPv4 address of the node
  - `ipv6_address`: IPv6 address of the node
- `node_pool`: A dictionary containing the node pool details of the instance. If the instance has no node pool set yet, it is null.
  - `cluster`: A dictionary containing the cluster details of the node pool
    - `type`: Type of the cluster
- `deployment`: Name of the deployment for which the instance is running for
- `version`: Name of the version for which the instance is running for

## Response Examples

```
{
  "id": "33a0541a-11a5-44f7-8722-b7428d1faf80",
  "status": "pending",
  "time_created": "2024-05-01T08:32:14.876451Z",
  "time_updated": "2024-05-01T08:32:14.876451Z",
  "instance_type": null,
  "node": {
    "ipv4_address": null,
    "ipv6_address": null
  },
  "node_pool": null,
  "deployment": "deployment-1",
  "version": "v1"
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
    instance_id = 'instance_id_example' # str
    version = 'version_example' # str

    # Get instance for deployment versions
    api_response = core_api.instances_get(project_name, deployment_name, instance_id, version)
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
    instance_id = 'instance_id_example' # str
    version = 'version_example' # str

    # Get instance for deployment versions
    api_response = core_api.instances_get(project_name, deployment_name, instance_id, version)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **instance_id** | **str** | 
 **version** | **str** | 

### Return type

[**InstanceDetail**](./models/InstanceDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **instances_list**
> InstanceListPaginated instances_list(project_name, deployment_name, version, cursor=cursor, limit=limit, status=status)

List instances for deployment versions

## Description
List the instances running for a deployment version. The results are paginated, use `cursor` and `limit` parameters to go between pages.

### Optional Parameters

- `status`: Filter on status of the instance. Separate multiple statuses with a comma (,). This parameter should be given as query parameter.

### Response Structure
A list of instance details

- `id`: Unique identifier for the instance (UUID)
- `status`: Status of the instance. It can be one of the following: pending, initialising, running, stopping.
- `time_created`: The date when the instance was created
- `time_updated`: The date when the instance was last updated
- `instance_type`: A dictionary containing instance type details of the instance. If the instance has no instance type set yet, it is null.
  - `id`: UUID of the instance type
  - `name`: Name of the instance type
  - `display_name`: Display name of the instance type

## Response Examples

```
{
  "previous": null,
  "next": null,
  "results": [
    {
      "id": "33a0541a-11a5-44f7-8722-b7428d1faf80",
      "status": "pending",
      "time_created": "2024-05-01T08:32:14.876451Z",
      "time_updated": "2024-05-01T08:32:14.876451Z",
      "instance_type": null
    },
    {
      "id": "12d376cf-11ee-4bec-b52a-d76f4daf4314",
      "status": "running",
      "time_created": "2024-05-01T07:13:13.973651Z",
      "time_updated": "2024-05-01T08:32:14.876451Z",
      "instance_type": {
        "id": "fe1485df-f4d8-466e-913e-06d3569e4b39",
        "name": "512mb",
        "display_name": "512 MB",
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
    deployment_name = 'deployment_name_example' # str
    version = 'version_example' # str
    cursor = 'cursor_example' # str (optional)
    limit = 56 # int (optional)
    status = 'status_example' # str (optional)

    # List instances for deployment versions
    api_response = core_api.instances_list(project_name, deployment_name, version, cursor=cursor, limit=limit, status=status)
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
    cursor = 'cursor_example' # str (optional)
    limit = 56 # int (optional)
    status = 'status_example' # str (optional)

    # List instances for deployment versions
    api_response = core_api.instances_list(project_name, deployment_name, version, cursor=cursor, limit=limit, status=status)
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
 **cursor** | **str** | [optional] 
 **limit** | **int** | [optional] 
 **status** | **str** | [optional] 

### Return type

[**InstanceListPaginated**](./models/InstanceListPaginated.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_instances_get**
> InstanceDetail project_instances_get(project_name, instance_id)

Get instance for projects

## Description
Get the details of an instance running in a project

### Response Structure

- `id`: Unique identifier for the instance (UUID)
- `status`: Status of the instance. It can be one of the following: pending, initialising, running, stopping.
- `time_created`: The date when the instance was created
- `time_updated`: The date when the instance was last updated
- `instance_type`: A dictionary containing instance type details of the instance. If the instance has no instance type set yet, it is null.
  - `id`: UUID of the instance type
  - `name`: Name of the instance type
  - `display_name`: Display name of the instance type
- `node`: A dictionary containing the node details of the instance
  - `ipv4_address`: IPv4 address of the node
  - `ipv6_address`: IPv6 address of the node
- `node_pool`: A dictionary containing the node pool details of the instance. If the instance has no node pool set yet, it is null.
  - `cluster`: A dictionary containing the cluster details of the node pool
    - `type`: Type of the cluster
- `deployment`: Name of the deployment for which the instance is running for
- `version`: Name of the version for which the instance is running for

## Response Examples

```
{
  "id": "33a0541a-11a5-44f7-8722-b7428d1faf80",
  "status": "pending",
  "time_created": "2024-05-01T08:32:14.876451Z",
  "time_updated": "2024-05-01T08:32:14.876451Z",
  "instance_type": null,
  "node": {
    "ipv4_address": null,
    "ipv6_address": null
  },
  "node_pool": null,
  "deployment": "deployment-1",
  "version": "v1"
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
    instance_id = 'instance_id_example' # str

    # Get instance for projects
    api_response = core_api.project_instances_get(project_name, instance_id)
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
    instance_id = 'instance_id_example' # str

    # Get instance for projects
    api_response = core_api.project_instances_get(project_name, instance_id)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **instance_id** | **str** | 

### Return type

[**InstanceDetail**](./models/InstanceDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_instances_list**
> ProjectInstanceListPaginated project_instances_list(project_name, cursor=cursor, limit=limit, status=status)

List instances for projects

## Description
List the instances running in a project. The results are paginated, use `cursor` and `limit` parameters to go between pages.

### Optional Parameters

- `status`: Filter on status of the instance. Separate multiple statuses with a comma (,). This parameter should be given as query parameter.

### Response Structure
A list of instance details

- `id`: Unique identifier for the instance (UUID)
- `status`: Status of the instance. It can be one of the following: pending, initialising, running, stopping.
- `time_created`: The date when the instance was created
- `time_updated`: The date when the instance was last updated
- `instance_type`: A dictionary containing instance type details of the instance. If the instance has no instance type set yet, it is null.
  - `id`: UUID of the instance type
  - `name`: Name of the instance type
  - `display_name`: Display name of the instance type
- `deployment`: Name of the deployment for which the instance is running for
- `version`: Name of the version for which the instance is running for

## Response Examples

```
{
  "previous": null,
  "next": null,
  "results": [
    {
      "id": "33a0541a-11a5-44f7-8722-b7428d1faf80",
      "status": "pending",
      "time_created": "2024-05-01T08:32:14.876451Z",
      "time_updated": "2024-05-01T08:32:14.876451Z",
      "instance_type": null,
      "deployment": "deployment-1",
      "version": "v1"
    },
    {
      "id": "12d376cf-11ee-4bec-b52a-d76f4daf4314",
      "status": "running",
      "time_created": "2024-05-01T07:13:13.973651Z",
      "time_updated": "2024-05-01T08:32:14.876451Z",
      "instance_type": {
        "id": "fe1485df-f4d8-466e-913e-06d3569e4b39",
        "name": "512mb",
        "display_name": "512 MB",
      },
      "deployment": "deployment-2",
      "version": "v1"
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
    cursor = 'cursor_example' # str (optional)
    limit = 56 # int (optional)
    status = 'status_example' # str (optional)

    # List instances for projects
    api_response = core_api.project_instances_list(project_name, cursor=cursor, limit=limit, status=status)
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
    cursor = 'cursor_example' # str (optional)
    limit = 56 # int (optional)
    status = 'status_example' # str (optional)

    # List instances for projects
    api_response = core_api.project_instances_list(project_name, cursor=cursor, limit=limit, status=status)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **cursor** | **str** | [optional] 
 **limit** | **int** | [optional] 
 **status** | **str** | [optional] 

### Return type

[**ProjectInstanceListPaginated**](./models/ProjectInstanceListPaginated.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


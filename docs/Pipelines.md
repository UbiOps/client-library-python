# Pipelines

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expressions_evaluate**](Pipelines.md#expressions_evaluate) | **POST** /expressions/evaluate | Evaluate expression
[**pipeline_audit_events_list**](Pipelines.md#pipeline_audit_events_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/audit | List audit events for a pipeline
[**pipeline_version_object_environment_variables_list**](Pipelines.md#pipeline_version_object_environment_variables_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/objects/{name}/environment-variables | List pipeline object environment variables
[**pipeline_versions_create**](Pipelines.md#pipeline_versions_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions | Create pipeline versions
[**pipeline_versions_delete**](Pipelines.md#pipeline_versions_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Delete pipeline version
[**pipeline_versions_get**](Pipelines.md#pipeline_versions_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Get pipeline version
[**pipeline_versions_list**](Pipelines.md#pipeline_versions_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions | List pipeline versions
[**pipeline_versions_update**](Pipelines.md#pipeline_versions_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Update pipeline version
[**pipelines_create**](Pipelines.md#pipelines_create) | **POST** /projects/{project_name}/pipelines | Create pipelines
[**pipelines_delete**](Pipelines.md#pipelines_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name} | Delete a pipeline
[**pipelines_get**](Pipelines.md#pipelines_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name} | Get details of a pipeline
[**pipelines_list**](Pipelines.md#pipelines_list) | **GET** /projects/{project_name}/pipelines | List pipelines
[**pipelines_update**](Pipelines.md#pipelines_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name} | Update a pipeline


# **expressions_evaluate**
> ExpressionEvaluateResponse expressions_evaluate(data)

Evaluate expression

## Description
Evaluate a pipeline version operator expression.

### Required Parameters

- `expression`: The expression to evaluate.
- `input_fields`: A list of input fields with name, data_type.
- `request_data`: Data to test the expression with. All its keys must be defined in 'input_fields'.

## Request Examples

```
{
  "expression": "var1 + 10",
  "input_fields": [
    {
      "name": "var1",
      "data_type": "int"
    }
  ],
  "request_data": {
    "var1": 123
  }
}
```

### Response Structure

- `result`: The result of the expression

## Response Examples

```
{
  "result": 133
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

    data = ubiops.ExpressionEvaluate() # ExpressionEvaluate

    # Evaluate expression
    api_response = core_api.expressions_evaluate(data)
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

    data = ubiops.ExpressionEvaluate() # ExpressionEvaluate

    # Evaluate expression
    api_response = core_api.expressions_evaluate(data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **data** | [**ExpressionEvaluate**](./models/ExpressionEvaluate.md) | 

### Return type

[**ExpressionEvaluateResponse**](./models/ExpressionEvaluateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_audit_events_list**
> list[AuditList] pipeline_audit_events_list(project_name, pipeline_name, action=action, limit=limit, offset=offset)

List audit events for a pipeline

## Description
List all audit events for a pipeline including objects and attachments

### Optional Parameters
The following parameters should be given as query parameters:

- `action`: Type of action. It can be one of: create, update, delete, info.
- `limit`: The maximum number of audit events given back, default is 50
- `offset`: The number which forms the starting point of the audit events given back. If offset equals 2, then the first 2 events will be omitted from the list.

### Response Structure
A list of details of the audit events for a pipeline

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
    "id": "44f326de-0ee3-4741-b72e-69e31b3ec55f",
    "date": "2020-10-23T12:21:12.460+00:00",
    "action": "create",
    "user": "user@example.com",
    "event": "Created pipeline object deployment-1 in version v1 of pipeline pipeline-1",
    "object_type": "pipeline",
    "object_name": "pipeline-1"
  },
  {
    "id": "905cdc19-a02c-4f09-b2fb-42d92da21bda",
    "date": "2020-10-23T12:21:37.247+00:00",
    "action": "update",
    "user": "user@example.com",
    "event": "Updated pipeline object deployment-object in version v1 of pipeline pipeline-1: name changed from deployment-1 to deployment-object",
    "object_type": "pipeline",
    "object_name": "pipeline-1"
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
    pipeline_name = 'pipeline_name_example' # str
    action = 'action_example' # str (optional)
    limit = 56 # int (optional)
    offset = 56 # int (optional)

    # List audit events for a pipeline
    api_response = core_api.pipeline_audit_events_list(project_name, pipeline_name, action=action, limit=limit, offset=offset)
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
    pipeline_name = 'pipeline_name_example' # str
    action = 'action_example' # str (optional)
    limit = 56 # int (optional)
    offset = 56 # int (optional)

    # List audit events for a pipeline
    api_response = core_api.pipeline_audit_events_list(project_name, pipeline_name, action=action, limit=limit, offset=offset)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **action** | **str** | [optional] 
 **limit** | **int** | [optional] 
 **offset** | **int** | [optional] 

### Return type

[**list[AuditList]**](./models/AuditList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_object_environment_variables_list**
> list[InheritedEnvironmentVariableList] pipeline_version_object_environment_variables_list(project_name, name, pipeline_name, version)

List pipeline object environment variables

## Description
List environment variables accessible to objects in the pipeline version

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from - can be `project`, `deployment`, or `version`
- `inheritance_name`: Name of the parent object that this variable is inherited from

## Response Examples

```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": "deployment",
    "inheritance_name": "deployment_name"
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": "project",
    "inheritance_name": "project_name"
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
    name = 'name_example' # str
    pipeline_name = 'pipeline_name_example' # str
    version = 'version_example' # str

    # List pipeline object environment variables
    api_response = core_api.pipeline_version_object_environment_variables_list(project_name, name, pipeline_name, version)
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
    name = 'name_example' # str
    pipeline_name = 'pipeline_name_example' # str
    version = 'version_example' # str

    # List pipeline object environment variables
    api_response = core_api.pipeline_version_object_environment_variables_list(project_name, name, pipeline_name, version)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 

### Return type

[**list[InheritedEnvironmentVariableList]**](./models/InheritedEnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_versions_create**
> PipelineVersionDetail pipeline_versions_create(project_name, pipeline_name, data)

Create pipeline versions

## Description
Create a version for a pipeline. The first version of a pipeline is set as default.
Provide the parameter 'monitoring' as the name of a notification group to send monitoring notifications to. A notification will be sent in the case of a failed/recovered request. Pass `null` to switch off monitoring notifications for this version.
Provide the parameter 'default_notification_group' as the name of a notification group to send notifications when requests for the version are completed. Pass `null` to switch off request notifications for this version.

### Required Parameters

- `version`: Name of the version of the pipeline

### Optional Parameters

- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `monitoring`: Name of a notification group which contains contacts to send notifications when requests for the version fail and recover
- `default_notification_group`: Name of a notification group which contains contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version. It defaults to 604800 seconds (1 week).
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored
- `objects`: List of pipeline version objects
- `attachments`: List of pipeline version object attachments

## Request Examples

```
{
  "version": "v1"
}
```


```
{
  "version": "v1",
  "description": "my description",
  "labels": {
    "type": "production"
  },
  "monitoring": "notification-group-1",
  "request_retention_time": 604800,
  "request_retention_mode": "full"
}
```

A pipeline version with objects and attachments

```
{
  "version": "v1",
  "description": "my description",
  "labels": {
    "type": "production"
  },
  "monitoring": ["test@example.com"],
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [
    {
      "name": "object-1",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1"
    }
  ],
  "attachments": [
    {
      "destination_name": "object-1",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    }
  ]
}
```

### Response Structure
Details of the created pipeline version

- `id`: Unique identifier for the pipeline version (UUID)
- `pipeline`: Name of the pipeline to which the version is associated
- `version`: Name of the version of the pipeline
- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline version was created
- `last_updated`: The date when the pipeline version was last updated
- `monitoring`: Name of a notification group which contains contacts to send notifications when requests for the version fail and recover
- `default_notification_group`: Name of a notification group which contains contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following: *none*, *metadata* or *full*.
- `objects`: List of pipeline version objects
- `attachments`: List of pipeline version object attachments

## Response Examples

```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": "notification-group-1",
  "default_notification_group": null,
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [],
  "attachments": []
}
```


```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": ["test@example.com"],
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [
    {
      "id": "38549ff5-5bf0-4803-8571-236077c77e62",
      "name": "object-1",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1",
      "input_type": "structured",
      "output_type": "structured",
      "configuration": {},
      "input_fields": [
        {
          "name": "input",
          "data_type": "int"
        }
      ],
      "output_fields": [
        {
          "name": "output",
          "data_type": "int"
        }
      ]
    }
  ],
  "attachments": [
    {
      "destination_name": "object-1",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
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
    pipeline_name = 'pipeline_name_example' # str
    data = ubiops.PipelineVersionCreate() # PipelineVersionCreate

    # Create pipeline versions
    api_response = core_api.pipeline_versions_create(project_name, pipeline_name, data)
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
    pipeline_name = 'pipeline_name_example' # str
    data = ubiops.PipelineVersionCreate() # PipelineVersionCreate

    # Create pipeline versions
    api_response = core_api.pipeline_versions_create(project_name, pipeline_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **data** | [**PipelineVersionCreate**](./models/PipelineVersionCreate.md) | 

### Return type

[**PipelineVersionDetail**](./models/PipelineVersionDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_versions_delete**
> pipeline_versions_delete(project_name, pipeline_name, version)

Delete pipeline version

## Description
Delete a pipeline version. This will also delete all objects and attachments in the pipeline version.

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    pipeline_name = 'pipeline_name_example' # str
    version = 'version_example' # str

    # Delete pipeline version
    core_api.pipeline_versions_delete(project_name, pipeline_name, version)

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
    pipeline_name = 'pipeline_name_example' # str
    version = 'version_example' # str

    # Delete pipeline version
    core_api.pipeline_versions_delete(project_name, pipeline_name, version)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_versions_get**
> PipelineVersionDetail pipeline_versions_get(project_name, pipeline_name, version)

Get pipeline version

## Description
Get the details of a single pipeline version

### Response Structure
Details of the pipeline version

- `id`: Unique identifier for the pipeline version (UUID)
- `pipeline`: Name of the pipeline to which the version is associated
- `version`: Name of the version of the pipeline
- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline version was created
- `last_updated`: The date when the pipeline version was last updated
- `monitoring`: Name of a notification group which contains contacts to send notifications when requests for the version fail and recover
- `default_notification_group`: Name of a notification group which contains contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored
- `objects`: List of pipeline version objects
- `attachments`: List of pipeline version object attachments

## Response Examples

```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": "notification-group-1",
  "default_notification_group": null,
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [],
  "attachments": []
}
```


```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": ["test@example.com"],
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [
    {
      "id": "38549ff5-5bf0-4803-8571-236077c77e62",
      "name": "object-1",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1",
      "input_type": "structured",
      "output_type": "structured",
      "configuration": {},
      "input_fields": [
        {
          "name": "input",
          "data_type": "int"
        }
      ],
      "output_fields": [
        {
          "name": "output",
          "data_type": "int"
        }
      ]
    }
  ],
  "attachments": [
    {
      "destination_name": "object-1",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
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
    pipeline_name = 'pipeline_name_example' # str
    version = 'version_example' # str

    # Get pipeline version
    api_response = core_api.pipeline_versions_get(project_name, pipeline_name, version)
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
    pipeline_name = 'pipeline_name_example' # str
    version = 'version_example' # str

    # Get pipeline version
    api_response = core_api.pipeline_versions_get(project_name, pipeline_name, version)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 

### Return type

[**PipelineVersionDetail**](./models/PipelineVersionDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_versions_list**
> list[PipelineVersionList] pipeline_versions_list(project_name, pipeline_name, labels=labels)

List pipeline versions

## Description
Pipeline versions can be filtered according to the labels they have by giving labels as a query parameter. Pipeline versions that have at least one of the labels on which is filtered, are returned.

### Optional Parameters

- `labels`: Filter on labels of the pipeline version. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.

### Response Structure
A list of details of the versions of the pipeline

- `id`: Unique identifier for the pipeline version (UUID)
- `pipeline`: Name of the pipeline to which the version is associated
- `version`: Name of the version of the pipeline
- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline version was created
- `last_updated`: The date when the pipeline version was last updated
- `monitoring`: Name of a notification group which contains contacts to send notifications when requests for the version fail and recover
- `default_notification_group`: Name of a notification group which contains contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored

## Response Examples

```
[
  {
    "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
    "pipeline": "pipeline-1",
    "version": "v1",
    "description": "my description",
    "labels": {
      "tag": "production"
    },
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z",
    "monitoring": "notification-group-1",
    "default_notification_group": null,
    "request_retention_time": 604800,
    "request_retention_mode": "full"
  },
  {
    "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
    "pipeline": "pipeline-1",
    "version": "v1",
    "description": "my description",
    "labels": {
      "tag": "production"
    },
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z",
    "monitoring": "notification-group-2",
    "default_notification_group": "notification-group-2",
    "request_retention_time": 86400,
    "request_retention_mode": "metadata"
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
    pipeline_name = 'pipeline_name_example' # str
    labels = 'labels_example' # str (optional)

    # List pipeline versions
    api_response = core_api.pipeline_versions_list(project_name, pipeline_name, labels=labels)
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
    pipeline_name = 'pipeline_name_example' # str
    labels = 'labels_example' # str (optional)

    # List pipeline versions
    api_response = core_api.pipeline_versions_list(project_name, pipeline_name, labels=labels)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **labels** | **str** | [optional] 

### Return type

[**list[PipelineVersionList]**](./models/PipelineVersionList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_versions_update**
> PipelineVersionDetail pipeline_versions_update(project_name, pipeline_name, version, data)

Update pipeline version

## Description
Update a pipeline version. When updating labels, the labels will replace the existing value for labels.
Provide the parameter 'monitoring' as the name of a notification group to send monitoring notifications to. A notification will be sent in the case of a failed/recovered request. Pass `null` to switch off monitoring notifications for this version.
Provide the parameter 'default_notification_group' as the name of a notification group to send notifications when requests for the version are completed. Pass `null` to switch off request notifications for this version.

**Attention:** *In case either the `objects` or `attachments` parameter is null or an empty list, all of the objects or attachments of the pipeline will be removed.*

### Optional Parameters

- `version`: Name of the version of the pipeline
- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `monitoring`: Name of a notification group which contains contacts to send notifications when requests for the version fail and recover
- `default_notification_group`: Name of a notification group which contains contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored
- `objects`: List of pipeline version objects
- `attachments`: List of pipeline version object attachments

## Request Examples

```
{
  "version": "v1",
  "description": "my description",
  "labels": {
    "type": "production"
  },
  "monitoring": "notification-group-1"
}
```

Updating a pipeline version with new objects and attachments

```
{
  "version": "v1",
  "description": "my description",
  "labels": {
    "type": "production"
  },
  "monitoring": ["test@example.com"],
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [
    {
      "name": "object-1",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1"
    }
  ],
  "attachments": [
    {
      "destination_name": "object-1",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    }
  ]
}
```

Updating a pipeline version by removing objects and attachments

```
{
  "version": "v1",
  "description": "my description",
  "labels": {
    "type": "production"
  },
  "monitoring": ["test@example.com"],
  "objects": null,
  "attachments": null
}
```

### Response Structure
Details of the created pipeline

- `id`: Unique identifier for the pipeline version (UUID)
- `pipeline`: Name of the pipeline to which the version is associated
- `version`: Name of the version of the pipeline
- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline version was created
- `last_updated`: The date when the pipeline version was last updated
- `monitoring`: Name of a notification group which contains contacts to send notifications when requests for the version fail and recover
- `default_notification_group`: Name of a notification group which contains contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following: *none*, *metadata* or *full*.
- `objects`: List of pipeline version objects
- `attachments`: List of pipeline version object attachments

## Response Examples

```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": "notification-group-1",
  "default_notification_group": null,
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [],
  "attachments": []
}
```


```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": ["test@example.com"],
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [
    {
      "id": "38549ff5-5bf0-4803-8571-236077c77e62",
      "name": "object-1",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1",
      "input_type": "structured",
      "output_type": "structured",
      "configuration": {},
      "input_fields": [
        {
          "name": "input",
          "data_type": "int"
        }
      ],
      "output_fields": [
        {
          "name": "output",
          "data_type": "int"
        }
      ]
    }
  ],
  "attachments": [
    {
      "destination_name": "object-1",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
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
    pipeline_name = 'pipeline_name_example' # str
    version = 'version_example' # str
    data = ubiops.PipelineVersionUpdate() # PipelineVersionUpdate

    # Update pipeline version
    api_response = core_api.pipeline_versions_update(project_name, pipeline_name, version, data)
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
    pipeline_name = 'pipeline_name_example' # str
    version = 'version_example' # str
    data = ubiops.PipelineVersionUpdate() # PipelineVersionUpdate

    # Update pipeline version
    api_response = core_api.pipeline_versions_update(project_name, pipeline_name, version, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 
 **data** | [**PipelineVersionUpdate**](./models/PipelineVersionUpdate.md) | 

### Return type

[**PipelineVersionDetail**](./models/PipelineVersionDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipelines_create**
> PipelineCreateResponse pipelines_create(project_name, data)

Create pipelines

## Description
Create a pipeline in a project.

The input_fields represent the fields that the input data for pipeline requests should contain. When an object is attached to the pipeline, it means that the input data will be forwarded to these objects.

### Required Parameters

- `name`: Name of the pipeline. It is unique within a project.
- `input_type`: Type of the pipeline input. It can be either structured or plain.
- `input_fields`: A list of input fields with name, data_type and (optional) widget. In case of plain pipelines, the input_fields should be omitted or given as an empty list. For structured pipelines, it is possible to leave this field empty.
- `output_type`: Type of the pipeline output. It can be either structured or plain.
- `output_fields`: A list of output fields with name, data_type and (optional) widget. In case of plain pipelines, the output_fields should be omitted or given as an empty list. For structured pipelines, it is possible to leave this field empty.

### Optional Parameters

- `description`: Description of the pipeline
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Request Examples
A structured pipeline

```
{
  "name": "pipeline-1",
  "input_type": "structured",
  "input_fields": [
    {
      "name": "field-1",
      "data_type": "int"
    },
    {
      "name": "field-2",
      "data_type": "double"
    }
  ],
  "output_type": "structured",
  "output_fields": [
    {
      "name": "field-1",
      "data_type": "int"
    },
    {
      "name": "field-2",
      "data_type": "double"
    }
  ]
}
```

A plain pipeline

```
{
  "name": "pipeline-2",
  "input_type": "plain",
  "output_type": "plain",
  "description": "my description"
}
```

A structured pipeline with input/output field widgets

```
{
  "name": "pipeline-1",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "field-1",
      "data_type": "int",
      "widget": {
        "type": "slider",
        "configuration": {"min": 0, "max": 10, "default": 4, "step": 2}
      }
    },
    {
      "name": "field-2",
      "data_type": "double",
      "widget": {
        "type": "numberbox",
        "configuration": {"min": 0, "max": 1, "default": 0.5, "step": 0.1}
      }
    }
  ],
  "output_fields": [
    {
      "name": "field-1",
      "data_type": "double",
      "widget": {
        "type": "textbox",
        "configuration": {}
      }
    },
    {
      "name": "field-2",
      "data_type": "double",
      "widget": {
        "type": "textbox",
        "configuration": {}
      }
    }
  ]
}
```

### Response Structure
Details of the created pipeline

- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `description`: Description of the pipeline
- `project`: Project name in which the pipeline is created
- `input_type`: Type of the pipeline input
- `input_fields`: A list of pipeline input fields with name, data_type and widget
- `output_type`: Type of the pipeline output
- `output_fields`: A list of pipeline output fields with name, data_type and widget
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated

## Response Examples

```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "name": "pipeline-1",
  "project": "project-1",
  "description": "my description",
  "input_type": "structured",
  "input_fields": [
    {
      "name": "field-1",
      "data_type": "int",
      "widget": {}
    },
    {
      "name": "field-2",
      "data_type": "double",
      "widget": {}
    }
  ],
  "output_type": "structured",
  "output_fields": [
    {
      "name": "field-1",
      "data_type": "int",
      "widget": {}
    },
    {
      "name": "field-2",
      "data_type": "double",
      "widget": {}
    }
  ],
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-03-24T09:43:51.791253Z",
  "last_updated": "2020-03-24T09:43:51.791253Z"
}
```


```
{
  "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
  "name": "pipeline-2",
  "project": "project-1",
  "description": "my description",
  "input_type": "plain",
  "input_fields": [],
  "output_type": "plain",
  "output_fields": [],
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-05-12T16:23:15.456812Z"
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
    data = ubiops.PipelineCreate() # PipelineCreate

    # Create pipelines
    api_response = core_api.pipelines_create(project_name, data)
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
    data = ubiops.PipelineCreate() # PipelineCreate

    # Create pipelines
    api_response = core_api.pipelines_create(project_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**PipelineCreate**](./models/PipelineCreate.md) | 

### Return type

[**PipelineCreateResponse**](./models/PipelineCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipelines_delete**
> pipelines_delete(project_name, pipeline_name)

Delete a pipeline

## Description
Delete a pipeline. This will also delete all versions of the pipeline.

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    pipeline_name = 'pipeline_name_example' # str

    # Delete a pipeline
    core_api.pipelines_delete(project_name, pipeline_name)

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
    pipeline_name = 'pipeline_name_example' # str

    # Delete a pipeline
    core_api.pipelines_delete(project_name, pipeline_name)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipelines_get**
> PipelineDetail pipelines_get(project_name, pipeline_name)

Get details of a pipeline

## Description
Get the details of a single pipeline

### Response Structure
Details of the pipeline

- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `description` Description of the pipeline
- `project`: Project name in which the pipeline is defined
- `input_type`: Type of the pipeline input
- `input_fields`: A list of pipeline input fields with name, data_type and widget
- `output_type`: Type of the pipeline output
- `output_fields`: A list of pipeline output fields with name, data_type and widget
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated
- `default_version`: Default version of the pipeline.  If it does not have a default version, it is not set.

## Response Examples

```
{
  "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
  "name": "pipeline-2",
  "project": "project-1",
  "description": "my description",
  "input_type": "plain",
  "input_fields": [],
  "output_type": "plain",
  "output_fields": [],
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-03-24T09:43:51.791253Z",
  "last_updated": "2020-05-19T11:52:21.163270Z",
  "default_version": "v1"
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
    pipeline_name = 'pipeline_name_example' # str

    # Get details of a pipeline
    api_response = core_api.pipelines_get(project_name, pipeline_name)
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
    pipeline_name = 'pipeline_name_example' # str

    # Get details of a pipeline
    api_response = core_api.pipelines_get(project_name, pipeline_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 

### Return type

[**PipelineDetail**](./models/PipelineDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipelines_list**
> list[PipelineList] pipelines_list(project_name, labels=labels)

List pipelines

## Description
Pipelines can be filtered according to the labels they have by giving labels as a query parameter. Pipelines that have at least one of the labels on which is filtered, are returned.

### Optional Parameters

- `labels`: Filter on labels of the pipeline. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.

### Response Structure
A list of details of the pipelines in the project

- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `project`: Project name in which the pipeline is defined
- `description`: Description of the pipeline
- `input_type`: Type of the pipeline input
- `input_fields`: A list of pipeline input fields with name and data_type
- `output_type`: Type of the pipeline output
- `output_fields`: A list of pipeline output fields with name and data_type
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated

## Response Examples

```
[
  {
    "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
    "name": "pipeline-1",
    "project": "project-1",
    "description": "my description",
    "input_type": "structured",
    "input_fields": [
      {
        "name": "field-1",
        "data_type": "int"
      },
      {
        "name": "field-2",
        "data_type": "double"
      }
    ],
    "output_type": "structured",
    "output_fields": [
      {
        "name": "field-1",
        "data_type": "int"
      },
      {
        "name": "field-2",
        "data_type": "double"
      }
    ],
    "labels": {
      "tag": "production"
    },
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z"
  },
  {
    "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
    "name": "pipeline-2",
    "project": "project-1",
    "description": "my description",
    "input_type": "plain",
    "input_fields": [],
    "output_type": "plain",
    "output_fields": [],
    "labels": {
      "tag": "production"
    },
    "creation_date": "2020-03-24T09:43:51.791253Z",
    "last_updated": "2020-05-19T11:52:21.163270Z"
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

    # List pipelines
    api_response = core_api.pipelines_list(project_name, labels=labels)
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

    # List pipelines
    api_response = core_api.pipelines_list(project_name, labels=labels)
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

[**list[PipelineList]**](./models/PipelineList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipelines_update**
> PipelineDetail pipelines_update(project_name, pipeline_name, data)

Update a pipeline

## Description
Update a pipeline. All necessary fields are validated again. When updating labels, the labels will replace the existing value for labels.

### Optional Parameters

- `name`: New name for the pipeline
- `description`: New description for the pipeline
- `labels`: New dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label. The new labels will replace the existing value for labels.
- `input_type`: New type for the pipeline input. It is possible to change the type from plain to structured and vice versa.
- `input_fields`: New input fields for the pipeline
- `output_type`: New type for the pipeline output. It is possible to change the type from plain to structured and vice versa.
- `output_fields`: New output fields for the pipeline
- `default_version`: Name of a version of this pipeline which will be assigned as default

If the input type of pipeline is updated to plain, the input fields are deleted. In this case, input_fields should either be omitted or provided as en empty list.
If the input type of pipeline is updated to structured, the old input fields are deleted, if there existed any. The new fields are created, if any is provided. If one or more old fields need to be kept, they must be provided again.
The same goes for updating the pipeline output.

**To delete the input/output fields of a pipeline**, provide an empty list for input_fields/output_fields field.

## Request Examples

```
{
  "name": "new-pipeline-name"
}
```


```
{
  "description": "New pipeline description",
  "labels": {
    "tag": "production"
  }
}
```


```
{
  "input_type": "plain"
}
```

```
{
  "input_type": "structured",
  "input_fields": [
    {
      "name": "new-field-1",
      "data_type": "array_double",
      "widget": {}
    },
    {
      "name": "new-field-2",
      "data_type": "array_string",
      "widget": {}
    }
  ]
}
```

```
{
  "input_type": "structured",
  "input_fields": []
}
```

```
{
  "output_type": "structured",
  "output_fields": [
    {
      "name": "new-field-1",
      "data_type": "array_double",
      "widget": {}
    },
    {
      "name": "new-field-2",
      "data_type": "array_string",
      "widget": {}
    }
  ]
}
```

### Response Structure
Details of the updated pipeline

- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `project`: Project name in which the pipeline is defined
- `description`: Description for the pipeline
- `input_type`: Type of the pipeline input
- `input_fields`: A list of pipeline input fields with name, data_type and widget
- `output_type`: Type of the pipeline output
- `output_fields`: A list of pipeline output fields with name, data_type and widget
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated
- `default_version`: Default version of the pipeline.  If it does not have a default version, it is not set.

## Response Examples

```
{
  "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
  "name": "new-pipeline-name",
  "project": "project-1",
  "description": "my description",
  "input_type": "structured",
  "input_fields": [
    {
      "name": "new-field-1",
      "data_type": "array_double",
      "widget": {}
    },
    {
      "name": "new-field-2",
      "data_type": "array_string",
      "widget": {}
    }
  ],
  "output_type": "structured",
  "output_fields": [
    {
      "name": "new-field-1",
      "data_type": "array_double",
      "widget": {}
    },
    {
      "name": "new-field-2",
      "data_type": "array_string",
      "widget": {}
    }
  ],
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-03-24T09:43:51.791253Z",
  "last_updated": "2020-05-19T11:52:21.163270Z",
  "default_version": "v1"
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
    pipeline_name = 'pipeline_name_example' # str
    data = ubiops.PipelineUpdate() # PipelineUpdate

    # Update a pipeline
    api_response = core_api.pipelines_update(project_name, pipeline_name, data)
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
    pipeline_name = 'pipeline_name_example' # str
    data = ubiops.PipelineUpdate() # PipelineUpdate

    # Update a pipeline
    api_response = core_api.pipelines_update(project_name, pipeline_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **data** | [**PipelineUpdate**](./models/PipelineUpdate.md) | 

### Return type

[**PipelineDetail**](./models/PipelineDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


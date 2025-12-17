# Imports_and_Exports

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exports_create**](./ImportsAndExports.md#exports_create) | **POST** /projects/{project_name}/exports | Create an export
[**exports_delete**](./ImportsAndExports.md#exports_delete) | **DELETE** /projects/{project_name}/exports/{export_id} | Delete an export
[**exports_download**](./ImportsAndExports.md#exports_download) | **GET** /projects/{project_name}/exports/{export_id}/download | Download an export
[**exports_get**](./ImportsAndExports.md#exports_get) | **GET** /projects/{project_name}/exports/{export_id} | Get an export
[**exports_list**](./ImportsAndExports.md#exports_list) | **GET** /projects/{project_name}/exports | List exports
[**imports_create**](./ImportsAndExports.md#imports_create) | **POST** /projects/{project_name}/imports | Create an import
[**imports_delete**](./ImportsAndExports.md#imports_delete) | **DELETE** /projects/{project_name}/imports/{import_id} | Delete an import
[**imports_download**](./ImportsAndExports.md#imports_download) | **GET** /projects/{project_name}/imports/{import_id}/download | Download an import
[**imports_get**](./ImportsAndExports.md#imports_get) | **GET** /projects/{project_name}/imports/{import_id} | Get an import
[**imports_list**](./ImportsAndExports.md#imports_list) | **GET** /projects/{project_name}/imports | List imports
[**imports_update**](./ImportsAndExports.md#imports_update) | **PATCH** /projects/{project_name}/imports/{import_id} | Confirm an import


# **exports_create**
> ExportList exports_create(project_name, data, all=all, packages=packages)

Create an export

## Description
Create an export by selecting the objects in the export

### Optional Parameters

- `deployments`: Dictionary containing the deployments to export
- `pipelines`: Dictionary containing the pipelines to export
- `environment_variables`: Dictionary containing the project-level environment variables to export
- `environments`: Dictionary containing the environments to export

The following parameters should be given as query parameter:
- `all`: If true, all objects will be exported. If false, only the objects specified in the request body will be exported.
- `packages`: If false, no packages (environment/deployment version revisions) will be exported. If true, all packages will be exported.

## Request Examples


```
{
  "deployments": {
    "deployment-1": {
      "versions": {
        "version-1": {
          "environment_variables": {
            "VERSION_ENV_VAR_NAME_1": {
              "include_value": true
            },
            "VERSION_ENV_VAR_NAME_2": {
              "include_value": false
            }
          }
        },
        "version-2": {}
      },
      "environment_variables": {
        "DEPLOYMENT_ENV_VAR_NAME_1": {
          "include_value": false
        }
      }
    },
    "deployment-2": {
      "versions": {}
    }
  },
  "pipelines": {
    "pipeline-1": {
      "versions": {
        "version-1": {},
        "version-2": {}
      }
    },
    "pipeline-2": {
      "versions": {}
    }
  },
  "environment_variables": {
    "PROJECT_ENV_VAR_NAME_1": {
      "include_value": false
    }
  },
  "environments": {
    "environment-1": {}
  }
}
```

### Response Structure
Details of the created export

- `id`: Unique identifier for the export (UUID)
- `status`: Status of the export
- `error_message`: The error message in case of a failure
- `creation_date`: The date when the export was created
- `size`: Size of the export in bytes

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "status": "pending",
  "error_message": "",
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "size": null
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
data = ubiops.ExportCreate() # ExportCreate
all = True # bool (optional)
packages = True # bool (optional)

# Create an export
api_response = core_api.exports_create(project_name, data, all=all, packages=packages)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**ExportCreate**](./models/ExportCreate.md) | 
 **all** | **bool** | [optional] 
 **packages** | **bool** | [optional] 

### Return type

[**ExportList**](./models/ExportList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **exports_delete**
> exports_delete(project_name, export_id)

Delete an export

## Description
Delete an export from a project

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
export_id = 'export_id_example' # str

# Delete an export
core_api.exports_delete(project_name, export_id)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **export_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **exports_download**
> file exports_download(project_name, export_id)

Download an export

## Description
Download an export in a project

### Response Structure

- `file`: Zip file

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
export_id = 'export_id_example' # str

# Download an export
with core_api.exports_download(project_name, export_id) as response:
    filename = response.getfilename()
    content = response.read()

# Or directly save the file in the current working directory using _preload_content=True
# output_path = core_api.exports_download(project_name, export_id, _preload_content=True)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **export_id** | **str** | 

### Return type

**file**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **exports_get**
> ExportDetail exports_get(project_name, export_id)

Get an export

## Description
Get the details of an export in a project

### Response Structure

- `id`: Unique identifier for the export (UUID)
- `status`: Status of the export
- `error_message`: The error message in case of a failure
- `creation_date`: The date when the export was created
- `size`: Size of the export in bytes
- `deployments`: Dictionary of the deployments in the export
- `pipelines`: Dictionary of the pipelines in the export
- `environment_variables`: Dictionary of the environment variables in the export
- `environments`: Dictionary of the environments in the export

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
export_id = 'export_id_example' # str

# Get an export
api_response = core_api.exports_get(project_name, export_id)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **export_id** | **str** | 

### Return type

[**ExportDetail**](./models/ExportDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **exports_list**
> list[ExportList] exports_list(project_name, status=status)

List exports

## Description
List all exports in a project

### Optional Parameters
The following parameter should be given as query parameter:

- `status`: Status of the export. Can be 'pending', 'processing', 'completed' and 'failed'.

### Response Structure
A list of details of the exports in the project

- `id`: Unique identifier for the export (UUID)
- `creation_date`: Time the export was created
- `status`: The status of the export
- `error_message`: The error message in case of a failure
- `size`: Size of the export in bytes

## Response Examples

```
[
  {
    "id": "ecb39626-2a14-4224-a57a-592a51567e17",
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "status": "pending",
    "error_message": "",
    "size": null
  },
  {
    "id": "f629a052-a827-44d9-97cf-3902504edc79",
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "status": "completed",
    "error_message": "",
    "size": 86400
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
status = 'status_example' # str (optional)

# List exports
api_response = core_api.exports_list(project_name, status=status)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **status** | **str** | [optional] 

### Return type

[**list[ExportList]**](./models/ExportList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **imports_create**
> ImportList imports_create(project_name, file=file, import_link=import_link, export_id=export_id, skip_confirmation=skip_confirmation)

Create an import

## Description
Create an import by uploading a zip file, providing a link to an import file or by giving an export id.
Only one of the fields `file`, `import_link` or `export_id` may be given at a time.
When providing a link to an import file, make sure it is publicly downloadable.

### Required Parameters
Only one of the following fields should be given:

- `file`: A zip file
- `import_link`: url to a publicly downloadable zip file
- `export_id`: UUID of a previously created export in the same project

### Optional Parameters

- `skip_confirmation`: Whether to skip the confirmation step, default to False

### Response Structure
Details of the created import

- `id`: Unique identifier for the import (UUID)
- `status`: Status of the import
- `error_message`: The error message in case of a failure
- `creation_date`: The date when the import was created
- `size`: Size of the import in bytes

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "status": "pending",
  "error_message": "",
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "size": 28391
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
file = '/path/to/file' # file (optional)
import_link = 'import_link_example' # str (optional)
export_id = 'export_id_example' # str (optional)
skip_confirmation = True # bool (optional)

# Create an import
api_response = core_api.imports_create(project_name, file=file, import_link=import_link, export_id=export_id, skip_confirmation=skip_confirmation)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **file** | **file** | [optional] 
 **import_link** | **str** | [optional] 
 **export_id** | **str** | [optional] 
 **skip_confirmation** | **bool** | [optional] 

### Return type

[**ImportList**](./models/ImportList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **imports_delete**
> imports_delete(project_name, import_id)

Delete an import

## Description
Delete an import from a project

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
import_id = 'import_id_example' # str

# Delete an import
core_api.imports_delete(project_name, import_id)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **import_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **imports_download**
> file imports_download(project_name, import_id)

Download an import

## Description
Download an import in a project

### Response Structure

- `file`: Zip file

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
import_id = 'import_id_example' # str

# Download an import
with core_api.imports_download(project_name, import_id) as response:
    filename = response.getfilename()
    content = response.read()

# Or directly save the file in the current working directory using _preload_content=True
# output_path = core_api.imports_download(project_name, import_id, _preload_content=True)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **import_id** | **str** | 

### Return type

**file**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **imports_get**
> ImportDetail imports_get(project_name, import_id)

Get an import

## Description
Get the details of an import in a project

### Response Structure

- `id`: Unique identifier for the import (UUID)
- `status`: Status of the import
- `error_message`: The error message in case of a failure
- `creation_date`: The date when the import was created
- `size`: Size of the import in bytes
- `deployments`: Dictionary of the deployments in the import
- `pipelines`: Dictionary of the pipelines in the import
- `environment_variables`: Dictionary of the environment variables in the import
- `environments`: Dictionary of the environments in the import

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
import_id = 'import_id_example' # str

# Get an import
api_response = core_api.imports_get(project_name, import_id)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **import_id** | **str** | 

### Return type

[**ImportDetail**](./models/ImportDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **imports_list**
> list[ImportList] imports_list(project_name, status=status)

List imports

## Description
List all imports in a project

### Optional Parameters
The following parameter should be given as query parameter:

- `status`: Status of the import. Can be 'pending', 'scanning', 'confirmation', 'confirmation_pending', 'processing', 'completed' and 'failed'.

### Response Structure
A list of details of the imports in the project

- `id`: Unique identifier for the import (UUID)
- `creation_date`: Time the import was created
- `status`: The status of the import
- `error_message`: The error message in case of a failure
- `size`: Size of the import in bytes

## Response Examples

```
[
  {
    "id": "ecb39626-2a14-4224-a57a-592a51567e17",
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "status": "pending",
    "error_message": "",
    "size": 126832
  },
  {
    "id": "f629a052-a827-44d9-97cf-3902504edc79",
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "status": "pending",
    "error_message": "",
    "size": 86400
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
status = 'status_example' # str (optional)

# List imports
api_response = core_api.imports_list(project_name, status=status)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **status** | **str** | [optional] 

### Return type

[**list[ImportList]**](./models/ImportList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **imports_update**
> ImportDetail imports_update(project_name, import_id, data)

Confirm an import

## Description
Confirm (and update) an import by selecting the objects in the import

### Optional Parameters

- `deployments`: Dictionary containing the deployments to create
- `pipelines`: Dictionary containing the pipelines to create
- `environment_variables`: Dictionary containing the project-level environment variables to create
- `environments`: Dictionary containing the environments to create

## Request Examples


```
{
    "deployments": {
    "deployment-1: {
      "description": "",
      "labels": {
        "my-label": "my-value"
      },
      "default_version": "v1",
      "versions": {
        "v1": {
          "zip": "deployments/deployment_deployment-1/versions/deployment_deployment-1_version_v1.zip",
          "description": "",
          "labels": {},
          "environment": "python3-12",
          "maximum_idle_time": 300,
          "maximum_instances": 5,
          "instance_type": "256mb",
          "minimum_instances": 0,
          "environment_variables": {
            "VERSION_ENV_VAR_1": {
              "value": "my-secret-value",
              "secret": true
            },
            "VERSION_ENV_VAR_2": {
              "value": "test2"
            }
          },
          "request_retention_mode": "full",
          "request_retention_time": 604800
        }
      },
      "input_type": "structured",
      "output_type": "structured",
      "input_fields": [
        {
          "name": "input",
          "data_type": "double"
        }
      ],
      "output_fields": [
        {
          "name": "output",
          "data_type": "double"
        }
      ],
      "environment_variables": {
        "DEPLOYMENT_ENV_VAR_1": {
          "value": "my-secret-value",
          "secret": true
        },
        "DEPLOYMENT_ENV_VAR_2": {
          "value": "test"
        }
      }
    }
  },
  "pipelines": {
    "pipeline-1: {
      "description": "",
      "labels": {
        "test": "label"
      },
      "default_version": "v1",
      "versions": {
        "v1": {
          "description": "",
          "labels": {},
          "objects": [
            {
              "name": "obj-1",
              "reference_name": "deployment-1",
              "reference_version": "v1"
            }
          ],
          "attachments": [
            {
              "sources": [
                {
                  "mapping": [
                    {
                      "source_field_name": "input",
                      "destination_field_name": "input"
                    }
                  ],
                  "source_name": "pipeline_start"
                }
              ],
              "destination_name": "obj-1"
            },
            {
              "sources": [
                {
                  "mapping": [
                    {
                      "source_field_name": "output",
                      "destination_field_name": "output"
                    }
                  ],
                  "source_name": "obj-1"
                }
              ],
              "destination_name": "pipeline_end"
            }
          ],
          "request_retention_mode": "full",
          "request_retention_time": 604800
        }
      },
      "input_type": "structured",
      "output_type": "structured",
      "input_fields": [
        {
          "name": "input",
          "data_type": "double"
        }
      ],
      "output_fields": [
        {
          "name": "output",
          "data_type": "double"
        }
      ]
    }
  },
  "environment_variables": {
    "PROJECT_ENV_VAR_1": {
      "value": "value1",
      "secret": true
    },
    "PROJECT_ENV_VAR_2": {
      "value": "value2"
    }
  },
  "environments": {
    "environment-1": {
        "display_name": "Environment 1",
        "description": "",
        "labels": {},
        "base_environment": "python3-12"
    }
  }
}
```

### Response Structure
Details of the updated import

- `id`: Unique identifier for the import (UUID)
- `status`: Status of the import
- `error_message`: The error message in case of a failure
- `creation_date`: The date when the import was created
- `size`: Size of the import in bytes

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "status": "pending",
  "error_message": "",
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "size": null
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
import_id = 'import_id_example' # str
data = ubiops.ImportUpdate() # ImportUpdate

# Confirm an import
api_response = core_api.imports_update(project_name, import_id, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **import_id** | **str** | 
 **data** | [**ImportUpdate**](./models/ImportUpdate.md) | 

### Return type

[**ImportDetail**](./models/ImportDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


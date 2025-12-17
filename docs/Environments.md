# Environments

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**environment_build_dependencies_list**](./Environments.md#environment_build_dependencies_list) | **GET** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id}/builds/{build_id}/dependency-files | List dependency files
[**environment_builds_get**](./Environments.md#environment_builds_get) | **GET** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id}/builds/{build_id} | Get build
[**environment_builds_list**](./Environments.md#environment_builds_list) | **GET** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id}/builds | List builds
[**environment_builds_update**](./Environments.md#environment_builds_update) | **PATCH** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id}/builds/{build_id} | Update build
[**environment_revisions_file_download**](./Environments.md#environment_revisions_file_download) | **GET** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id}/download | Download environment file
[**environment_revisions_file_upload**](./Environments.md#environment_revisions_file_upload) | **POST** /projects/{project_name}/environments/{environment_name}/revisions | Upload environment file
[**environment_revisions_get**](./Environments.md#environment_revisions_get) | **GET** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id} | Get revision
[**environment_revisions_list**](./Environments.md#environment_revisions_list) | **GET** /projects/{project_name}/environments/{environment_name}/revisions | List revisions
[**environment_revisions_rebuild**](./Environments.md#environment_revisions_rebuild) | **POST** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id}/rebuild | Rebuild revision
[**environments_create**](./Environments.md#environments_create) | **POST** /projects/{project_name}/environments | Create environments
[**environments_delete**](./Environments.md#environments_delete) | **DELETE** /projects/{project_name}/environments/{environment_name} | Delete environment
[**environments_get**](./Environments.md#environments_get) | **GET** /projects/{project_name}/environments/{environment_name} | Get environment
[**environments_list**](./Environments.md#environments_list) | **GET** /projects/{project_name}/environments | List environments
[**environments_update**](./Environments.md#environments_update) | **PATCH** /projects/{project_name}/environments/{environment_name} | Update environment
[**environments_usage**](./Environments.md#environments_usage) | **GET** /projects/{project_name}/environments/{environment_name}/usage | List usage of environment


# **environment_build_dependencies_list**
> list[EnvironmentBuildDependency] environment_build_dependencies_list(project_name, build_id, environment_name, revision_id)

List dependency files

## Description
List the dependency files and their contents in an environment build

### Response Structure
A list of details of the dependency files

- `name`: Name of the dependency file
- `content`: Content of the dependency file

## Response Examples

```
[
  {
    "name": "requirements.txt",
    "content": "ubiops==3.6.1\nrequests==2.30.0\n"
  },
  {
    "name": "ubiops.yaml",
    "content": "environment_variables:\n- ACCEPT_EULA=Y\napt:\n  packages:\n    - python3-dev\n"
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
build_id = 'build_id_example' # str
environment_name = 'environment_name_example' # str
revision_id = 'revision_id_example' # str

# List dependency files
api_response = core_api.environment_build_dependencies_list(project_name, build_id, environment_name, revision_id)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **build_id** | **str** | 
 **environment_name** | **str** | 
 **revision_id** | **str** | 

### Return type

[**list[EnvironmentBuildDependency]**](./models/EnvironmentBuildDependency.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_builds_get**
> EnvironmentBuildList environment_builds_get(project_name, build_id, environment_name, revision_id)

Get build

## Description
Retrieve details of a build of an environment

### Response Structure
Details of a build

- `id`: Unique identifier for the build
- `revision`: ID of the revision to which the build is linked
- `creation_date`: The date when the build was created
- `status`: Status of the build. It can be one of the following: 'queued', 'processing', 'success' or 'failed'.
- `error_message`: Error message which explains why the build has failed. It is empty if the build is successful.
- `trigger`: Action that triggered the build
- `size`: Size of docker image of the environment build in bytes

## Response Examples

```
{
  "id": "e2c5f430-265d-4f79-a828-259ada415ae4",
  "revision": "8760570f-6eda-470b-99af-bde810d418d8",
  "creation_date": "2023-01-30T12:27:12.108+00:00",
  "status": "success",
  "error_message": "",
  "trigger": "Rebuild triggered",
  "size": 257862432
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
build_id = 'build_id_example' # str
environment_name = 'environment_name_example' # str
revision_id = 'revision_id_example' # str

# Get build
api_response = core_api.environment_builds_get(project_name, build_id, environment_name, revision_id)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **build_id** | **str** | 
 **environment_name** | **str** | 
 **revision_id** | **str** | 

### Return type

[**EnvironmentBuildList**](./models/EnvironmentBuildList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_builds_list**
> list[EnvironmentBuildList] environment_builds_list(project_name, environment_name, revision_id)

List builds

## Description
List builds of an environment. A build is triggered when a new environment file is uploaded.

### Response Structure
A list of details of the builds

- `id`: Unique identifier for the build
- `revision`: ID of the revision to which the build is linked
- `creation_date`: The date when the build was created
- `status`: Status of the build. It can be one of the following: 'queued', 'processing', 'success' or 'failed'.
- `error_message`: Error message which explains why the build has failed. It is empty if the build is successful.
- `trigger`: Action that triggered the build
- `size`: Size of docker image of the environment build in bytes

## Response Examples

```
[
  {
    "id": "e3021050-b9ac-4b8e-89f4-adb9e7c9aba6",
    "revision": "593bac21-7cd2-476a-aee8-ec9fc7f56232",
    "creation_date": "2023-01-23T12:17:11.863+00:00",
    "status": "failed",
    "error_message": "Could not find the requirements file",
    "trigger": "Environment file upload",
    "size": 197280883
  },
  {
    "id": "038ae310-6629-4887-952d-868b6e533b90",
    "revision": "8760570f-6eda-470b-99af-bde810d418d8",
    "creation_date": "2023-01-29T17:12:43.108+00:00",
    "status": "queued",
    "error_message": "",
    "trigger": "Environment file upload",
    "size": 257862432
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
revision_id = 'revision_id_example' # str

# List builds
api_response = core_api.environment_builds_list(project_name, environment_name, revision_id)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **revision_id** | **str** | 

### Return type

[**list[EnvironmentBuildList]**](./models/EnvironmentBuildList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_builds_update**
> EnvironmentBuildList environment_builds_update(project_name, build_id, environment_name, revision_id, data)

Update build

## Description
Cancel a build of an environment

### Required Parameters

- `status`: Status that the build will be updated to. It can only be cancelled.

## Request Examples

```
{
    "status": "cancelled"
}
```

### Response Structure
Details of the cancelled build

- `id`: Unique identifier for the build
- `revision`: ID of the revision to which the build is linked
- `creation_date`: The date when the build was created
- `status`: Status of the build. It can be one of the following: 'queued', 'processing', 'success' or 'failed'.
- `error_message`: Error message which explains why the build has failed. It is empty if the build is successful.
- `trigger`: Action that triggered the build
- `size`: Size of docker image of the environment build in bytes

## Response Examples

```
{
  "id": "e2c5f430-265d-4f79-a828-259ada415ae4",
  "revision": "8760570f-6eda-470b-99af-bde810d418d8",
  "creation_date": "2023-01-30T12:27:12.108+00:00",
  "status": "cancelled",
  "error_message": "",
  "trigger": "Rebuild triggered"
  "size": 257862432
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
build_id = 'build_id_example' # str
environment_name = 'environment_name_example' # str
revision_id = 'revision_id_example' # str
data = ubiops.EnvironmentBuildUpdate() # EnvironmentBuildUpdate

# Update build
api_response = core_api.environment_builds_update(project_name, build_id, environment_name, revision_id, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **build_id** | **str** | 
 **environment_name** | **str** | 
 **revision_id** | **str** | 
 **data** | [**EnvironmentBuildUpdate**](./models/EnvironmentBuildUpdate.md) | 

### Return type

[**EnvironmentBuildList**](./models/EnvironmentBuildList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_revisions_file_download**
> file environment_revisions_file_download(project_name, environment_name, revision_id)

Download environment file

## Description
Download the file of a revision of an environment

### Response Structure

- `file`: Environment file

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
revision_id = 'revision_id_example' # str

# Download environment file
with core_api.environment_revisions_file_download(project_name, environment_name, revision_id) as response:
    filename = response.getfilename()
    content = response.read()

# Or directly save the file in the current working directory using _preload_content=True
# output_path = core_api.environment_revisions_file_download(project_name, environment_name, revision_id, _preload_content=True)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **revision_id** | **str** | 

### Return type

**file**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_revisions_file_upload**
> EnvironmentRevisionCreate environment_revisions_file_upload(project_name, environment_name, file=file, source_environment=source_environment)

Upload environment file

## Description
Upload a file for an environment. Uploading a file will create a new revision and trigger a build. This file should contain all the dependencies that the environment should have in the zip format.

It is **also possible** to provide a source environment from which the environment file will be copied. This will also create a new revision and trigger a build.

### Optional Parameters

- `file`: Environment file
- `source_environment`: Environment from which the environment file will be copied

Either **file** or **source_environment** must be provided.

### Response Structure

- `success`: Boolean indicating whether the environment file upload/copy succeeded
- `revision`: ID of the created revision for the file upload
- `build`: ID of the build created for the file upload

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
file = '/path/to/file' # file (optional)
source_environment = 'source_environment_example' # str (optional)

# Upload environment file
api_response = core_api.environment_revisions_file_upload(project_name, environment_name, file=file, source_environment=source_environment)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **file** | **file** | [optional] 
 **source_environment** | **str** | [optional] 

### Return type

[**EnvironmentRevisionCreate**](./models/EnvironmentRevisionCreate.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_revisions_get**
> EnvironmentRevisionDetail environment_revisions_get(project_name, environment_name, revision_id)

Get revision

## Description
Retrieve details of a revision of an environment

### Response Structure
Details of a revision

- `id`: Unique identifier for the revision
- `environment`: Environment to which the revision is linked
- `creation_date`: The date when the revision was created
- `created_by`: The email of the user that uploaded the environment file. In case the revision is created by a service, the field will have a "UbiOps" value.
- `expired`: A boolean indicating whether the environment file has been deleted for the revision

## Response Examples

```
{
  "id": "593bac21-7cd2-476a-aee8-ec9fc7f56232",
  "environment": "python3-12-custom",
  "creation_date": "2023-01-29T17:12:43.108+00:00",
  "created_by": "test@example.com",
  "expired": false
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
revision_id = 'revision_id_example' # str

# Get revision
api_response = core_api.environment_revisions_get(project_name, environment_name, revision_id)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **revision_id** | **str** | 

### Return type

[**EnvironmentRevisionDetail**](./models/EnvironmentRevisionDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_revisions_list**
> list[EnvironmentRevisionDetail] environment_revisions_list(project_name, environment_name)

List revisions

## Description
List revisions of an environment

### Response Structure
A list of details of the revisions

- `id`: Unique identifier for the revision
- `environment`: Environment to which the revision is linked
- `creation_date`: The date when the revision was created
- `created_by`: The email of the user that uploaded the environment file. In case the revision is created by a service, the field will have a "UbiOps" value.
- `expired`: A boolean indicating whether the environment file has been deleted for the revision

## Response Examples

```
[
  {
    "id": "8760570f-6eda-470b-99af-bde810d418d8",
    "environment": "python3-12-custom",
    "creation_date": "2023-01-23T12:17:11.863+00:00",
    "created_by": "UbiOps",
    "expired": false
  },
  {
    "id": "593bac21-7cd2-476a-aee8-ec9fc7f56232",
    "environment": "python3-12-custom",
    "creation_date": "2023-01-29T17:12:43.108+00:00",
    "created_by": "test@example.com",
    "expired": false
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str

# List revisions
api_response = core_api.environment_revisions_list(project_name, environment_name)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 

### Return type

[**list[EnvironmentRevisionDetail]**](./models/EnvironmentRevisionDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_revisions_rebuild**
> EnvironmentBuildList environment_revisions_rebuild(project_name, environment_name, revision_id, data=data)

Rebuild revision

## Description
Trigger a rebuild for a revision of an environment

### Response Structure
Details of the created build

- `id`: Unique identifier for the build
- `revision`: ID of the revision to which the build is linked
- `creation_date`: The date when the build was created
- `status`: Status of the build. It can be one of the following: 'queued', 'processing', 'success' or 'failed'.
- `error_message`: Error message which explains why the build has failed. It is empty if the build is successful.
- `trigger`: Action that triggered the build

## Response Examples

```
{
  "id": "e2c5f430-265d-4f79-a828-259ada415ae4",
  "revision": "8760570f-6eda-470b-99af-bde810d418d8",
  "creation_date": "2023-01-30T12:27:12.108+00:00",
  "status": "queued",
  "error_message": "",
  "trigger": "Rebuild triggered"
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
revision_id = 'revision_id_example' # str
data = None # empty dict or None (optional)

# Rebuild revision
api_response = core_api.environment_revisions_rebuild(project_name, environment_name, revision_id, data=data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **revision_id** | **str** | 
 **data** | **empty dict or None** | [optional] 

### Return type

[**EnvironmentBuildList**](./models/EnvironmentBuildList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environments_create**
> EnvironmentList environments_create(project_name, data)

Create environments

## Description
Create a custom environment. Two types of custom environments can be created:

- Custom environment based on a base environment: In this type you must specify a base environment. When creating a revision for this environment, any packages listed in the requirements.txt or ubiops.yaml file will be installed on top of the base environment.
- Custom environment based on your own Docker image: For this type do not specify a base environment. The custom environment will be the Docker image you upload when creating a revision.
  - In this case, if you want to use the requests functionality, your Docker image must be based on one of the base environments, and `supports_request_format` must be set to true. If the image only needs to run as-is, without the requests functionality, this field can be set to false.

### Required Parameters

- `name`: Name of the environment

### Optional Parameters

- `base_environment`: Base environment name on which this environment is based
- `display_name`: Display name of the environment. If not set, 'name' is used instead.
- `description`: Description for the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `supports_request_format`: A boolean indicating whether the environment supports the request format

## Request Examples

```
{
  "name": "python3-12-custom",
  "base_environment": "python3-12"
}
```


```
{
  "name": "python3-12-custom-1",
  "display_name": "Custom Python 3.12",
  "base_environment": "python3-12"
}
```

### Response Structure
Details of the created environment

- `id`: Unique identifier for the environment
- `name`: Name of the environment
- `display_name`: Display name of the environment
- `base_environment`: Base environment name on which this environment is based
- `project`: Project name in which the environment is defined
- `creation_date`: The date when the environment was created
- `last_updated`: The date when the environment was last updated
- `description`: Description of the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `gpu_required`: A boolean indicating whether the environment requires GPUs
- `status`: Status of the environment
- `implicit`: A boolean indicating whether the environment is implicitly created
- `hidden`: A boolean indicating whether the environment is hidden
- `deprecated`: A boolean indicating whether the environment is deprecated
- `system`: A boolean indicating whether the environment was created by the system
- `supports_request_format`: A boolean indicating whether the environment supports the request format

## Response Examples

```
{
  "id": "3a7d94ca-4df4-4be3-857c-d6b9995cd17a",
  "name": "python3-12-custom",
  "display_name": "Custom Python 3.12",
  "base_environment": "python3-12",
  "project": "project-1",
  "creation_date": "2023-03-01T08:32:14.876451Z",
  "last_updated": "2023-03-01T08:32:14.876451Z",
  "description": "Custom environment based on Python 3.12",
  "labels": {
    "type": "environment"
  },
  "gpu_required": false,
  "status": "active",
  "implicit": false,
  "deprecated": false,
  "hidden": false,
  "system": false,
  "supports_request_format": true
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
data = ubiops.EnvironmentCreate() # EnvironmentCreate

# Create environments
api_response = core_api.environments_create(project_name, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**EnvironmentCreate**](./models/EnvironmentCreate.md) | 

### Return type

[**EnvironmentList**](./models/EnvironmentList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environments_delete**
> environments_delete(project_name, environment_name)

Delete environment

## Description
Delete an environment. The environment cannot be deleted if it is referenced by a deployment version.

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str

# Delete environment
core_api.environments_delete(project_name, environment_name)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environments_get**
> EnvironmentDetail environments_get(project_name, environment_name)

Get environment

## Description
Retrieve details of an environment

### Response Structure
Details of an environment

- `id`: Unique identifier for the environment
- `name`: Name of the environment
- `display_name`: Display name of the environment
- `base_environment`: Base environment name on which this environment is based
- `project`: Project name in which the environment is defined
- `creation_date`: The date when the environment was created
- `last_updated`: The date when the environment was last updated
- `description`: Description of the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `gpu_required`: A boolean indicating whether the environment requires GPUs
- `status`: Status of the environment
- `active_revision`: UUID of the active revision of the environment
- `active_build`: UUID of the active build of the environment
- `latest_revision`: UUID of the latest revision of the environment
- `latest_build`: UUID of the latest build of the environment
- `implicit`: A boolean indicating whether the environment is implicitly created
- `hidden`: A boolean indicating whether the environment is hidden
- `deprecated`: A boolean indicating whether the environment is deprecated
- `system`: A boolean indicating whether the environment was created by the system
- `supports_request_format`: A boolean indicating whether the environment supports the request format

## Response Examples

```
{
  "id": "3a7d94ca-4df4-4be3-857c-d6b9995cd17a",
  "name": "python3-12-custom",
  "display_name": "Custom Python 3.12",
  "base_environment": "python3-12",
  "project": "project-1",
  "creation_date": "2023-03-01T08:32:14.876451Z",
  "last_updated": "2023-03-01T10:52:23.124784Z",
  "description": "Custom environment based on Python 3.12",
  "labels": {
    "type": "environment"
  },
  "gpu_required": false,
  "status": "active",
  "implicit": false,
  "deprecated": false,
  "hidden": false,
  "system": false,
  "supports_request_format": true,
  "active_revision": "8760570f-6eda-470b-99af-bde810d418d8",
  "active_build": "e3021050-b9ac-4b8e-89f4-adb9e7c9aba6",
  "latest_revision": "8760570f-6eda-470b-99af-bde810d418d8",
  "latest_build": "e3021050-b9ac-4b8e-89f4-adb9e7c9aba6"
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str

# Get environment
api_response = core_api.environments_get(project_name, environment_name)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 

### Return type

[**EnvironmentDetail**](./models/EnvironmentDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environments_list**
> list[EnvironmentList] environments_list(project_name, labels=labels, environment_type=environment_type, supports_request_format=supports_request_format)

List environments

## Description
Environments can be filtered according to the labels they have by giving labels as a query parameter. Environments that have at least one of the labels on which is filtered, are returned.

### Optional Parameters

- `labels`: Filter on labels of the environment. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.
- `environment_type`: Filter on the type of the environment. It can be one of the following: 'base', 'custom' or 'all'. The default value is 'all'.
- `supports_request_format`: Filter on whether the environment supports the request format

### Response Structure
A list of details of the environments

- `id`: Unique identifier for the environment
- `name`: Name of the environment
- `display_name`: Display name of the environment
- `base_environment`: Base environment name on which this environment is based
- `project`: Project name in which the environment is defined. It is null for base environments.
- `creation_date`: The date when the environment was created
- `last_updated`: The date when the environment was last updated
- `description`: Description of the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `gpu_required`: A boolean indicating whether the environment requires GPUs
- `status`: Status of the environment
- `implicit`: A boolean indicating whether the environment is implicitly created
- `hidden`: A boolean indicating whether the environment is hidden
- `deprecated`: A boolean indicating whether the environment is deprecated
- `supports_request_format`: A boolean indicating whether the environment supports the request format

## Response Examples

```
[
  {
    "id": "1319895f-467b-4732-9804-7de500099233",
    "name": "python3-12",
    "display_name": "Ubuntu 24.04 + Python 3.12",
    "base_environment": null,
    "project": null,
    "creation_date": "2023-03-01T08:32:14.876451Z",
    "last_updated": "2023-03-01T10:52:23.124784Z",
    "description": "Base environment containing Python 3.12",
    "labels": {},
    "gpu_required": false,
    "status": "active",
    "implicit": false,
    "deprecated": false,
    "hidden": false,
    "supports_request_format": true
  },
  {
    "id": "3a7d94ca-4df4-4be3-857c-d6b9995cd17a",
    "name": "python3-12-custom",
    "display_name": "Custom Python 3.12",
    "base_environment": "python3-12",
    "project": "project-1",
    "creation_date": "2023-03-02T12:15:43.124751Z",
    "last_updated": "2023-03-03T13:14:23.865421Z",
    "description": "Custom environment based on Python 3.12",
    "labels": {
      "type": "environment"
    },
    "gpu_required": false,
    "status": "active",
    "implicit": false,
    "deprecated": false,
    "hidden": false,
    "supports_request_format": true
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
labels = "label1:value1,label2:value2" # str (optional)
environment_type = 'environment_type_example' # str (optional)
supports_request_format = True # bool (optional)

# List environments
api_response = core_api.environments_list(project_name, labels=labels, environment_type=environment_type, supports_request_format=supports_request_format)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **labels** | **str** | [optional] 
 **environment_type** | **str** | [optional] 
 **supports_request_format** | **bool** | [optional] 

### Return type

[**list[EnvironmentList]**](./models/EnvironmentList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environments_update**
> EnvironmentDetail environments_update(project_name, environment_name, data)

Update environment

## Description
Update an environment. When updating labels, the labels will replace the existing value for labels.

### Optional Parameters

- `name`: Name of the environment
- `display_name`: Display name of the environment
- `description`: Description for the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Request Examples

```
{
  "name": "new-python3-12-custom"
}
```

### Response Structure
Details of the updated environment

- `id`: Unique identifier for the environment
- `name`: Name of the environment
- `display_name`: Display name of the environment
- `base_environment`: Base environment name on which this environment is based
- `project`: Project name in which the environment is defined
- `creation_date`: The date when the environment was created
- `last_updated`: The date when the environment was last updated
- `description`: Description of the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `gpu_required`: A boolean indicating whether the environment requires GPUs
- `status`: Status of the environment
- `active_revision`: UUID of the active revision of the environment
- `active_build`: UUID of the active build of the environment
- `latest_revision`: UUID of the latest revision of the environment
- `latest_build`: UUID of the latest build of the environment
- `implicit`: A boolean indicating whether the environment is implicitly created
- `hidden`: A boolean indicating whether the environment is hidden
- `deprecated`: A boolean indicating whether the environment is deprecated
- `system`: A boolean indicating whether the environment was created by the system
- `supports_request_format`: A boolean indicating whether the environment supports the request format

## Response Examples

```
{
  "id": "3a7d94ca-4df4-4be3-857c-d6b9995cd17a",
  "name": "new-python3-12-custom",
  "display_name": "Custom Python 3.12",
  "base_environment": "python3-12",
  "project": "project-1",
  "creation_date": "2023-03-01T08:32:14.876451Z",
  "last_updated": "2023-03-01T10:52:23.124784Z",
  "description": "Custom environment based on Python 3.12",
  "labels": {
    "type": "environment"
  },
  "gpu_required": false,
  "status": "active",
  "implicit": false,
  "deprecated": false,
  "hidden": false,
  "system": false,
  "supports_request_format": true,
  "active_revision": "8760570f-6eda-470b-99af-bde810d418d8",
  "active_build": "e3021050-b9ac-4b8e-89f4-adb9e7c9aba6",
  "latest_revision": "8760570f-6eda-470b-99af-bde810d418d8",
  "latest_build": "e3021050-b9ac-4b8e-89f4-adb9e7c9aba6"
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
data = ubiops.EnvironmentUpdate() # EnvironmentUpdate

# Update environment
api_response = core_api.environments_update(project_name, environment_name, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **data** | [**EnvironmentUpdate**](./models/EnvironmentUpdate.md) | 

### Return type

[**EnvironmentDetail**](./models/EnvironmentDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environments_usage**
> list[EnvironmentUsage] environments_usage(project_name, environment_name, environment_type=environment_type)

List usage of environment

## Description
List the deployment versions used by an environment

### Response Structure
A list of details of the deployment versions

- `id`: Unique identifier for the deployment version (UUID)
- `deployment`: Deployment name to which the version is associated
- `version`: Version name
- `environment`: Environment of the version
- `environment_display_name`: Human readable name of the environment
- `status`: The status of the version

## Response Examples

```
[
  {
    "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
    "deployment": "deployment-1",
    "version": "version-1",
    "environment": "python3-12",
    "environment_display_name": "Ubuntu 24.04 + Python 3.12",
    "status": "available"
  },
  {
    "id": "24f6b80a-08c3-4d52-ac1a-2ea7e70f16a6",
    "deployment": "deployment-1",
    "version": "version-2",
    "environment": "python3-12",
    "environment_display_name": "Ubuntu 24.04 + Python 3.12",
    "status": "unavailable"
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
environment_type = 'environment_type_example' # str (optional)

# List usage of environment
api_response = core_api.environments_usage(project_name, environment_name, environment_type=environment_type)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **environment_type** | **str** | [optional] 

### Return type

[**list[EnvironmentUsage]**](./models/EnvironmentUsage.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


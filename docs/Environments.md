# Environments

All URIs are relative to *https://api.ubiops.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**environment_tag_dependencies_list**](./Environments.md#environment_tag_dependencies_list) | **GET** /projects/{project_name}/environments/{environment_name}/tags/{tag_name}/dependency-files | List dependency files
[**environment_tag_secrets_copy**](./Environments.md#environment_tag_secrets_copy) | **POST** /projects/{project_name}/environments/{environment_name}/tags/{tag_name}/copy-secrets | Copy tag secret
[**environment_tag_secrets_create**](./Environments.md#environment_tag_secrets_create) | **POST** /projects/{project_name}/environments/{environment_name}/tags/{tag_name}/secrets | Create tag secret
[**environment_tag_secrets_delete**](./Environments.md#environment_tag_secrets_delete) | **DELETE** /projects/{project_name}/environments/{environment_name}/tags/{tag_name}/secrets/{id} | Delete tag secret
[**environment_tag_secrets_get**](./Environments.md#environment_tag_secrets_get) | **GET** /projects/{project_name}/environments/{environment_name}/tags/{tag_name}/secrets/{id} | Get tag secret
[**environment_tag_secrets_list**](./Environments.md#environment_tag_secrets_list) | **GET** /projects/{project_name}/environments/{environment_name}/tags/{tag_name}/secrets | List tag secrets
[**environment_tag_secrets_update**](./Environments.md#environment_tag_secrets_update) | **PATCH** /projects/{project_name}/environments/{environment_name}/tags/{tag_name}/secrets/{id} | Update tag secret
[**environment_tags_build**](./Environments.md#environment_tags_build) | **POST** /projects/{project_name}/environments/{environment_name}/tags/{tag_name}/build | Build tag
[**environment_tags_create**](./Environments.md#environment_tags_create) | **POST** /projects/{project_name}/environments/{environment_name}/tags | Create tag
[**environment_tags_delete**](./Environments.md#environment_tags_delete) | **DELETE** /projects/{project_name}/environments/{environment_name}/tags/{tag_name} | Delete tag
[**environment_tags_download**](./Environments.md#environment_tags_download) | **GET** /projects/{project_name}/environments/{environment_name}/tags/{tag_name}/download | Download tag file
[**environment_tags_get**](./Environments.md#environment_tags_get) | **GET** /projects/{project_name}/environments/{environment_name}/tags/{tag_name} | Get tag
[**environment_tags_list**](./Environments.md#environment_tags_list) | **GET** /projects/{project_name}/environments/{environment_name}/tags | List tags
[**environment_tags_rebuild**](./Environments.md#environment_tags_rebuild) | **POST** /projects/{project_name}/environments/{environment_name}/tags/{tag_name}/rebuild | Rebuild tag
[**environment_tags_update**](./Environments.md#environment_tags_update) | **PATCH** /projects/{project_name}/environments/{environment_name}/tags/{tag_name} | Update tag
[**environment_tags_usage**](./Environments.md#environment_tags_usage) | **GET** /projects/{project_name}/environments/{environment_name}/tags/{tag_name}/usage | List usage of tag
[**environments_create**](./Environments.md#environments_create) | **POST** /projects/{project_name}/environments | Create environments
[**environments_delete**](./Environments.md#environments_delete) | **DELETE** /projects/{project_name}/environments/{environment_name} | Delete environment
[**environments_get**](./Environments.md#environments_get) | **GET** /projects/{project_name}/environments/{environment_name} | Get environment
[**environments_list**](./Environments.md#environments_list) | **GET** /projects/{project_name}/environments | List environments
[**environments_update**](./Environments.md#environments_update) | **PATCH** /projects/{project_name}/environments/{environment_name} | Update environment


# **environment_tag_dependencies_list**
> list[EnvironmentTagDependency] environment_tag_dependencies_list(project_name, environment_name, tag_name)

List dependency files

## Description
List the dependency files and their contents for a tag

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
environment_name = 'environment_name_example' # str
tag_name = 'tag_name_example' # str

# List dependency files
api_response = core_api.environment_tag_dependencies_list(project_name, environment_name, tag_name)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **tag_name** | **str** | 

### Return type

[**list[EnvironmentTagDependency]**](./models/EnvironmentTagDependency.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_tag_secrets_copy**
> list[InheritedEnvironmentVariableList] environment_tag_secrets_copy(project_name, environment_name, tag_name, data)

Copy tag secret

## Description
Copy existing secrets from a source object to the tag. Secrets of the tag with the same name as ones from the source object will be overwritten with the new value. Only the copied secrets are returned.

### Required Parameters

- `source_environment_name`: The name of the environment from which the secrets will be copied
- `source_tag_name`: The name of the tag from which the secrets will be copied

## Request Examples


```
{
  "source_environment_name": "example-environment",
  "source_tag_name": "example-tag",
}
```

### Response Structure
A list of the copied secrets described by the following fields:

- `id`: Unique identifier for the secret
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information (always true)

## Response Examples

```
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "UV_DEFAULT_INDEX",
    "value": null,
    "secret": true,
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
tag_name = 'tag_name_example' # str
data = ubiops.EnvironmentSecretCopy() # EnvironmentSecretCopy

# Copy tag secret
api_response = core_api.environment_tag_secrets_copy(project_name, environment_name, tag_name, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **tag_name** | **str** | 
 **data** | [**EnvironmentSecretCopy**](./models/EnvironmentSecretCopy.md) | 

### Return type

[**list[InheritedEnvironmentVariableList]**](./models/InheritedEnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_tag_secrets_create**
> EnvironmentVariableList environment_tag_secrets_create(project_name, environment_name, tag_name, data)

Create tag secret

## Description
Create a secret for the tag

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed during tag building. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information. Must be true for tags.

## Request Examples

```
{
  "name": "UV_DEFAULT_INDEX",
  "value": "https://pypi.org/simple",
  "secret": true
}
```

### Response Structure

- `id`: Unique identifier for the secret
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information (always true)

## Response Examples

```
{
  "id": "7c28a2be-507e-4fae-981d-54e94f22dab0",
  "name": "UV_DEFAULT_INDEX",
  "value": null,
  "secret": true
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
tag_name = 'tag_name_example' # str
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate

# Create tag secret
api_response = core_api.environment_tag_secrets_create(project_name, environment_name, tag_name, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **tag_name** | **str** | 
 **data** | [**EnvironmentVariableCreate**](./models/EnvironmentVariableCreate.md) | 

### Return type

[**EnvironmentVariableList**](./models/EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_tag_secrets_delete**
> environment_tag_secrets_delete(project_name, environment_name, id, tag_name)

Delete tag secret

## Description
Delete a secret of the tag

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
id = 'id_example' # str
tag_name = 'tag_name_example' # str

# Delete tag secret
core_api.environment_tag_secrets_delete(project_name, environment_name, id, tag_name)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **id** | **str** | 
 **tag_name** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_tag_secrets_get**
> EnvironmentVariableList environment_tag_secrets_get(project_name, environment_name, id, tag_name)

Get tag secret

## Description
Retrieve details of a tag secret

### Response Structure

- `id`: Unique identifier for the secret
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information (always true)

## Response Examples

```
{
  "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
  "name": "UV_DEFAULT_INDEX",
  "value": null,
  "secret": true
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
id = 'id_example' # str
tag_name = 'tag_name_example' # str

# Get tag secret
api_response = core_api.environment_tag_secrets_get(project_name, environment_name, id, tag_name)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **id** | **str** | 
 **tag_name** | **str** | 

### Return type

[**EnvironmentVariableList**](./models/EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_tag_secrets_list**
> list[EnvironmentVariableList] environment_tag_secrets_list(project_name, environment_name, tag_name)

List tag secrets

## Description
List the secrets defined for the tag

### Response Structure
A list of secrets described by the following fields:

- `id`: Unique identifier for the secret
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information (always true)

## Response Examples

```
[
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "UV_DEFAULT_INDEX",
    "value": null,
    "secret": true
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
tag_name = 'tag_name_example' # str

# List tag secrets
api_response = core_api.environment_tag_secrets_list(project_name, environment_name, tag_name)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **tag_name** | **str** | 

### Return type

[**list[EnvironmentVariableList]**](./models/EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_tag_secrets_update**
> EnvironmentVariableList environment_tag_secrets_update(project_name, environment_name, id, tag_name, data)

Update tag secret

## Description
Update a secret for the tag

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed during tag building. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information (always true)

## Request Examples

```
{
  "name": "UV_DEFAULT_INDEX",
  "value": "https://pypi.org/simple",
  "secret": true
}
```

### Response Structure

- `id`: Unique identifier for the secret
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information (always true)

## Response Examples

```
{
  "id": "7c28a2be-507e-4fae-981d-54e94f22dab0",
  "name": "UV_DEFAULT_INDEX",
  "value": null,
  "secret": true
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
id = 'id_example' # str
tag_name = 'tag_name_example' # str
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate

# Update tag secret
api_response = core_api.environment_tag_secrets_update(project_name, environment_name, id, tag_name, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **id** | **str** | 
 **tag_name** | **str** | 
 **data** | [**EnvironmentVariableCreate**](./models/EnvironmentVariableCreate.md) | 

### Return type

[**EnvironmentVariableList**](./models/EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_tags_build**
> Success environment_tags_build(project_name, environment_name, tag_name, base_environment_name=base_environment_name, base_environment_tag=base_environment_tag, file=file, source_environment=source_environment, source_tag=source_tag)

Build tag

## Description
Build a tag by uploading a file or copying it from a source tag. The base environment should be given as query parameter.

- When uploading a file, any packages listed in the requirements.txt or ubiops.yaml file will be installed on top of the given base environment.
- When uploading a Docker image archive, you don't need to specify a base environment. The environment will be the Docker image you upload.

### Optional Parameters

- `base_environment_name`: Base environment name on which this tag is based
- `base_environment_tag`: Base environment tag on which this tag is based
- `file`: Environment file
- `source_environment`: Environment of the source tag from which the environment file will be copied
- `source_tag`: Tag from which the environment file will be copied

Either **file** or both **source_environment** and **source_tag** must be provided.

### Response Structure

- `success`: Boolean indicating whether the environment file upload/copy succeeded

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
tag_name = 'tag_name_example' # str
base_environment_name = 'base_environment_name_example' # str (optional)
base_environment_tag = 'base_environment_tag_example' # str (optional)
file = '/path/to/file' # file (optional)
source_environment = 'source_environment_example' # str (optional)
source_tag = 'source_tag_example' # str (optional)

# Build tag
api_response = core_api.environment_tags_build(project_name, environment_name, tag_name, base_environment_name=base_environment_name, base_environment_tag=base_environment_tag, file=file, source_environment=source_environment, source_tag=source_tag)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **tag_name** | **str** | 
 **base_environment_name** | **str** | [optional] 
 **base_environment_tag** | **str** | [optional] 
 **file** | **file** | [optional] 
 **source_environment** | **str** | [optional] 
 **source_tag** | **str** | [optional] 

### Return type

[**Success**](./models/Success.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_tags_create**
> EnvironmentTagList environment_tags_create(project_name, environment_name, data)

Create tag

## Description
Create a tag for an environment

### Required Parameters

- `name`: Name of the tag

### Optional Parameters

- `supports_request_format`: A boolean indicating whether the tag supports the UbiOps request format

## Request Examples

```
{
  "name": "v1"
}
```

### Response Structure
Details of the created tag

- `id`: Unique identifier for the tag
- `name`: Name of the tag
- `environment`: Environment to which the tag is linked
- `creation_date`: The date when the tag was created
- `status`: The status of the tag
- `supports_request_format`: A boolean indicating whether the tag supports the UbiOps request format
- `implicit`: A boolean indicating whether the tag is implicitly created
- `deprecated`: A boolean indicating whether the tag is deprecated
- `size`: Size of docker image of the tag
- `error_message`: Error message which explains why the build has failed if the tag has failed to build
- `base_environment_name`: Name of the base environment that the tag was built on top of, if applicable
- `base_environment_tag`: Name of the base environment tag that the tag was built on top of, if applicable
- `built`: A boolean indicating whether the tag is built by UbiOps

## Response Examples

```
{
  "id": "8760570f-6eda-470b-99af-bde810d418d8",
  "name": "v1",
  "environment": "python3-12-custom",
  "creation_date": "2023-01-23T12:17:11.863+00:00",
  "status": "pending",
  "supports_request_format": true,
  "implicit": false,
  "deprecated": false,
  "size": null,
  "error_message": null,
  "base_environment_name": null,
  "base_environment_tag": null,
  "built": true
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
data = ubiops.EnvironmentTagCreate() # EnvironmentTagCreate

# Create tag
api_response = core_api.environment_tags_create(project_name, environment_name, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **data** | [**EnvironmentTagCreate**](./models/EnvironmentTagCreate.md) | 

### Return type

[**EnvironmentTagList**](./models/EnvironmentTagList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_tags_delete**
> environment_tags_delete(project_name, environment_name, tag_name)

Delete tag

## Description
Delete a tag of an environment. The tag cannot be deleted while it is queued or building.

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
tag_name = 'tag_name_example' # str

# Delete tag
core_api.environment_tags_delete(project_name, environment_name, tag_name)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **tag_name** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_tags_download**
> file environment_tags_download(project_name, environment_name, tag_name)

Download tag file

## Description
Download the file of a tag of an environment

### Response Structure

- `file`: Environment file

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
tag_name = 'tag_name_example' # str

# Download tag file
with core_api.environment_tags_download(project_name, environment_name, tag_name) as response:
    filename = response.getfilename()
    content = response.read()

# Or directly save the file in the current working directory using _preload_content=True
# output_path = core_api.environment_tags_download(project_name, environment_name, tag_name, _preload_content=True)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **tag_name** | **str** | 

### Return type

**file**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_tags_get**
> EnvironmentTagList environment_tags_get(project_name, environment_name, tag_name)

Get tag

## Description
Retrieve the details of a tag of an environment

### Response Structure
Details of the tag

- `id`: Unique identifier for the tag
- `name`: Name of the tag
- `environment`: Environment to which the tag is linked
- `creation_date`: The date when the tag was created
- `status`: The status of the tag
- `supports_request_format`: A boolean indicating whether the tag supports the UbiOps request format
- `implicit`: A boolean indicating whether the tag is implicitly created
- `deprecated`: A boolean indicating whether the tag is deprecated
- `size`: Size of docker image of the tag
- `error_message`: Error message which explains why the build has failed if the tag has failed to build
- `base_environment_name`: Name of the base environment that the tag was built on top of, if applicable
- `base_environment_tag`: Name of the base environment tag that the tag was built on top of, if applicable
- `built`: A boolean indicating whether the tag is built by UbiOps

## Response Examples

```
{
  "id": "8760570f-6eda-470b-99af-bde810d418d8",
  "name": "v1",
  "environment": "python3-12-custom",
  "creation_date": "2023-01-23T12:17:11.863+00:00",
  "status": "available",
  "supports_request_format": true,
  "implicit": false,
  "deprecated": false,
  "size": 104857600,
  "error_message": null,
  "base_environment_name": "ubiops-ubuntu24-04-python3-12",
  "base_environment_tag": "v5.25.0",
  "built": true
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
tag_name = 'tag_name_example' # str

# Get tag
api_response = core_api.environment_tags_get(project_name, environment_name, tag_name)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **tag_name** | **str** | 

### Return type

[**EnvironmentTagList**](./models/EnvironmentTagList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_tags_list**
> list[EnvironmentTagList] environment_tags_list(project_name, environment_name, supports_request_format=supports_request_format)

List tags

## Description
List tags of an environment

### Optional Parameters

- `supports_request_format`: Filter on whether the tag supports the UbiOps request format

### Response Structure
A list of details of the tags

- `id`: Unique identifier for the tag
- `name`: Name of the tag
- `environment`: Environment to which the tag is linked
- `creation_date`: The date when the tag was created
- `status`: The status of the tag
- `supports_request_format`: A boolean indicating whether the tag supports the UbiOps request format
- `implicit`: A boolean indicating whether the tag is implicitly created
- `deprecated`: A boolean indicating whether the tag is deprecated
- `size`: Size of docker image of the tag
- `error_message`: Error message which explains why the build has failed if the tag has failed to build
- `base_environment_name`: Name of the base environment that the tag was built on top of, if applicable
- `base_environment_tag`: Name of the base environment tag that the tag was built on top of, if applicable
- `built`: A boolean indicating whether the tag is built by UbiOps

## Response Examples

```
[
  {
    "id": "8760570f-6eda-470b-99af-bde810d418d8",
    "name": "v1",
    "environment": "python3-12-custom",
    "creation_date": "2023-01-23T12:17:11.863+00:00",
    "status": "available",
    "supports_request_format": true,
    "implicit": false,
    "deprecated": false,
    "size": 104857600,
    "error_message": null,
    "base_environment_name": "ubiops-ubuntu24-04-python3-12",
    "base_environment_tag": "v5.25.0",
    "built": true
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
supports_request_format = True # bool (optional)

# List tags
api_response = core_api.environment_tags_list(project_name, environment_name, supports_request_format=supports_request_format)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **supports_request_format** | **bool** | [optional] 

### Return type

[**list[EnvironmentTagList]**](./models/EnvironmentTagList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_tags_rebuild**
> Success environment_tags_rebuild(project_name, environment_name, tag_name, data=data)

Rebuild tag

## Description
Trigger a rebuild for a tag

### Response Structure

- `success`: Boolean indicating whether the rebuild was triggered successful

## Response Examples

```
{
  "success": true
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
tag_name = 'tag_name_example' # str
data = None # empty dict or None (optional)

# Rebuild tag
api_response = core_api.environment_tags_rebuild(project_name, environment_name, tag_name, data=data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **tag_name** | **str** | 
 **data** | **empty dict or None** | [optional] 

### Return type

[**Success**](./models/Success.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_tags_update**
> EnvironmentTagList environment_tags_update(project_name, environment_name, tag_name, data)

Update tag

## Description
Update a tag of an environment

### Optional Parameters

- `status`: The status of the tag to cancel a build
- `supports_request_format`: A boolean indicating whether the tag supports the UbiOps request format

## Request Examples

```
{
  "supports_request_format": false
}
```

### Response Structure
Details of the updated tag

- `id`: Unique identifier for the tag
- `name`: Name of the tag
- `environment`: Environment to which the tag is linked
- `creation_date`: The date when the tag was created
- `status`: The status of the tag
- `supports_request_format`: A boolean indicating whether the tag supports the UbiOps request format
- `implicit`: A boolean indicating whether the tag is implicitly created
- `deprecated`: A boolean indicating whether the tag is deprecated
- `size`: Size of docker image of the tag
- `error_message`: Error message which explains why the build has failed if the tag has failed to build
- `base_environment_name`: Name of the base environment that the tag was built on top of, if applicable
- `base_environment_tag`: Name of the base environment tag that the tag was built on top of, if applicable
- `built`: A boolean indicating whether the tag is built by UbiOps

## Response Examples

```
{
  "id": "8760570f-6eda-470b-99af-bde810d418d8",
  "name": "v1",
  "environment": "python3-12-custom",
  "creation_date": "2023-01-23T12:17:11.863+00:00",
  "status": "available",
  "supports_request_format": false,
  "implicit": false,
  "deprecated": false,
  "size": 104857600,
  "error_message": null,
  "base_environment_name": ""ubiops-ubuntu24-04-python3-12",
  "base_environment_tag": "v5.25.0",
  "built": true
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
tag_name = 'tag_name_example' # str
data = ubiops.EnvironmentTagUpdate() # EnvironmentTagUpdate

# Update tag
api_response = core_api.environment_tags_update(project_name, environment_name, tag_name, data)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **tag_name** | **str** | 
 **data** | [**EnvironmentTagUpdate**](./models/EnvironmentTagUpdate.md) | 

### Return type

[**EnvironmentTagList**](./models/EnvironmentTagList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environment_tags_usage**
> list[EnvironmentTagUsage] environment_tags_usage(project_name, environment_name, tag_name)

List usage of tag

## Description
List the deployment versions used by a tag

### Response Structure
A list of details of the deployment versions

- `id`: Unique identifier for the deployment version (UUID)
- `deployment`: Deployment name to which the version is associated
- `version`: Version name
- `environment_name`: The name of the environment of the tag
- `environment_tag`: The name of the tag
- `tag`: Tag of the environment
- `status`: The status of the version

## Response Examples

```
[
  {
    "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
    "deployment": "deployment-1",
    "version": "version-1",
    "environment_name": "ubiops-ubuntu24-04-python3-12",
    "environment_tag": "v5.25.0",
    "status": "available"
  },
  {
    "id": "24f6b80a-08c3-4d52-ac1a-2ea7e70f16a6",
    "deployment": "deployment-1",
    "version": "version-2",
    "environment_name": "ubiops-ubuntu24-04-python3-12",
    "environment_tag": "v5.25.0",
    "status": "unavailable"
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
environment_name = 'environment_name_example' # str
tag_name = 'tag_name_example' # str

# List usage of tag
api_response = core_api.environment_tags_usage(project_name, environment_name, tag_name)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **environment_name** | **str** | 
 **tag_name** | **str** | 

### Return type

[**list[EnvironmentTagUsage]**](./models/EnvironmentTagUsage.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environments_create**
> EnvironmentList environments_create(project_name, data)

Create environments

## Description
Create an environment

### Required Parameters

- `name`: Name of the environment

### Optional Parameters

- `description`: Description for the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Request Examples

```
{
  "name": "python3-12-custom"
}
```

### Response Structure
Details of the created environment

- `id`: Unique identifier for the environment
- `name`: Name of the environment
- `project`: Project name in which the environment is defined
- `creation_date`: The date when the environment was created
- `last_updated`: The date when the environment was last updated
- `description`: Description of the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `system`: A boolean indicating whether the environment was created by the system

## Response Examples

```
{
  "id": "3a7d94ca-4df4-4be3-857c-d6b9995cd17a",
  "name": "python3-12-custom",
  "project": "project-1",
  "creation_date": "2023-03-01T08:32:14.876451Z",
  "last_updated": "2023-03-01T08:32:14.876451Z",
  "description": "Custom environment based on Python 3.12",
  "labels": {
    "type": "environment"
  },
  "system": false
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
> EnvironmentList environments_get(project_name, environment_name)

Get environment

## Description
Retrieve details of an environment

### Response Structure
Details of the environment

- `id`: Unique identifier for the environment
- `name`: Name of the environment
- `project`: Project name in which the environment is defined
- `creation_date`: The date when the environment was created
- `last_updated`: The date when the environment was last updated
- `description`: Description of the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `system`: A boolean indicating whether the environment was created by the system

## Response Examples

```
{
  "id": "3a7d94ca-4df4-4be3-857c-d6b9995cd17a",
  "name": "python3-12-custom",
  "project": "project-1",
  "creation_date": "2023-03-01T08:32:14.876451Z",
  "last_updated": "2023-03-01T10:52:23.124784Z",
  "description": "Custom environment based on Python 3.12",
  "labels": {
    "type": "environment"
  },
  "system": false
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

[**EnvironmentList**](./models/EnvironmentList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environments_list**
> list[EnvironmentList] environments_list(project_name, labels=labels, system=system)

List environments

## Description
Environments can be filtered according to the labels they have by giving labels as a query parameter. Environments that have at least one of the labels on which is filtered, are returned.

### Optional Parameters

- `labels`: Filter on labels of the environment. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.
- `system`: Filter on whether the environment was created by the system

### Response Structure
A list of details of the environments

- `id`: Unique identifier for the environment
- `name`: Name of the environment
- `project`: Project name in which the environment is defined. It is null for base environments.
- `creation_date`: The date when the environment was created
- `last_updated`: The date when the environment was last updated
- `description`: Description of the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Response Examples

```
[
  {
    "id": "1319895f-467b-4732-9804-7de500099233",
    "name": "ubiops-ubuntu24-04-python3-12",
    "project": null,
    "creation_date": "2023-03-01T08:32:14.876451Z",
    "last_updated": "2023-03-01T10:52:23.124784Z",
    "description": "Base environment containing Python 3.12",
    "labels": {}
},
  {
    "id": "3a7d94ca-4df4-4be3-857c-d6b9995cd17a",
    "name": "python3-12-custom",
    "project": "project-1",
    "creation_date": "2023-03-02T12:15:43.124751Z",
    "last_updated": "2023-03-03T13:14:23.865421Z",
    "description": "Custom environment based on Python 3.12",
    "labels": {
      "type": "environment"
    }
  }
]
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python
project_name = 'project_name_example' # str
labels = "label1:value1,label2:value2" # str (optional)
system = True # bool (optional)

# List environments
api_response = core_api.environments_list(project_name, labels=labels, system=system)
print(api_response)
```

### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **labels** | **str** | [optional] 
 **system** | **bool** | [optional] 

### Return type

[**list[EnvironmentList]**](./models/EnvironmentList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **environments_update**
> EnvironmentList environments_update(project_name, environment_name, data)

Update environment

## Description
Update an environment. When updating labels, the labels will replace the existing value for labels.

### Optional Parameters

- `description`: Description for the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Request Examples

```
{
  "description": "A description of the environment"
}
```

### Response Structure
Details of the updated environment

- `id`: Unique identifier for the environment
- `name`: Name of the environment
- `project`: Project name in which the environment is defined
- `creation_date`: The date when the environment was created
- `last_updated`: The date when the environment was last updated
- `description`: Description of the environment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `system`: A boolean indicating whether the environment was created by the system

## Response Examples

```
{
  "id": "3a7d94ca-4df4-4be3-857c-d6b9995cd17a",
  "name": "new-python3-12-custom",
  "project": "project-1",
  "creation_date": "2023-03-01T08:32:14.876451Z",
  "last_updated": "2023-03-01T10:52:23.124784Z",
  "description": "Custom environment based on Python 3.12",
  "labels": {
    "type": "environment"
  },
  "system": false
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

[**EnvironmentList**](./models/EnvironmentList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


# Blobs

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blobs_create**](./Blobs.md#blobs_create) | **POST** /projects/{project_name}/blobs | Upload a blob
[**blobs_delete**](./Blobs.md#blobs_delete) | **DELETE** /projects/{project_name}/blobs/{blob_id} | Delete a blob
[**blobs_get**](./Blobs.md#blobs_get) | **GET** /projects/{project_name}/blobs/{blob_id} | Get a blob
[**blobs_list**](./Blobs.md#blobs_list) | **GET** /projects/{project_name}/blobs | List blobs
[**blobs_update**](./Blobs.md#blobs_update) | **PUT** /projects/{project_name}/blobs/{blob_id} | Update a blob


# **blobs_create**
> BlobList blobs_create(project_name, file, blob_ttl=blob_ttl)

Upload a blob

## Description
Upload a blob to a project. The uploaded blob file can be retrieved by passing the blob_id. The returned blob_id may be passed in a deployment or pipeline request as input.

### Optional Parameters
These parameters should be given in the header.

- `blob-ttl`: The Blob-TTL parameter designates the time to live of the blob in seconds. The default value is 86400 seconds (1 day).

### Response Structure
The details of the uploaded blob

- `id`: Unique identifier for the blob (UUID)
- `created_by`: The email of the user who created/updated the blob
- `creation_date`: Time the blob was created
- `last_updated`: Time the blob was last updated
- `filename`: Original filename of the blob
- `size`: Size of the uploaded blob in bytes
- `ttl`: Time to live of the blob in seconds

## Response Examples

```
{
  "id": "b58fb853-9311-4583-9688-abed61830abc",
  "created_by": "test-user@ubiops.com",
  "creation_date": "2020-05-18T11:26:57.904+00:00",
  "last_updated": "2020-05-18T11:26:57.904+00:00",
  "filename": "original-filename.jpg",
  "size": 3439,
  "ttl": 86400
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
    file = '/path/to/file' # file
    blob_ttl = 56 # int (optional)

    # Upload a blob
    api_response = core_api.blobs_create(project_name, file, blob_ttl=blob_ttl)
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
    file = '/path/to/file' # file
    blob_ttl = 56 # int (optional)

    # Upload a blob
    api_response = core_api.blobs_create(project_name, file, blob_ttl=blob_ttl)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **file** | **file** | 
 **blob_ttl** | **int** | [optional] 

### Return type

[**BlobList**](./models/BlobList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **blobs_delete**
> blobs_delete(project_name, blob_id)

Delete a blob

## Description
Delete a blob from a project

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    blob_id = 'blob_id_example' # str

    # Delete a blob
    core_api.blobs_delete(project_name, blob_id)

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
    blob_id = 'blob_id_example' # str

    # Delete a blob
    core_api.blobs_delete(project_name, blob_id)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **blob_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **blobs_get**
> file blobs_get(project_name, blob_id)

Get a blob

## Description
Download a blob file in a project

### Response Structure

- `file`: Blob file

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    blob_id = 'blob_id_example' # str

    # Get a blob
    with core_api.blobs_get(project_name, blob_id) as response:
        filename = response.getfilename()
        content = response.read()

    # Or directly save the file in the current working directory using _preload_content=True
    # output_path = core_api.blobs_get(project_name, blob_id, _preload_content=True)
    
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
    blob_id = 'blob_id_example' # str

    # Get a blob
    with core_api.blobs_get(project_name, blob_id) as response:
        filename = response.getfilename()
        content = response.read()

    # Or directly save the file in the current working directory using _preload_content=True
    # output_path = core_api.blobs_get(project_name, blob_id, _preload_content=True)
    
    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **blob_id** | **str** | 

### Return type

**file**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **blobs_list**
> list[BlobList] blobs_list(project_name, range=range, creation_date=creation_date)

List blobs

## Description
List all blobs in a project

### Optional Parameters
These parameters should be given as GET parameters.

- `range`: Number of blobs to be returned. It may be a positive or a negative value. If it is positive, blobs uploaded starting from the creation_date towards the present time are returned. Otherwise, blobs uploaded towards the past are returned. The default value is -50.
- `creation_date`: Get the blobs uploaded starting from this date. If it is not provided, the uploaded blobs are returned according to the *range* parameter. It should be provided in year-month-day hour:minute:second format.

### Response Structure
A list of details of the blobs in the project

- `id`: Unique identifier for the blob (UUID)
- `created_by`: The email of the user who created the blob
- `creation_date`: Time the blob was created
- `last_updated`: Time the blob was last updated
- `filename`: Original filename of the blob
- `size`: Size of the uploaded blob in bytes
- `ttl`: Time to live of the blob in seconds

## Response Examples

```
[
  {
    "id": "ecb39626-2a14-4224-a57a-592a51567e17",
    "created_by": "test-user@ubiops.com",
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "last_updated": "2020-05-18T11:26:57.904+00:00",
    "filename": "original-filename.jpg",
    "size": 562,
    "ttl": 12338
  },
  {
    "id": "f629a052-a827-44d9-97cf-3902504edc79",
    "created_by": "test-user@ubiops.com",
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "last_updated": "2020-05-18T11:26:57.904+00:00",
    "filename": "original-filename2.jpg",
    "size": 3439,
    "ttl": 86400
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
    range = 56 # int (optional)
    creation_date = 'creation_date_example' # str (optional)

    # List blobs
    api_response = core_api.blobs_list(project_name, range=range, creation_date=creation_date)
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
    range = 56 # int (optional)
    creation_date = 'creation_date_example' # str (optional)

    # List blobs
    api_response = core_api.blobs_list(project_name, range=range, creation_date=creation_date)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **range** | **int** | [optional] 
 **creation_date** | **str** | [optional] 

### Return type

[**list[BlobList]**](./models/BlobList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **blobs_update**
> BlobList blobs_update(project_name, blob_id, file, blob_ttl=blob_ttl)

Update a blob

## Description
Overwrite a blob with given blob id. The uploaded blob file can be retrieved by passing the blob_id.

### Optional Parameters
These parameters should be given in the header.

- `blob-ttl`: The Blob-TTL parameter designates the time to live of the blob in seconds. The default value is 86400 seconds (1 day).

### Response Structure
The details of the uploaded blob

- `id`: Unique identifier for the blob (UUID)
- `created_by`: The email of the user who created the blob
- `creation_date`: Time the blob was created
- `last_updated`: Time the blob was last updated
- `filename`: Original filename of the blob
- `size`: Size of the uploaded blob in bytes
- `ttl`: Time to live of the blob in seconds

## Response Examples

```
{
  "id": "b58fb853-9311-4583-9688-abed61830abc",
  "created_by": "test-user@ubiops.com",
  "creation_date": "2020-05-18T11:26:57.904+00:00",
  "last_updated": "2020-05-18T11:26:57.904+00:00",
  "filename": "original-filename.jpg",
  "size": 3439,
  "ttl": 86400
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
    blob_id = 'blob_id_example' # str
    file = '/path/to/file' # file
    blob_ttl = 56 # int (optional)

    # Update a blob
    api_response = core_api.blobs_update(project_name, blob_id, file, blob_ttl=blob_ttl)
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
    blob_id = 'blob_id_example' # str
    file = '/path/to/file' # file
    blob_ttl = 56 # int (optional)

    # Update a blob
    api_response = core_api.blobs_update(project_name, blob_id, file, blob_ttl=blob_ttl)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **blob_id** | **str** | 
 **file** | **file** | 
 **blob_ttl** | **int** | [optional] 

### Return type

[**BlobList**](./models/BlobList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


# Files

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buckets_create**](./Files.md#buckets_create) | **POST** /projects/{project_name}/buckets | Create bucket
[**buckets_delete**](./Files.md#buckets_delete) | **DELETE** /projects/{project_name}/buckets/{bucket_name} | Delete a bucket
[**buckets_get**](./Files.md#buckets_get) | **GET** /projects/{project_name}/buckets/{bucket_name} | Get details of a bucket
[**buckets_list**](./Files.md#buckets_list) | **GET** /projects/{project_name}/buckets | List buckets
[**buckets_update**](./Files.md#buckets_update) | **PATCH** /projects/{project_name}/buckets/{bucket_name} | Update a bucket
[**files_complete_multipart_upload**](./Files.md#files_complete_multipart_upload) | **POST** /projects/{project_name}/buckets/{bucket_name}/files/{file}/complete-multipart-upload | Complete multipart upload
[**files_delete**](./Files.md#files_delete) | **DELETE** /projects/{project_name}/buckets/{bucket_name}/files/{file} | Delete a file
[**files_download**](./Files.md#files_download) | **GET** /projects/{project_name}/buckets/{bucket_name}/files/{file}/download | Download a file
[**files_get**](./Files.md#files_get) | **GET** /projects/{project_name}/buckets/{bucket_name}/files/{file} | Get a file
[**files_list**](./Files.md#files_list) | **GET** /projects/{project_name}/buckets/{bucket_name}/files | List files
[**files_start_multipart_upload**](./Files.md#files_start_multipart_upload) | **POST** /projects/{project_name}/buckets/{bucket_name}/files/{file}/start-multipart-upload | Start multipart upload
[**files_upload**](./Files.md#files_upload) | **POST** /projects/{project_name}/buckets/{bucket_name}/files/{file} | Upload a file


# **buckets_create**
> BucketList buckets_create(project_name, data)

Create bucket

## Description
Create a bucket in a project

### Required Parameters

- `name`: Name of the bucket. It is unique within a project.

### Optional Parameters

- `provider`: Provider of the bucket. It can be 'ubiops', 'google_cloud_storage', 'amazon_s3' or 'azure_blob_storage'. The default is **ubiops**.
- `credentials`: A dictionary for credentials to connect to the bucket. It is only required for providers other than *ubiops*. Each provider requires a different set of fields:
    - For Amazon S3, provide the fields `access_key` and `secret_key`.
    - For Azure Blob Storage, provide the field `connection_string` in the format: *DefaultEndpointsProtocol=https;AccountName=<account-name>;AccountKey=<account-key>;EndpointSuffix=core.windows.net*.
    - For Google Cloud Storage, provide the field `json_key_file`.
- `configuration`: A dictionary for additional configuration details for the bucket. It is only required for providers other than *ubiops*. Each provider requires a different set of fields:
    - For Amazon S3, provide the fields `bucket` and `prefix`. One of the fields `region` or `endpoint_url` needs to be provided. The fields `signature_version`, `verify` and `use_ssl` are optional.
    - For Azure Blob Storage, provide the fields `container` and `prefix`.
    - For Google Cloud Storage, provide the fields `bucket` and `prefix`.
    UbiOps always makes sure that the prefix ends with a '/'.
- `description`: Description of the bucket
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `ttl`: Time to live for the files in the bucket. It must be a multiple of 604800 (1 week). Pass `null` to keep them forever.

## Request Examples

```
{
  "name": "bucket-1",
  "provider": "ubiops",
  "credentials": {},
  "configuration": {},
  "labels": {
    "type": "bucket"
  },
  "description": "My bucket description"
}
```

### Response Structure
Details of the created bucket

- `id`: Unique identifier for the bucket (UUID)
- `name`: Name of the bucket
- `project`: Project name in which the bucket is created
- `provider`: Provider of the bucket
- `credentials`: Credentials to connect to the bucket
- `configuration`: Additional configuration details for the bucket
- `creation_date`: The date when the bucket was created
- `description`: Description of the bucket
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `ttl`: Time to live for the files in the bucket

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "bucket-1",
  "project": "project-1",
  "provider": "ubiops",
  "credentials": {},
  "configuration": {},
  "creation_date": "2022-05-12T16:23:15.456812Z",
  "labels": {
    "type": "bucket"
  },
  "description": "My bucket description",
  "ttl": null
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
    data = ubiops.BucketCreate() # BucketCreate

    # Create bucket
    api_response = core_api.buckets_create(project_name, data)
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
    data = ubiops.BucketCreate() # BucketCreate

    # Create bucket
    api_response = core_api.buckets_create(project_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**BucketCreate**](./models/BucketCreate.md) | 

### Return type

[**BucketList**](./models/BucketList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **buckets_delete**
> buckets_delete(project_name, bucket_name)

Delete a bucket

## Description
Delete a bucket. If the bucket provider is UbiOps, the files in the bucket will be deleted together with the bucket. For other providers, the files in the bucket are not removed but just the connection from UbiOps to the bucket.

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    bucket_name = 'bucket_name_example' # str

    # Delete a bucket
    core_api.buckets_delete(project_name, bucket_name)

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
    bucket_name = 'bucket_name_example' # str

    # Delete a bucket
    core_api.buckets_delete(project_name, bucket_name)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **bucket_name** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **buckets_get**
> BucketDetail buckets_get(project_name, bucket_name)

Get details of a bucket

## Description
Retrieve details of a bucket in a project

### Response Structure
Details of a bucket

- `id`: Unique identifier for the bucket (UUID)
- `name`: Name of the bucket
- `project`: Project name in which the bucket is defined
- `provider`: Provider of the bucket
- `configuration`: Additional configuration details for the bucket
- `creation_date`: The date when the bucket was created
- `description`: Description of the bucket
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `ttl`: Time to live for the files in the bucket
- `size`: Size of the bucket according to the last measurement date
- `size_measurement_date`: Last measurement date of the size of the bucket

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "bucket-1",
  "project": "project-1",
  "provider": "ubiops",
  "configuration": {},
  "creation_date": "2022-05-12T16:23:15.456812Z",
  "labels": {
    "type": "bucket"
  },
  "description": "My bucket description",
  "ttl": null,
  "size": 2048,
  "size_measurement_date": "2022-05-24T02:23:15.456812Z",
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
    bucket_name = 'bucket_name_example' # str

    # Get details of a bucket
    api_response = core_api.buckets_get(project_name, bucket_name)
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
    bucket_name = 'bucket_name_example' # str

    # Get details of a bucket
    api_response = core_api.buckets_get(project_name, bucket_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **bucket_name** | **str** | 

### Return type

[**BucketDetail**](./models/BucketDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **buckets_list**
> list[BucketList] buckets_list(project_name, labels=labels)

List buckets

## Description
List buckets in a project

### Optional Parameters

- `labels`: Filter on labels of the buckets. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). Buckets that have at least one of the labels in the filter are returned. This parameter should be given as query parameter.

### Response Structure
A list of details of the buckets in the project

- `id`: Unique identifier for the bucket (UUID)
- `name`: Name of the bucket
- `project`: Project name in which the bucket is defined
- `provider`: Provider of the bucket
- `configuration`: Additional configuration details for the bucket
- `creation_date`: The date when the bucket was created
- `description`: Description of the bucket
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `ttl`: Time to live for the files in the bucket

## Response Examples

```
[
  {
    "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
    "name": "bucket-1",
    "project": "project-1",
    "provider": "ubiops",
    "creation_date": "2022-05-12T16:23:15.456812Z",
    "configuration": {},
    "labels": {
      "type": "bucket"
    },
    "description": "My bucket description",
    "ttl": null
  },
  {
    "id": "5f4e942f-d5b8-4d62-99b2-870c15a82127",
    "name": "bucket-2",
    "project": "project-1",
    "provider": "ubiops",
    "creation_date": "2022-05-12T16:23:15.456812Z",
    "configuration": {},
    "labels": {},
    "description": "My bucket 2 description",
    "ttl": null
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
    labels = "label1:value1,label2:value2" # str (optional)

    # List buckets
    api_response = core_api.buckets_list(project_name, labels=labels)
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
    labels = "label1:value1,label2:value2" # str (optional)

    # List buckets
    api_response = core_api.buckets_list(project_name, labels=labels)
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

[**list[BucketList]**](./models/BucketList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **buckets_update**
> BucketDetail buckets_update(project_name, bucket_name, data)

Update a bucket

## Description
Update a bucket

### Optional Parameters

- `credentials`: Credentials to connect to the bucket
- `configuration`: Additional configuration details for the bucket
- `description`: New description for the bucket
- `labels`: New dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label. The new labels will replace the existing value for labels.
- `ttl`: Time to live for the files in the bucket. It must be a multiple of 604800 (1 week).

## Request Examples

```
{
  "description": "New description for the bucket"
}
```

### Response Structure
Details of the updated bucket

- `id`: Unique identifier for the bucket (UUID)
- `name`: Name of the bucket
- `project`: Project name in which the bucket is defined
- `provider`: Provider of the bucket
- `configuration`: Additional configuration details for the bucket
- `creation_date`: The date when the bucket was created
- `description`: Description of the bucket
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `ttl`: Time to live for the files in the bucket
- `size`: Size of the bucket according to the last measurement date
- `size_measurement_date`: Last measurement date of the size of the bucket

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "new-bucket-name",
  "project": "project-1",
  "provider": "ubiops",
  "configuration": {},
  "creation_date": "2022-05-12T16:23:15.456812Z",
  "labels": {
    "type": "bucket"
  },
  "description": "My bucket description",
  "ttl": null,
  "size": 2048,
  "size_measurement_date": "2022-05-24T02:23:15.456812Z",
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
    bucket_name = 'bucket_name_example' # str
    data = ubiops.BucketUpdate() # BucketUpdate

    # Update a bucket
    api_response = core_api.buckets_update(project_name, bucket_name, data)
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
    bucket_name = 'bucket_name_example' # str
    data = ubiops.BucketUpdate() # BucketUpdate

    # Update a bucket
    api_response = core_api.buckets_update(project_name, bucket_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **bucket_name** | **str** | 
 **data** | [**BucketUpdate**](./models/BucketUpdate.md) | 

### Return type

[**BucketDetail**](./models/BucketDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **files_complete_multipart_upload**
> FileMultipartUpload files_complete_multipart_upload(project_name, bucket_name, file, data)

Complete multipart upload

## Description
Complete a multipart upload for a file

### Request Structure
- `parts`: A list of parts that were uploaded

## Request Examples

```
{
  "parts": [
    {
      "ETag": "etag-2",
      "PartNumber": 1
    },
    {
      "ETag": "etag-2",
      "PartNumber": 2
    }
  ]
}
```

### Response Structure

- `upload_id`: ID of the uploaded for the file
- `provider`: Provider of the bucket where the file will be uploaded

## Response Examples

```
{
  "upload_id": "upload-id",
  "provider": "google_cloud_storage"
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
    bucket_name = 'bucket_name_example' # str
    file = 'file_example' # str
    data = ubiops.FileCompleteMultipartUpload() # FileCompleteMultipartUpload

    # Complete multipart upload
    api_response = core_api.files_complete_multipart_upload(project_name, bucket_name, file, data)
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
    bucket_name = 'bucket_name_example' # str
    file = 'file_example' # str
    data = ubiops.FileCompleteMultipartUpload() # FileCompleteMultipartUpload

    # Complete multipart upload
    api_response = core_api.files_complete_multipart_upload(project_name, bucket_name, file, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **bucket_name** | **str** | 
 **file** | **str** | 
 **data** | [**FileCompleteMultipartUpload**](./models/FileCompleteMultipartUpload.md) | 

### Return type

[**FileMultipartUpload**](./models/FileMultipartUpload.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **files_delete**
> files_delete(project_name, bucket_name, file)

Delete a file

## Description
Delete a file from a bucket

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    bucket_name = 'bucket_name_example' # str
    file = 'file_example' # str

    # Delete a file
    core_api.files_delete(project_name, bucket_name, file)

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
    bucket_name = 'bucket_name_example' # str
    file = 'file_example' # str

    # Delete a file
    core_api.files_delete(project_name, bucket_name, file)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **bucket_name** | **str** | 
 **file** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **files_download**
> FileUploadResponse files_download(project_name, bucket_name, file)

Download a file

## Description
Generate a signed url to download a file. Request body should be an empty dictionary.

### Response Structure

- `url`: A url which can be used to download the file from bucket. Make a GET request to this url to download the file.
- `provider`: Provider of the bucket where the file will be uploaded

## Response Examples

```
{
  "url": "https://storage.apis.com/my-bucket/my-file.jpg...",
  "provider": "ubiops"
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
    bucket_name = 'bucket_name_example' # str
    file = 'file_example' # str

    # Download a file
    api_response = core_api.files_download(project_name, bucket_name, file)
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
    bucket_name = 'bucket_name_example' # str
    file = 'file_example' # str

    # Download a file
    api_response = core_api.files_download(project_name, bucket_name, file)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **bucket_name** | **str** | 
 **file** | **str** | 

### Return type

[**FileUploadResponse**](./models/FileUploadResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **files_get**
> FileItem files_get(project_name, bucket_name, file)

Get a file

## Description
Get the details of a file in the bucket

### Response Structure

- `file`: Name of the file
- `size`: Size of the file
- `time_created`: The time that the file was created

## Response Examples

```
{
  "file": "my-file-1",
  "size": 123,
  "time_created": "2022-05-12T16:23:15.456812Z"
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
    bucket_name = 'bucket_name_example' # str
    file = 'file_example' # str

    # Get a file
    api_response = core_api.files_get(project_name, bucket_name, file)
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
    bucket_name = 'bucket_name_example' # str
    file = 'file_example' # str

    # Get a file
    api_response = core_api.files_get(project_name, bucket_name, file)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **bucket_name** | **str** | 
 **file** | **str** | 

### Return type

[**FileItem**](./models/FileItem.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **files_list**
> FileDetail files_list(project_name, bucket_name, prefix=prefix, delimiter=delimiter, continuation_token=continuation_token, limit=limit)

List files

## Description
List files in a bucket

### Optional Parameters
The following parameters should be given as query parameters:

- `prefix`: Prefix to filter files
- `delimiter`: Delimiter used with prefix to emulate hierarchy to filter files
- `limit`: The maximum number of files returned, default is 100
- `continuation_token`: A token that indicates the start point of the returned the files

### Response Structure
A dictionary containing the details of files and prefixes in the bucket

- `continuation_token`: Next token to get the next set of files
- `files`: A list of dictionaries containing the details of the files. It contains the file name ('file'), size of the file ('size') and the creation time of the file ('time_created').
- `prefixes`: A list of directories

## Response Examples

```
{
  "continuation_token": "1234",
  "files": [
    {
      "file": "my-file-1",
      "size": 123,
      "time_created": "2022-05-12T16:23:15.456812Z"
    },
    {
      "file": "my-file-2",
      "size": 456,
      "time_created": "2022-06-05T10:56:12.186046Z"
    }
  ],
  "prefixes": [
    "my-dir-1",
    "my-dir-2"
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
    bucket_name = 'bucket_name_example' # str
    prefix = 'prefix_example' # str (optional)
    delimiter = 'delimiter_example' # str (optional)
    continuation_token = 'continuation_token_example' # str (optional)
    limit = 56 # int (optional)

    # List files
    api_response = core_api.files_list(project_name, bucket_name, prefix=prefix, delimiter=delimiter, continuation_token=continuation_token, limit=limit)
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
    bucket_name = 'bucket_name_example' # str
    prefix = 'prefix_example' # str (optional)
    delimiter = 'delimiter_example' # str (optional)
    continuation_token = 'continuation_token_example' # str (optional)
    limit = 56 # int (optional)

    # List files
    api_response = core_api.files_list(project_name, bucket_name, prefix=prefix, delimiter=delimiter, continuation_token=continuation_token, limit=limit)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **bucket_name** | **str** | 
 **prefix** | **str** | [optional] 
 **delimiter** | **str** | [optional] 
 **continuation_token** | **str** | [optional] 
 **limit** | **int** | [optional] 

### Return type

[**FileDetail**](./models/FileDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **files_start_multipart_upload**
> FileMultipartUpload files_start_multipart_upload(project_name, bucket_name, file, data=data)

Start multipart upload

## Description
Start a multipart upload for a file

### Response Structure

- `upload_id`: ID of the upload for the file
- `provider`: Provider of the bucket where the file will be uploaded

## Response Examples

```
{
  "upload_id": "upload-id",
  "provider": "google_cloud_storage"
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
    bucket_name = 'bucket_name_example' # str
    file = 'file_example' # str
    data = None # empty dict or None (optional)

    # Start multipart upload
    api_response = core_api.files_start_multipart_upload(project_name, bucket_name, file, data=data)
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
    bucket_name = 'bucket_name_example' # str
    file = 'file_example' # str
    data = None # empty dict or None (optional)

    # Start multipart upload
    api_response = core_api.files_start_multipart_upload(project_name, bucket_name, file, data=data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **bucket_name** | **str** | 
 **file** | **str** | 
 **data** | **empty dict or None** | [optional] 

### Return type

[**FileMultipartUpload**](./models/FileMultipartUpload.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **files_upload**
> FileUploadResponse files_upload(project_name, bucket_name, file, upload_id=upload_id, part_number=part_number, data=data)

Upload a file

## Description
Generate a signed url to upload a file. Request body should be an empty dictionary.

Note: When using the url generated by this endpoint for Azure Blob Storage, the following headers must be added to the upload request to Azure Blob Storage:
- `x-ms-version`: '2020-04-08'
- `x-ms-blob-type`: 'BlockBlob'

### Optional Parameters

- `upload_id`: ID of the upload for the file. It should be used with multipart uploads.
- `part_number`: Part number of the upload. It should be used with multipart uploads.

### Response Structure

- `url`: A url which can be used to upload the file to bucket. Make a PUT request to this url with the file content to upload the file.
- `provider`: Provider of the bucket where the file will be uploaded

## Response Examples

```
{
  "url": "https://storage.apis.com/my-bucket/my-file.jpg...",
  "provider": "ubiops"
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
    bucket_name = 'bucket_name_example' # str
    file = 'file_example' # str
    upload_id = 'upload_id_example' # str (optional)
    part_number = 'part_number_example' # str (optional)
    data = None # empty dict or None (optional)

    # Upload a file
    api_response = core_api.files_upload(project_name, bucket_name, file, upload_id=upload_id, part_number=part_number, data=data)
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
    bucket_name = 'bucket_name_example' # str
    file = 'file_example' # str
    upload_id = 'upload_id_example' # str (optional)
    part_number = 'part_number_example' # str (optional)
    data = None # empty dict or None (optional)

    # Upload a file
    api_response = core_api.files_upload(project_name, bucket_name, file, upload_id=upload_id, part_number=part_number, data=data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **bucket_name** | **str** | 
 **file** | **str** | 
 **upload_id** | **str** | [optional] 
 **part_number** | **str** | [optional] 
 **data** | **empty dict or None** | [optional] 

### Return type

[**FileUploadResponse**](./models/FileUploadResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


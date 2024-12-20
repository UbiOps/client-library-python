# FileOperations

Helper functions for file operations.

| Method                                                   | Description                                                                        |
|----------------------------------------------------------|------------------------------------------------------------------------------------|
| [**upload_file**](./FileOperations.md#upload_file)       | Upload a file to a bucket                                                          |
| [**upload_files**](./FileOperations.md#upload_files)     | Upload multiple files to a bucket, recursive directory upload is also supported    |
| [**download_file**](./FileOperations.md#download_file)   | Download a file from a bucket                                                      |
| [**download_files**](./FileOperations.md#download_files) | Download multiple files from a bucket to local directory preserving tree structure |

# **upload_file**
> upload_file(client, project_name, file_path, bucket_name='default', file_name=None)

Upload a file to a bucket

## Description
Helper function to upload a file to a bucket. A signed url will be generated and used to upload the file.

### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

project_name = 'project_name_example' # str 
file_path = 'path/to/local_file_example' # str
bucket_name = 'default' # str  (optional)
file_name = 'remote_file_example' # str  (optional) - may contain prefixes

# Upload a file
ubiops.utils.upload_file(api_client, project_name, file_path, bucket_name=bucket_name, file_name=file_name)

# Close the connection
api_client.close()
```

### Parameters

| Name             | Type                 | Notes                                              |
|------------------|----------------------|----------------------------------------------------|
| **client**       | **ubiops.ApiClient** |                                                    |
| **project_name** | **str**              |                                                    |
| **file_path**    | **str**              |                                                    |
| **bucket_name**  | **str**              | [optional] [default to 'default']                  |
| **file_name**    | **str**              | [optional] [default to None (use local file name)] |


### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


# **upload_files**
> upload_files(client, project_name, file_paths, bucket_name='default', file_prefix=None, parallel_uploads=5)

Upload multiple files and directories with files to a bucket

## Description
Helper function to upload a list of files and directories to a bucket. When a directory path is specified, the directory is recursively uploaded to a bucket preserving tree structure.

Signed urls will be generated and used to upload the files.

If a 'file_prefix' is provided, it will be added to all file names. This allows putting all files and uploaded directories in a 'sub-directory' in the bucket.

By specifying the number of parallel uploads, the uploads can be made faster.


### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

project_name = 'project_name_example' # str 
file_paths = [
    'path/to/local_file_1',
    'path/to/other/local_file_2',
    'path/to/local_directory',
] # list[str]
bucket_name = 'default' # str  (optional)
file_prefix = 'remote/directory' # str  (optional) - may contain slashes
parallel_uploads = 10 # int  (optional) - number of parallel uploads, default - 5

# Upload list of files
ubiops.utils.upload_files(
    api_client,
    project_name,
    file_paths,
    bucket_name=bucket_name,
    file_prefix=file_prefix, 
    parallel_uploads=parallel_uploads
)

# Close the connection
api_client.close()
```

### Parameters

| Name                 | Type                 | Notes                                                            |
|----------------------|----------------------|------------------------------------------------------------------|
| **client**           | **ubiops.ApiClient** |                                                                  |
| **project_name**     | **str**              |                                                                  |
| **file_paths**       | **list[str]**        |                                                                  |
| **bucket_name**      | **str**              | [optional] [default to 'default']                                |
| **file_prefix**      | **str**              | [optional] [default to None (files are uploaded to bucket root)] |
| **parallel_uploads** | **int**              | [optional] [default to 5]                                        |


### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


# **download_file**
> download_file(client, project_name, bucket_name='default', file_name=None, file_uri=None, output_path='.', stream=True, chunk_size=8192)

Download a file from a bucket

## Description
Helper function to download a file from a bucket. A signed url will be generated and used to download the file.

### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

project_name = 'project_name_example' # str
output_path = '.' # str  (optional) - path to file or directory

# Download a file using a file_uri
file_uri = 'ubiops-file://default/remote_file_example' # str  (optional)
ubiops.utils.download_file(
    api_client, project_name, file_uri=file_uri, output_path=output_path, stream=True, chunk_size=8192
)

# Or download a file using a bucket_name and file_name
bucket_name = 'default' # str  (optional)
file_name = 'remote_file_example' # str  (optional) - may contain prefixes
ubiops.utils.download_file(
    api_client,
    project_name,
    bucket_name=bucket_name,
    file_name=file_name,
    output_path=output_path,
    stream=True,
    chunk_size=8192
)

# Close the connection
api_client.close()
```

### Parameters

| Name             | Type                 | Notes                                                   |
|------------------|----------------------|---------------------------------------------------------|
| **client**       | **ubiops.ApiClient** |                                                         |
| **project_name** | **str**              |                                                         |
| **bucket_name**  | **str**              | [optional] [default to 'default']                       |
| **file_name**    | **str**              | [optional]                                              |
| **file_uri**     | **str**              | [optional]                                              |
| **output_path**  | **str**              | [optional] [default to '.' (current working directory)] |
| **stream**       | **bool**             | [optional] [default to True]                            |
| **chunk_size**   | **int**              | [optional] [default to 8192]                            |


### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


# **download_files**
> download_files(client, project_name, bucket_name='default', prefix=None, output_path='.', stream=True, chunk_size=8192, parellel_download=5)

Download multiple files from a bucket

## Description
Helper function to download multiple files or all files from a bucket. A signed url will be generated and used to download the file.

If a 'prefix' is provided, only files with this prefix will be downloaded. This is useful to download files from a 'sub-directory' in the bucket.

By specifying the number of parallel downloads, the downloads can be made faster.


### Example

```python
import ubiops
configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)

project_name = 'project_name_example' # str
output_path = '.' # str  (optional) - path to file or directory

# Download all files from "default" bucket
ubiops.utils.download_files(
    api_client, project_name, output_path=output_path, stream=True, chunk_size=8192
)

# Or download files from a certain location in the bucket with 10 parallel downloads
bucket_name = 'bucket_name' # str  (optional)
prefix = 'remote/directory' # str  (optional) - may contain slashes
ubiops.utils.download_files(
    api_client,
    project_name,
    bucket_name=bucket_name,
    prefix=prefix,
    output_path=output_path,
    stream=True,
    chunk_size=8192,
    parallel_downloads=10
)

# Close the connection
api_client.close()
```

### Parameters

| Name                  | Type                 | Notes                                                   |
|-----------------------|----------------------|---------------------------------------------------------|
| **client**            | **ubiops.ApiClient** |                                                         |
| **project_name**      | **str**              |                                                         |
| **bucket_name**       | **str**              | [optional] [default to 'default']                       |
| **prefix**            | **str**              | [optional]                                              |
| **output_path**       | **str**              | [optional] [default to '.' (current working directory)] |
| **stream**            | **bool**             | [optional] [default to True]                            |
| **chunk_size**        | **int**              | [optional] [default to 8192]                            |
| **parallel_download** | **int**              | [optional] [default to 5]                               |


### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

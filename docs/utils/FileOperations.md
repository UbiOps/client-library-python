# FileOperations

Helper functions for file operations.

| Method                                               | Description                   |
|------------------------------------------------------|-------------------------------|
| [**upload_file**](FileOperations.md#upload_file)     | Upload a file to a bucket     |
| [**download_file**](FileOperations.md#download_file) | Download a file from a bucket |

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
    api_client, project_name, file_uri=file_uri, output_path=output_path,
    stream=True, chunk_size=8192
)

# Or download a file using a bucket_name and file_name
bucket_name = 'default' # str  (optional)
file_name = 'remote_file_example' # str  (optional) - may contain prefixes
ubiops.utils.download_file(
    api_client, project_name, bucket_name=bucket_name, file_name=file_name, output_path=output_path,
    stream=True, chunk_size=8192
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

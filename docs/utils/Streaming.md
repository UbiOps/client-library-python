# Streaming

Helper functions for creating streaming pipeline and deployment requests.

| Method                                                                    | Description                           |
|---------------------------------------------------------------------------|---------------------------------------|
| [**stream_deployment_request**](./Streaming.md#stream_deployment_request) | Create a streaming deployment request |
| [**stream_pipeline_request**](./Streaming.md#stream_pipeline_request)     | Create a streaming pipeline request   |

# **stream_deployment_request**

> stream_deployment_request(client, project_name, deployment_name, version=None, data=None, timeout=3600, full_response=False)

Create a streaming request to a deployment version

## Description

Create a streaming request to a deployment version and obtain the partial results while the request is still going on.

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
deployment_name = 'deployment_name_example' # str 
version = 'version_example' # str (optional)
data = 'data' # str or dict  (optional)
timeout = 3600 # int  (optional)
full_response = False # bool  (optional)

# Create a streaming deployment request
for item in ubiops.utils.stream_deployment_request(
    client=api_client,
    project_name=project_name,
    deployment_name=deployment_name,
    version=version,
    data=data,
    timeout=timeout,
    full_response=full_response,
):
    print(f"Received: {item}")

# Close the connection
api_client.close()
```

### Parameters

| Name                 | Type                 | Notes                         |
|----------------------|----------------------|-------------------------------|
| **client**           | **ubiops.ApiClient** |                               |
| **project_name**     | **str**              |                               |
| **deployment_name**  | **str**              |                               |
| **version**          | **str**              | [optional] [default to None]  |
| **data**             | **str or dict**      | [optional] [default to ""]    |
| **timeout**          | **int**              | [optional] [default to 3600]  |
| **full_response**    | **bool**             | [optional] [default to False] |

### Return type

**str** (partial result) or [**DeploymentRequestCreateResponse**](../models/DeploymentRequestCreateResponse.md) (full response)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


# **stream_pipeline_request**

> stream_pipeline_request(client, project_name, pipeline_name, version=None, data=None, timeout=7200, full_response=False)

Create a streaming request to a pipeline version

## Description

Create a streaming request to a pipeline version and obtain the partial results while the request is still going on.

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
pipeline_name = 'pipeline_name_example' # str 
version = 'version_example' # str (optional)
data = 'data' # str or dict  (optional)
timeout = 7200 # int  (optional)
full_response = False # bool  (optional)

# Create a streaming pipeline request
for item in ubiops.utils.stream_pipeline_request(
    client=api_client,
    project_name=project_name,
    pipeline_name=pipeline_name,
    version=version,
    data=data,
    timeout=timeout,
    full_response=full_response,
):
    print(f"Received: {item}")

# Close the connection
api_client.close()
```

### Parameters

| Name              | Type                 | Notes                         |
|-------------------|----------------------|-------------------------------|
| **client**        | **ubiops.ApiClient** |                               |
| **project_name**  | **str**              |                               |
| **pipeline_name** | **str**              |                               |
| **version**       | **str**              | [optional] [default to None]  |
| **data**          | **str or dict**      | [optional] [default to ""]    |
| **timeout**       | **int**              | [optional] [default to 7200]  |
| **full_response** | **bool**             | [optional] [default to False] |

### Return type

**str** (partial result) or [**PipelineRequestCreateResponse**](../models/PipelineRequestCreateResponse.md) (full response)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

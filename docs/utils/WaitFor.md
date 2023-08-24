# WaitFor

A collection of wait-for functions that can be used for improved workflow.

| Method                                                                                      | Description                                          |
|---------------------------------------------------------------------------------------------|------------------------------------------------------|
| [**wait_for_deployment_version**](./WaitFor.md#wait_for_deployment_version)                 | Wait for deployment version to be available          |
| [**wait_for_experiment**](./WaitFor.md#wait_for_experiment)                                 | Wait for experiment to be available                  |
| [**wait_for_environment**](./WaitFor.md#wait_for_environment)                               | Wait for environment to build                        |
| [**wait_for_revision**](./WaitFor.md#wait_for_revision)                                     | Wait for deployment version revision to be available |
| [**wait_for_deployment_request**](./WaitFor.md#wait_for_deployment_request)                 | Wait for deployment request to complete              |
| [**wait_for_deployment_version_request**](./WaitFor.md#wait_for_deployment_version_request) | Wait for deployment version request to complete      |
| [**wait_for_experiment_run**](./WaitFor.md#wait_for_experiment_run)                         | Wait for experiment run to complete                  |
| [**wait_for_pipeline_request**](./WaitFor.md#wait_for_pipeline_request)                     | Wait for pipeline request to complete                |
| [**wait_for_pipeline_version_request**](./WaitFor.md#wait_for_pipeline_version_request)     | Wait for pipeline version request to complete        |
| [**wait_for_export**](./WaitFor.md#wait_for_export)                                         | Wait for export to complete                          |
| [**wait_for_import**](./WaitFor.md#wait_for_import)                                         | Wait for import to complete                          |

# **wait_for_deployment_version**

> wait_for_deployment_version(client, project_name, deployment_name, version, revision_id=None, timeout=1800, quiet=False, stream_logs=False)

Wait for successful deployment version build

## Description

This function waits for a deployment version to be built successfully before returning. This is done by checking if the
corresponding environment is built successfully and if the deployment version revision is successful. If the environment
build or revision fails or does not complete in the given timeout, an exception will be raised.

If no revision id is given, the latest revision of the deployment version will be used.

When stream_logs is set to True, we will wait 20 seconds longer than the environment/revision was first seen as
completed to make sure all logs are retrieved. Logs will be shown from environment/revision creation time onwards.

### Example

- Use system environment variables
    ```python
    import ubiops
    
    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()
    
    project_name = "project"
    deployment_name = "deployment"
    version = 'version'
    
    # Create a deployment, version and revision
    version_template = ubiops.DeploymentVersionCreate(version=version)
    core_api.deployment_versions_create(project_name, deployment_name, data=version_template)
    response = core_api.revisions_file_upload(project_name, deployment_name, version, file='deployment.zip')
    print("Upload response is:", response)
    
    # Wait for the deployment version to be available
    ubiops.utils.wait_for_deployment_version(
        core_api.api_client, project_name, deployment_name, version, revision_id=response.revision,
        timeout=1800, quiet=False, stream_logs=False
    )
    print("Deployment version is available")
    
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
    
    project_name = "project"
    deployment_name = "deployment"
    version = 'version'
    
    # Create a deployment, version and revision
    version_template = ubiops.DeploymentVersionCreate(version=version)
    core_api.deployment_versions_create(project_name, deployment_name, data=version_template)
    response = core_api.revisions_file_upload(project_name, deployment_name, version, file='deployment.zip')
    print("Upload response is:", response)
    
    # Wait for the deployment version to be available
    ubiops.utils.wait_for_deployment_version(
        api_client, project_name, deployment_name, version, revision_id=response.revision,
        timeout=1800, quiet=False, stream_logs=False
    )
    print("Deployment version is available")
    
    # Close the connection
    api_client.close()
    ```

### Parameters

| Name                | Type                 | Notes                         |
|---------------------|----------------------|-------------------------------|
| **client**          | **ubiops.ApiClient** |                               |
| **project_name**    | **str**              |                               |
| **deployment_name** | **str**              |                               |
| **version**         | **str**              |                               |
| **revision_id**     | **str**              | [optional] [default to None]  |
| **timeout**         | **float**            | [optional] [default to 1800]  |
| **quiet**           | **bool**             | [optional] [default to False] |
| **stream_logs**     | **bool**             | [optional] [default to False] |


### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **wait_for_experiment**

> wait_for_experiment(client, project_name, experiment_name, revision_id=None, timeout=1800, quiet=False, stream_logs=False)

Wait for successful experiment build

## Description

This function waits for an experiment to be built successfully before returning. This is done by checking if the
corresponding environment is built successfully and if the experiment revision is successful. If the environment
build or revision fails or does not complete in the given timeout, an exception will be raised.

If no revision id is given, the latest revision of the experiment will be used.

When stream_logs is set to True, we will wait 20 seconds longer than the environment/revision was first seen as
completed to make sure all logs are retrieved. Logs will be shown from environment/revision creation time onwards.

### Example

- Use system environment variables
    ```python
    import ubiops
    
    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()
    
    project_name = "project"
    experiment_name = "experiment"
    
    ubiops.utils.wait_for_experiment(
        core_api.api_client, project_name, experiment_name,
        timeout=1800, quiet=False, stream_logs=False
    )
    print("Experiment is available")
    
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
    
    project_name = "project"
    experiment_name = "experiment"
    
    ubiops.utils.wait_for_experiment(
        core_api.api_client, project_name, experiment_name,
        timeout=1800, quiet=False, stream_logs=False
    )
    print("Experiment is available")
    
    # Close the connection
    api_client.close()
    ```

### Parameters

| Name                | Type                 | Notes                         |
|---------------------|----------------------|-------------------------------|
| **client**          | **ubiops.ApiClient** |                               |
| **project_name**    | **str**              |                               |
| **experiment_name** | **str**              |                               |
| **revision_id**     | **str**              | [optional] [default to None]  |
| **timeout**         | **float**            | [optional] [default to 1800]  |
| **quiet**           | **bool**             | [optional] [default to False] |
| **stream_logs**     | **bool**             | [optional] [default to False] |


### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **wait_for_environment**

> wait_for_environment(client, project_name, environment_name, timeout=1800, quiet=False, stream_logs=False)

Wait for successful environment build

## Description

This function waits for an environment build to be successful before returning. If the build fails or does not complete
in the given timeout, an exception will be raised.

When stream_logs is set to True, we will wait 20 seconds longer than the environment was first seen as completed to make
sure all logs are retrieved. Logs will be shown from environment creation time onwards.

### Example

- Use system environment variables:
  ```python
    import ubiops
  
    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()
    
    project_name = "project"
    environment_name = "environment"
    
    # Create an environment and revision
    environment_template = ubiops.EnvironmentCreate(
      name=environment_name,
      description="Environment Example",
      base_environment="python3-10"
    )
    core_api.environments_create(project_name, data=environment_template)
    response = core_api.environment_revisions_file_upload(project_name, environment_name, file='environment.zip')
    print("Upload response is:", response)
    
    # Wait for the environment to be available
    ubiops.utils.wait_for_environment(
        core_api.api_client, project_name, environment_name,
        timeout=1800, quiet=False, stream_logs=False
    )
    
    # Close the connection
    core_api.api_client.close()
  ```

- Use authorization parameters
    ```python
    import ubiops  
  
    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token ..."
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = "project"
    environment_name = "environment"
    
    # Create an environment and revision
    environment_template = ubiops.EnvironmentCreate(
      name=environment_name,
      description="Environment Example",
      base_environment="python3-10"
    )
    core_api.environments_create(project_name, data=environment_template)
    response = core_api.environment_revisions_file_upload(project_name, environment_name, file='environment.zip')
    print("Upload response is:", response)
    
    # Wait for the environment to be available
    ubiops.utils.wait_for_environment(
        api_client, project_name, environment_name,
        timeout=1800, quiet=False, stream_logs=False
    )

    # Close the connection
    api_client.close()
    ```

### Parameters

| Name                 | Type                 | Notes                          |
|----------------------|----------------------|--------------------------------|
| **client**           | **ubiops.ApiClient** |                                |
| **project_name**     | **str**              |                                |
| **environment_name** | **str**              |                                |
| **timeout**          | **float**            | [optional] [default to 1800]   |
| **quiet**            | **bool**             | [optional] [default to False]  |
| **stream_logs**      | **bool**             | [optional] [default to False]  |


### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **wait_for_revision**

> wait_for_revision(client, project_name, deployment_name, version, revision_id, timeout=1800, quiet=False, stream_logs=False)

Wait for a deployment version revision to be available

## Description

This function waits for a deployment version revision to be validated. If the revision fails or does not
complete in the given timeout, an exception will be raised.

When stream_logs is set to True, we will wait 20 seconds longer than the revision was first seen as completed to make
sure all logs are retrieved. Logs will be shown from revision creation time onwards.

### Example

- Use system environment variables:
  ```python
    import ubiops
  
    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()
    
    project_name = "project"
    environment_name = "environment"
    
    # Create an environment and revision
    environment_template = ubiops.EnvironmentCreate(
      name=environment_name,
      description="Environment Example",
      base_environment="python3-10"
    )
    core_api.environments_create(project_name, data=environment_template)
    response = core_api.environment_revisions_file_upload(project_name, environment_name, file='environment.zip')
    print("Upload response is:", response)
    
    # Wait for the environment to be available
    ubiops.utils.wait_for_environment(
        core_api.api_client, project_name, environment_name,
        timeout=1800, quiet=False, stream_logs=False
    )
    
    # Close the connection
    core_api.api_client.close()
  ```

- Use authorization parameters
    ```python
    import ubiops  
  
    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token ..."
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = "project"
    environment_name = "environment"
    
    # Create an environment and revision
    environment_template = ubiops.EnvironmentCreate(
      name=environment_name,
      description="Environment Example",
      base_environment="python3-10"
    )
    core_api.environments_create(project_name, data=environment_template)
    response = core_api.environment_revisions_file_upload(project_name, environment_name, file='environment.zip')
    print("Upload response is:", response)
    
    # Wait for the environment to be available
    ubiops.utils.wait_for_environment(
        api_client, project_name, environment_name,
        timeout=1800, quiet=False, stream_logs=False
    )

    # Close the connection
    api_client.close()
    ```

### Parameters

| Name                | Type                 | Notes                         |
|---------------------|----------------------|-------------------------------|
| **client**          | **ubiops.ApiClient** |                               |
| **project_name**    | **str**              |                               |
| **deployment_name** | **str**              |                               |
| **version**         | **str**              |                               |
| **revision_id**     | **str**              |                               |
| **timeout**         | **float**            | [optional] [default to 1800]  |
| **quiet**           | **bool**             | [optional] [default to False] |
| **stream_logs**     | **bool**             | [optional] [default to False] |


### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **wait_for_deployment_request**

> wait_for_deployment_request(client, project_name, deployment_name, request_id, timeout=1800, quiet=False, stream_logs=False)

Wait for a deployment request to complete

## Description

This function waits for a deployment request to complete. If the request fails or does not complete in the given
timeout, an exception will be raised.

When stream_logs is set to True, we will wait 20 seconds longer than the request was first seen as completed to make
sure all logs are retrieved. Logs will be shown from request creation time onwards.

### Example

- Use system environment variables:
  ```python
    import ubiops
  
    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()
    
    project_name = "project"
    deployment_name = "deployment"
    request_id = "b4858f80-1ad6-4399-8757-b9eac29778dc"
    
    # Wait for the request to complete
    ubiops.utils.wait_for_deployment_request(
      core_api.api_client, project_name, deployment_name, request_id,
      timeout=1800, quiet=False, stream_logs=False
    )
    
    # Close the connection
    core_api.api_client.close()
  ```

- Use authorization parameters
    ```python
    import ubiops  
  
    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token ..."
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = "project"
    deployment_name = "deployment"
    request_id = "b4858f80-1ad6-4399-8757-b9eac29778dc"
    
    # Wait for the request to complete
    ubiops.utils.wait_for_deployment_request(
      core_api.api_client, project_name, deployment_name, request_id,
      timeout=1800, quiet=False, stream_logs=False
    )

    # Close the connection
    api_client.close()
    ```

### Parameters

| Name                | Type                 | Notes                         |
|---------------------|----------------------|-------------------------------|
| **client**          | **ubiops.ApiClient** |                               |
| **project_name**    | **str**              |                               |
| **deployment_name** | **str**              |                               |
| **request_id**      | **str**              |                               |
| **timeout**         | **float**            | [optional] [default to 1800]  |
| **quiet**           | **bool**             | [optional] [default to False] |
| **stream_logs**     | **bool**             | [optional] [default to False] |


### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **wait_for_deployment_version_request**

> wait_for_deployment_version_request(client, project_name, deployment_name, version request_id, timeout=1800, quiet=False, stream_logs=False)

Wait for a deployment version request to complete

## Description

This function waits for a deployment version request to complete. If the request fails or does not complete in the given
timeout, an exception will be raised.

When stream_logs is set to True, we will wait 20 seconds longer than the request was first seen as completed to make
sure all logs are retrieved. Logs will be shown from request creation time onwards.

### Example

- Use system environment variables:
  ```python
    import ubiops
  
    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()
    
    project_name = "project"
    deployment_name = "deployment"
    version = "v1"
    request_id = "b4858f80-1ad6-4399-8757-b9eac29778dc"
    
    # Wait for the request to complete
    ubiops.utils.wait_for_deployment_version_request(
      core_api.api_client, project_name, deployment_name, version, request_id,
      timeout=1800, quiet=False, stream_logs=False
    )
    
    # Close the connection
    core_api.api_client.close()
  ```

- Use authorization parameters
    ```python
    import ubiops  
  
    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token ..."
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = "project"
    deployment_name = "deployment"
    version = "v1"
    request_id = "b4858f80-1ad6-4399-8757-b9eac29778dc"
    
    # Wait for the request to complete
    ubiops.utils.wait_for_deployment_version_request(
      core_api.api_client, project_name, deployment_name, version, request_id,
      timeout=1800, quiet=False, stream_logs=False
    )

    # Close the connection
    api_client.close()
    ```

### Parameters

| Name                | Type                 | Notes                         |
|---------------------|----------------------|-------------------------------|
| **client**          | **ubiops.ApiClient** |                               |
| **project_name**    | **str**              |                               |
| **deployment_name** | **str**              |                               |
| **version**         | **str**              |                               |
| **request_id**      | **str**              |                               |
| **timeout**         | **float**            | [optional] [default to 1800]  |
| **quiet**           | **bool**             | [optional] [default to False] |
| **stream_logs**     | **bool**             | [optional] [default to False] |


### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **wait_for_experiment_run**

> wait_for_experiment_run(client, project_name, experiment_name, run_id, timeout=1800, quiet=False, stream_logs=False)

Wait for an experiment run to complete

## Description

This function waits for an experiment run to complete. If the run fails or does not complete in the given timeout, an
exception will be raised.

When stream_logs is set to True, we will wait 20 seconds longer than the run was first seen as completed to make
sure all logs are retrieved. Logs will be shown from run creation time onwards.

### Example

- Use system environment variables:
  ```python
    import ubiops
  
    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()
    
    project_name = "project"
    experiment_name = "experiment"
    run_id = "b4858f80-1ad6-4399-8757-b9eac29778dc"
    
    # Wait for the run to complete
    ubiops.utils.wait_for_experiment_run(
      core_api.api_client, project_name, experiment_name, run_id,
      timeout=1800, quiet=False, stream_logs=False
    )
    
    # Close the connection
    core_api.api_client.close()
  ```

- Use authorization parameters
    ```python
    import ubiops  
  
    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token ..."
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = "project"
    experiment_name = "experiment"
    run_id = "b4858f80-1ad6-4399-8757-b9eac29778dc"
    
    # Wait for the run to complete
    ubiops.utils.wait_for_experiment_run(
      core_api.api_client, project_name, experiment_name, run_id,
      timeout=1800, quiet=False, stream_logs=False
    )

    # Close the connection
    api_client.close()
    ```

### Parameters

| Name                | Type                 | Notes                         |
|---------------------|----------------------|-------------------------------|
| **client**          | **ubiops.ApiClient** |                               |
| **project_name**    | **str**              |                               |
| **experiment_name** | **str**              |                               |
| **run_id**          | **str**              |                               |
| **timeout**         | **float**            | [optional] [default to 1800]  |
| **quiet**           | **bool**             | [optional] [default to False] |
| **stream_logs**     | **bool**             | [optional] [default to False] |


### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **wait_for_pipeline_request**

> wait_for_pipeline_request(client, project_name, pipeline_name, request_id, timeout=1800, quiet=False, stream_logs=False)

Wait for a pipeline request to complete

## Description

This function waits for a pipeline request to complete. If the request fails or does not complete in the given
timeout, an exception will be raised.

When stream_logs is set to True, we will wait 20 seconds longer than the request was first seen as completed to make
sure all logs are retrieved. Logs will be shown from request creation time onwards.

### Example

- Use system environment variables:
  ```python
    import ubiops
  
    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()
    
    project_name = "project"
    pipeline_name = "pipeline"
    request_id = "b4858f80-1ad6-4399-8757-b9eac29778dc"
    
    # Wait for the request to complete
    ubiops.utils.wait_for_pipeline_request(
      core_api.api_client, project_name, pipeline_name, request_id,
      timeout=1800, quiet=False, stream_logs=False
    )
    
    # Close the connection
    core_api.api_client.close()
  ```

- Use authorization parameters
    ```python
    import ubiops  
  
    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token ..."
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = "project"
    pipeline_name = "pipeline"
    request_id = "b4858f80-1ad6-4399-8757-b9eac29778dc"
    
    # Wait for the request to complete
    ubiops.utils.wait_for_pipeline_request(
      core_api.api_client, project_name, pipeline_name, request_id,
      timeout=1800, quiet=False, stream_logs=False
    )

    # Close the connection
    api_client.close()
    ```

### Parameters

| Name                | Type                 | Notes                         |
|---------------------|----------------------|-------------------------------|
| **client**          | **ubiops.ApiClient** |                               |
| **project_name**    | **str**              |                               |
| **pipeline_name**   | **str**              |                               |
| **request_id**      | **str**              |                               |
| **timeout**         | **float**            | [optional] [default to 1800]  |
| **quiet**           | **bool**             | [optional] [default to False] |
| **stream_logs**     | **bool**             | [optional] [default to False] |


### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **wait_for_pipeline_version_request**

> wait_for_pipeline_version_request(client, project_name, pipeline_name, version request_id, timeout=1800, quiet=False, stream_logs=False)

Wait for a pipeline version request to complete

## Description

This function waits for a pipeline version request to complete. If the request fails or does not complete in the given
timeout, an exception will be raised.

When stream_logs is set to True, we will wait 20 seconds longer than the request was first seen as completed to make
sure all logs are retrieved. Logs will be shown from request creation time onwards.

### Example

- Use system environment variables:
  ```python
    import ubiops
  
    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()
    
    project_name = "project"
    pipeline_name = "pipeline"
    version = "v1"
    request_id = "b4858f80-1ad6-4399-8757-b9eac29778dc"
    
    # Wait for the request to complete
    ubiops.utils.wait_for_pipeline_version_request(
      core_api.api_client, project_name, pipeline_name, version, request_id,
      timeout=1800, quiet=False, stream_logs=False
    )
    
    # Close the connection
    core_api.api_client.close()
  ```

- Use authorization parameters
    ```python
    import ubiops  
  
    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token ..."
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)

    project_name = "project"
    pipeline_name = "pipeline"
    version = "v1"
    request_id = "b4858f80-1ad6-4399-8757-b9eac29778dc"
    
    # Wait for the request to complete
    ubiops.utils.wait_for_pipeline_version_request(
      core_api.api_client, project_name, pipeline_name, version, request_id,
      timeout=1800, quiet=False, stream_logs=False
    )

    # Close the connection
    api_client.close()
    ```

### Parameters

| Name                | Type                 | Notes                         |
|---------------------|----------------------|-------------------------------|
| **client**          | **ubiops.ApiClient** |                               |
| **project_name**    | **str**              |                               |
| **pipeline_name**   | **str**              |                               |
| **version**         | **str**              |                               |
| **request_id**      | **str**              |                               |
| **timeout**         | **float**            | [optional] [default to 1800]  |
| **quiet**           | **bool**             | [optional] [default to False] |
| **stream_logs**     | **bool**             | [optional] [default to False] |


### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **wait_for_export**

> wait_for_export(client, project_name, export_id, timeout=1800, quiet=False)

Wait for an export to complete

## Description

This function waits for an export to complete before returning. If the export fails or does not complete in the given
timeout, an exception will be raised.

### Example

- Use system environment variables
    ```python
    import ubiops
    
    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()
    
    project_name = "project"
    export_id = "b4858f80-1ad6-4399-8757-b9eac29778dc"
    
    ubiops.utils.wait_for_export(
        core_api.api_client, project_name, export_id,
        timeout=1800, quiet=False
    )
    
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
    
    project_name = "project"
    export_id = "b4858f80-1ad6-4399-8757-b9eac29778dc"
    
    ubiops.utils.wait_for_export(
        core_api.api_client, project_name, export_id,
        timeout=1800, quiet=False
    )
    
    # Close the connection
    api_client.close()
    ```

### Parameters

| Name              | Type                 | Notes                         |
|-------------------|----------------------|-------------------------------|
| **client**        | **ubiops.ApiClient** |                               |
| **project_name**  | **str**              |                               |
| **export_id**     | **str**              | [optional] [default to None]  |
| **timeout**       | **float**            | [optional] [default to 1800]  |
| **quiet**         | **bool**             | [optional] [default to False] |


### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **wait_for_import**

> wait_for_import(client, project_name, import_id, timeout=1800, quiet=False)

Wait for an import to complete

## Description

This function waits for an import to complete or wait for confirmation before returning. If the import fails or does
not complete in the given timeout, an exception will be raised.

### Example

- Use system environment variables
    ```python
    import ubiops
    
    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()
    
    project_name = "project"
    import_id = "b4858f80-1ad6-4399-8757-b9eac29778dc"
    
    ubiops.utils.wait_for_import(
        core_api.api_client, project_name, import_id,
        timeout=1800, quiet=False
    )
    
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
    
    project_name = "project"
    import_id = "b4858f80-1ad6-4399-8757-b9eac29778dc"
    
    ubiops.utils.wait_for_import(
        core_api.api_client, project_name, import_id,
        timeout=1800, quiet=False
    )
    
    # Close the connection
    api_client.close()
    ```

### Parameters

| Name              | Type                 | Notes                         |
|-------------------|----------------------|-------------------------------|
| **client**        | **ubiops.ApiClient** |                               |
| **project_name**  | **str**              |                               |
| **import_id**     | **str**              | [optional] [default to None]  |
| **timeout**       | **float**            | [optional] [default to 1800]  |
| **quiet**         | **bool**             | [optional] [default to False] |


### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

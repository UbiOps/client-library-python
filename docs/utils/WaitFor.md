# WaitFor

A collection of wait-for functions that can be used for improved workflow.

| Method                                                                    | Description                                     |
|---------------------------------------------------------------------------|-------------------------------------------------|
| [**wait_for_deployment_version**](WaitFor.md#wait_for_deployment_version) | Wait for successful deployment version          |
| [**wait_for_environment**](WaitFor.md#wait_for_environment)               | Wait for successful environment build           |
| [**wait_for_revision**](WaitFor.md#wait_for_revision)                     | Wait for successful deployment version revision |


# **wait_for_deployment_version**

> wait_for_deployment_version(client, project_name, deployment_name, version, revision_id=None, timeout=1800, quiet=False)

Wait for successful deployment version build

## Description

This function waits for a deployment version to be built successfully before returning. This is done by checking if the
corresponding environment is built successfully and if the deployment version revision is successful. If the environment
build or revision fails or does not complete in the given timeout, an exception will be raised.

If no revision id is given, the latest revision of the deployment version will be used.

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
    ubiops.utils.wait_for_deployment_version(core_api.api_client, project_name, deployment_name, version, revision_id=response.revision)
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
    ubiops.utils.wait_for_deployment_version(api_client, project_name, deployment_name, version, revision_id=response.revision)
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


### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **wait_for_environment**

> wait_for_environment(client, project_name, environment_name, timeout=1800, quiet=False)

Wait for successful environment build

## Description

This function waits for an environment build to be successful before returning. If the build fails or does not complete
in the given timeout, an exception will be raised.

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
    ubiops.utils.wait_for_environment(core_api.api_client, project_name, environment_name)
    
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
    ubiops.utils.wait_for_environment(api_client, project_name, environment_name)

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


### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **wait_for_revision**

> wait_for_revision(client, project_name, deployment_name, version, revision_id, timeout=1800, quiet=False)

Wait for a deployment version revision to be available

## Description

This function waits for a deployment version revision to be validated. If the revision fails or does not
complete in the given timeout, an exception will be raised.

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
    ubiops.utils.wait_for_environment(core_api.api_client, project_name, environment_name)
    
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
    ubiops.utils.wait_for_environment(api_client, project_name, environment_name)

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


### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# ubiops

[www.ubiops.com](https://ubiops.com)

Client Library to interact with the UbiOps API.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v2.1
- Package version: 3.11.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

For more information, please visit [https://ubiops.com/docs](https://ubiops.com/docs)

## Requirements.

Python 3.5+

## Installation & Usage
### pip install

You can install directly using:

```sh
pip install ubiops
```
(you may need to run `pip` with root permission: `sudo pip install ubiops`)

Then import the package:
```python
import ubiops
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ubiops
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import ubiops


configuration = ubiops.Configuration()
# Configure API token authorization
configuration.api_key['Authorization'] = 'Token <YOUR_API_TOKEN>'

# Defining host is optional and default to https://api.ubiops.com/v2.1
configuration.host = "https://api.ubiops.com/v2.1"
# Enter a context with an instance of the API client
api_client = ubiops.ApiClient(configuration)
# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

api_response = api_instance.service_status()
print(api_response)

# Close the connection
api_client.close()

```

## Documentation for API Endpoints

All URIs are relative to *https://api.ubiops.com/v2.1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CoreApi* | [**batch_deployment_requests_create**](docs/CoreApi.md#batch_deployment_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/batch | Create a batch deployment request
*CoreApi* | [**batch_deployment_version_requests_create**](docs/CoreApi.md#batch_deployment_version_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/batch | Create a batch deployment version request
*CoreApi* | [**batch_pipeline_requests_create**](docs/CoreApi.md#batch_pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/batch | Create a batch pipeline request
*CoreApi* | [**batch_pipeline_version_requests_create**](docs/CoreApi.md#batch_pipeline_version_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/batch | Create a batch pipeline version request
*CoreApi* | [**blobs_create**](docs/CoreApi.md#blobs_create) | **POST** /projects/{project_name}/blobs | Upload a blob
*CoreApi* | [**blobs_delete**](docs/CoreApi.md#blobs_delete) | **DELETE** /projects/{project_name}/blobs/{blob_id} | Delete a blob
*CoreApi* | [**blobs_get**](docs/CoreApi.md#blobs_get) | **GET** /projects/{project_name}/blobs/{blob_id} | Get a blob
*CoreApi* | [**blobs_list**](docs/CoreApi.md#blobs_list) | **GET** /projects/{project_name}/blobs | List blobs
*CoreApi* | [**blobs_update**](docs/CoreApi.md#blobs_update) | **PUT** /projects/{project_name}/blobs/{blob_id} | Update a blob
*CoreApi* | [**builds_get**](docs/CoreApi.md#builds_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/builds/{build_id} | Get build
*CoreApi* | [**builds_list**](docs/CoreApi.md#builds_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/builds | List builds
*CoreApi* | [**deployment_audit_events_list**](docs/CoreApi.md#deployment_audit_events_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/audit | List audit events for a deployment
*CoreApi* | [**deployment_environment_variables_copy**](docs/CoreApi.md#deployment_environment_variables_copy) | **POST** /projects/{project_name}/deployments/{deployment_name}/copy-environment-variables | Copy deployment environment variable
*CoreApi* | [**deployment_environment_variables_create**](docs/CoreApi.md#deployment_environment_variables_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/environment-variables | Create deployment environment variable
*CoreApi* | [**deployment_environment_variables_delete**](docs/CoreApi.md#deployment_environment_variables_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Delete deployment environment variable
*CoreApi* | [**deployment_environment_variables_get**](docs/CoreApi.md#deployment_environment_variables_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Get deployment environment variable
*CoreApi* | [**deployment_environment_variables_list**](docs/CoreApi.md#deployment_environment_variables_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/environment-variables | List deployment environment variables
*CoreApi* | [**deployment_environment_variables_update**](docs/CoreApi.md#deployment_environment_variables_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Update deployment environment variable
*CoreApi* | [**deployment_requests_batch_delete**](docs/CoreApi.md#deployment_requests_batch_delete) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/delete | Delete multiple deployment requests
*CoreApi* | [**deployment_requests_batch_get**](docs/CoreApi.md#deployment_requests_batch_get) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/collect | Retrieve multiple deployment requests
*CoreApi* | [**deployment_requests_create**](docs/CoreApi.md#deployment_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests | Create a direct deployment request
*CoreApi* | [**deployment_requests_delete**](docs/CoreApi.md#deployment_requests_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Delete a deployment request
*CoreApi* | [**deployment_requests_get**](docs/CoreApi.md#deployment_requests_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Get a deployment request
*CoreApi* | [**deployment_requests_list**](docs/CoreApi.md#deployment_requests_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/requests | List deployment requests
*CoreApi* | [**deployment_requests_update**](docs/CoreApi.md#deployment_requests_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Update a deployment request
*CoreApi* | [**deployment_version_environment_variables_copy**](docs/CoreApi.md#deployment_version_environment_variables_copy) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/copy-environment-variables | Copy deployment version environment variable
*CoreApi* | [**deployment_version_environment_variables_create**](docs/CoreApi.md#deployment_version_environment_variables_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables | Create deployment version environment variable
*CoreApi* | [**deployment_version_environment_variables_delete**](docs/CoreApi.md#deployment_version_environment_variables_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Delete deployment version environment variable
*CoreApi* | [**deployment_version_environment_variables_get**](docs/CoreApi.md#deployment_version_environment_variables_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Get deployment version environment variable
*CoreApi* | [**deployment_version_environment_variables_list**](docs/CoreApi.md#deployment_version_environment_variables_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables | List deployment version environment variables
*CoreApi* | [**deployment_version_environment_variables_update**](docs/CoreApi.md#deployment_version_environment_variables_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Update deployment version environment variable
*CoreApi* | [**deployment_version_requests_batch_delete**](docs/CoreApi.md#deployment_version_requests_batch_delete) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/delete | Delete multiple deployment version requests
*CoreApi* | [**deployment_version_requests_batch_get**](docs/CoreApi.md#deployment_version_requests_batch_get) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/collect | Retrieve multiple deployment version requests
*CoreApi* | [**deployment_version_requests_create**](docs/CoreApi.md#deployment_version_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests | Create a direct deployment version request
*CoreApi* | [**deployment_version_requests_delete**](docs/CoreApi.md#deployment_version_requests_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Delete a deployment version request
*CoreApi* | [**deployment_version_requests_get**](docs/CoreApi.md#deployment_version_requests_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Get a deployment version request
*CoreApi* | [**deployment_version_requests_list**](docs/CoreApi.md#deployment_version_requests_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests | List deployment version requests
*CoreApi* | [**deployment_version_requests_update**](docs/CoreApi.md#deployment_version_requests_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Update a deployment version request
*CoreApi* | [**deployment_versions_create**](docs/CoreApi.md#deployment_versions_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions | Create deployment versions
*CoreApi* | [**deployment_versions_delete**](docs/CoreApi.md#deployment_versions_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Delete deployment version
*CoreApi* | [**deployment_versions_get**](docs/CoreApi.md#deployment_versions_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Get deployment version
*CoreApi* | [**deployment_versions_list**](docs/CoreApi.md#deployment_versions_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions | List deployment versions
*CoreApi* | [**deployment_versions_update**](docs/CoreApi.md#deployment_versions_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Update deployment version
*CoreApi* | [**deployments_create**](docs/CoreApi.md#deployments_create) | **POST** /projects/{project_name}/deployments | Create deployments
*CoreApi* | [**deployments_delete**](docs/CoreApi.md#deployments_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name} | Delete a deployment
*CoreApi* | [**deployments_get**](docs/CoreApi.md#deployments_get) | **GET** /projects/{project_name}/deployments/{deployment_name} | Get details of a deployment
*CoreApi* | [**deployments_list**](docs/CoreApi.md#deployments_list) | **GET** /projects/{project_name}/deployments | List deployments
*CoreApi* | [**deployments_update**](docs/CoreApi.md#deployments_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name} | Update a deployment
*CoreApi* | [**exports_create**](docs/CoreApi.md#exports_create) | **POST** /projects/{project_name}/exports | Create an export
*CoreApi* | [**exports_delete**](docs/CoreApi.md#exports_delete) | **DELETE** /projects/{project_name}/exports/{export_id} | Delete an export
*CoreApi* | [**exports_download**](docs/CoreApi.md#exports_download) | **GET** /projects/{project_name}/exports/{export_id}/download | Download an export
*CoreApi* | [**exports_get**](docs/CoreApi.md#exports_get) | **GET** /projects/{project_name}/exports/{export_id} | Get an export
*CoreApi* | [**exports_list**](docs/CoreApi.md#exports_list) | **GET** /projects/{project_name}/exports | List exports
*CoreApi* | [**imports_create**](docs/CoreApi.md#imports_create) | **POST** /projects/{project_name}/imports | Create an import
*CoreApi* | [**imports_delete**](docs/CoreApi.md#imports_delete) | **DELETE** /projects/{project_name}/imports/{import_id} | Delete an import
*CoreApi* | [**imports_download**](docs/CoreApi.md#imports_download) | **GET** /projects/{project_name}/imports/{import_id}/download | Download an import
*CoreApi* | [**imports_get**](docs/CoreApi.md#imports_get) | **GET** /projects/{project_name}/imports/{import_id} | Get an import
*CoreApi* | [**imports_list**](docs/CoreApi.md#imports_list) | **GET** /projects/{project_name}/imports | List imports
*CoreApi* | [**imports_update**](docs/CoreApi.md#imports_update) | **PATCH** /projects/{project_name}/imports/{import_id} | Confirm an import
*CoreApi* | [**instance_types_list**](docs/CoreApi.md#instance_types_list) | **GET** /projects/{project_name}/instance-types | List instance types
*CoreApi* | [**metrics_get**](docs/CoreApi.md#metrics_get) | **GET** /projects/{project_name}/metrics/{metric} | Get metrics
*CoreApi* | [**notification_groups_create**](docs/CoreApi.md#notification_groups_create) | **POST** /projects/{project_name}/monitoring/notification-groups | Create notification groups
*CoreApi* | [**notification_groups_delete**](docs/CoreApi.md#notification_groups_delete) | **DELETE** /projects/{project_name}/monitoring/notification-groups/{notification_group_name} | Delete notification group
*CoreApi* | [**notification_groups_get**](docs/CoreApi.md#notification_groups_get) | **GET** /projects/{project_name}/monitoring/notification-groups/{notification_group_name} | Get notification group
*CoreApi* | [**notification_groups_list**](docs/CoreApi.md#notification_groups_list) | **GET** /projects/{project_name}/monitoring/notification-groups | List notification groups
*CoreApi* | [**notification_groups_update**](docs/CoreApi.md#notification_groups_update) | **PATCH** /projects/{project_name}/monitoring/notification-groups/{notification_group_name} | Update notification group
*CoreApi* | [**organization_users_create**](docs/CoreApi.md#organization_users_create) | **POST** /organizations/{organization_name}/users | Add a user to an organization
*CoreApi* | [**organization_users_delete**](docs/CoreApi.md#organization_users_delete) | **DELETE** /organizations/{organization_name}/users/{user_id} | Delete a user from an organization
*CoreApi* | [**organization_users_get**](docs/CoreApi.md#organization_users_get) | **GET** /organizations/{organization_name}/users/{user_id} | Get details of a user in an organization
*CoreApi* | [**organization_users_list**](docs/CoreApi.md#organization_users_list) | **GET** /organizations/{organization_name}/users | List the users in an organization
*CoreApi* | [**organization_users_update**](docs/CoreApi.md#organization_users_update) | **PATCH** /organizations/{organization_name}/users/{user_id} | Update details of a user in an organization
*CoreApi* | [**organizations_create**](docs/CoreApi.md#organizations_create) | **POST** /organizations | Create organizations
*CoreApi* | [**organizations_get**](docs/CoreApi.md#organizations_get) | **GET** /organizations/{organization_name} | Get details of an organization
*CoreApi* | [**organizations_list**](docs/CoreApi.md#organizations_list) | **GET** /organizations | List organizations
*CoreApi* | [**organizations_resource_usage**](docs/CoreApi.md#organizations_resource_usage) | **GET** /organizations/{organization_name}/resources | List resource usage of an organization
*CoreApi* | [**organizations_update**](docs/CoreApi.md#organizations_update) | **PATCH** /organizations/{organization_name} | Update details of an organization
*CoreApi* | [**organizations_usage_get**](docs/CoreApi.md#organizations_usage_get) | **GET** /organizations/{organization_name}/usage | Get resource usage
*CoreApi* | [**permissions_list**](docs/CoreApi.md#permissions_list) | **GET** /permissions | List the available permissions
*CoreApi* | [**pipeline_audit_events_list**](docs/CoreApi.md#pipeline_audit_events_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/audit | List audit events for a pipeline
*CoreApi* | [**pipeline_requests_batch_delete**](docs/CoreApi.md#pipeline_requests_batch_delete) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/delete | Delete multiple pipeline requests
*CoreApi* | [**pipeline_requests_batch_get**](docs/CoreApi.md#pipeline_requests_batch_get) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/collect | Retrieve multiple pipeline requests
*CoreApi* | [**pipeline_requests_create**](docs/CoreApi.md#pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests | Create a pipeline request
*CoreApi* | [**pipeline_requests_delete**](docs/CoreApi.md#pipeline_requests_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/requests/{request_id} | Delete a pipeline request
*CoreApi* | [**pipeline_requests_get**](docs/CoreApi.md#pipeline_requests_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/requests/{request_id} | Get a pipeline request
*CoreApi* | [**pipeline_requests_list**](docs/CoreApi.md#pipeline_requests_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/requests | List pipeline requests
*CoreApi* | [**pipeline_version_object_environment_variables_list**](docs/CoreApi.md#pipeline_version_object_environment_variables_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/objects/{name}/environment-variables | List pipeline object environment variables
*CoreApi* | [**pipeline_version_requests_batch_delete**](docs/CoreApi.md#pipeline_version_requests_batch_delete) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/delete | Delete multiple pipeline version requests
*CoreApi* | [**pipeline_version_requests_batch_get**](docs/CoreApi.md#pipeline_version_requests_batch_get) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/collect | Retrieve multiple pipeline version requests
*CoreApi* | [**pipeline_version_requests_create**](docs/CoreApi.md#pipeline_version_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests | Create a pipeline version request
*CoreApi* | [**pipeline_version_requests_delete**](docs/CoreApi.md#pipeline_version_requests_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/{request_id} | Delete a pipeline version request
*CoreApi* | [**pipeline_version_requests_get**](docs/CoreApi.md#pipeline_version_requests_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/{request_id} | Get a pipeline version request
*CoreApi* | [**pipeline_version_requests_list**](docs/CoreApi.md#pipeline_version_requests_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests | List pipeline version requests
*CoreApi* | [**pipeline_versions_create**](docs/CoreApi.md#pipeline_versions_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions | Create pipeline versions
*CoreApi* | [**pipeline_versions_delete**](docs/CoreApi.md#pipeline_versions_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Delete pipeline version
*CoreApi* | [**pipeline_versions_get**](docs/CoreApi.md#pipeline_versions_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Get pipeline version
*CoreApi* | [**pipeline_versions_list**](docs/CoreApi.md#pipeline_versions_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions | List pipeline versions
*CoreApi* | [**pipeline_versions_update**](docs/CoreApi.md#pipeline_versions_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Update pipeline version
*CoreApi* | [**pipelines_create**](docs/CoreApi.md#pipelines_create) | **POST** /projects/{project_name}/pipelines | Create pipelines
*CoreApi* | [**pipelines_delete**](docs/CoreApi.md#pipelines_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name} | Delete a pipeline
*CoreApi* | [**pipelines_get**](docs/CoreApi.md#pipelines_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name} | Get details of a pipeline
*CoreApi* | [**pipelines_list**](docs/CoreApi.md#pipelines_list) | **GET** /projects/{project_name}/pipelines | List pipelines
*CoreApi* | [**pipelines_update**](docs/CoreApi.md#pipelines_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name} | Update a pipeline
*CoreApi* | [**project_audit_events_list**](docs/CoreApi.md#project_audit_events_list) | **GET** /projects/{project_name}/audit | List audit events in a project
*CoreApi* | [**project_environment_variables_create**](docs/CoreApi.md#project_environment_variables_create) | **POST** /projects/{project_name}/environment-variables | Create project environment variable
*CoreApi* | [**project_environment_variables_delete**](docs/CoreApi.md#project_environment_variables_delete) | **DELETE** /projects/{project_name}/environment-variables/{id} | Delete project environment variable
*CoreApi* | [**project_environment_variables_get**](docs/CoreApi.md#project_environment_variables_get) | **GET** /projects/{project_name}/environment-variables/{id} | Get project environment variable
*CoreApi* | [**project_environment_variables_list**](docs/CoreApi.md#project_environment_variables_list) | **GET** /projects/{project_name}/environment-variables | List project environment variables
*CoreApi* | [**project_environment_variables_update**](docs/CoreApi.md#project_environment_variables_update) | **PATCH** /projects/{project_name}/environment-variables/{id} | Update project environment variable
*CoreApi* | [**project_requests_list**](docs/CoreApi.md#project_requests_list) | **GET** /projects/{project_name}/requests | List requests in project
*CoreApi* | [**project_users_create**](docs/CoreApi.md#project_users_create) | **POST** /projects/{project_name}/users | Add user to a project
*CoreApi* | [**project_users_delete**](docs/CoreApi.md#project_users_delete) | **DELETE** /projects/{project_name}/users/{user_id} | Delete user from a project
*CoreApi* | [**project_users_get**](docs/CoreApi.md#project_users_get) | **GET** /projects/{project_name}/users/{user_id} | Get user in a project
*CoreApi* | [**project_users_list**](docs/CoreApi.md#project_users_list) | **GET** /projects/{project_name}/users | List users in a project
*CoreApi* | [**projects_create**](docs/CoreApi.md#projects_create) | **POST** /projects | Create projects
*CoreApi* | [**projects_delete**](docs/CoreApi.md#projects_delete) | **DELETE** /projects/{project_name} | Delete a project
*CoreApi* | [**projects_get**](docs/CoreApi.md#projects_get) | **GET** /projects/{project_name} | Get details of a project
*CoreApi* | [**projects_list**](docs/CoreApi.md#projects_list) | **GET** /projects | List projects
*CoreApi* | [**projects_log_list**](docs/CoreApi.md#projects_log_list) | **POST** /projects/{project_name}/logs | List logs for a project
*CoreApi* | [**projects_resource_usage**](docs/CoreApi.md#projects_resource_usage) | **GET** /projects/{project_name}/resources | List resource usage of a project
*CoreApi* | [**projects_update**](docs/CoreApi.md#projects_update) | **PATCH** /projects/{project_name} | Update a project
*CoreApi* | [**projects_usage_get**](docs/CoreApi.md#projects_usage_get) | **GET** /projects/{project_name}/usage | Get resource usage
*CoreApi* | [**request_schedules_create**](docs/CoreApi.md#request_schedules_create) | **POST** /projects/{project_name}/schedules | Create request schedules
*CoreApi* | [**request_schedules_delete**](docs/CoreApi.md#request_schedules_delete) | **DELETE** /projects/{project_name}/schedules/{schedule_name} | Delete a request schedule
*CoreApi* | [**request_schedules_get**](docs/CoreApi.md#request_schedules_get) | **GET** /projects/{project_name}/schedules/{schedule_name} | Get details of a request schedule
*CoreApi* | [**request_schedules_list**](docs/CoreApi.md#request_schedules_list) | **GET** /projects/{project_name}/schedules | List request schedules
*CoreApi* | [**request_schedules_update**](docs/CoreApi.md#request_schedules_update) | **PATCH** /projects/{project_name}/schedules/{schedule_name} | Update a request schedule
*CoreApi* | [**revisions_file_download**](docs/CoreApi.md#revisions_file_download) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions/{revision_id}/download | Download deployment file
*CoreApi* | [**revisions_file_upload**](docs/CoreApi.md#revisions_file_upload) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions | Upload deployment file
*CoreApi* | [**revisions_get**](docs/CoreApi.md#revisions_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions/{revision_id} | Get revision
*CoreApi* | [**revisions_list**](docs/CoreApi.md#revisions_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions | List revisions
*CoreApi* | [**role_assignments_create**](docs/CoreApi.md#role_assignments_create) | **POST** /projects/{project_name}/role-assignments | Assign a role to a user in a project
*CoreApi* | [**role_assignments_delete**](docs/CoreApi.md#role_assignments_delete) | **DELETE** /projects/{project_name}/role-assignments/{id} | Delete a role from a user with the given role assignment id
*CoreApi* | [**role_assignments_get**](docs/CoreApi.md#role_assignments_get) | **GET** /projects/{project_name}/role-assignments/{id} | Get details of a role assignment
*CoreApi* | [**role_assignments_per_user_list**](docs/CoreApi.md#role_assignments_per_user_list) | **GET** /projects/{project_name}/users/{user_id}/role-assignments | List the roles assigned to a specific user in a project
*CoreApi* | [**roles_create**](docs/CoreApi.md#roles_create) | **POST** /projects/{project_name}/roles | Create a custom role scoped in a project
*CoreApi* | [**roles_delete**](docs/CoreApi.md#roles_delete) | **DELETE** /projects/{project_name}/roles/{role_name} | Delete a role from a project
*CoreApi* | [**roles_get**](docs/CoreApi.md#roles_get) | **GET** /projects/{project_name}/roles/{role_name} | Get details of a role
*CoreApi* | [**roles_list**](docs/CoreApi.md#roles_list) | **GET** /projects/{project_name}/roles | List the available roles in a project
*CoreApi* | [**roles_update**](docs/CoreApi.md#roles_update) | **PATCH** /projects/{project_name}/roles/{role_name} | Update a role in a project
*CoreApi* | [**service_status**](docs/CoreApi.md#service_status) | **GET** /status | Service status
*CoreApi* | [**service_users_create**](docs/CoreApi.md#service_users_create) | **POST** /projects/{project_name}/service-users | Create a new service user
*CoreApi* | [**service_users_delete**](docs/CoreApi.md#service_users_delete) | **DELETE** /projects/{project_name}/service-users/{service_user_id} | Delete service user
*CoreApi* | [**service_users_get**](docs/CoreApi.md#service_users_get) | **GET** /projects/{project_name}/service-users/{service_user_id} | Retrieve details of a service user
*CoreApi* | [**service_users_list**](docs/CoreApi.md#service_users_list) | **GET** /projects/{project_name}/service-users | List service users
*CoreApi* | [**service_users_token**](docs/CoreApi.md#service_users_token) | **PUT** /projects/{project_name}/service-users/{service_user_id}/token | Reset the token of a service user
*CoreApi* | [**service_users_update**](docs/CoreApi.md#service_users_update) | **PATCH** /projects/{project_name}/service-users/{service_user_id} | Update service user details
*CoreApi* | [**user_create**](docs/CoreApi.md#user_create) | **POST** /user | Create a new user
*CoreApi* | [**user_delete**](docs/CoreApi.md#user_delete) | **DELETE** /user | Delete user


## Documentation For Models

 - [AttachmentFieldsList](docs/AttachmentFieldsList.md)
 - [AttachmentSourcesList](docs/AttachmentSourcesList.md)
 - [AttachmentsCreate](docs/AttachmentsCreate.md)
 - [AttachmentsList](docs/AttachmentsList.md)
 - [AuditList](docs/AuditList.md)
 - [BlobList](docs/BlobList.md)
 - [BuildList](docs/BuildList.md)
 - [DeploymentCreate](docs/DeploymentCreate.md)
 - [DeploymentCreateResponse](docs/DeploymentCreateResponse.md)
 - [DeploymentDetail](docs/DeploymentDetail.md)
 - [DeploymentInputFieldCreate](docs/DeploymentInputFieldCreate.md)
 - [DeploymentInstanceType](docs/DeploymentInstanceType.md)
 - [DeploymentList](docs/DeploymentList.md)
 - [DeploymentOutputFieldCreate](docs/DeploymentOutputFieldCreate.md)
 - [DeploymentRequestBatchCreateResponse](docs/DeploymentRequestBatchCreateResponse.md)
 - [DeploymentRequestBatchDetail](docs/DeploymentRequestBatchDetail.md)
 - [DeploymentRequestCreateResponse](docs/DeploymentRequestCreateResponse.md)
 - [DeploymentRequestList](docs/DeploymentRequestList.md)
 - [DeploymentRequestSingleDetail](docs/DeploymentRequestSingleDetail.md)
 - [DeploymentRequestUpdate](docs/DeploymentRequestUpdate.md)
 - [DeploymentRequestUpdateResponse](docs/DeploymentRequestUpdateResponse.md)
 - [DeploymentUpdate](docs/DeploymentUpdate.md)
 - [DeploymentVersionCreate](docs/DeploymentVersionCreate.md)
 - [DeploymentVersionDetail](docs/DeploymentVersionDetail.md)
 - [DeploymentVersionList](docs/DeploymentVersionList.md)
 - [DeploymentVersionUpdate](docs/DeploymentVersionUpdate.md)
 - [DirectPipelineRequestDeploymentRequest](docs/DirectPipelineRequestDeploymentRequest.md)
 - [EnvironmentVariableCopy](docs/EnvironmentVariableCopy.md)
 - [EnvironmentVariableCreate](docs/EnvironmentVariableCreate.md)
 - [EnvironmentVariableList](docs/EnvironmentVariableList.md)
 - [ExportCreate](docs/ExportCreate.md)
 - [ExportDetail](docs/ExportDetail.md)
 - [ExportList](docs/ExportList.md)
 - [ImportDetail](docs/ImportDetail.md)
 - [ImportList](docs/ImportList.md)
 - [ImportUpdate](docs/ImportUpdate.md)
 - [InheritedEnvironmentVariableList](docs/InheritedEnvironmentVariableList.md)
 - [InputFieldWidgetCreate](docs/InputFieldWidgetCreate.md)
 - [InputOutputFieldDetail](docs/InputOutputFieldDetail.md)
 - [InputOutputFieldList](docs/InputOutputFieldList.md)
 - [InputOutputWidgetList](docs/InputOutputWidgetList.md)
 - [Logs](docs/Logs.md)
 - [LogsCreate](docs/LogsCreate.md)
 - [Metrics](docs/Metrics.md)
 - [NotificationGroupContact](docs/NotificationGroupContact.md)
 - [NotificationGroupCreate](docs/NotificationGroupCreate.md)
 - [NotificationGroupList](docs/NotificationGroupList.md)
 - [NotificationGroupUpdate](docs/NotificationGroupUpdate.md)
 - [OrganizationCreate](docs/OrganizationCreate.md)
 - [OrganizationDetail](docs/OrganizationDetail.md)
 - [OrganizationList](docs/OrganizationList.md)
 - [OrganizationUpdate](docs/OrganizationUpdate.md)
 - [OrganizationUserCreate](docs/OrganizationUserCreate.md)
 - [OrganizationUserDetail](docs/OrganizationUserDetail.md)
 - [OrganizationUserUpdate](docs/OrganizationUserUpdate.md)
 - [OutputFieldWidgetCreate](docs/OutputFieldWidgetCreate.md)
 - [PermissionList](docs/PermissionList.md)
 - [PipelineCreate](docs/PipelineCreate.md)
 - [PipelineCreateResponse](docs/PipelineCreateResponse.md)
 - [PipelineDetail](docs/PipelineDetail.md)
 - [PipelineInputFieldCreate](docs/PipelineInputFieldCreate.md)
 - [PipelineList](docs/PipelineList.md)
 - [PipelineOutputFieldCreate](docs/PipelineOutputFieldCreate.md)
 - [PipelineRequestBatchCreateResponse](docs/PipelineRequestBatchCreateResponse.md)
 - [PipelineRequestCreateResponse](docs/PipelineRequestCreateResponse.md)
 - [PipelineRequestDeploymentRequest](docs/PipelineRequestDeploymentRequest.md)
 - [PipelineRequestDetail](docs/PipelineRequestDetail.md)
 - [PipelineRequestList](docs/PipelineRequestList.md)
 - [PipelineRequestSingleDetail](docs/PipelineRequestSingleDetail.md)
 - [PipelineUpdate](docs/PipelineUpdate.md)
 - [PipelineVersionCreate](docs/PipelineVersionCreate.md)
 - [PipelineVersionDetail](docs/PipelineVersionDetail.md)
 - [PipelineVersionList](docs/PipelineVersionList.md)
 - [PipelineVersionObjectCreate](docs/PipelineVersionObjectCreate.md)
 - [PipelineVersionObjectList](docs/PipelineVersionObjectList.md)
 - [PipelineVersionUpdate](docs/PipelineVersionUpdate.md)
 - [ProjectCreate](docs/ProjectCreate.md)
 - [ProjectDetail](docs/ProjectDetail.md)
 - [ProjectList](docs/ProjectList.md)
 - [ProjectResourceUsage](docs/ProjectResourceUsage.md)
 - [ProjectUpdate](docs/ProjectUpdate.md)
 - [ProjectUserCreate](docs/ProjectUserCreate.md)
 - [ProjectUserList](docs/ProjectUserList.md)
 - [RequestsOverview](docs/RequestsOverview.md)
 - [ResourceUsage](docs/ResourceUsage.md)
 - [RevisionCreate](docs/RevisionCreate.md)
 - [RevisionList](docs/RevisionList.md)
 - [RoleAssignmentCreate](docs/RoleAssignmentCreate.md)
 - [RoleAssignmentList](docs/RoleAssignmentList.md)
 - [RoleCreate](docs/RoleCreate.md)
 - [RoleDetailList](docs/RoleDetailList.md)
 - [RoleList](docs/RoleList.md)
 - [RoleUpdate](docs/RoleUpdate.md)
 - [ScheduleCreate](docs/ScheduleCreate.md)
 - [ScheduleList](docs/ScheduleList.md)
 - [ScheduleUpdate](docs/ScheduleUpdate.md)
 - [ServiceUserCreate](docs/ServiceUserCreate.md)
 - [ServiceUserList](docs/ServiceUserList.md)
 - [ServiceUserTokenDetail](docs/ServiceUserTokenDetail.md)
 - [ServiceUserTokenList](docs/ServiceUserTokenList.md)
 - [Status](docs/Status.md)
 - [Usage](docs/Usage.md)
 - [UsageMetric](docs/UsageMetric.md)
 - [UserPendingCreate](docs/UserPendingCreate.md)
 - [UserPendingDetail](docs/UserPendingDetail.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header



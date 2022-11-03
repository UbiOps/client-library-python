# ubiops.CoreApi

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_deployment_requests_create**](CoreApi.md#batch_deployment_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/batch | Create a batch deployment request
[**batch_deployment_version_requests_create**](CoreApi.md#batch_deployment_version_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/batch | Create a batch deployment version request
[**batch_pipeline_requests_create**](CoreApi.md#batch_pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/batch | Create a batch pipeline request
[**batch_pipeline_version_requests_create**](CoreApi.md#batch_pipeline_version_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/batch | Create a batch pipeline version request
[**blobs_create**](CoreApi.md#blobs_create) | **POST** /projects/{project_name}/blobs | Upload a blob
[**blobs_delete**](CoreApi.md#blobs_delete) | **DELETE** /projects/{project_name}/blobs/{blob_id} | Delete a blob
[**blobs_get**](CoreApi.md#blobs_get) | **GET** /projects/{project_name}/blobs/{blob_id} | Get a blob
[**blobs_list**](CoreApi.md#blobs_list) | **GET** /projects/{project_name}/blobs | List blobs
[**blobs_update**](CoreApi.md#blobs_update) | **PUT** /projects/{project_name}/blobs/{blob_id} | Update a blob
[**buckets_create**](CoreApi.md#buckets_create) | **POST** /projects/{project_name}/buckets | Create bucket
[**buckets_delete**](CoreApi.md#buckets_delete) | **DELETE** /projects/{project_name}/buckets/{bucket_name} | Delete a bucket
[**buckets_get**](CoreApi.md#buckets_get) | **GET** /projects/{project_name}/buckets/{bucket_name} | Get details of a bucket
[**buckets_list**](CoreApi.md#buckets_list) | **GET** /projects/{project_name}/buckets | List buckets
[**buckets_update**](CoreApi.md#buckets_update) | **PATCH** /projects/{project_name}/buckets/{bucket_name} | Update a bucket
[**builds_get**](CoreApi.md#builds_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/builds/{build_id} | Get build
[**builds_list**](CoreApi.md#builds_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/builds | List builds
[**deployment_audit_events_list**](CoreApi.md#deployment_audit_events_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/audit | List audit events for a deployment
[**deployment_environment_variables_copy**](CoreApi.md#deployment_environment_variables_copy) | **POST** /projects/{project_name}/deployments/{deployment_name}/copy-environment-variables | Copy deployment environment variable
[**deployment_environment_variables_create**](CoreApi.md#deployment_environment_variables_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/environment-variables | Create deployment environment variable
[**deployment_environment_variables_delete**](CoreApi.md#deployment_environment_variables_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Delete deployment environment variable
[**deployment_environment_variables_get**](CoreApi.md#deployment_environment_variables_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Get deployment environment variable
[**deployment_environment_variables_list**](CoreApi.md#deployment_environment_variables_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/environment-variables | List deployment environment variables
[**deployment_environment_variables_update**](CoreApi.md#deployment_environment_variables_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Update deployment environment variable
[**deployment_requests_batch_delete**](CoreApi.md#deployment_requests_batch_delete) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/delete | Delete multiple deployment requests
[**deployment_requests_batch_get**](CoreApi.md#deployment_requests_batch_get) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/collect | Retrieve multiple deployment requests
[**deployment_requests_create**](CoreApi.md#deployment_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests | Create a direct deployment request
[**deployment_requests_delete**](CoreApi.md#deployment_requests_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Delete a deployment request
[**deployment_requests_get**](CoreApi.md#deployment_requests_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Get a deployment request
[**deployment_requests_list**](CoreApi.md#deployment_requests_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/requests | List deployment requests
[**deployment_requests_update**](CoreApi.md#deployment_requests_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Update a deployment request
[**deployment_version_environment_variables_copy**](CoreApi.md#deployment_version_environment_variables_copy) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/copy-environment-variables | Copy deployment version environment variable
[**deployment_version_environment_variables_create**](CoreApi.md#deployment_version_environment_variables_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables | Create deployment version environment variable
[**deployment_version_environment_variables_delete**](CoreApi.md#deployment_version_environment_variables_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Delete deployment version environment variable
[**deployment_version_environment_variables_get**](CoreApi.md#deployment_version_environment_variables_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Get deployment version environment variable
[**deployment_version_environment_variables_list**](CoreApi.md#deployment_version_environment_variables_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables | List deployment version environment variables
[**deployment_version_environment_variables_update**](CoreApi.md#deployment_version_environment_variables_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Update deployment version environment variable
[**deployment_version_requests_batch_delete**](CoreApi.md#deployment_version_requests_batch_delete) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/delete | Delete multiple deployment version requests
[**deployment_version_requests_batch_get**](CoreApi.md#deployment_version_requests_batch_get) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/collect | Retrieve multiple deployment version requests
[**deployment_version_requests_create**](CoreApi.md#deployment_version_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests | Create a direct deployment version request
[**deployment_version_requests_delete**](CoreApi.md#deployment_version_requests_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Delete a deployment version request
[**deployment_version_requests_get**](CoreApi.md#deployment_version_requests_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Get a deployment version request
[**deployment_version_requests_list**](CoreApi.md#deployment_version_requests_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests | List deployment version requests
[**deployment_version_requests_update**](CoreApi.md#deployment_version_requests_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Update a deployment version request
[**deployment_versions_create**](CoreApi.md#deployment_versions_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions | Create deployment versions
[**deployment_versions_delete**](CoreApi.md#deployment_versions_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Delete deployment version
[**deployment_versions_get**](CoreApi.md#deployment_versions_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Get deployment version
[**deployment_versions_list**](CoreApi.md#deployment_versions_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions | List deployment versions
[**deployment_versions_update**](CoreApi.md#deployment_versions_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Update deployment version
[**deployments_create**](CoreApi.md#deployments_create) | **POST** /projects/{project_name}/deployments | Create deployments
[**deployments_delete**](CoreApi.md#deployments_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name} | Delete a deployment
[**deployments_get**](CoreApi.md#deployments_get) | **GET** /projects/{project_name}/deployments/{deployment_name} | Get details of a deployment
[**deployments_list**](CoreApi.md#deployments_list) | **GET** /projects/{project_name}/deployments | List deployments
[**deployments_update**](CoreApi.md#deployments_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name} | Update a deployment
[**exports_create**](CoreApi.md#exports_create) | **POST** /projects/{project_name}/exports | Create an export
[**exports_delete**](CoreApi.md#exports_delete) | **DELETE** /projects/{project_name}/exports/{export_id} | Delete an export
[**exports_download**](CoreApi.md#exports_download) | **GET** /projects/{project_name}/exports/{export_id}/download | Download an export
[**exports_get**](CoreApi.md#exports_get) | **GET** /projects/{project_name}/exports/{export_id} | Get an export
[**exports_list**](CoreApi.md#exports_list) | **GET** /projects/{project_name}/exports | List exports
[**expressions_evaluate**](CoreApi.md#expressions_evaluate) | **POST** /expressions/evaluate | Evaluate expression
[**files_delete**](CoreApi.md#files_delete) | **DELETE** /projects/{project_name}/buckets/{bucket_name}/files/{file} | Delete a file
[**files_download**](CoreApi.md#files_download) | **GET** /projects/{project_name}/buckets/{bucket_name}/files/{file}/download | Download a file
[**files_get**](CoreApi.md#files_get) | **GET** /projects/{project_name}/buckets/{bucket_name}/files/{file} | Get a file
[**files_list**](CoreApi.md#files_list) | **GET** /projects/{project_name}/buckets/{bucket_name}/files | List files
[**files_upload**](CoreApi.md#files_upload) | **POST** /projects/{project_name}/buckets/{bucket_name}/files/{file} | Upload a file
[**imports_create**](CoreApi.md#imports_create) | **POST** /projects/{project_name}/imports | Create an import
[**imports_delete**](CoreApi.md#imports_delete) | **DELETE** /projects/{project_name}/imports/{import_id} | Delete an import
[**imports_download**](CoreApi.md#imports_download) | **GET** /projects/{project_name}/imports/{import_id}/download | Download an import
[**imports_get**](CoreApi.md#imports_get) | **GET** /projects/{project_name}/imports/{import_id} | Get an import
[**imports_list**](CoreApi.md#imports_list) | **GET** /projects/{project_name}/imports | List imports
[**imports_update**](CoreApi.md#imports_update) | **PATCH** /projects/{project_name}/imports/{import_id} | Confirm an import
[**instance_types_list**](CoreApi.md#instance_types_list) | **GET** /projects/{project_name}/instance-types | List instance types
[**metrics_get**](CoreApi.md#metrics_get) | **GET** /projects/{project_name}/metrics/{metric} | Get metrics
[**notification_groups_create**](CoreApi.md#notification_groups_create) | **POST** /projects/{project_name}/monitoring/notification-groups | Create notification groups
[**notification_groups_delete**](CoreApi.md#notification_groups_delete) | **DELETE** /projects/{project_name}/monitoring/notification-groups/{notification_group_name} | Delete notification group
[**notification_groups_get**](CoreApi.md#notification_groups_get) | **GET** /projects/{project_name}/monitoring/notification-groups/{notification_group_name} | Get notification group
[**notification_groups_list**](CoreApi.md#notification_groups_list) | **GET** /projects/{project_name}/monitoring/notification-groups | List notification groups
[**notification_groups_update**](CoreApi.md#notification_groups_update) | **PATCH** /projects/{project_name}/monitoring/notification-groups/{notification_group_name} | Update notification group
[**organization_users_create**](CoreApi.md#organization_users_create) | **POST** /organizations/{organization_name}/users | Add a user to an organization
[**organization_users_delete**](CoreApi.md#organization_users_delete) | **DELETE** /organizations/{organization_name}/users/{user_id} | Delete a user from an organization
[**organization_users_get**](CoreApi.md#organization_users_get) | **GET** /organizations/{organization_name}/users/{user_id} | Get details of a user in an organization
[**organization_users_list**](CoreApi.md#organization_users_list) | **GET** /organizations/{organization_name}/users | List the users in an organization
[**organization_users_update**](CoreApi.md#organization_users_update) | **PATCH** /organizations/{organization_name}/users/{user_id} | Update details of a user in an organization
[**organizations_create**](CoreApi.md#organizations_create) | **POST** /organizations | Create organizations
[**organizations_get**](CoreApi.md#organizations_get) | **GET** /organizations/{organization_name} | Get details of an organization
[**organizations_list**](CoreApi.md#organizations_list) | **GET** /organizations | List organizations
[**organizations_resource_usage**](CoreApi.md#organizations_resource_usage) | **GET** /organizations/{organization_name}/resources | Get resource usage
[**organizations_update**](CoreApi.md#organizations_update) | **PATCH** /organizations/{organization_name} | Update details of an organization
[**organizations_usage_get**](CoreApi.md#organizations_usage_get) | **GET** /organizations/{organization_name}/usage | Get organization usage
[**permissions_list**](CoreApi.md#permissions_list) | **GET** /permissions | List the available permissions
[**pipeline_audit_events_list**](CoreApi.md#pipeline_audit_events_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/audit | List audit events for a pipeline
[**pipeline_requests_batch_delete**](CoreApi.md#pipeline_requests_batch_delete) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/delete | Delete multiple pipeline requests
[**pipeline_requests_batch_get**](CoreApi.md#pipeline_requests_batch_get) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/collect | Retrieve multiple pipeline requests
[**pipeline_requests_create**](CoreApi.md#pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests | Create a pipeline request
[**pipeline_requests_delete**](CoreApi.md#pipeline_requests_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/requests/{request_id} | Delete a pipeline request
[**pipeline_requests_get**](CoreApi.md#pipeline_requests_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/requests/{request_id} | Get a pipeline request
[**pipeline_requests_list**](CoreApi.md#pipeline_requests_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/requests | List pipeline requests
[**pipeline_version_object_environment_variables_list**](CoreApi.md#pipeline_version_object_environment_variables_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/objects/{name}/environment-variables | List pipeline object environment variables
[**pipeline_version_requests_batch_delete**](CoreApi.md#pipeline_version_requests_batch_delete) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/delete | Delete multiple pipeline version requests
[**pipeline_version_requests_batch_get**](CoreApi.md#pipeline_version_requests_batch_get) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/collect | Retrieve multiple pipeline version requests
[**pipeline_version_requests_create**](CoreApi.md#pipeline_version_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests | Create a pipeline version request
[**pipeline_version_requests_delete**](CoreApi.md#pipeline_version_requests_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/{request_id} | Delete a pipeline version request
[**pipeline_version_requests_get**](CoreApi.md#pipeline_version_requests_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/{request_id} | Get a pipeline version request
[**pipeline_version_requests_list**](CoreApi.md#pipeline_version_requests_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests | List pipeline version requests
[**pipeline_versions_create**](CoreApi.md#pipeline_versions_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions | Create pipeline versions
[**pipeline_versions_delete**](CoreApi.md#pipeline_versions_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Delete pipeline version
[**pipeline_versions_get**](CoreApi.md#pipeline_versions_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Get pipeline version
[**pipeline_versions_list**](CoreApi.md#pipeline_versions_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions | List pipeline versions
[**pipeline_versions_update**](CoreApi.md#pipeline_versions_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Update pipeline version
[**pipelines_create**](CoreApi.md#pipelines_create) | **POST** /projects/{project_name}/pipelines | Create pipelines
[**pipelines_delete**](CoreApi.md#pipelines_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name} | Delete a pipeline
[**pipelines_get**](CoreApi.md#pipelines_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name} | Get details of a pipeline
[**pipelines_list**](CoreApi.md#pipelines_list) | **GET** /projects/{project_name}/pipelines | List pipelines
[**pipelines_update**](CoreApi.md#pipelines_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name} | Update a pipeline
[**project_audit_events_list**](CoreApi.md#project_audit_events_list) | **GET** /projects/{project_name}/audit | List audit events in a project
[**project_environment_variables_create**](CoreApi.md#project_environment_variables_create) | **POST** /projects/{project_name}/environment-variables | Create project environment variable
[**project_environment_variables_delete**](CoreApi.md#project_environment_variables_delete) | **DELETE** /projects/{project_name}/environment-variables/{id} | Delete project environment variable
[**project_environment_variables_get**](CoreApi.md#project_environment_variables_get) | **GET** /projects/{project_name}/environment-variables/{id} | Get project environment variable
[**project_environment_variables_list**](CoreApi.md#project_environment_variables_list) | **GET** /projects/{project_name}/environment-variables | List project environment variables
[**project_environment_variables_update**](CoreApi.md#project_environment_variables_update) | **PATCH** /projects/{project_name}/environment-variables/{id} | Update project environment variable
[**project_requests_list**](CoreApi.md#project_requests_list) | **GET** /projects/{project_name}/requests | List requests in project
[**project_users_create**](CoreApi.md#project_users_create) | **POST** /projects/{project_name}/users | Add user to a project
[**project_users_delete**](CoreApi.md#project_users_delete) | **DELETE** /projects/{project_name}/users/{user_id} | Delete user from a project
[**project_users_get**](CoreApi.md#project_users_get) | **GET** /projects/{project_name}/users/{user_id} | Get user in a project
[**project_users_list**](CoreApi.md#project_users_list) | **GET** /projects/{project_name}/users | List users in a project
[**projects_create**](CoreApi.md#projects_create) | **POST** /projects | Create projects
[**projects_delete**](CoreApi.md#projects_delete) | **DELETE** /projects/{project_name} | Delete a project
[**projects_get**](CoreApi.md#projects_get) | **GET** /projects/{project_name} | Get details of a project
[**projects_list**](CoreApi.md#projects_list) | **GET** /projects | List projects
[**projects_log_list**](CoreApi.md#projects_log_list) | **POST** /projects/{project_name}/logs | List logs for a project
[**projects_resource_usage**](CoreApi.md#projects_resource_usage) | **GET** /projects/{project_name}/resources | List resource usage of a project
[**projects_update**](CoreApi.md#projects_update) | **PATCH** /projects/{project_name} | Update a project
[**projects_usage_get**](CoreApi.md#projects_usage_get) | **GET** /projects/{project_name}/usage | Get resource usage
[**request_schedules_create**](CoreApi.md#request_schedules_create) | **POST** /projects/{project_name}/schedules | Create request schedules
[**request_schedules_delete**](CoreApi.md#request_schedules_delete) | **DELETE** /projects/{project_name}/schedules/{schedule_name} | Delete a request schedule
[**request_schedules_get**](CoreApi.md#request_schedules_get) | **GET** /projects/{project_name}/schedules/{schedule_name} | Get details of a request schedule
[**request_schedules_list**](CoreApi.md#request_schedules_list) | **GET** /projects/{project_name}/schedules | List request schedules
[**request_schedules_update**](CoreApi.md#request_schedules_update) | **PATCH** /projects/{project_name}/schedules/{schedule_name} | Update a request schedule
[**revisions_file_download**](CoreApi.md#revisions_file_download) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions/{revision_id}/download | Download deployment file
[**revisions_file_upload**](CoreApi.md#revisions_file_upload) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions | Upload deployment file
[**revisions_get**](CoreApi.md#revisions_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions/{revision_id} | Get revision
[**revisions_list**](CoreApi.md#revisions_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions | List revisions
[**role_assignments_create**](CoreApi.md#role_assignments_create) | **POST** /projects/{project_name}/role-assignments | Assign role to user/object
[**role_assignments_delete**](CoreApi.md#role_assignments_delete) | **DELETE** /projects/{project_name}/role-assignments/{id} | Delete role of user
[**role_assignments_get**](CoreApi.md#role_assignments_get) | **GET** /projects/{project_name}/role-assignments/{id} | Get role assignment
[**role_assignments_per_object_list**](CoreApi.md#role_assignments_per_object_list) | **GET** /projects/{project_name}/role-assignments | List roles on object/user
[**roles_create**](CoreApi.md#roles_create) | **POST** /projects/{project_name}/roles | Create a custom role scoped in a project
[**roles_delete**](CoreApi.md#roles_delete) | **DELETE** /projects/{project_name}/roles/{role_name} | Delete a role from a project
[**roles_get**](CoreApi.md#roles_get) | **GET** /projects/{project_name}/roles/{role_name} | Get details of a role
[**roles_list**](CoreApi.md#roles_list) | **GET** /projects/{project_name}/roles | List the available roles in a project
[**roles_update**](CoreApi.md#roles_update) | **PATCH** /projects/{project_name}/roles/{role_name} | Update a role in a project
[**service_status**](CoreApi.md#service_status) | **GET** /status | Service status
[**service_users_create**](CoreApi.md#service_users_create) | **POST** /projects/{project_name}/service-users | Create a new service user
[**service_users_delete**](CoreApi.md#service_users_delete) | **DELETE** /projects/{project_name}/service-users/{service_user_id} | Delete service user
[**service_users_get**](CoreApi.md#service_users_get) | **GET** /projects/{project_name}/service-users/{service_user_id} | Retrieve details of a service user
[**service_users_list**](CoreApi.md#service_users_list) | **GET** /projects/{project_name}/service-users | List service users
[**service_users_token**](CoreApi.md#service_users_token) | **PUT** /projects/{project_name}/service-users/{service_user_id}/token | Reset the token of a service user
[**service_users_update**](CoreApi.md#service_users_update) | **PATCH** /projects/{project_name}/service-users/{service_user_id} | Update service user details
[**user_create**](CoreApi.md#user_create) | **POST** /user | Create a new user
[**user_delete**](CoreApi.md#user_delete) | **DELETE** /user | Delete user


# **batch_deployment_requests_create**
> list[DeploymentRequestBatchCreateResponse] batch_deployment_requests_create(project_name, deployment_name, data, timeout=timeout, notification_group=notification_group)

Create a batch deployment request

## Description
Request multiple predictions from the default version of a deployment. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the deployment request collect methods.

If one of the requests is faulty, all requests are denied. The maximum number of requests per batch call is 250.

### Required Parameters
In case of structured input deployment: A list of dictionaries, where each dictionary contains the input fields of the deployment as keys. It is also possible to send a single dictionary as input.
In case of plain input deployment: A list of strings. It is also possible to send a single string as input.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the batch deployment request in seconds. The maximum allowed value is 172800 (48 hours) and the default value is 14400 (4 hours).
- `notification_group`: Name of a notification group to send notifications (e.g., emails) when the request is completed

## Request Examples
Multiple structured batch deployment requests

```
[
  {
    "input-field-1": 5.0,
    "input-field-2": "N",
    "input-field-3": [0.25, 0.25, 2.1, 16.3]
  },
  {
    "input-field-1": 3.0,
    "input-field-2": "S",
    "input-field-3": [4.23, 3.27, 2.41, 12.4]
  }
]
```

Multiple plain batch deployment requests

```
[
  "plain-data-goes-here", "plain-example-data"
]
```

### Response Structure
A list of dictionaries containing the details of the created deployment requests with the following fields:

- `id`: Unique identifier for the deployment request, which can be used to collect the result
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `time_created`: Server time that the request was made (current time)

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
data = [{'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'}] # list[str or dict()] 
timeout = 56 # int  (optional)
notification_group = 'notification_group_example' # str  (optional)

# Create a batch deployment request
api_response = api_instance.batch_deployment_requests_create(project_name, deployment_name, data, timeout=timeout, notification_group=notification_group)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **data** | **list[str or dict()]** | 
 **timeout** | **int** | [optional] 
 **notification_group** | **str** | [optional] 

### Return type

[**list[DeploymentRequestBatchCreateResponse]**](DeploymentRequestBatchCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **batch_deployment_version_requests_create**
> list[DeploymentRequestBatchCreateResponse] batch_deployment_version_requests_create(project_name, deployment_name, version, data, timeout=timeout, notification_group=notification_group)

Create a batch deployment version request

## Description
Request multiple predictions from a deployment version. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the deployment request collect methods. It is only possible to make a request if a deployment file is uploaded for that version and the deployment build has succeeded (meaning that the version is in available state).

If one of the requests is faulty, all requests are denied. The maximum number of requests per batch call is 250.

### Required Parameters
In case of structured input deployment: A list of dictionaries, where each dictionary contains the input fields of the deployment as keys. It is also possible to send a single dictionary as input.
In case of plain input deployment: A list of strings. It is also possible to send a single string as input.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the batch deployment request in seconds. The maximum allowed value is 172800 (48 hours) and the default value is 14400 (4 hours).
- `notification_group`: Name of a notification group to send notifications (e.g., emails) when the request is completed

## Request Examples
Multiple structured batch deployment requests

```
[
  {
    "input-field-1": 5.0,
    "input-field-2": "N",
    "input-field-3": [0.25, 0.25, 2.1, 16.3]
  },
  {
    "input-field-1": 3.0,
    "input-field-2": "S",
    "input-field-3": [4.23, 3.27, 2.41, 12.4]
  }
]
```

Multiple plain batch deployment requests

```
[
  "plain-data-goes-here", "plain-example-data"
]
```

### Response Structure
A list of dictionaries containing the details of the created deployment requests with the following fields:

- `id`: Unique identifier for the deployment request, which can be used to collect the result
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `time_created`: Server time that the request was made (current time)

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
version = 'version_example' # str 
data = [{'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'}] # list[str or dict()] 
timeout = 56 # int  (optional)
notification_group = 'notification_group_example' # str  (optional)

# Create a batch deployment version request
api_response = api_instance.batch_deployment_version_requests_create(project_name, deployment_name, version, data, timeout=timeout, notification_group=notification_group)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 
 **data** | **list[str or dict()]** | 
 **timeout** | **int** | [optional] 
 **notification_group** | **str** | [optional] 

### Return type

[**list[DeploymentRequestBatchCreateResponse]**](DeploymentRequestBatchCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **batch_pipeline_requests_create**
> list[PipelineRequestBatchCreateResponse] batch_pipeline_requests_create(project_name, pipeline_name, data, timeout=timeout, notification_group=notification_group)

Create a batch pipeline request

## Description
Make a batch request to the default version of a pipeline. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the pipeline request collect methods.

The maximum number of requests that can be created per batch is 100.

### Required Parameters
In case of structured input pipeline: A list of dictionaries, where each dictionary contains the input fields of the pipeline as keys. It is also possible to send a single dictionary as input.
In case of plain input pipeline: A list of strings. It is also possible to send a single string as input.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the entire pipeline request in seconds. The maximum allowed value is 172800 (48 hours) and the default value is 14400 (4 hours).
The deployment request timeouts default to 14400 seconds for deployments in the pipeline.
- `notification_group`: Name of a notification group to send notifications (e.g., emails) when the request is completed

## Request Examples
Multiple structured batch pipeline requests

```
[
  {
    "pipeline-input-field-1": 5.0,
    "pipeline-input-field-2": "N",
    "pipeline-input-field-3": [0.25, 0.25, 2.1, 16.3]
  },
  {
    "pipeline-input-field-1": 3.0,
    "pipeline-input-field-2": "S",
    "pipeline-input-field-3": [4.23, 3.27, 2.41, 12.4]
  }
]
```

Multiple plain batch pipeline requests

```
[
  "plain-data-goes-here", "plain-example-data"
]
```

### Response Structure
A list of dictionaries containing the details of the created pipeline requests with the following fields:

- `id`: Unique identifier for the pipeline request, which can be used to collect the result
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request is made
- `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
- `time_created`: Server time that the request was made (current time)

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
data = [{'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'}] # list[str or dict()] 
timeout = 56 # int  (optional)
notification_group = 'notification_group_example' # str  (optional)

# Create a batch pipeline request
api_response = api_instance.batch_pipeline_requests_create(project_name, pipeline_name, data, timeout=timeout, notification_group=notification_group)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **data** | **list[str or dict()]** | 
 **timeout** | **int** | [optional] 
 **notification_group** | **str** | [optional] 

### Return type

[**list[PipelineRequestBatchCreateResponse]**](PipelineRequestBatchCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **batch_pipeline_version_requests_create**
> list[PipelineRequestBatchCreateResponse] batch_pipeline_version_requests_create(project_name, pipeline_name, version, data, timeout=timeout, notification_group=notification_group)

Create a batch pipeline version request

## Description
Make a batch request to a pipeline version. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the pipeline version request collect methods.

The maximum number of requests that can be created per batch is 100.

### Required Parameters
In case of structured input pipeline: A list of dictionaries, where each dictionary contains the input fields of the pipeline as keys. It is also possible to send a single dictionary as input.
In case of plain input pipeline: A list of strings. It is also possible to send a single string as input.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the entire pipeline request in seconds. The maximum allowed value is 172800 (48 hours) and the default value is 14400 (4 hours).
The deployment request timeouts default to 14400 seconds for deployments in the pipeline.
- `notification_group`: Name of a notification group to send notifications (e.g., emails) when the request is completed

## Request Examples
Multiple structured batch pipeline requests

```
[
  {
    "pipeline-input-field-1": 5.0,
    "pipeline-input-field-2": "N",
    "pipeline-input-field-3": [0.25, 0.25, 2.1, 16.3]
  },
  {
    "pipeline-input-field-1": 3.0,
    "pipeline-input-field-2": "S",
    "pipeline-input-field-3": [4.23, 3.27, 2.41, 12.4]
  }
]
```

Multiple plain batch pipeline requests

```
[
  "plain-data-goes-here", "plain-example-data"
]
```

### Response Structure
A list of dictionaries containing the details of the created pipeline version requests with the following fields:

- `id`: Unique identifier for the pipeline version request, which can be used to collect the result
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request is made
- `status`: Status of the request. Always 'pending' when initialised, later it can be 'processing', 'failed' or 'completed'.
- `time_created`: Server time that the request was made (current time)

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "time_created": "2020-03-28T20:00:26.613+00:00"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
version = 'version_example' # str 
data = [{'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'}] # list[str or dict()] 
timeout = 56 # int  (optional)
notification_group = 'notification_group_example' # str  (optional)

# Create a batch pipeline version request
api_response = api_instance.batch_pipeline_version_requests_create(project_name, pipeline_name, version, data, timeout=timeout, notification_group=notification_group)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 
 **data** | **list[str or dict()]** | 
 **timeout** | **int** | [optional] 
 **notification_group** | **str** | [optional] 

### Return type

[**list[PipelineRequestBatchCreateResponse]**](PipelineRequestBatchCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

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
- `creation_date`: Time the blob was created
- `last_updated`: Time the blob was last updated
- `filename`: Original filename of the blob
- `size`: Size of the uploaded blob in bytes
- `ttl`: Time to live of the blob in seconds

## Response Examples

```
{{
  "id": "b58fb853-9311-4583-9688-abed61830abc",
  "creation_date": "2020-05-18T11:26:57.904+00:00",
  "last_updated": "2020-05-18T11:26:57.904+00:00",
  "filename": "original-filename.jpg",
  "size": 3439,
  "ttl": 86400
}}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
file = '/path/to/file' # file 
blob_ttl = 56 # int  (optional)

# Upload a blob
api_response = api_instance.blobs_create(project_name, file, blob_ttl=blob_ttl)
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

[**BlobList**](BlobList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **blobs_delete**
> blobs_delete(project_name, blob_id)

Delete a blob

## Description
Delete a blob from a project

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
blob_id = 'blob_id_example' # str 

# Delete a blob
api_instance.blobs_delete(project_name, blob_id)

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

project_name = 'project_name_example' # str 
blob_id = 'blob_id_example' # str 

# Get a blob
with api_instance.blobs_get(project_name, blob_id) as response:
    filename = response.getfilename()
    content = response.read()

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
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "last_updated": "2020-05-18T11:26:57.904+00:00",
    "filename": "original-filename.jpg",
    "size": 562,
    "ttl": 12338
  },
  {
    "id": "f629a052-a827-44d9-97cf-3902504edc79",
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "last_updated": "2020-05-18T11:26:57.904+00:00",
    "filename": "original-filename2.jpg",
    "size": 3439,
    "ttl": 86400
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
range = 56 # int  (optional)
creation_date = 'creation_date_example' # str  (optional)

# List blobs
api_response = api_instance.blobs_list(project_name, range=range, creation_date=creation_date)
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

[**list[BlobList]**](BlobList.md)

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
- `creation_date`: Time the blob was created
- `last_updated`: Time the blob was last updated
- `filename`: Original filename of the blob
- `size`: Size of the uploaded blob in bytes
- `ttl`: Time to live of the blob in seconds

## Response Examples

```
{{
  "id": "b58fb853-9311-4583-9688-abed61830abc",
  "creation_date": "2020-05-18T11:26:57.904+00:00",
  "last_updated": "2020-05-18T11:26:57.904+00:00",
  "filename": "original-filename.jpg",
  "size": 3439,
  "ttl": 86400
}}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
blob_id = 'blob_id_example' # str 
file = '/path/to/file' # file 
blob_ttl = 56 # int  (optional)

# Update a blob
api_response = api_instance.blobs_update(project_name, blob_id, file, blob_ttl=blob_ttl)
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

[**BlobList**](BlobList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

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
  - For Amazon S3, provide the fields `region`, `bucket` and `prefix`.
  - For Azure Blob Storage, provide the fields `container` and `prefix`.
  - For Google Cloud Storage, provide the fields `bucket` and `prefix`.
  UbiOps always makes sure that the prefix ends with a '/'.
- `description`: Description of the bucket
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `ttl`: Time to live for the files in the bucket. It must be a multiple of 604800 (1 week).

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

project_name = 'project_name_example' # str 
data = ubiops.BucketCreate() # BucketCreate 

# Create bucket
api_response = api_instance.buckets_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**BucketCreate**](BucketCreate.md) | 

### Return type

[**BucketList**](BucketList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **buckets_delete**
> buckets_delete(project_name, bucket_name)

Delete a bucket

## Description
Delete a bucket. If the bucket provider is UbiOps, the files in the bucket will be deleted together with the bucket. For other providers, the files in the bucket are not removed but just the connection from UbiOps to the bucket.

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
bucket_name = 'bucket_name_example' # str 

# Delete a bucket
api_instance.buckets_delete(project_name, bucket_name)

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

project_name = 'project_name_example' # str 
bucket_name = 'bucket_name_example' # str 

# Get details of a bucket
api_response = api_instance.buckets_get(project_name, bucket_name)
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

[**BucketDetail**](BucketDetail.md)

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

project_name = 'project_name_example' # str 
labels = 'labels_example' # str  (optional)

# List buckets
api_response = api_instance.buckets_list(project_name, labels=labels)
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

[**list[BucketList]**](BucketList.md)

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

project_name = 'project_name_example' # str 
bucket_name = 'bucket_name_example' # str 
data = ubiops.BucketUpdate() # BucketUpdate 

# Update a bucket
api_response = api_instance.buckets_update(project_name, bucket_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **bucket_name** | **str** | 
 **data** | [**BucketUpdate**](BucketUpdate.md) | 

### Return type

[**BucketDetail**](BucketDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **builds_get**
> BuildList builds_get(project_name, build_id, deployment_name, version)

Get build

## Description
Retrieve details of a single build of a version

### Response Structure
A dictionary containing details of the build

- `id`: Unique identifier for the build (UUID)
- `revision`: UUID of the revision to which the build is linked
- `creation_date`: The date when the build was created
- `status`: Status of the build. Can be 'queued', 'building', 'validating', 'success' or 'failed'.
- `error_message`: Error message which explains why the build has failed. It is empty if the build is successful.
- `trigger`: Action that triggered the build
- `has_request_method`: Whether the build has a 'request' method
- `has_requests_method`: Whether the build has a 'requests' method

## Response Examples

```
{
  "id": "49d857fd-39ca-48db-9547-0d5d1a91b62d",
  "revision": "7ead8a18-c1d2-4751-80d2-d8e0e0e2fed6",
  "creation_date": "2020-12-23T16:15:11.200+00:00",
  "status": "building",
  "error_message": "",
  "trigger": "Deployment file upload",
  "has_request_method": true,
  "has_requests_method": false
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
build_id = 'build_id_example' # str 
deployment_name = 'deployment_name_example' # str 
version = 'version_example' # str 

# Get build
api_response = api_instance.builds_get(project_name, build_id, deployment_name, version)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **build_id** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 

### Return type

[**BuildList**](BuildList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **builds_list**
> list[BuildList] builds_list(project_name, deployment_name, version)

List builds

## Description
List all builds associated with a version. A build is triggered when a new deployment file is uploaded.

### Response Structure
A list of details of the builds

- `id`: Unique identifier for the build (UUID)
- `revision`: UUID of the revision to which the build is linked
- `creation_date`: The date when the build was created
- `status`: Status of the build. Can be 'queued', 'building', 'validating', 'success' or 'failed'.
- `error_message`: Error message which explains why the build has failed. It is empty if the build is successful.
- `trigger`: Action that triggered the build
- `has_request_method`: Whether the build has a 'request' method
- `has_requests_method`: Whether the build has a 'requests' method

## Response Examples

```
[
  {
    "id": "49d857fd-39ca-48db-9547-0d5d1a91b62d",
    "revision": "7ead8a18-c1d2-4751-80d2-d8e0e0e2fed6",
    "creation_date": "2020-12-23T16:15:11.200+00:00",
    "status": "failed",
    "error_message": "Could not find the deployment file",
    "trigger": "Deployment file upload",
    "has_request_method": true,
    "has_requests_method": false
  },
  {
    "id": "baf88570-d884-4bc6-9308-01068b051f5f",
    "revision": "a009d7c9-67e4-4d3c-89fd-d3c8b07c7242",
    "creation_date": "2020-12-23T16:35:13.088+00:00",
    "status": "queued",
    "error_message": "",
    "trigger": "Deployment file upload",
    "has_request_method": true,
    "has_requests_method": false
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
version = 'version_example' # str 

# List builds
api_response = api_instance.builds_list(project_name, deployment_name, version)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 

### Return type

[**list[BuildList]**](BuildList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_audit_events_list**
> list[AuditList] deployment_audit_events_list(project_name, deployment_name, action=action, limit=limit, offset=offset)

List audit events for a deployment

## Description
List all audit events for a deployment including versions

### Optional Parameters
The following parameters should be given as query parameters:

- `action`: Type of action. It can be one of: create, update, delete, info.
- `limit`: The maximum number of audit events given back, default is 50
- `offset`: The number which forms the starting point of the audit events given back. If offset equals 2, then the first 2 events will be omitted from the list.

### Response Structure
A list of details of the audit events for a deployment

- `id`: Unique identifier for the audit event (UUID)
- `date`: The date when the action was performed
- `action`: Type of action. It can be one of: create, update, delete, info. *info* action denotes that the action does not fall into create, update or delete categories.
- `user`: Email of the user who performed the action
- `event`: Description of the event
- `object_type`: Type of the object on which the action was performed
- `object_name`: Name of the object on which the action was performed. If the object is deleted at the time of listing audit events, this field is empty.

## Response Examples

```
[
  {
    "id": "25750859-e082-44df-bde9-cd85ca3f869c",
    "date": "2020-10-23T12:03:55.675+00:00",
    "action": "delete",
    "user": "user@example.com",
    "event": "Deleted environment variable ENV_VAR for deployment deployment-1",
    "object_type": "deployment",
    "object_name": "deployment-1"
  },
  {
    "id": "ce81814d-b00c-4094-a483-814afdb80875",
    "date": "2020-10-23T12:04:28.645+00:00",
    "action": "create",
    "user": "user@example.com",
    "event": "Created version v1 for deployment deployment-1",
    "object_type": "deployment",
    "object_name": "audit-deployment"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
action = 'action_example' # str  (optional)
limit = 56 # int  (optional)
offset = 56 # int  (optional)

# List audit events for a deployment
api_response = api_instance.deployment_audit_events_list(project_name, deployment_name, action=action, limit=limit, offset=offset)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **action** | **str** | [optional] 
 **limit** | **int** | [optional] 
 **offset** | **int** | [optional] 

### Return type

[**list[AuditList]**](AuditList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_environment_variables_copy**
> list[InheritedEnvironmentVariableList] deployment_environment_variables_copy(project_name, deployment_name, data)

Copy deployment environment variable

## Description
Copy existing environment variables from a source object to the deployment. Variables of the deployment with the same name as ones from the source object will be overwritten with the new value. Only the copied variables are returned.

### Required Parameters

- `source_deployment`: The name of the deployment from which the variables will be copied

### Optional Parameters

- `source_version`: The version of the deployment from which the variables will be copied

## Request Examples
Copy the environment variables from a deployment

```
{
  "source_deployment": "example-deployment"
}
```

Copy the environment variables from a version

```
{
  "source_deployment": "example-deployment",
  "source_version": "v1"
}
```

### Response Structure
A list of the copied variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from. Will be null for copied environment variables.
- `inheritance_name`: Name of the parent object that this variable is inherited from. Will be null for copied environment variables.

## Response Examples

```
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "deployment_specific_variable",
    "value": "some_value",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": null,
    "inheritance_name": null
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
data = ubiops.EnvironmentVariableCopy() # EnvironmentVariableCopy 

# Copy deployment environment variable
api_response = api_instance.deployment_environment_variables_copy(project_name, deployment_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **data** | [**EnvironmentVariableCopy**](EnvironmentVariableCopy.md) | 

### Return type

[**list[InheritedEnvironmentVariableList]**](InheritedEnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_environment_variables_create**
> EnvironmentVariableList deployment_environment_variables_create(project_name, deployment_name, data)

Create deployment environment variable

## Description
Create an environment variable for the deployment. This variable will be inherited by all versions of this deployment. Variables inherited from the project can be shadowed by creating a variable with the same name.

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users.

## Request Examples

```
{
  "name": "deployment_variable_a",
  "value": "some_value",
  "secret": false
}
```

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

```
{
"id": "7c28a2be-507e-4fae-981d-54e94f22dab0",
"name": "deployment_variable_a",
"value": "some_value",
"secret": false
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate 

# Create deployment environment variable
api_response = api_instance.deployment_environment_variables_create(project_name, deployment_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md) | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_environment_variables_delete**
> deployment_environment_variables_delete(project_name, deployment_name, id)

Delete deployment environment variable

## Description
Delete an environment variable of the deployment

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
id = 'id_example' # str 

# Delete deployment environment variable
api_instance.deployment_environment_variables_delete(project_name, deployment_name, id)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_environment_variables_get**
> EnvironmentVariableList deployment_environment_variables_get(project_name, deployment_name, id)

Get deployment environment variable

## Description
Retrieve details of a deployment environment variable. This cannot be used to retrieve details of inherited variables.

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
id = 'id_example' # str 

# Get deployment environment variable
api_response = api_instance.deployment_environment_variables_get(project_name, deployment_name, id)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **id** | **str** | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_environment_variables_list**
> list[InheritedEnvironmentVariableList] deployment_environment_variables_list(project_name, deployment_name)

List deployment environment variables

## Description
List the environment variables defined for the deployment. Includes environment variables defined at project level.

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from - can be `project` or null if the variable was defined for the deployment directly
- `inheritance_name`: Name of the parent object that this variable is inherited from - will be null if the variable was defined for the deployment directly

## Response Examples

```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": "project",
    "inheritance_name": "project_name"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 

# List deployment environment variables
api_response = api_instance.deployment_environment_variables_list(project_name, deployment_name)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 

### Return type

[**list[InheritedEnvironmentVariableList]**](InheritedEnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_environment_variables_update**
> EnvironmentVariableList deployment_environment_variables_update(project_name, deployment_name, id, data)

Update deployment environment variable

## Description
Update an environment variable for the deployment. This cannot be used to update inherited variables; to change an inherited variable for a specific deployment you can create a variable with the same name for the deployment.

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users. Can be updated from false to true, but not from true to false (i.e. secrets will stay secrets).

## Request Examples

```
{
  "name": "deployment_variable_a",
  "value": "some new value",
  "secret": false
}
```

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

```
{
  "id": "7c28a2be-507e-4fae-981d-54e94f22dab0",
  "name": "deployment_variable_a",
  "value": "some new value",
  "secret": false
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
id = 'id_example' # str 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate 

# Update deployment environment variable
api_response = api_instance.deployment_environment_variables_update(project_name, deployment_name, id, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **id** | **str** | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md) | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_requests_batch_delete**
> object deployment_requests_batch_delete(project_name, deployment_name, data)

Delete multiple deployment requests

## Description
Delete multiple deployment requests for the default version of a deployment. If one of the given deployment requests does not exist, an error message is given and no request is deleted. A maximum of 250 deployment requests can be deleted with this method.

### Required Parameters
A list of ids for the requests

## Request Examples

```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
data = ['request_id_1', 'request_id_2'] # list[str] 

# Delete multiple deployment requests
api_response = api_instance.deployment_requests_batch_delete(project_name, deployment_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **data** | **list[str]** | 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_requests_batch_get**
> list[DeploymentRequestBatchDetail] deployment_requests_batch_get(project_name, deployment_name, data)

Retrieve multiple deployment requests

## Description
Retrieve multiple deployment requests for the default version of a deployment. If one of the given deployment requests does not exist, an error message is given and no request is returned. A maximum of 250 deployment requests can be retrieved with this method. The deployment requests are NOT returned in the order they are given in.

### Required Parameters
A list of ids for the requests

## Request Examples

```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```

### Response Structure
A list of dictionaries containing the details of the retrieved deployment requests with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request. Can be 'pending', 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `success`: A boolean value that indicates whether the deployment request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed
- `request_data`: A dictionary containing the data that was sent when the request was created
- `result`: Deployment request result value. NULL if the request is 'pending', 'processing' or 'failed'.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.

## Response Examples

```
[
  {
    "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-29T08:09:10.729+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {
      "input": 82.2
    },
    "result": null,
    "error_message": null
  },
  {
    "id": "85711124-54db-4794-b83d-24492247c6e1",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-06-25T09:37:17.765+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {
      "input": 52.4
    },
    "result": null,
    "error_message": null
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
data = ['request_id_1', 'request_id_2'] # list[str] 

# Retrieve multiple deployment requests
api_response = api_instance.deployment_requests_batch_get(project_name, deployment_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **data** | **list[str]** | 

### Return type

[**list[DeploymentRequestBatchDetail]**](DeploymentRequestBatchDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_requests_create**
> DeploymentRequestCreateResponse deployment_requests_create(project_name, deployment_name, data, timeout=timeout)

Create a direct deployment request

## Description
Request a prediction from a deployment. Deployment requests are made for the default version of a deployment.
When using the 'requests' function of a deployment a list should be provided as input, see the example below.

### Required Parameters
The input for the request. In case of a structured deployment, this is a dictionary which contains the input fields of the deployment as keys. In case of a plain deployment, give a string or list of strings.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the deployment request in seconds. The maximum allowed value is 3600 (1 hour) and the default value is 300 (5 minutes).

## Request Examples
A structured deployment request

```
{
  "input-field-1": 5.0,
  "input-field-2": "N",
  "input-field-3": [0.25, 0.25, 2.1, 16.3]
}
```

A structured deployment request with a file field

```
{
  "input-field-1": 5.0,
  "file-input-field": "ubiops-file://my-bucket/file-1.jpg"
}
```

A plain deployment request

```
"example-plain-data"
```

Multiple structured deployment requests using the 'requests' function of a deployment
```
[
    {
        "input-field-1": 5.0
    },
    {
        "input-field-1": 10.0
    }
]
```

### Response Structure
Details of the created deployment request

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `success`: A boolean value that indicates whether the deployment request was successful
- `result`: Deployment request result value. NULL if the request failed.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.

## Response Examples
A failed deployment request

```
{
  "id": "85ae32a7-fe3a-4a55-be27-9db88ae68501",
  "deployment": "deployment-1",
  "version": "v1",
  "success": false,
  "result": None,
  "error_message": "Asset ID not supported"
}
```

A successful deployment request

```
{
  "id": "ffce45da-1562-419a-89a0-0a0837e55392",
  "deployment": "deployment-1",
  "version": "v2",
  "success": true,
  "result": {
    "output-field-1": "2.1369",
    "output-field-2": "5.5832",
  },
  "error_message": null
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
data = {'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'} # str or dict() 
timeout = 56 # int  (optional)

# Create a direct deployment request
api_response = api_instance.deployment_requests_create(project_name, deployment_name, data, timeout=timeout)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **data** | **str or dict()** | 
 **timeout** | **int** | [optional] 

### Return type

[**DeploymentRequestCreateResponse**](DeploymentRequestCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_requests_delete**
> deployment_requests_delete(project_name, deployment_name, request_id)

Delete a deployment request

## Description
Delete a deployment request for the default version of a deployment

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
request_id = 'request_id_example' # str 

# Delete a deployment request
api_instance.deployment_requests_delete(project_name, deployment_name, request_id)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **request_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_requests_get**
> DeploymentRequestSingleDetail deployment_requests_get(project_name, deployment_name, request_id, metadata_only=metadata_only)

Get a deployment request

## Description
Get a request of the default version of a deployment. With this method, the result of a request may be retrieved.

### Optional Parameters
The following parameters should be given as query parameters:

- `metadata_only`: A boolean value that indicates whether the response should include the request data and result. The default value is False.

### Response Structure
A dictionary containing the details of the deployment request with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request. Can be 'pending', 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `success`: A boolean value that indicates whether the deployment request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed
- `request_data`: A dictionary containing the data that was sent when the request was created
- `result`: Deployment request result value. NULL if the request is 'pending', 'processing' or 'failed'.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `created_by`: The email of the user that created the request. In case the request is created by a service, the field will have a "UbiOps" value.
- `notification_group`: Name of a notification group to send notifications (e.g., emails) when the request is completed
- `origin`: A dictionary containing the information on where the request originated from. It contains:
   - the deployment (and version) names if the request is directly made to the deployment
   - the pipeline (and version) names if the request is part of a pipeline request
   - the request schedule name if the request is created via a request schedule

## Response Examples

```
{
  "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
  "deployment": "deployment-1",
  "version": "v1",
  "status": "pending",
  "success": false,
  "time_created": "2020-03-29T08:09:10.729+00:00",
  "time_started": "2020-03-28T20:00:41.276+00:00",
  "time_completed": "2020-03-28T20:00:42.241+00:00",
  "request_data": {
    "input": 82.3
  },
  "result": null,
  "error_message": null,
  "created_by": "my.example.user@ubiops.com",
  "notification_group": "notification-group-1",
  "origin": {
    "deployment": "deployment-1",
    "deployment_version": "v1"
  }
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
request_id = 'request_id_example' # str 
metadata_only = True # bool  (optional)

# Get a deployment request
api_response = api_instance.deployment_requests_get(project_name, deployment_name, request_id, metadata_only=metadata_only)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **request_id** | **str** | 
 **metadata_only** | **bool** | [optional] 

### Return type

[**DeploymentRequestSingleDetail**](DeploymentRequestSingleDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_requests_list**
> list[DeploymentRequestList] deployment_requests_list(project_name, deployment_name, status=status, success=success, limit=limit, offset=offset, sort=sort, pipeline=pipeline, start_date=start_date, end_date=end_date, search_id=search_id)

List deployment requests

## Description
List all requests for the default version of a deployment

### Optional Parameters
The following parameters should be given as query parameters:

- `status`: Status of the request. Can be 'pending', 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `success`: A boolean value that indicates whether the deployment request was successful
- `limit`: The maximum number of requests given back, default is 50
- `offset`: The number which forms the starting point of the requests given back. If offset equals 2, then the first 2 requests will be omitted from the list.
- `sort`: Direction of sorting according to the creation date of the request, can be 'asc' or 'desc'. The default sorting is done in descending order.
- `pipeline`: A boolean value that indicates whether the deployment request was part of a pipeline request
- `start_date`: Start date of the interval for which the requests are retrieved, looking at the creation date of the request
- `end_date`: End date of the interval for which the requests are retrieved, looking at the creation date of the request
- `search_id`: A string to search inside request ids. It will filter all request ids that contain this string

If no start or end date is provided, the most recent requests are returned.

### Response Structure
A list of dictionaries containing the details of the deployment requests with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request
- `success`: A boolean value that indicates whether the deployment request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
status = 'status_example' # str  (optional)
success = True # bool  (optional)
limit = 56 # int  (optional)
offset = 56 # int  (optional)
sort = 'sort_example' # str  (optional)
pipeline = True # bool  (optional)
start_date = 'start_date_example' # str  (optional)
end_date = 'end_date_example' # str  (optional)
search_id = 'search_id_example' # str  (optional)

# List deployment requests
api_response = api_instance.deployment_requests_list(project_name, deployment_name, status=status, success=success, limit=limit, offset=offset, sort=sort, pipeline=pipeline, start_date=start_date, end_date=end_date, search_id=search_id)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **status** | **str** | [optional] 
 **success** | **bool** | [optional] 
 **limit** | **int** | [optional] 
 **offset** | **int** | [optional] 
 **sort** | **str** | [optional] 
 **pipeline** | **bool** | [optional] 
 **start_date** | **str** | [optional] 
 **end_date** | **str** | [optional] 
 **search_id** | **str** | [optional] 

### Return type

[**list[DeploymentRequestList]**](DeploymentRequestList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_requests_update**
> DeploymentRequestUpdateResponse deployment_requests_update(project_name, deployment_name, request_id, data)

Update a deployment request

## Description
Update a deployment request for the default version of a deployment. It is possible to **cancel** a request by giving `cancelled` in the status field.

### Required Parameters

- `status`: Status that the request will be updated to. It can only be `cancelled`.

## Request Examples


```
{
"status": "cancelled"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
request_id = 'request_id_example' # str 
data = ubiops.DeploymentRequestUpdate() # DeploymentRequestUpdate 

# Update a deployment request
api_response = api_instance.deployment_requests_update(project_name, deployment_name, request_id, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **request_id** | **str** | 
 **data** | [**DeploymentRequestUpdate**](DeploymentRequestUpdate.md) | 

### Return type

[**DeploymentRequestUpdateResponse**](DeploymentRequestUpdateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_environment_variables_copy**
> list[InheritedEnvironmentVariableList] deployment_version_environment_variables_copy(project_name, deployment_name, version, data)

Copy deployment version environment variable

## Description
Copy existing environment variables from a source object to the deployment version. Variables of the deployment version with the same name as ones from the source object will be overwritten with the new value. Only the copied variables are returned.

### Required Parameters

- `source_deployment`: The name of the deployment from which the variables will be copied

### Optional Parameters

- `source_version`: The version of the deployment from which the variables will be copied

## Request Examples
Copy the environment variables from a deployment

```
{
  "source_deployment": "example-deployment"
}
```

Copy the environment variables from a deployment version

```
{
  "source_deployment": "example-deployment",
  "source_version": "v1"
}
```

### Response Structure
A list of the copied variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from. Will be null for copied environment variables.
- `inheritance_name`: Name of the parent object that this variable is inherited from. Will be null for copied environment variables.

## Response Examples

```
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "version_specific_variable",
    "value": "some_value",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": null,
    "inheritance_name": null
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
version = 'version_example' # str 
data = ubiops.EnvironmentVariableCopy() # EnvironmentVariableCopy 

# Copy deployment version environment variable
api_response = api_instance.deployment_version_environment_variables_copy(project_name, deployment_name, version, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 
 **data** | [**EnvironmentVariableCopy**](EnvironmentVariableCopy.md) | 

### Return type

[**list[InheritedEnvironmentVariableList]**](InheritedEnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_environment_variables_create**
> EnvironmentVariableList deployment_version_environment_variables_create(project_name, deployment_name, version, data)

Create deployment version environment variable

## Description
Create an environment variable for the deployment version. Variables inherited from the project or deployment can be shadowed by creating a variable with the same name.

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users.

## Request Examples

```
{
  "name": "deployment_version_variable",
  "value": "another one",
  "secret": false
}
```

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

```
{
  "id": "54e94fbe-507e-4fae-981d-227c28a2dab0",
  "name": "deployment_version_variable",
  "value": "another one",
  "secret": false
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
version = 'version_example' # str 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate 

# Create deployment version environment variable
api_response = api_instance.deployment_version_environment_variables_create(project_name, deployment_name, version, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md) | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_environment_variables_delete**
> deployment_version_environment_variables_delete(project_name, deployment_name, id, version)

Delete deployment version environment variable

## Description
Delete an environment variable of a deployment version

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
id = 'id_example' # str 
version = 'version_example' # str 

# Delete deployment version environment variable
api_instance.deployment_version_environment_variables_delete(project_name, deployment_name, id, version)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **id** | **str** | 
 **version** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_environment_variables_get**
> EnvironmentVariableList deployment_version_environment_variables_get(project_name, deployment_name, id, version)

Get deployment version environment variable

## Description
Retrieve details of a deployment version environment variable. This cannot be used to retrieve details of inherited variables.

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
id = 'id_example' # str 
version = 'version_example' # str 

# Get deployment version environment variable
api_response = api_instance.deployment_version_environment_variables_get(project_name, deployment_name, id, version)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **id** | **str** | 
 **version** | **str** | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_environment_variables_list**
> list[InheritedEnvironmentVariableList] deployment_version_environment_variables_list(project_name, deployment_name, version)

List deployment version environment variables

## Description
List the environment variables defined for the deployment version. Includes environment variables defined at project level and deployment level.

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from - can be `project`, `deployment`, or null if the variable was defined for the version directly
- `inheritance_name`: Name of the parent object that this variable is inherited from - will be null if the variable was defined for the version directly

## Response Examples

```
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "deployment_version_specific_variable",
    "value": "some_value",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": "deployment",
    "inheritance_name": "deployment_name"
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": "project",
    "inheritance_name": "project_name"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
version = 'version_example' # str 

# List deployment version environment variables
api_response = api_instance.deployment_version_environment_variables_list(project_name, deployment_name, version)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 

### Return type

[**list[InheritedEnvironmentVariableList]**](InheritedEnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_environment_variables_update**
> EnvironmentVariableList deployment_version_environment_variables_update(project_name, deployment_name, id, version, data)

Update deployment version environment variable

## Description
Update an environment variable for the deployment version. This cannot be used to update inherited variables; to change an inherited variable for a specific version you can create a variable with the same name for the deployment version.

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users. Can be updated from false to true, but not from true to false (i.e. secrets will stay secrets).

## Request Examples

```
{
  "name": "deployment_version_variable",
  "value": "yet another one",
  "secret": false
}
```

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

```
{
  "id": "54e94fbe-507e-4fae-981d-227c28a2dab0",
  "name": "deployment_version_variable",
  "value": "yet another one",
  "secret": false
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
id = 'id_example' # str 
version = 'version_example' # str 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate 

# Update deployment version environment variable
api_response = api_instance.deployment_version_environment_variables_update(project_name, deployment_name, id, version, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **id** | **str** | 
 **version** | **str** | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md) | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_requests_batch_delete**
> object deployment_version_requests_batch_delete(project_name, deployment_name, version, data)

Delete multiple deployment version requests

## Description
Delete multiple deployment requests for a deployment version. If one of the given deployment requests does not exist, an error message is given and no request is deleted. A maximum of 250 deployment requests can be deleted with this method.

### Required Parameters
A list of ids for the requests

## Request Examples

```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
version = 'version_example' # str 
data = ['request_id_1', 'request_id_2'] # list[str] 

# Delete multiple deployment version requests
api_response = api_instance.deployment_version_requests_batch_delete(project_name, deployment_name, version, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 
 **data** | **list[str]** | 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_requests_batch_get**
> list[DeploymentRequestBatchDetail] deployment_version_requests_batch_get(project_name, deployment_name, version, data)

Retrieve multiple deployment version requests

## Description
Retrieve multiple deployment requests for a deployment version. If one of the given deployment requests does not exist, an error message is given and no request is returned. A maximum of 250 deployment requests can be retrieved with this method. The deployment requests are NOT returned in the order they are given in.

### Required Parameters
A list of ids for the requests

## Request Examples

```
["2f909aeb-5c7e-4974-970d-cd0a6a073aca", "85711124-54db-4794-b83d-24492247c6e1"]
```

### Response Structure
A list of dictionaries containing the details of the retrieved deployment requests with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request. Can be 'pending', 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `success`: A boolean value that indicates whether the deployment request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed
- `request_data`: A dictionary containing the data that was sent when the request was created
- `result`: Deployment request result value. NULL if the request is 'pending', 'processing' or 'failed'.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `retries`: Number of times that the request has been retried

## Response Examples

```
[
  {
    "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-29T08:09:10.729+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {
      "input": 82.2
    },
    "result": null,
    "error_message": null,
    "retries": 0
  },
  {
    "id": "85711124-54db-4794-b83d-24492247c6e1",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-06-25T09:37:17.765+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {
      "input": 52.4
    },
    "result": null,
    "error_message": null,
    "retries": 1
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
version = 'version_example' # str 
data = ['request_id_1', 'request_id_2'] # list[str] 

# Retrieve multiple deployment version requests
api_response = api_instance.deployment_version_requests_batch_get(project_name, deployment_name, version, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 
 **data** | **list[str]** | 

### Return type

[**list[DeploymentRequestBatchDetail]**](DeploymentRequestBatchDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_requests_create**
> DeploymentRequestCreateResponse deployment_version_requests_create(project_name, deployment_name, version, data, timeout=timeout)

Create a direct deployment version request

## Description
Request a prediction from a deployment version. It is only possible to make a request if a deployment file is uploaded for that version and the deployment build has succeeded (meaning that the version is in available state).
When using the 'requests' function of a deployment a list should be provided as input, see the example below.

### Required Parameters
The input for the request. In case of a structured deployment, this is a dictionary which contains the input fields of the deployment as keys. In case of a plain deployment, give a string or list of strings.

### Optional Parameters
These parameters should be given as query parameters

- `timeout`: Timeout for the deployment request in seconds. The maximum allowed value is 3600 (1 hour) and the default value is 300 (5 minutes).

## Request Examples
A structured deployment request

```
{
  "input-field-1": 5.0,
  "input-field-2": "N",
  "input-field-3": [0.25, 0.25, 2.1, 16.3]
}
```

A structured deployment request with a file field

```
{
  "input-field-1": 5.0,
  "file-input-field": "ubiops-file://my-bucket/file-1.jpg"
}
```

A plain deployment request

```
"example-plain-data"
```

Multiple structured deployment requests using the 'requests' function of a deployment version
```
[
    {
        "input-field-1": 5.0
    },
    {
        "input-field-1": 10.0
    }
]
```

### Response Structure
Details of the created deployment request

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `success`: A boolean value that indicates whether the deployment request was successful
- `result`: Deployment request result value. NULL if the request failed.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.

## Response Examples
A failed deployment request

```
{
  "id": "85ae32a7-fe3a-4a55-be27-9db88ae68501",
  "deployment": "deployment-1",
  "version": "v1",
  "success": false,
  "result": None,
  "error_message": "Asset ID not supported"
}
```

A successful deployment request

```
{
  "id": "ffce45da-1562-419a-89a0-0a0837e55392",
  "deployment": "deployment-1",
  "version": "v2",
  "success": true,
  "result": {
    "output-field-1": "2.1369",
    "output-field-2": "5.5832",
  },
  "error_message": None
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
version = 'version_example' # str 
data = {'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'} # str or dict() 
timeout = 56 # int  (optional)

# Create a direct deployment version request
api_response = api_instance.deployment_version_requests_create(project_name, deployment_name, version, data, timeout=timeout)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 
 **data** | **str or dict()** | 
 **timeout** | **int** | [optional] 

### Return type

[**DeploymentRequestCreateResponse**](DeploymentRequestCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_requests_delete**
> deployment_version_requests_delete(project_name, deployment_name, request_id, version)

Delete a deployment version request

## Description
Delete a deployment request for a deployment version

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
request_id = 'request_id_example' # str 
version = 'version_example' # str 

# Delete a deployment version request
api_instance.deployment_version_requests_delete(project_name, deployment_name, request_id, version)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **request_id** | **str** | 
 **version** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_requests_get**
> DeploymentRequestSingleDetail deployment_version_requests_get(project_name, deployment_name, request_id, version, metadata_only=metadata_only)

Get a deployment version request

## Description
Get a request for a deployment version. With this method, the result of a request may be retrieved.

### Optional Parameters
The following parameters should be given as query parameters:

- `metadata_only`: A boolean value that indicates whether the response should include the request data and result. The default value is False.

### Response Structure
A dictionary containing the details of the deployment request with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request. Can be 'pending', 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `success`: A boolean value that indicates whether the deployment request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed
- `request_data`: A dictionary containing the data that was sent when the request was created
- `result`: Deployment request result value. NULL if the request is 'pending', 'processing' or 'failed'.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `created_by`: The email of the user that created the request. In case the request is created by a service, the field will have a "UbiOps" value.
- `notification_group`: Name of a notification group to send notifications (e.g., emails) when the request is completed
- `retries`: Number of times that the request has been retried

## Response Examples

```
{
  "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
  "deployment": "deployment-1",
  "version": "v1",
  "status": "pending",
  "success": false,
  "time_created": "2020-03-29T08:09:10.729+00:00",
  "time_started": "2020-03-28T20:00:41.276+00:00",
  "time_completed": "2020-03-28T20:00:42.241+00:00",
  "request_data": {
    "input": 82.3
  },
  "result": null,
  "error_message": null,
  "created_by": "my.example.user@ubiops.com",
  "notification_group": "notification-group-1",
  "retries": 0
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
request_id = 'request_id_example' # str 
version = 'version_example' # str 
metadata_only = True # bool  (optional)

# Get a deployment version request
api_response = api_instance.deployment_version_requests_get(project_name, deployment_name, request_id, version, metadata_only=metadata_only)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **request_id** | **str** | 
 **version** | **str** | 
 **metadata_only** | **bool** | [optional] 

### Return type

[**DeploymentRequestSingleDetail**](DeploymentRequestSingleDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_requests_list**
> list[DeploymentRequestList] deployment_version_requests_list(project_name, deployment_name, version, status=status, success=success, limit=limit, offset=offset, sort=sort, pipeline=pipeline, start_date=start_date, end_date=end_date, search_id=search_id)

List deployment version requests

## Description
List all requests for a deployment version

### Optional Parameters
The following parameters should be given as query parameters:

- `status`: Status of the request. Can be 'pending', 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `success`: A boolean value that indicates whether the deployment request was successful
- `limit`: The maximum number of requests given back, default is 50
- `offset`: The number which forms the starting point of the requests given back. If offset equals 2, then the first 2 requests will be omitted from the list.
- `sort`: Direction of sorting according to the creation date of the request, can be 'asc' or 'desc'. The default sorting is done in descending order.
- `pipeline`: A boolean value that indicates whether the deployment request was part of a pipeline request
- `start_date`: Start date of the interval for which the requests are retrieved, looking at the creation date of the request
- `end_date`: End date of the interval for which the requests are retrieved, looking at the creation date of the request
- `search_id`: A string to search inside request ids. It will filter all request ids that contain this string

If no start or end date is provided, the most recent requests are returned.

### Response Structure
A list of dictionaries containing the details of the deployment requests with the following fields:

- `id`: Unique identifier for the deployment request
- `deployment`: Name of the deployment the request was made to
- `version`: Name of the version the request was made to
- `status`: Status of the request
- `success`: A boolean value that indicates whether the deployment request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "deployment": "deployment-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
version = 'version_example' # str 
status = 'status_example' # str  (optional)
success = True # bool  (optional)
limit = 56 # int  (optional)
offset = 56 # int  (optional)
sort = 'sort_example' # str  (optional)
pipeline = True # bool  (optional)
start_date = 'start_date_example' # str  (optional)
end_date = 'end_date_example' # str  (optional)
search_id = 'search_id_example' # str  (optional)

# List deployment version requests
api_response = api_instance.deployment_version_requests_list(project_name, deployment_name, version, status=status, success=success, limit=limit, offset=offset, sort=sort, pipeline=pipeline, start_date=start_date, end_date=end_date, search_id=search_id)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 
 **status** | **str** | [optional] 
 **success** | **bool** | [optional] 
 **limit** | **int** | [optional] 
 **offset** | **int** | [optional] 
 **sort** | **str** | [optional] 
 **pipeline** | **bool** | [optional] 
 **start_date** | **str** | [optional] 
 **end_date** | **str** | [optional] 
 **search_id** | **str** | [optional] 

### Return type

[**list[DeploymentRequestList]**](DeploymentRequestList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_version_requests_update**
> DeploymentRequestUpdateResponse deployment_version_requests_update(project_name, deployment_name, request_id, version, data)

Update a deployment version request

## Description
Update a deployment request for a deployment version. It is possible to **cancel** a request by giving `cancelled` in the status field.

### Required Parameters

- `status`: Status that the request will be updated to. It can only be `cancelled`.

## Request Examples


```
{
"status": "cancelled"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
request_id = 'request_id_example' # str 
version = 'version_example' # str 
data = ubiops.DeploymentRequestUpdate() # DeploymentRequestUpdate 

# Update a deployment version request
api_response = api_instance.deployment_version_requests_update(project_name, deployment_name, request_id, version, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **request_id** | **str** | 
 **version** | **str** | 
 **data** | [**DeploymentRequestUpdate**](DeploymentRequestUpdate.md) | 

### Return type

[**DeploymentRequestUpdateResponse**](DeploymentRequestUpdateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_versions_create**
> DeploymentVersionList deployment_versions_create(project_name, deployment_name, data)

Create deployment versions

## Description
Create a version for a deployment. The first version of a deployment is set as default.
Provide the parameter 'monitoring' as the name of a notification group to send monitoring notifications to. A notification will be sent in the case of a failed/recovered request. Pass `null` to switch off monitoring notifications for this version.
Provide the parameter 'default_notification_group' as the name of a notification group to send notifications when requests for the version are completed. Pass `null` to switch off request notifications for this version.

### Required Parameters

- `version`: Name of the version of the deployment

### Optional Parameters

- `language`: Language in which the version is provided. It can be python3.6, python3.7, python3.8, python3.9, python3.10, python3.6_cuda, python3.7_cuda, python3.8_cuda, python3.9_cuda, python3.10_cuda or r4.0. The default value is python3.7.
- `memory_allocation`: (deprecated) Reserved memory for the version in MiB. This value determines the memory allocated to the version: it should be enough to encompass the deployment file and all requirements that need to be installed. The default value is 2048. The minimum and maximum values are 256 and 16384 respectively.
- `instance_type`: Reserved instance type for the version. This value determines the allocation of memory to the version: it should be enough to encompass the deployment file and all requirements that need to be installed. The default value is 2048mb. The minimum and maximum values are 256mb and 16384mb respectively.
- `maximum_instances`: Upper bound of number of versions running. The default value is 5. *Indicator of resource capacity:* if many deployment requests need to be handled in a short time, this number can be set higher to avoid long waiting times.
- `minimum_instances`: Lower bound of number of versions running. The default value is 0. Set this value greater than 0 to always have a always running version.
- `maximum_idle_time`: Maximum time in seconds a version stays idle before it is stopped. The default value is 300, the minimum value is 10 (300 for GPU deployments) and the maximum value is 3600. A high value means that the version stays available longer. Sending requests to a running version means that it will be already initialized and thus take a shorter timer.

- `description`: Description for the version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the version. It defaults to 604800 seconds (1 week).
- `request_retention_mode`: Mode of request retention for requests to the version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored
- `maximum_queue_size_express`: Maximum number of queued express requests for all instances of this deployment version
- `maximum_queue_size_batch`: Maximum number of queued batch requests for all instances of this deployment version
- `static_ip`: A boolean indicating whether the deployment version should get a static IP. It defaults to False.
- `restart_request_interruption`: A boolean indicating whether the requests should be restarted in case of an interruption. It defaults to False.

If the time that a request takes does not matter, keep the default values.

## Request Examples

```
{
  "version": "version-1",
  "language": "python3.8"
}
```


```
{
  "version": "version-1",
  "language": "r4.0",
  "instance_type": "512mb"
}
```


```
  "version": "version-1",
  "language": "python3.6_cuda",
  "instance_type": "16384mb_t4",
  "maximum_instances": 1
```

```
{
  "version": "version-1",
  "maximum_instances": 4,
  "minimum_instances": 1,
  "monitoring": "notification-group-1"
}
```

### Response Structure
Details of the created version

- `id`: Unique identifier for the deployment (UUID)
- `deployment`: Deployment name to which the version is associated
- `version`: Version name
- `description`: Description of the version
- `language`: Language in which the version is provided
- `status`: The status of the version
- `active_revision`: Active revision of the version. It is initialised as None since there are no deployment files uploaded for the version yet.
- `latest_build`: Latest build of the version. It is initialised as None since no build is triggered for the version yet.
- `memory_allocation`: (deprecated) Reserved memory for the version in MiB
- `instance_type`: The reserved instance type for the version
- `maximum_instances`: Upper bound of number of versions running
- `minimum_instances`: Lower bound of number of versions running
- `maximum_idle_time`: Maximum time in seconds a version stays idle before it is stopped
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the version was created
- `last_updated`: The date when the version was last updated
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the version
- `request_retention_mode`: Mode of request retention for requests to the version. It can be one of the following: *none*, *metadata* or *full*.
- `maximum_queue_size_express`: Maximum number of queued express requests for all instances of this deployment version
- `maximum_queue_size_batch`: Maximum number of queued batch requests for all instances of this deployment version
- `static_ip`: A boolean indicating whether the deployment version should get a static IP
- `restart_request_interruption`: A boolean indicating whether the requests should be restarted in case of an interruption

## Response Examples

```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "deployment": "deployment-1",
  "version": "version-1",
  "description": "",
  "language": "python3.8",
  "status": "unavailable",
  "active_revision": null,
  "latest_build": null,
  "memory_allocation": 512,
  "instance_type": "512mb",
  "maximum_instances": 5,
  "minimum_instances": 0,
  "maximum_idle_time": 10,
  "labels": {
    "type": "version"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-05-12T16:23:15.456812Z",
  "monitoring": "notification-group-1",
  "default_notification_group": null,
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "maximum_queue_size_express": 100,
  "maximum_queue_size_batch": 100000,
  "static_ip": false,
  "restart_request_interruption": false
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
data = ubiops.DeploymentVersionCreate() # DeploymentVersionCreate 

# Create deployment versions
api_response = api_instance.deployment_versions_create(project_name, deployment_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **data** | [**DeploymentVersionCreate**](DeploymentVersionCreate.md) | 

### Return type

[**DeploymentVersionList**](DeploymentVersionList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_versions_delete**
> deployment_versions_delete(project_name, deployment_name, version)

Delete deployment version

## Description
Delete a deployment version. The version cannot be deleted if:
- It is referenced in a pipeline, it must be removed from the pipeline first.
- It is the default version of its deployment and is referenced in a request schedule.

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
version = 'version_example' # str 

# Delete deployment version
api_instance.deployment_versions_delete(project_name, deployment_name, version)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_versions_get**
> DeploymentVersionDetail deployment_versions_get(project_name, deployment_name, version)

Get deployment version

## Description
Retrieve details of a version of a deployment in a project

### Response Structure
Details of a version

- `id`: Unique identifier for the version (UUID)
- `deployment`: Deployment name to which the version is associated
- `version`: Version name
- `description`: Description of the version
- `language`: Language in which the version is provided
- `status`: The status of the version
- `active_revision`: UUID of the active revision of the version. If no deployment files have been uploaded yet, it is None.
- `latest_build`: UUID of the latest build of the version. If no build has been triggered yet, it is None.
- `memory_allocation`: (deprecated) Reserved memory for the version in MiB
- `instance_type`: The reserved instance type for the version
- `maximum_instances`: Upper bound of number of deployment pods running in parallel
- `minimum_instances`: Lower bound of number of deployment pods running in parallel
- `maximum_idle_time`: Maximum time in seconds a version stays idle before it is stopped
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the version was created
- `last_updated`: The date when the version was last updated
- `last_file_upload`: The date when a deployment file was last uploaded for the version
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the version
- `request_retention_mode`: Mode of request retention for requests to the version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored
- `maximum_queue_size_express`: Maximum number of queued express requests for all instances of this deployment version
- `maximum_queue_size_batch`: Maximum number of queued batch requests for all instances of this deployment version
- `has_request_method`: Whether the latest build of the version has a 'request' method
- `has_requests_method`: Whether the latest build of the version has a 'requests' method
- `static_ip`: A boolean indicating whether the deployment version should get a static IP
- `restart_request_interruption`: A boolean indicating whether the requests should be restarted in case of an interruption

## Response Examples

```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "deployment": "deployment-1",
  "version": "version-1",
  "description": "",
  "language": "python3.7",
  "status": "available",
  "active_revision": "a74662be-c938-4104-872a-8be1b85f64ff",
  "latest_build": "9f7fd6ec-53b7-41c6-949e-09efc2ee2d31",
  "memory_allocation": 512,
  "instance_type": "512mb",
  "maximum_instances": 4,
  "minimum_instances": 1,
  "maximum_idle_time": 10,
  "labels": {
    "type": "version"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "last_file_uploaded": "2020-06-21T09:03:01.875391Z",
  "monitoring": "notification-group-1",
  "default_notification_group": null,
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "maximum_queue_size_express": 100,
  "maximum_queue_size_batch": 100000,
  "has_request_method": true,
  "has_requests_method": false,
  "static_ip": false,
  "restart_request_interruption": false
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
version = 'version_example' # str 

# Get deployment version
api_response = api_instance.deployment_versions_get(project_name, deployment_name, version)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 

### Return type

[**DeploymentVersionDetail**](DeploymentVersionDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_versions_list**
> list[DeploymentVersionList] deployment_versions_list(project_name, deployment_name, labels=labels)

List deployment versions

## Description
Versions can be filtered according to the labels they have by giving labels as a query parameter. Versions that have at least one of the labels on which is filtered, are returned.

### Optional Parameters

- `labels`: Filter on labels of the version. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.

### Response Structure
A list of details of the versions

- `id`: Unique identifier for the deployment (UUID)
- `deployment`: Deployment name to which the version is associated
- `version`: Version name
- `description`: Description of the version
- `language`: Language in which the version is provided
- `status`: The status of the version
- `active_revision`: UUID of the active revision of the version. If no deployment files have been uploaded yet, it is None.
- `latest_build`: UUID of the latest build of the version. If no build has been triggered yet, it is None.
- `memory_allocation`: (deprecated) Reserved memory usage for the version in MiB
- `instance_type`: The reserved instance type for the version
- `maximum_instances`: Upper bound of number of versions running
- `minimum_instances`: Lower bound of number of versions running
- `maximum_idle_time`: Maximum time in seconds a version stays idle before it is stopped
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the version was created
- `last_updated`: The date when the version was last updated
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the version
- `request_retention_mode`: Mode of request retention for requests to the version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored
- `maximum_queue_size_express`: Maximum number of queued express requests for all instances of this deployment version
- `maximum_queue_size_batch`: Maximum number of queued batch requests for all instances of this deployment version
- `static_ip`: A boolean indicating whether the deployment version should get a static IP
- `restart_request_interruption`: A boolean indicating whether the requests should be restarted in case of an interruption

## Response Examples

```
[
  {
    "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
    "deployment": "deployment-1",
    "version": "version-1",
    "description": "",
    "language": "python3.8",
    "status": "available",
    "active_revision": "da27ef7c-aa3f-4963-a815-6ebf1865638e",
    "latest_build": "0f4a94c6-ec4c-4d1e-81d7-8f3e40471f75",
    "memory_allocation": 512,
    "instance_type": "512mb",
    "maximum_instances": 4,
    "minimum_instances": 1,
    "maximum_idle_time": 10,
    "labels": {
      "type": "version"
    },
    "creation_date": "2020-06-18T08:32:14.876451Z",
    "last_updated": "2020-06-19T10:52:23.124784Z",
    "monitoring": "notification-group-1",
    "default_notification_group": null,
    "request_retention_time": 604800,
    "request_retention_mode": "full",
    "maximum_queue_size_express": 100,
    "maximum_queue_size_batch": 100000,
    "static_ip": false,
    "restart_request_interruption": false
  },
  {
    "id": "24f6b80a-08c3-4d52-ac1a-2ea7e70f16a6",
    "deployment": "deployment-1",
    "version": "version-2",
    "description": "",
    "language": "r4.0",
    "status": "available",
    "active_revision": "a74662be-c938-4104-872a-8be1b85f64ff",
    "latest_build": "4534e479-ea2e-4161-876a-1d382191a031",
    "memory_allocation": 256,
    "instance_type": "256mb",
    "maximum_instances": 5,
    "minimum_instances": 0,
    "maximum_idle_time": 10,
    "labels": {
      "type": "version"
    },
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z",
    "monitoring": "notification-group-2",
    "default_notification_group": "notification-group-2",
    "request_retention_time": 86400,
    "request_retention_mode": "metadata",
    "maximum_queue_size_express": 100,
    "maximum_queue_size_batch": 100000,
    "static_ip": true,
    "restart_request_interruption": false
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
labels = 'labels_example' # str  (optional)

# List deployment versions
api_response = api_instance.deployment_versions_list(project_name, deployment_name, labels=labels)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **labels** | **str** | [optional] 

### Return type

[**list[DeploymentVersionList]**](DeploymentVersionList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployment_versions_update**
> DeploymentVersionDetail deployment_versions_update(project_name, deployment_name, version, data)

Update deployment version

## Description
Update a version of a deployment in a project. All necessary fields are validated again. When updating labels, the labels will replace the existing value for labels.
Provide the parameter 'monitoring' as the name of a notification group to send monitoring notifications to. A notification will be sent in the case of a failed/recovered request. Pass `null` to switch off monitoring notifications for this version.
Provide the parameter 'default_notification_group' as the name of a notification group to send notifications when requests for the version are completed. Pass `null` to switch off request notifications for this version.

### Optional Parameters

- `version`: New name for the version
- `memory_allocation`: (deprecated) New reserved memory for the version in MiB
- `instance_type`: New instance type for the version
- `maximum_instances`: New upper bound of number of versions running
- `minimum_instances`: New lower bound of number of versions running
- `maximum_idle_time`: New maximum time in seconds a version stays idle before it is stopped
- `description`: New description for the version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label. The new labels will replace the existing value for labels.
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the version
- `request_retention_mode`: Mode of request retention for requests to the version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored
- `maximum_queue_size_express`: Maximum number of queued express requests for all instances of this deployment version
- `maximum_queue_size_batch`: Maximum number of queued batch requests for all instances of this deployment version
- `static_ip`: A boolean indicating whether the deployment version should get a static IP
- `restart_request_interruption`: A boolean indicating whether the requests should be restarted in case of an interruption

## Request Examples

```
{
  "version": "new-version"
}
```


```
{
  "instance_type": "512mb",
  "maximum_instances": 4,
  "minimum_instances": 1,
  "monitoring": "notification-group-1"
}
```

### Response Structure
Details of the updated version

- `id`: Unique identifier for the deployment (UUID)
- `deployment`: Deployment name to which the version is associated
- `version`: Version name
- `description`: Description of the version
- `language`: Language in which the version is provided
- `status`: The status of the version
- `active_revision`: UUID of the active revision of the version. If no deployment files have been uploaded yet, it is None.
- `latest_build`: UUID of the latest build of the version. If no build has been triggered yet, it is None.
- `memory_allocation`: (deprecated) Reserved memory for the version in MiB
- `instance_type`: The reserved instance type for the version
- `maximum_instances`: Upper bound of number of versions running
- `minimum_instances`: Lower bound of number of versions running
- `maximum_idle_time`: Maximum time in seconds a version stays idle before it is stopped
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the version was created
- `last_updated`: The date when the version was last updated
- `last_file_upload`: The date when a deployment file was last uploaded for the version
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the version
- `request_retention_mode`: Mode of request retention for requests to the version. It can be one of the following: *none*, *metadata* or *full*.
- `maximum_queue_size_express`: Maximum number of queued express requests for all instances of this deployment version
- `maximum_queue_size_batch`: Maximum number of queued batch requests for all instances of this deployment version
- `has_request_method`: Whether the latest build of the version has a 'request' method
- `has_requests_method`: Whether the latest build of the version has a 'requests' method
- `static_ip`: A boolean indicating whether the deployment version should get a static IP
- `restart_request_interruption`: A boolean indicating whether the requests should be restarted in case of an interruption

## Response Examples

```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "deployment": "deployment-1",
  "version": "version-1",
  "description": "",
  "language": "python3.8",
  "status": "available",
  "active_revision": "a74662be-c938-4104-872a-8be1b85f64ff",
  "latest_build": "0d07337e-96d6-4ce6-8c63-c2f07edd2ce4",
  "memory_allocation": 512,
  "instance_type": "512mb",
  "maximum_instances": 4,
  "minimum_instances": 1,
  "maximum_idle_time": 10,
  "labels": {
    "type": "version"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-23T18:04:76.123754Z",
  "last_file_uploaded": "2020-06-21T09:03:01.875391Z",
  "monitoring": "notification-group-1",
  "default_notification_group": null,
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "maximum_queue_size_express": 100,
  "maximum_queue_size_batch": 100000,
  "has_request_method": true,
  "has_requests_method": false,
  "static_ip": false,
  "restart_request_interruption": false
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
version = 'version_example' # str 
data = ubiops.DeploymentVersionUpdate() # DeploymentVersionUpdate 

# Update deployment version
api_response = api_instance.deployment_versions_update(project_name, deployment_name, version, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 
 **data** | [**DeploymentVersionUpdate**](DeploymentVersionUpdate.md) | 

### Return type

[**DeploymentVersionDetail**](DeploymentVersionDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployments_create**
> DeploymentCreateResponse deployments_create(project_name, data)

Create deployments

## Description
Create a deployment by defining the input/output type and input/output fields. In case of **plain** type of input or output, input and output fields should not be given or passed as an empty list.

Possible data types for the input and output fields are:
- **int**: integer
- **string**: string
- **double**: double precision floating point
- **bool**: boolean value (False/True)
- **timestamp**: timestamp
- **array_int**: an array of integers
- **array_double**: an array of double precision floating points
- **array_string**: an array of strings
- **file**: a file field. This type of field can be used to pass files to the deployment. In deployment and pipeline requests, the path to the file in the bucket must be provided for this field.

Possible widgets for the input fields are:
- **textbox**: textbox
- **numberbox**: numberbox
- **slider**: slider
- **dropdown**: dropdown
- **switch**: switch
- **button**: upload button
- **drawer**: drawer
- **image_preview**: image upload with preview

Possible widgets for the output fields are:
- **textbox**: textbox
- **button**: download button
- **image_preview**: image preview

### Required Parameters

- `name`: Name of the deployment. It is unique within a project.
- `input_type`: Type of the input of the deployment. It can be either structured or plain.
- `output_type`: Type of the output of the deployment. It can be either structured or plain.
- `input_fields`: The list of required deployment input fields. It must contain the fields: name and data_type, and it may contain the field: widget. The name of an input field is unique for a deployment.
- `output_fields`: The list of required deployment output fields. It must contain the fields: name and data_type, and it may contain the field: widget. The name of an output field is unique for a deployment.

### Optional Parameters

- `description`: Description of the deployment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Request Examples
A deployment with structured input and output type

```
{
  "name": "deployment-1",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int"
    },
    {
      "name": "input-field-2",
      "data_type": "double"
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ]
}
```

A deployment with plain input type

```
{
  "name": "deployment-1",
  "description": "Deployment one"
  "input_type": "plain",
  "output_type": "structured",
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ]
}
```

A deployment with plain input and output type

```
{
  "name": "deployment-1",
  "input_type": "plain",
  "output_type": "plain"
  "labels": {
    "type": "deployment"
  }
}
```

A deployment with structured input and output type and field widgets
```
{
  "name": "deployment-1",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int",
      "widget": {
        "type": "slider",
        "configuration": {"min": 0, "max": 10, "default": 4, "step": 2}
      }
    },
    {
      "name": "input-field-2",
      "data_type": "double",
      "widget": {
        "type": "numberbox",
        "configuration": {"min": 0, "max": 1, "default": 0.5, "step": 0.1}
      }
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double",
      "widget": {
        "type": "textbox",
        "configuration": {}
      }
    }
  ]
}
```

### Response Structure
Details of the created deployment

- `id`: Unique identifier for the deployment (UUID)
- `name`: Name of the deployment
- `project`: Project name in which the deployment is created
- `input_type`: Type of the input of the deployment
- `output_type`: Type of the output of the deployment
- `input_fields`: The list of deployment input fields containing name and data_type
- `output_fields`: The list of deployment output fields containing name and data_type
- `description`: Description of the deployment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the deployment was created
- `last_updated`: The date when the deployment was last updated

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "deployment-1",
  "project": "project-1",
  "description": "",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int",
      "widget": {}
    },
    {
      "name": "input-field-2",
      "data_type": "double",
      "widget": {}
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double",
      "widget": {}
    }
  ],
  "labels": {
    "type": "deployment"
  },
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "last_updated": "2020-06-18T08:32:14.876451Z"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
data = ubiops.DeploymentCreate() # DeploymentCreate 

# Create deployments
api_response = api_instance.deployments_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**DeploymentCreate**](DeploymentCreate.md) | 

### Return type

[**DeploymentCreateResponse**](DeploymentCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployments_delete**
> deployments_delete(project_name, deployment_name)

Delete a deployment

## Description
Delete a deployment. If any of the versions of the deployment are referenced in a pipeline, the deployment cannot be deleted.

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 

# Delete a deployment
api_instance.deployments_delete(project_name, deployment_name)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployments_get**
> DeploymentDetail deployments_get(project_name, deployment_name)

Get details of a deployment

## Description
Retrieve details of a single deployment in a project

### Response Structure
Details of a deployment

- `id`: Unique identifier for the deployment (UUID)
- `name`: Name of the deployment
- `project`: Project name in which the deployment is defined
- `input_type`: Type of the input of the deployment
- `output_type`: Type of the output of the deployment
- `input_fields`: The list of deployment input fields containing name, data_type and widget
- `output_fields`: The list of deployment output fields containing name, data_type and widget
- `description`: Description of the deployment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the deployment was created
- `last_updated`: The date when the deployment was last updated
- `default_version`: Default version of the deployment.  If it does not have a default version, it is not set.

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "deployment-1",
  "project": "project-1",
  "description": "",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int",
      "widget": {}
    },
    {
      "name": "input-field-2",
      "data_type": "double",
      "widget": {}
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double",
      "widget": {}
    }
  ],
  "labels": {
    "type": "deployment"
  },
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "last_updated": "2020-06-19T10:52:23.124784Z",
  "default_version": "v1"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 

# Get details of a deployment
api_response = api_instance.deployments_get(project_name, deployment_name)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 

### Return type

[**DeploymentDetail**](DeploymentDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployments_list**
> list[DeploymentList] deployments_list(project_name, labels=labels)

List deployments

## Description
Deployments can be filtered according to the labels they have by giving labels as a query parameter. Deployments that have at least one of the labels on which is filtered, are returned.

### Optional Parameters

- `labels`: Filter on labels of the deployment. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.

### Response Structure
A list of details of the deployments in the project

- `id`: Unique identifier for the deployment (UUID)
- `name`: Name of the deployment
- `project`: Project name in which the deployment is defined
- `input_type`: Type of the input of the deployment
- `output_type`: Type of the output of the deployment
- `input_fields`: The list of deployment input fields containing name and data_type. It is empty in case of plain input type deployments.
- `output_fields`: The list of deployment output fields containing name and data_type. It is empty in case of plain output type deployments.
- `description`: Description of the deployment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the deployment was created
- `last_updated`: The date when the deployment was last updated

## Response Examples

```
[
  {
    "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
    "name": "deployment-1",
    "project": "project-1",
    "description": "Temperature deployment",
    "input_type": "structured",
    "output_type": "structured",
    "input_fields": [
      {
        "name": "input-field-1",
        "data_type": "int"
      },
      {
        "name": "input-field-2",
        "data_type": "double"
      }
    ],
    "output_fields": [
      {
        "name": "output-field",
        "data_type": "double"
      }
    ],
    "labels": {
      "type": "deployment"
    },
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z"
  },
  {
    "id": "5f4e942f-d5b8-4d62-99b2-870c15a82127",
    "name": "deployment-2",
    "project": "project-1",
    "description": "Deployment two",
    "input_type": "structured",
    "output_type": "plain",
    "input_fields": [
      {
        "name": "input-field",
        "data_type": "int"
      }
    ],
    "output_fields": [],
    "labels": {
      "type": "deployment"
    },
    "creation_date": "2020-03-24T09:43:51.791253Z",
    "last_updated": "2020-05-19T11:52:21.163270Z"
  },
  {
    "id": "bd3fae9d-aeec-4cf3-8ef0-5f9224d41904",
    "name": "deployment-3",
    "description": "",
    "project": "project-1",
    "input_type": "plain",
    "output_type": "plain",
    "input_fields": [],
    "output_fields": [],
    "creation_date": "2020-06-18T08:32:14.876451Z",
    "last_updated": "2020-06-19T10:52:23.124784Z"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
labels = 'labels_example' # str  (optional)

# List deployments
api_response = api_instance.deployments_list(project_name, labels=labels)
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

[**list[DeploymentList]**](DeploymentList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **deployments_update**
> DeploymentDetail deployments_update(project_name, deployment_name, data)

Update a deployment

## Description
Update a deployment

### Optional Parameters

- `name`: New name for the deployment
- `description`: New description for the deployment
- `labels`: New dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label. The new labels will replace the existing value for labels.
- `default_version`: Name of a version of this deployment which will be assigned as default. Only **available** versions can be assigned as default.
- `input_fields`: New input fields for the deployment
- `output_fields`: New output fields for the deployment

Input and output fields can be updated (name, data type or widget), added or removed. For deployments that are attached in a pipeline or contain any input/output widgets, fields must be updated one at a time so that the updates can be performed while preserving the mapping/widgets.

## Request Examples

```
{
  "name": "new-deployment-name"
}
```

### Response Structure
Details of the updated deployment

- `id`: Unique identifier for the deployment (UUID)
- `name`: Name of the deployment
- `project`: Project name in which the deployment is defined
- `input_type`: Type of the input of the deployment
- `output_type`: Type of the output of the deployment
- `input_fields`: The list of deployment input fields containing name, data_type and (optional) widget
- `output_fields`: The list of deployment output fields containing name, data_type and (optional) widget
- `description`: Description of the deployment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the deployment was created
- `last_updated`: The date when the deployment was last updated
- `default_version`: Default version of the deployment. If it does not have a default version, it is not set.

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "new-deployment-name",
  "project": "project-1",
  "description": "New deployment description",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int",
      "widget": {}
    },
    {
      "name": "input-field-2",
      "data_type": "double",
      "widget": {}
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double",
      "widget": {}
    }
  ],
  "labels": {
    "type": "deployment"
  },
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "last_updated": "2020-06-19T10:52:23.124784Z",
  "default_version": "v1"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
data = ubiops.DeploymentUpdate() # DeploymentUpdate 

# Update a deployment
api_response = api_instance.deployments_update(project_name, deployment_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **data** | [**DeploymentUpdate**](DeploymentUpdate.md) | 

### Return type

[**DeploymentDetail**](DeploymentDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **exports_create**
> ExportList exports_create(project_name, data)

Create an export

## Description
Create an export by selecting the objects in the export

### Optional Parameters

- `deployments`: Dictionary containing the deployments to export
- `pipelines`: Dictionary containing the pipelines to export
- `environment_variables`: Dictionary containing the project-level environment variables to export

## Request Examples


```
{
  "deployments": {
    "deployment-1": {
      "versions": {
        "version-1": {
          "environment_variables": {
            "VERSION_ENV_VAR_NAME_1": {
              "include_value": true
            },
            "VERSION_ENV_VAR_NAME_2": {
              "include_value": false
            }
          }
        },
        "version-2": {}
      },
      "environment_variables": {
        "DEPLOYMENT_ENV_VAR_NAME_1": {
          "include_value": false
        }
      }
    },
    "deployment-2": {
      "versions": {}
    }
  },
  "pipelines": {
    "pipeline-1": {
      "versions": {
        "version-1": {},
        "version-2": {}
      }
    },
    "pipeline-2": {
      "versions": {}
    }
  },
  "environment_variables": {
    "PROJECT_ENV_VAR_NAME_1": {
      "include_value": false
    }
  }
}
```

### Response Structure
Details of the created export

- `id`: Unique identifier for the export (UUID)
- `status`: Status of the export
- `error_message`: The error message in case of a failure
- `creation_date`: The date when the export was created
- `size`: Size of the export in bytes

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "status": "pending",
  "error_message": "",
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "size": null
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
data = ubiops.ExportCreate() # ExportCreate 

# Create an export
api_response = api_instance.exports_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**ExportCreate**](ExportCreate.md) | 

### Return type

[**ExportList**](ExportList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **exports_delete**
> exports_delete(project_name, export_id)

Delete an export

## Description
Delete an export from a project

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
export_id = 'export_id_example' # str 

# Delete an export
api_instance.exports_delete(project_name, export_id)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **export_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **exports_download**
> file exports_download(project_name, export_id)

Download an export

## Description
Download an export in a project

### Response Structure

- `file`: Zip file

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
export_id = 'export_id_example' # str 

# Download an export
with api_instance.exports_download(project_name, export_id) as response:
    filename = response.getfilename()
    content = response.read()

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **export_id** | **str** | 

### Return type

**file**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **exports_get**
> ExportDetail exports_get(project_name, export_id)

Get an export

## Description
Get the details of an export in a project

### Response Structure

- `id`: Unique identifier for the export (UUID)
- `status`: Status of the export
- `error_message`: The error message in case of a failure
- `creation_date`: The date when the export was created
- `size`: Size of the export in bytes
- `deployments`: Dictionary of the deployments in the export
- `pipelines`: Dictionary of the pipelines in the export
- `environment_variables`: Dictionary of the environment variables in the export

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
export_id = 'export_id_example' # str 

# Get an export
api_response = api_instance.exports_get(project_name, export_id)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **export_id** | **str** | 

### Return type

[**ExportDetail**](ExportDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **exports_list**
> list[ExportList] exports_list(project_name, status=status)

List exports

## Description
List all exports in a project

### Optional Parameters
The following parameter should be given as query parameter:

- `status`: Status of the export. Can be 'pending', 'processing', 'completed' and 'failed'.

### Response Structure
A list of details of the exports in the project

- `id`: Unique identifier for the export (UUID)
- `creation_date`: Time the export was created
- `status`: The status of the export
- `error_message`: The error message in case of a failure
- `size`: Size of the export in bytes

## Response Examples

```
[
  {
    "id": "ecb39626-2a14-4224-a57a-592a51567e17",
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "status": "pending",
    "error_message": "",
    "size": null
  },
  {
    "id": "f629a052-a827-44d9-97cf-3902504edc79",
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "status": "completed",
    "error_message": "",
    "size": 86400
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
status = 'status_example' # str  (optional)

# List exports
api_response = api_instance.exports_list(project_name, status=status)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **status** | **str** | [optional] 

### Return type

[**list[ExportList]**](ExportList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **expressions_evaluate**
> ExpressionEvaluateResponse expressions_evaluate(data)

Evaluate expression

## Description
Evaluate a pipeline version operator expression.

### Required Parameters

- `expression`: The expression to evaluate.
- `input_fields`: A list of input fields with name, data_type.
- `request_data`: Data to test the expression with. All its keys must be defined in 'input_fields'.

## Request Examples

```
{
  "expression": "var1 + 10",
  "input_fields": [
    {
      "name": "var1",
      "data_type": "int"
    }
  ],
  "request_data": {
    "var1": 123
  }
}
```

### Response Structure

- `result`: The result of the expression

## Response Examples

```
{
  "result": 133
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

data = ubiops.ExpressionEvaluate() # ExpressionEvaluate 

# Evaluate expression
api_response = api_instance.expressions_evaluate(data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **data** | [**ExpressionEvaluate**](ExpressionEvaluate.md) | 

### Return type

[**ExpressionEvaluateResponse**](ExpressionEvaluateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **files_delete**
> files_delete(project_name, bucket_name, file)

Delete a file

## Description
Delete a file from a bucket

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
bucket_name = 'bucket_name_example' # str 
file = 'file_example' # str 

# Delete a file
api_instance.files_delete(project_name, bucket_name, file)

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

project_name = 'project_name_example' # str 
bucket_name = 'bucket_name_example' # str 
file = 'file_example' # str 

# Download a file
api_response = api_instance.files_download(project_name, bucket_name, file)
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

[**FileUploadResponse**](FileUploadResponse.md)

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

project_name = 'project_name_example' # str 
bucket_name = 'bucket_name_example' # str 
file = 'file_example' # str 

# Get a file
api_response = api_instance.files_get(project_name, bucket_name, file)
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

[**FileItem**](FileItem.md)

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

project_name = 'project_name_example' # str 
bucket_name = 'bucket_name_example' # str 
prefix = 'prefix_example' # str  (optional)
delimiter = 'delimiter_example' # str  (optional)
continuation_token = 'continuation_token_example' # str  (optional)
limit = 56 # int  (optional)

# List files
api_response = api_instance.files_list(project_name, bucket_name, prefix=prefix, delimiter=delimiter, continuation_token=continuation_token, limit=limit)
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

[**FileDetail**](FileDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **files_upload**
> FileUploadResponse files_upload(project_name, bucket_name, file, data=data)

Upload a file

## Description
Generate a signed url to upload a file. Request body should be an empty dictionary.

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

project_name = 'project_name_example' # str 
bucket_name = 'bucket_name_example' # str 
file = 'file_example' # str 
data = None # object  (optional)

# Upload a file
api_response = api_instance.files_upload(project_name, bucket_name, file, data=data)
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
 **data** | **object** | [optional] 

### Return type

[**FileUploadResponse**](FileUploadResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **imports_create**
> ImportList imports_create(project_name, file=file, import_link=import_link, export_id=export_id, skip_confirmation=skip_confirmation)

Create an import

## Description
Create an import by uploading a zip file, providing a link to an import file or by giving an export id.
Only one of the fields `file`, `import_link` or `export_id` may be given at a time.
When providing a link to an import file, make sure it is publicly downloadable.

### Required Parameters
Only one of the following fields should be given:

- `file`: A zip file
- `import_link`: url to a publicly downloadable zip file
- `export_id`: UUID of a previously created export in the same project

### Optional Parameters

- `skip_confirmation`: Whether to skip the confirmation step, default to False

### Response Structure
Details of the created import

- `id`: Unique identifier for the import (UUID)
- `status`: Status of the import
- `error_message`: The error message in case of a failure
- `creation_date`: The date when the import was created
- `size`: Size of the import in bytes

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "status": "pending",
  "error_message": "",
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "size": 28391
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
file = '/path/to/file' # file  (optional)
import_link = 'import_link_example' # str  (optional)
export_id = 'export_id_example' # str  (optional)
skip_confirmation = True # bool  (optional)

# Create an import
api_response = api_instance.imports_create(project_name, file=file, import_link=import_link, export_id=export_id, skip_confirmation=skip_confirmation)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **file** | **file** | [optional] 
 **import_link** | **str** | [optional] 
 **export_id** | **str** | [optional] 
 **skip_confirmation** | **bool** | [optional] 

### Return type

[**ImportList**](ImportList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **imports_delete**
> imports_delete(project_name, import_id)

Delete an import

## Description
Delete an import from a project

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
import_id = 'import_id_example' # str 

# Delete an import
api_instance.imports_delete(project_name, import_id)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **import_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **imports_download**
> file imports_download(project_name, import_id)

Download an import

## Description
Download an import in a project

### Response Structure

- `file`: Zip file

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
import_id = 'import_id_example' # str 

# Download an import
with api_instance.imports_download(project_name, import_id) as response:
    filename = response.getfilename()
    content = response.read()

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **import_id** | **str** | 

### Return type

**file**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **imports_get**
> ImportDetail imports_get(project_name, import_id)

Get an import

## Description
Get the details of an import in a project

### Response Structure

- `id`: Unique identifier for the import (UUID)
- `status`: Status of the import
- `error_message`: The error message in case of a failure
- `creation_date`: The date when the import was created
- `size`: Size of the import in bytes
- `deployments`: Dictionary of the deployments in the import
- `pipelines`: Dictionary of the pipelines in the import
- `environment_variables`: Dictionary of the environment variables in the import

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
import_id = 'import_id_example' # str 

# Get an import
api_response = api_instance.imports_get(project_name, import_id)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **import_id** | **str** | 

### Return type

[**ImportDetail**](ImportDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **imports_list**
> list[ImportList] imports_list(project_name, status=status)

List imports

## Description
List all imports in a project

### Optional Parameters
The following parameter should be given as query parameter:

- `status`: Status of the import. Can be 'pending', 'scanning', 'confirmation', 'confirmation_pending', 'processing', 'completed' and 'failed'.

### Response Structure
A list of details of the imports in the project

- `id`: Unique identifier for the import (UUID)
- `creation_date`: Time the import was created
- `status`: The status of the import
- `error_message`: The error message in case of a failure
- `size`: Size of the import in bytes

## Response Examples

```
[
  {
    "id": "ecb39626-2a14-4224-a57a-592a51567e17",
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "status": "pending",
    "error_message": "",
    "size": 126832
  },
  {
    "id": "f629a052-a827-44d9-97cf-3902504edc79",
    "creation_date": "2020-05-18T11:26:57.904+00:00",
    "status": "pending",
    "error_message": "",
    "size": 86400
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
status = 'status_example' # str  (optional)

# List imports
api_response = api_instance.imports_list(project_name, status=status)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **status** | **str** | [optional] 

### Return type

[**list[ImportList]**](ImportList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **imports_update**
> ImportDetail imports_update(project_name, import_id, data)

Confirm an import

## Description
Confirm (and update) an import by selecting the objects in the import

### Optional Parameters

- `deployments`: Dictionary containing the deployments to create
- `pipelines`: Dictionary containing the pipelines to create
- `environment_variables`: Dictionary containing the project-level environment variables to create

## Request Examples


```
{
    "deployments": {
    "deployment-1: {
      "description": "",
      "labels": {
        "my-label": "my-value"
      },
      "default_version": "v1",
      "versions": {
        "v1": {
          "zip": "deployments/deployment_deployment-1/versions/deployment_deployment-1_version_v1.zip",
          "description": "",
          "labels": {},
          "language": "python3.7",
          "maximum_idle_time": 300,
          "maximum_instances": 5,
          "memory_allocation": 256,
          "minimum_instances": 0,
          "environment_variables": {
            "VERSION_ENV_VAR_1": {
              "value": "my-secret-value",
              "secret": true
            },
            "VERSION_ENV_VAR_2": {
              "value": "test2"
            }
          },
          "request_retention_mode": "full",
          "request_retention_time": 604800
        }
      },
      "input_type": "structured",
      "output_type": "structured",
      "input_fields": [
        {
          "name": "input",
          "data_type": "double"
        }
      ],
      "output_fields": [
        {
          "name": "output",
          "data_type": "double"
        }
      ],
      "environment_variables": {
        "DEPLOYMENT_ENV_VAR_1": {
          "value": "my-secret-value",
          "secret": true
        },
        "DEPLOYMENT_ENV_VAR_2": {
          "value": "test"
        }
      }
    }
  },
  "pipelines": {
    "pipeline-1: {
      "description": "",
      "labels": {
        "test": "label"
      },
      "default_version": "v1",
      "versions": {
        "v1": {
          "description": "",
          "labels": {},
          "objects": [
            {
              "name": "obj-1",
              "reference_name": "deployment-1",
              "reference_version": "v1"
            }
          ],
          "attachments": [
            {
              "sources": [
                {
                  "mapping": [
                    {
                      "source_field_name": "input",
                      "destination_field_name": "input"
                    }
                  ],
                  "source_name": "pipeline_start"
                }
              ],
              "destination_name": "obj-1"
            },
            {
              "sources": [
                {
                  "mapping": [
                    {
                      "source_field_name": "output",
                      "destination_field_name": "output"
                    }
                  ],
                  "source_name": "obj-1"
                }
              ],
              "destination_name": "pipeline_end"
            }
          ],
          "request_retention_mode": "full",
          "request_retention_time": 604800
        }
      },
      "input_type": "structured",
      "output_type": "structured",
      "input_fields": [
        {
          "name": "input",
          "data_type": "double"
        }
      ],
      "output_fields": [
        {
          "name": "output",
          "data_type": "double"
        }
      ]
    }
  },
  "environment_variables": {
    "PROJECT_ENV_VAR_1": {
      "value": "value1",
      "secret": true
    },
    "PROJECT_ENV_VAR_2": {
      "value": "value2"
    }
  }
}
```

### Response Structure
Details of the updated import

- `id`: Unique identifier for the import (UUID)
- `status`: Status of the import
- `error_message`: The error message in case of a failure
- `creation_date`: The date when the import was created
- `size`: Size of the import in bytes

## Response Examples

```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "status": "pending",
  "error_message": "",
  "creation_date": "2020-06-18T08:32:14.876451Z",
  "size": null
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
import_id = 'import_id_example' # str 
data = ubiops.ImportUpdate() # ImportUpdate 

# Confirm an import
api_response = api_instance.imports_update(project_name, import_id, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **import_id** | **str** | 
 **data** | [**ImportUpdate**](ImportUpdate.md) | 

### Return type

[**ImportDetail**](ImportDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **instance_types_list**
> list[DeploymentInstanceType] instance_types_list(project_name)

List instance types

## Description
Get list of available deployment instance types for a project

### Response Structure
Details of the instance type

- `id`: Unique identifier for the instance type (UUID)

- `name`: Name of the deployment instance type

- `display_name`: Readable name of the deployment instance type

- `memory_allocation`: Integer indicating memory allocation for this instance type (Mi)

- `cpu_allocation`: Integer indicating CPU allocation for this instance type (milliCPU)

- `gpu_allocation`: Integer indicating number of GPU cores for this instance type

- `gpu_allocation_type`: Type of the GPU allocation. Normally, this is nvidia.com/gpu, but in case of mixed mode MIG
this can change to nvidia.com/mig-1g.10gb or alike

## Response Examples

```
[
  {
    "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
    "name": "512mb",
    "display_name": "512 MB",
    "memory_allocation": 512,
    "cpu_allocation": 125,
    "gpu_allocation": 0,
    "gpu_allocation_type": null
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 

# List instance types
api_response = api_instance.instance_types_list(project_name)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 

### Return type

[**list[DeploymentInstanceType]**](DeploymentInstanceType.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **metrics_get**
> list[Metrics] metrics_get(project_name, metric, start_date, end_date, object_type, interval=interval, object_id=object_id, user_id=user_id)

Get metrics

## Description
Get metrics for the project or a specified object. The following metrics are available:

Metrics on pipeline version level:
- `requests`: Number of requests made to the object
- `failed_requests`: Number of failed requests made to the object
- `request_duration`: Average time in seconds for a pipeline request to complete
- `input_volume`: Volume of incoming data in bytes
- `object_requests`: Number of requests made to objects in the pipeline version
- `object_failed_requests`: Number of failed requests made to deployments in a pipeline

Metrics on deployment version level:
- `requests`: Number of requests made to the object
- `failed_requests`: Number of failed requests made to the object
- `input_volume`: Volume of incoming data in bytes
- `output_volume`: Volume of outgoing data in bytes
- `outputs`: Number of outgoing data items
- `compute`: Average time in seconds for a request to complete
- `memory_peak`: Peak memory used during a request
- `instances`: Number of active deployment instances
- `credits`: Usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours the deployments are running
- `active_time`: Time in seconds that the deployment is active
- `express_queue_size`: Average number of queued express requests
- `batch_queue_size`: Average number of queued batch requests
- `express_queue_time`: Average time in seconds for an express request to start processing
- `batch_queue_time`: Average time in seconds for a batch request to start processing

### Required Parameters

- `start_date`: Starting date for the metric values to be returned. It should be provided in datetime isoformat.
- `end_date`: Ending date for the metric values to be returned. It should be provided in datetime isoformat.
- `object_type`: The type of the object for which the metrics are requested. It can be either `deployment_version` or `pipeline_version`.

### Optional Parameters

- `interval`: Interval for the metric value. It can be minute, hour, day or month. The metric values will be aggregated according to this interval. The default value is hour.
- `object_id`: Uuid of the specific object for which the metrics are requested. When it is not provided, the metrics are aggregated for the given `object_type`.
- `user_id`: Uuid of the user for which the metrics are requested. When it is not provided, the metrics are aggregated for the given `object_type` generated by all users.

### Response Structure

- `start_date`: Timestamp denoting the start of the period over which the metric was measured
- `end_date`: Timestamp denoting the end of the period over which the metric was measured
- `value`: Aggregated metric value for the given interval

## Response Examples
With interval as minute, start_date as 2019-11-13 12:00:00 and end_date as 2019-11-13 12:03:00

```
[
  {
    "start_date": "2019-11-13T12:00:00+00:00",
    "end_date": "2019-11-13T12:01:00+00:00",
    "value": 100
  },
  {
    "start_date": "2019-11-13T12:01:00+00:00",
    "end_date": "2019-11-13T12:02:00+00:00",
    "value": 134
  },
  {
    "start_date": "2019-11-13T12:02:00+00:00",
    "end_date": "2019-11-13T12:03:00+00:00",
    "value": 112
  }
]

```

With interval as hour, start_date as 2019-11-13 12:00:00 and end_date as 2019-11-13 14:00:00

```
[
  {
   "start_date": "2019-11-13T12:00:00+00:00",
   "end_date": "2019-11-13T13:00:00+00:00",
   "value": 92
  },
  {
    "start_date": "2019-11-13T13:00:00+00:00",
    "end_date": "2019-11-13T14:00:00+00:00",
    "value": 120
  },
  {
    "start_date": "2019-11-13T14:00:00+00:00",
    "end_date": "2019-11-13T15:00:00+00:00",
    "value": 0
  }
]
```

With interval as day, start_date as 2019-11-13 12:00:00 and end_date as 2019-11-14 12:00:00

```
[
  {
   "start_date": "2019-11-13T00:00:00+00:00",
   "end_date": "2019-11-14T00:00:00+00:00",
   "value": 528
  },
  {
    "start_date": "2019-11-14T00:00:00+00:00",
    "end_date": "2019-11-15T00:00:00+00:00",
    "value": 342
  }
]
```

With interval as month, start_date as 2019-11-13 12:00:00 and end_date as 2019-12-13 12:00:00
```
[
  {
   "start_date": "2019-11-01T00:00:00+00:00",
   "end_date": "2019-12-01T00:00:00+00:00",
   "value": 1983
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
metric = 'metric_example' # str 
start_date = 'start_date_example' # str 
end_date = 'end_date_example' # str 
object_type = 'object_type_example' # str 
interval = 'interval_example' # str  (optional)
object_id = 'object_id_example' # str  (optional)
user_id = 'user_id_example' # str  (optional)

# Get metrics
api_response = api_instance.metrics_get(project_name, metric, start_date, end_date, object_type, interval=interval, object_id=object_id, user_id=user_id)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **metric** | **str** | 
 **start_date** | **str** | 
 **end_date** | **str** | 
 **object_type** | **str** | 
 **interval** | **str** | [optional] 
 **object_id** | **str** | [optional] 
 **user_id** | **str** | [optional] 

### Return type

[**list[Metrics]**](Metrics.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **notification_groups_create**
> NotificationGroupList notification_groups_create(project_name, data)

Create notification groups

## Description
Create a notification group by defining a name and a list of contacts

### Required Parameters

- `name`: Name of the notification group. It is unique within a project.

### Optional Parameters

- `contacts`: A list of dictionaries containing the following keys:
  - `type`: Type of the contact. It can be `email`.
  - `configuration`: A custom dictionary that contains required information for the type. For `email` type, it should contain the key `email_address`.

## Request Examples

```
{
  "name": "notification-group-1",
  "contacts": [
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user@ubiops.com"
      }
    },
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user.2@ubiops.com"
      }
    }
  ]
}
```

### Response Structure
Details of the created notification group

- `id`: Unique identifier for the notification group (UUID)
- `name`: Name of the notification group
- `contacts`: A list of contacts in the notification group

## Response Examples

```
{
  "id": "dc083d2a-74aa-4c49-8806-8adbeadca8a8",
  "name": "notification-group-1",
  "contacts": [
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user@ubiops.com"
      }
    },
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user.2@ubiops.com"
      }
    }
  ]
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
data = ubiops.NotificationGroupCreate() # NotificationGroupCreate 

# Create notification groups
api_response = api_instance.notification_groups_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**NotificationGroupCreate**](NotificationGroupCreate.md) | 

### Return type

[**NotificationGroupList**](NotificationGroupList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **notification_groups_delete**
> notification_groups_delete(project_name, notification_group_name)

Delete notification group

## Description
Delete a notification group

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
notification_group_name = 'notification_group_name_example' # str 

# Delete notification group
api_instance.notification_groups_delete(project_name, notification_group_name)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **notification_group_name** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **notification_groups_get**
> NotificationGroupList notification_groups_get(project_name, notification_group_name)

Get notification group

## Description
Retrieve details of a single notification group in a project

### Response Structure
Details of a notification group

- `id`: Unique identifier for the notification group (UUID)
- `name`: Name of the notification group
- `contacts`: A list of contacts in the notification group

## Response Examples

```
{
  "id": "dc083d2a-74aa-4c49-8806-8adbeadca8a8",
  "name": "notification-group-1",
  "contacts": [
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user@ubiops.com"
      }
    },
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user.2@ubiops.com"
      }
    }
  ]
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
notification_group_name = 'notification_group_name_example' # str 

# Get notification group
api_response = api_instance.notification_groups_get(project_name, notification_group_name)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **notification_group_name** | **str** | 

### Return type

[**NotificationGroupList**](NotificationGroupList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **notification_groups_list**
> list[NotificationGroupList] notification_groups_list(project_name)

List notification groups

## Description
List the notification groups in a project

### Response Structure
A list of details of the notification groups in the project

- `id`: Unique identifier for the notification group (UUID)
- `name`: Name of the notification group
- `contacts`: A list of contacts in the notification group

## Response Examples

```
[
  {
    "id": "dc083d2a-74aa-4c49-8806-8adbeadca8a8",
    "name": "notification-group-1",
    "contacts": [
      {
        "type": "email",
        "configuration": {
          "email_address": "my.example.user@ubiops.com"
        }
      },
      {
        "type": "email",
        "configuration": {
          "email_address": "my.example.user.2@ubiops.com"
        }
      }
    ],
  },
  {
    "id": "7193ca09-d28b-4fce-a15a-11e0bc9f7f6f",
    "name": "notification-group-2",
     "contacts": [
      {
        "type": "email",
        "configuration": {
          "email_address": "my.example.user.3@ubiops.com"
        }
      }
    ]
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 

# List notification groups
api_response = api_instance.notification_groups_list(project_name)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 

### Return type

[**list[NotificationGroupList]**](NotificationGroupList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **notification_groups_update**
> NotificationGroupList notification_groups_update(project_name, notification_group_name, data)

Update notification group

## Description
Update a notification group

### Optional Parameters

- `name`: New name for the deployment
- `contacts`: A list of dictionaries containing the following keys:
- `type`: Type of the contact. It can be `email`.
- `configuration`: A custom dictionary that contains required information for the type. For `email` type, it should contain the key `email_address`.

## Request Examples

```
{
  "name": "new-notification-group-name"
}
```

### Response Structure
Details of the updated notification group

- `id`: Unique identifier for the notification group (UUID)
- `name`: Name of the notification group
- `contacts`: A list of contacts in the notification group

## Response Examples

```
{
  "id": "dc083d2a-74aa-4c49-8806-8adbeadca8a8",
  "name": "new-notification-group-name",
  "contacts": [
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user@ubiops.com"
      }
    },
    {
      "type": "email",
      "configuration": {
        "email_address": "my.example.user.2@ubiops.com"
      }
    }
  ]
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
notification_group_name = 'notification_group_name_example' # str 
data = ubiops.NotificationGroupUpdate() # NotificationGroupUpdate 

# Update notification group
api_response = api_instance.notification_groups_update(project_name, notification_group_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **notification_group_name** | **str** | 
 **data** | [**NotificationGroupUpdate**](NotificationGroupUpdate.md) | 

### Return type

[**NotificationGroupList**](NotificationGroupList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organization_users_create**
> OrganizationUserDetail organization_users_create(organization_name, data)

Add a user to an organization

## Description
Add a user to an organization as admin or normal user. The user making the request must be admin of the organization.
The user can later be assigned roles in the projects defined in the scope the organization, such as project-admin, project-viewer etc.

### Required Parameters

- `email`: Email of the user

- `admin`: Boolean value indicating whether the user is added as an admin of the organization or not

## Request Examples

```
{
  "email": "test@example.com",
  "admin": false
}
```

### Response Structure
Details of the added user

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

- `admin`: Boolean value indicating whether the user is an admin of the organization or not

## Response Examples

```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": false
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str 
data = ubiops.OrganizationUserCreate() # OrganizationUserCreate 

# Add a user to an organization
api_response = api_instance.organization_users_create(organization_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 
 **data** | [**OrganizationUserCreate**](OrganizationUserCreate.md) | 

### Return type

[**OrganizationUserDetail**](OrganizationUserDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organization_users_delete**
> organization_users_delete(organization_name, user_id)

Delete a user from an organization

## Description
Delete a user from an organization. The user making the request must be admin of the organization.
It is not possible to delete the last admin of an organization.

**When a user is deleted from an organization, all his roles from all projects defined in the scope of the organization are also deleted.**

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str 
user_id = 'user_id_example' # str 

# Delete a user from an organization
api_instance.organization_users_delete(organization_name, user_id)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 
 **user_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organization_users_get**
> OrganizationUserDetail organization_users_get(organization_name, user_id)

Get details of a user in an organization

## Description
Get the details of a user in an organization. The user making the request must be admin of the organization.

### Response Structure
Details of the user

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

- `admin`: Boolean value indicating whether the user is an admin of the organization or not

## Response Examples

```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": false
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str 
user_id = 'user_id_example' # str 

# Get details of a user in an organization
api_response = api_instance.organization_users_get(organization_name, user_id)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 
 **user_id** | **str** | 

### Return type

[**OrganizationUserDetail**](OrganizationUserDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organization_users_list**
> list[OrganizationUserDetail] organization_users_list(organization_name)

List the users in an organization

## Description
List users and their details in an organization

### Response Structure
List of details of users

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

- `admin`: Boolean value indicating whether the user is an admin of the organization or not

## Response Examples

```
[
  {
    "id": "54977bc3-2c3b-4d8f-97c7-aff89a95bf21",
    "email": "user@example.com",
    "name": "user",
    "surname": "name",
    "admin": true
  },
  {
    "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
    "email": "user2@example.com",
    "name": "user",
    "surname": "name",
    "admin": false
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str 

# List the users in an organization
api_response = api_instance.organization_users_list(organization_name)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 

### Return type

[**list[OrganizationUserDetail]**](OrganizationUserDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organization_users_update**
> OrganizationUserDetail organization_users_update(organization_name, user_id, data)

Update details of a user in an organization

## Description
Update the admin status of a user in an organization. The user making the request must be admin of the organization.
It is not possible to change the last admin of an organization to a regular user.

### Required Parameters

- `admin`: Boolean value indicating whether the user is added as an admin of the organization or not

## Request Examples

```
{
  "admin": true
}
```

### Response Structure
Details of the user

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

- `admin`: Boolean value indicating whether the user is an admin of the organization or not

## Response Examples

```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": true
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str 
user_id = 'user_id_example' # str 
data = ubiops.OrganizationUserUpdate() # OrganizationUserUpdate 

# Update details of a user in an organization
api_response = api_instance.organization_users_update(organization_name, user_id, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 
 **user_id** | **str** | 
 **data** | [**OrganizationUserUpdate**](OrganizationUserUpdate.md) | 

### Return type

[**OrganizationUserDetail**](OrganizationUserDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organizations_create**
> OrganizationList organizations_create(data)

Create organizations

## Description
Create a new organization. When a user creates an organization, s/he will automatically become an organization admin.

### Required Parameters

- `name`: Name of the organization. The name is globally unique. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter.

- `subscription`: Name of the subscription for the organization

### Optional Parameters

- `subscription_end_date`: End date of the subscription. The subscription will be cancelled on this date. A 'free' subscription cannot have a custom end_date as this subscription is always valid for a year.
If you are going to use a subscription other than the free subscription, you should provide the end date.

## Request Examples

```
{
  "name": "test-organization",
  "subscription": "professional",
  "subscription_end_date": "2021-03-25"
}
```


```
{
  "name": "test-organization",
  "subscription": "professional",
  "subscription_end_date": "2021-03-25"
}
```

### Response Structure
Details of the created organization

- `id`: Unique identifier for the organization (UUID)

- `name`: Name of the organization

- `creation_date`: Date and time the organization was created

## Response Examples

```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

data = ubiops.OrganizationCreate() # OrganizationCreate 

# Create organizations
api_response = api_instance.organizations_create(data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **data** | [**OrganizationCreate**](OrganizationCreate.md) | 

### Return type

[**OrganizationList**](OrganizationList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organizations_get**
> OrganizationDetail organizations_get(organization_name)

Get details of an organization

## Description
Get the details of an organization

### Response Structure
Details of the organization

- `id`: Unique identifier for the organization (UUID)

- `name`: Name of the organization

- `creation_date`: Time the organization was created

- `subscription`: Name of the subscription of the organization

- `subscription_self_service`: Boolean indicating if the organization subscription is self service

## Response Examples

```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z",
  "subscription": "free",
  "subscription_self_service": true
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str 

# Get details of an organization
api_response = api_instance.organizations_get(organization_name)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 

### Return type

[**OrganizationDetail**](OrganizationDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organizations_list**
> list[OrganizationList] organizations_list()

List organizations

## Description
List all organizations where the user making the request is a member

### Response Structure
A list of details of the organizations

- `id`: Unique identifier for the organization (UUID)

- `name`: Name of the organization

- `creation_date`: Date and time the organization was created

## Response Examples

```
[
  {
    "id": "45a1f903-4146-4f15-be4a-302455cd6f7e",
    "name": "organization-name",
    "creation_date": "2020-03-23T11:47:15.436240Z"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)


# List organizations
api_response = api_instance.organizations_list()
print(api_response)

# Close the connection
api_client.close()
```


### Parameters

This endpoint does not need any parameter.

### Return type

[**list[OrganizationList]**](OrganizationList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organizations_resource_usage**
> ResourceUsage organizations_resource_usage(organization_name)

Get resource usage

## Description
List the total number of resources used by this organization

### Response Structure
A list containing the number of

- projects

- users

- deployments

- deployment_versions

- pipelines

- pipeline_versions

currently used by the organization.

## Response Examples

```
{
  "projects": 5,
  "users": 3,
  "deployments": 30,
  "deployment_versions": 47,
  "pipelines": 2,
  "pipeline_versions": 4
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str 

# Get resource usage
api_response = api_instance.organizations_resource_usage(organization_name)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 

### Return type

[**ResourceUsage**](ResourceUsage.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organizations_update**
> OrganizationDetail organizations_update(organization_name, data)

Update details of an organization

## Description
Update an organization. The user making the request must be admin of the organization. Users are able to update the name of the organization, but changes to the subscription can only be done by Dutch Analytics.
To delete the end date of the current subscription, give the 'subscription_end_date' parameter with value null.

### Optional Parameters

- `name`: New organization name
- `subscription`: New subscription
- `subscription_end_date`: End date of the new subscription. The required format is `YYYY-MM-DD`. The subscription will be cancelled on this date. If you are going to update the subscription plan of the organization to a subscription other than free, you have to provide the end date.
- `subscription_start_date`: Start date of the new subscription. The required format is `YYYY-MM-DD`. The subscription will start from the provided date. If you are going to update the subscription of the organization or schedule a subscription for a time in future, you have to provide the start date.

## Request Examples



```
{
  "name": "new-organization-name"
}
```

```
{
  "subscription": "professional",
  "subscription_end_date": "2020-08-30",
  "subscription_start_date": "2020-07-30"
}
```

```
{
  "subscription_end_date": "2020-08-30",
  "subscription_start_date": "2020-07-30"
}
```

### Response Structure
Details of the organization

- `id`: Unique identifier for the organization (UUID)

- `name`: Name of the organization

- `creation_date`: Time the organization was created

- `subscription`: Name of the subscription

## Response Examples

```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z",
  "subscription": "free"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str 
data = ubiops.OrganizationUpdate() # OrganizationUpdate 

# Update details of an organization
api_response = api_instance.organizations_update(organization_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 
 **data** | [**OrganizationUpdate**](OrganizationUpdate.md) | 

### Return type

[**OrganizationDetail**](OrganizationDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **organizations_usage_get**
> list[Usage] organizations_usage_get(organization_name, start_date=start_date, end_date=end_date, interval=interval)

Get organization usage

## Description
Get resource usage for the organization. It contains **the details of each metric aggregated per month.**

### Optional Parameters

- `start_date`: date indicating the start date to fetch usage data from. If omitted, results are generated for current subscription period.
- `end_date`: date indicating the end date to fetch usage data until. If omitted, results are generated for current subscription period.
- `interval`: interval for which the usage data is fetched. It can be 'day' or 'month'. It defaults to 'month'.

If no **start_date** or **end_date** is given, the current subscription period is used, e.g. if the usage details are requested on 01-12-2020 and the subscription started on 20-11-2020, the results will contain data from 20-11-2020 to 20-12-2020.
When **start_date** and **end_date** are given, this month period is used, e.g. if 12-11-2020 is given as start date and 12-12-2020 as end date, the results will contain data from 12-11-2020 to 12-12-2020.

### Response Structure

- `metric`: Metric name
- `object_type`: Type of object the metric was measured for (deployment_version or pipeline_version)
- `usage`: an array of objects each containing the following:
  - `start_date`: Timestamp denoting the start of the current subscription period or the provided date
  - `end_date`: Timestamp denoting the end of the current subscription period or the provided date
  - `value`: Aggregated metric value for the given unit over the given month

## Response Examples
2019-08-01 as start date and 2019-09-01 as end date

```
[
  {
    "object_type": "deployment_version",
    "metric": "credits",
    "usage": [
      {
        "start_date": "2019-08-01T00:00:00Z",
        "end_date": "2019-09-01T00:00:00Z",
        "value": 1484124
      } 
    ]
  },
  {
    "object_type": "deployment_version",
    "metric": "input_volume",
    "usage": [
      {
        "start_date": "2019-08-01T00:00:00Z",
        "end_date": "2019-09-01T00:00:00Z",
        "value": 1204
      } 
    ]
  },
  {
    "object_type": "deployment_version",
    "metric": "output_volume",
    "usage": [
      {
        "start_date": "2019-08-01T00:00:00Z",
        "end_date": "2019-09-01T00:00:00Z",
        "value": 1598
      } 
    ]
  },
  {
    "object_type": "pipeline_version",
    "metric": "input_volume",
    "usage": [
      {
        "start_date": "2019-08-01T00:00:00Z",
        "end_date": "2019-09-01T00:00:00Z",
        "value": 1840
      } 
    ]
  },
  {
    "object_type": "pipeline_version",
    "metric": "output_volume",
    "usage": [
      {
        "start_date": "2019-08-01T00:00:00Z",
        "end_date": "2019-09-01T00:00:00Z",
        "value": 400
      } 
    ]
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization_name = 'organization_name_example' # str 
start_date = str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')) # datetime  (optional)
end_date = str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')) # datetime  (optional)
interval = 'month' # str  (optional) (default to 'month')

# Get organization usage
api_response = api_instance.organizations_usage_get(organization_name, start_date=start_date, end_date=end_date, interval=interval)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization_name** | **str** | 
 **start_date** | **datetime** | [optional] 
 **end_date** | **datetime** | [optional] 
 **interval** | **str** | [optional] [default to &#39;month&#39;]

### Return type

[**list[Usage]**](Usage.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **permissions_list**
> list[PermissionList] permissions_list()

List the available permissions

## Description
List all the available permissions which can be used to create custom roles.

### Response Structure
A list of available permissions

- `name`: Name of the permission

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)


# List the available permissions
api_response = api_instance.permissions_list()
print(api_response)

# Close the connection
api_client.close()
```


### Parameters

This endpoint does not need any parameter.

### Return type

[**list[PermissionList]**](PermissionList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_audit_events_list**
> list[AuditList] pipeline_audit_events_list(project_name, pipeline_name, action=action, limit=limit, offset=offset)

List audit events for a pipeline

## Description
List all audit events for a pipeline including objects and attachments

### Optional Parameters
The following parameters should be given as query parameters:

- `action`: Type of action. It can be one of: create, update, delete, info.
- `limit`: The maximum number of audit events given back, default is 50
- `offset`: The number which forms the starting point of the audit events given back. If offset equals 2, then the first 2 events will be omitted from the list.

### Response Structure
A list of details of the audit events for a pipeline

- `id`: Unique identifier for the audit event (UUID)
- `date`: The date when the action was performed
- `action`: Type of action. It can be one of: create, update, delete, info. *info* action denotes that the action does not fall into create, update or delete categories.
- `user`: Email of the user who performed the action
- `event`: Description of the event
- `object_type`: Type of the object on which the action was performed
- `object_name`: Name of the object on which the action was performed. If the object is deleted at the time of listing audit events, this field is empty.

## Response Examples

```
[
  {
    "id": "44f326de-0ee3-4741-b72e-69e31b3ec55f",
    "date": "2020-10-23T12:21:12.460+00:00",
    "action": "create",
    "user": "user@example.com",
    "event": "Created pipeline object deployment-1 in version v1 of pipeline pipeline-1",
    "object_type": "pipeline",
    "object_name": "pipeline-1"
  },
  {
    "id": "905cdc19-a02c-4f09-b2fb-42d92da21bda",
    "date": "2020-10-23T12:21:37.247+00:00",
    "action": "update",
    "user": "user@example.com",
    "event": "Updated pipeline object deployment-object in version v1 of pipeline pipeline-1: name changed from deployment-1 to deployment-object",
    "object_type": "pipeline",
    "object_name": "pipeline-1"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
action = 'action_example' # str  (optional)
limit = 56 # int  (optional)
offset = 56 # int  (optional)

# List audit events for a pipeline
api_response = api_instance.pipeline_audit_events_list(project_name, pipeline_name, action=action, limit=limit, offset=offset)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **action** | **str** | [optional] 
 **limit** | **int** | [optional] 
 **offset** | **int** | [optional] 

### Return type

[**list[AuditList]**](AuditList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_batch_delete**
> object pipeline_requests_batch_delete(project_name, pipeline_name, data)

Delete multiple pipeline requests

## Description
Delete multiple pipeline requests for the default version of a pipeline. If one of the given pipeline requests does not exist, an error message is given and no request is deleted. A maximum of 100 pipeline requests can be deleted with this method.

### Required Parameters
A list of ids of the requests

## Request Examples

```
["2521378e-263e-4e2e-85e9-a96254b36536", "69eca481-8576-49e8-8e20-ea56f2005bcb"]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
data = ['request_id_1', 'request_id_2'] # list[str] 

# Delete multiple pipeline requests
api_response = api_instance.pipeline_requests_batch_delete(project_name, pipeline_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **data** | **list[str]** | 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_batch_get**
> list[PipelineRequestDetail] pipeline_requests_batch_get(project_name, pipeline_name, data)

Retrieve multiple pipeline requests

## Description
Retrieve multiple pipeline requests for the default version of a pipeline. If one of the given pipeline requests does not exist, an error message is given and no request is returned. A maximum of 100 pipeline requests can be retrieved with this method. The pipeline requests are NOT returned in the order they are given in.

### Required Parameters
A list of ids of the requests

## Request Examples

```
["2521378e-263e-4e2e-85e9-a96254b36536", "69eca481-8576-49e8-8e20-ea56f2005bcb"]
```

### Response Structure
A list of dictionaries containing the details of the retrieved pipeline requests with the following fields:

- `id`: Unique identifier for the pipeline request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request was made
- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'.
- `success`: A boolean value that indicates whether the pipeline request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed
- `request_data`: A dictionary (structured input type) or string (plain input type) containing the data that was sent when the request was created
- `result`: A dictionary (structured output type) or string (plain output type) containing the data connected to the pipeline end
- `deployment_requests`: A list of requests to the deployments in the pipeline. With the deployment request ids provided in this list, it's possible to collect the results of the deployment requests separately.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-063-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {
      "input_field": 23.5
    },
    "deployment_requests": [
      {
        "id": "4b9c8a81-b3ef-437a-8d35-187490eda3e4",
        "pipeline_object": "deployment-1-v1-object",
        "deployment": "deployment-1",
        "version": "v1"
      }
    ],
    "result": {
      "output_field": 23.5
    },
    "error_message": null
  },
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-063-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {
      "input_field": 23.5
    },
    "deployment_requests": [
      {
        "id": "5fa86ad1-7949-48f5-8e2c-210cce78f427",
        "pipeline_object": "deployment-1-v1-object",
        "deployment": "deployment-1",
        "version": "v1"
      }
    ],
    "result": {
      "output_field": 23.5
    },
    "error_message": null
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
data = ['request_id_1', 'request_id_2'] # list[str] 

# Retrieve multiple pipeline requests
api_response = api_instance.pipeline_requests_batch_get(project_name, pipeline_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **data** | **list[str]** | 

### Return type

[**list[PipelineRequestDetail]**](PipelineRequestDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_create**
> PipelineRequestCreateResponse pipeline_requests_create(project_name, pipeline_name, data, pipeline_timeout=pipeline_timeout, deployment_timeout=deployment_timeout)

Create a pipeline request

## Description
Make a direct request to the default version of a pipeline. This method returns all the results of the deployment requests made within the pipeline version.

### Required Parameters
The input for the request. In case of a structured pipeline, this is a dictionary which contains the input fields of the pipeline as keys. In case of a plain pipeline, give a string or list of strings.

### Optional Parameters
The following parameters should be given as query parameters:

- `pipeline_timeout`: Timeout for the entire pipeline request in seconds. The maximum allowed value is 7200 (2 hours) and the default value is 3600 (1 hour).
- `deployment_timeout`: Timeout for each deployment request in the pipeline in seconds. The maximum allowed value is 3600 (1 hour) and the default value is 300  (5 minutes).

## Request Examples
A structured pipeline request

```
{
  "pipeline-input-field-1": 5.0,
  "pipeline-input-field-2": "N"
}
```

A plain pipeline request

```
example-plain-data
```

### Response Structure

- `id`: Unique identifier for the pipeline request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request is made
- `success`: A boolean value that indicates whether the pipeline request was successful
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `deployment_requests`: A list of dictionaries containing the results of the deployment requests made for the version objects in the pipeline. The dictionaries contain the following fields:
    - `id`: Unique identifier for the deployment request
    - `pipeline_object`: Name of the object in the pipeline
    - `deployment`: Name of the deployment the request was made to
    - `version`: Name of the version the request was made to
    - `success`: A boolean value that indicates whether the deployment request was successful
    - `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `result`: A dictionary (structured output type) or string (plain output type) containing the data connected to the pipeline end

## Response Examples

```
{
  "id": "286f771b-6617-4985-ab49-12ed720e62b1",
  "pipeline": "pipeline-1",
  "version": "v1",
  "success": false,
  "error_message": "Error while processing a deployment request",
  "deployment_requests": [
    {
      "id": "a7524614-bdb7-41e1-b4c1-653bb72c30b4",
      "pipeline_object": "deployment-object-1",
      "success": true,
      "error_message": null
    },
    {
      "id": "fe322c50-58f8-4e67-b7d6-cba14273874e",
      "pipeline_object": "deployment-object-2",
      "success": false,
      "error_message": "Invalid message format"
    }
  ],
  "result": {
    "output_field": 23.5
  }
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
data = {'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'} # str or dict() 
pipeline_timeout = 56 # int  (optional)
deployment_timeout = 56 # int  (optional)

# Create a pipeline request
api_response = api_instance.pipeline_requests_create(project_name, pipeline_name, data, pipeline_timeout=pipeline_timeout, deployment_timeout=deployment_timeout)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **data** | **str or dict()** | 
 **pipeline_timeout** | **int** | [optional] 
 **deployment_timeout** | **int** | [optional] 

### Return type

[**PipelineRequestCreateResponse**](PipelineRequestCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_delete**
> pipeline_requests_delete(project_name, pipeline_name, request_id)

Delete a pipeline request

## Description
Delete a request for the default version of a pipeline. This action deletes all the deployment requests in the pipeline.

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
request_id = 'request_id_example' # str 

# Delete a pipeline request
api_instance.pipeline_requests_delete(project_name, pipeline_name, request_id)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_get**
> PipelineRequestSingleDetail pipeline_requests_get(project_name, pipeline_name, request_id, metadata_only=metadata_only)

Get a pipeline request

## Description
Get a request for the default version of a pipeline. With this method, the result of the request may be retrieved.

### Optional Parameters
The following parameters should be given as query parameters:

- `metadata_only`: A boolean value that indicates whether the response should include the request data and result. The default value is False.

### Response Structure
A dictionary containing the details of the pipeline request with the following fields:

- `id`: Unique identifier for the pipeline request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request was made
- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'.
- `success`: A boolean value that indicates whether the pipeline request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed
- `request_data`: A dictionary (structured input type) or string (plain input type) containing the data that was sent when the request was created
- `deployment_requests`: A list of requests of the deployments in the pipeline. With the deployment request ids provided in this list, it's possible to collect the results of the deployment requests separately.
- `result`: A dictionary (structured output type) or string (plain output type) containing the data connected to the pipeline end
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `created_by`: The email of the user that created the request. In case the request is created by a service, the field will have a "UbiOps" value.
- `notification_group`: Name of a notification group to send notifications (e.g., emails) when the request is completed
- `origin`: A dictionary containing the information on where the request originated from. It contains:
   - the pipeline (and version) names if the request is directly made to the pipeline
   - the request schedule name if the request is created via a request schedule

## Response Examples

```
{
  "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
  "pipeline": "pipeline-1",
  "version": "v1",
  "status": "pending",
  "success": true,
  "time_created": "2020-03-28T20:00:26.613+00:00",
  "time_started": "2020-03-28T20:00:41.276+00:00",
  "time_completed": "2020-03-28T20:00:42.241+00:00",
  "request_data": {
    "input_field": 23.5
  },
  "deployment_requests": [
    {
      "id": "4b9c8a81-b3ef-437a-8d35-187490eda3e4",
      "pipeline_object": "deployment-1-v1-object",
      "deployment": "deployment-1",
      "version": "v1"
    }
  ],
  "result": {
    "output_field": 23.5
  },
  "error_message": null,
  "created_by": "my.example.user@ubiops.com",
  "notification_group": "notification-group-1",
  "origin": {
    "pipeline": "pipeline-1",
    "pipeline"_version": "v1"
  }
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
request_id = 'request_id_example' # str 
metadata_only = True # bool  (optional)

# Get a pipeline request
api_response = api_instance.pipeline_requests_get(project_name, pipeline_name, request_id, metadata_only=metadata_only)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 
 **metadata_only** | **bool** | [optional] 

### Return type

[**PipelineRequestSingleDetail**](PipelineRequestSingleDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_requests_list**
> list[PipelineRequestList] pipeline_requests_list(project_name, pipeline_name, status=status, success=success, limit=limit, offset=offset, sort=sort, start_date=start_date, end_date=end_date, search_id=search_id)

List pipeline requests

## Description
List all requests for the default version of a pipeline

### Optional Parameters
The following parameters should be given as query parameters:

- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'.
- `success`: A boolean value that indicates whether the pipeline request was successful
- `limit`: The maximum number of requests given back, default is 50
- `offset`: The number which forms the starting point of the requests given back. If offset equals 2, then the first 2 requests will be omitted from the list.
- `sort`: Direction of sorting according to the creation date of the request, can be 'asc' or 'desc'. The default sorting is done in descending order.
- `start_date`: Start date of the interval for which the requests are retrieved, looking at the creation date of the request
- `end_date`: End date of the interval for which the requests are retrieved, looking at the creation date of the request
- `search_id`: A string to search inside request ids. It will filter all request ids that contain this string

If no start or end date is provided, the most recent requests are returned.

### Response Structure
A list of dictionaries containing the details of the pipeline requests with the following fields:

- `id`: Unique identifier for the pipeline request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request was made
- `status`: Status of the request
- `success`: A boolean value that indicates whether the pipeline request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
status = 'status_example' # str  (optional)
success = True # bool  (optional)
limit = 56 # int  (optional)
offset = 56 # int  (optional)
sort = 'sort_example' # str  (optional)
start_date = 'start_date_example' # str  (optional)
end_date = 'end_date_example' # str  (optional)
search_id = 'search_id_example' # str  (optional)

# List pipeline requests
api_response = api_instance.pipeline_requests_list(project_name, pipeline_name, status=status, success=success, limit=limit, offset=offset, sort=sort, start_date=start_date, end_date=end_date, search_id=search_id)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **status** | **str** | [optional] 
 **success** | **bool** | [optional] 
 **limit** | **int** | [optional] 
 **offset** | **int** | [optional] 
 **sort** | **str** | [optional] 
 **start_date** | **str** | [optional] 
 **end_date** | **str** | [optional] 
 **search_id** | **str** | [optional] 

### Return type

[**list[PipelineRequestList]**](PipelineRequestList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_object_environment_variables_list**
> list[InheritedEnvironmentVariableList] pipeline_version_object_environment_variables_list(project_name, name, pipeline_name, version)

List pipeline object environment variables

## Description
List environment variables accessible to objects in the pipeline version

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from - can be `project`, `deployment`, or `version`
- `inheritance_name`: Name of the parent object that this variable is inherited from

## Response Examples

```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": "deployment",
    "inheritance_name": "deployment_name"
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": "project",
    "inheritance_name": "project_name"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
name = 'name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
version = 'version_example' # str 

# List pipeline object environment variables
api_response = api_instance.pipeline_version_object_environment_variables_list(project_name, name, pipeline_name, version)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 

### Return type

[**list[InheritedEnvironmentVariableList]**](InheritedEnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_batch_delete**
> object pipeline_version_requests_batch_delete(project_name, pipeline_name, version, data)

Delete multiple pipeline version requests

## Description
Delete multiple requests for a pipeline version. If one of the given pipeline requests does not exist, an error message is given and no request is deleted. A maximum of 100 pipeline requests can be deleted with this method.

### Required Parameters
A list of ids of the requests

## Request Examples

```
["2521378e-263e-4e2e-85e9-a96254b36536", "69eca481-8576-49e8-8e20-ea56f2005bcb"]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
version = 'version_example' # str 
data = ['request_id_1', 'request_id_2'] # list[str] 

# Delete multiple pipeline version requests
api_response = api_instance.pipeline_version_requests_batch_delete(project_name, pipeline_name, version, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 
 **data** | **list[str]** | 

### Return type

**object**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_batch_get**
> list[PipelineRequestDetail] pipeline_version_requests_batch_get(project_name, pipeline_name, version, data)

Retrieve multiple pipeline version requests

## Description
Retrieve multiple requests for a pipeline version. If one of the given pipeline requests does not exist, an error message is given and no request is returned. A maximum of 100 pipeline version requests can be retrieved with this method. The pipeline version requests are NOT returned in the order they are given in.

### Required Parameters
A list of ids of the requests

## Request Examples

```
["2521378e-263e-4e2e-85e9-a96254b36536", "69eca481-8576-49e8-8e20-ea56f2005bcb"]
```

### Response Structure
A list of dictionaries containing the details of the retrieved pipeline requests with the following fields:

- `id`: Unique identifier for the pipeline request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request was made
- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'.
- `success`: A boolean value that indicates whether the pipeline request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed
- `request_data`: A dictionary (structured input type) or string (plain input type) containing the data that was sent when the request was created
- `result`: A dictionary (structured output type) or string (plain output type) containing the data connected to the pipeline end
- `deployment_requests`: A list of requests to the deployments in the pipeline. With the deployment request ids provided in this list, it's possible to collect the results of the deployment requests separately.
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-063-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {
      "input_field": 23.5
    },
    "deployment_requests": [
      {
        "id": "4b9c8a81-b3ef-437a-8d35-187490eda3e4",
        "pipeline_object": "deployment-1-v1-object",
        "deployment": "deployment-1",
        "version": "v1"
      }
    ],
    "result": {
      "output_field": 23.5
    },
    "error_message": null
  },
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-063-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00",
    "request_data": {
      "input_field": 23.5
    },
    "deployment_requests": [
      {
        "id": "5fa86ad1-7949-48f5-8e2c-210cce78f427",
        "pipeline_object": "deployment-1-v1-object",
        "deployment": "deployment-1",
        "version": "v1"
      }
    ],
    "result": {
      "output_field": 23.5
    },
    "error_message": null
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
version = 'version_example' # str 
data = ['request_id_1', 'request_id_2'] # list[str] 

# Retrieve multiple pipeline version requests
api_response = api_instance.pipeline_version_requests_batch_get(project_name, pipeline_name, version, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 
 **data** | **list[str]** | 

### Return type

[**list[PipelineRequestDetail]**](PipelineRequestDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_create**
> PipelineRequestCreateResponse pipeline_version_requests_create(project_name, pipeline_name, version, data, pipeline_timeout=pipeline_timeout, deployment_timeout=deployment_timeout)

Create a pipeline version request

## Description
Make a direct request to a pipeline version. This method returns all the results of the deployment requests made within the pipeline version.

### Required Parameters
The input for the request. In case of a structured pipeline, this is a dictionary which contains the input fields of the pipeline as keys. In case of a plain pipeline, give a string or list of strings.

### Optional Parameters
The following parameters should be given as query parameters:

- `pipeline_timeout`: Timeout for the entire pipeline request in seconds. The maximum allowed value is 7200 (2 hours) and the default value is 3600 (1 hour).
- `deployment_timeout`: Timeout for each deployment request in the pipeline in seconds. The maximum allowed value is 3600 (1 hour) and the default value is 300 (5 minutes).

## Request Examples
A structured pipeline request

```
{
  "pipeline-input-field-1": 5.0,
  "pipeline-input-field-2": "N"
}
```

A plain pipeline request

```
example-plain-data
```

### Response Structure

- `id`: Unique identifier for the pipeline request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request is made
- `success`: A boolean value that indicates whether the pipeline request was successful
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `deployment_requests`: A list of dictionaries containing the results of the deployment requests made for the version objects in the pipeline. The dictionaries contain the following fields:
    - `id`: Unique identifier for the deployment request
    - `pipeline_object`: Name of the object in the pipeline
    - `deployment`: Name of the deployment the request was made to
    - `version`: Name of the version the request was made to
    - `success`: A boolean value that indicates whether the deployment request was successful
    - `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `result`: A dictionary (structured output type) or string (plain output type) containing the data connected to the pipeline end

## Response Examples

```
{
  "id": "286f771b-6617-4985-ab49-12ed720e62b1",
  "project": "project-1",
  "pipeline": "pipeline-1",
  "version": "v1",
  "success": false,
  "error_message": "Error while processing a deployment request",
  "deployment_requests": [
    {
      "id": "a7524614-bdb7-41e1-b4c1-653bb72c30b4",
      "pipeline_object": "deployment-object-1",
      "success": true,
      "error_message": null
    },
    {
      "id": "fe322c50-58f8-4e67-b7d6-cba14273874e",
      "pipeline_object": "deployment-object-2",
      "success": false,
      "error_message": "Invalid message format"
    }
  ],
  "result": {
    "output_field": 23.5
  }
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
version = 'version_example' # str 
data = {'input-field-1': 'input-value-1', 'input-field-2': 'input-value-2'} # str or dict() 
pipeline_timeout = 56 # int  (optional)
deployment_timeout = 56 # int  (optional)

# Create a pipeline version request
api_response = api_instance.pipeline_version_requests_create(project_name, pipeline_name, version, data, pipeline_timeout=pipeline_timeout, deployment_timeout=deployment_timeout)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 
 **data** | **str or dict()** | 
 **pipeline_timeout** | **int** | [optional] 
 **deployment_timeout** | **int** | [optional] 

### Return type

[**PipelineRequestCreateResponse**](PipelineRequestCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_delete**
> pipeline_version_requests_delete(project_name, pipeline_name, request_id, version)

Delete a pipeline version request

## Description
Delete a request for a pipeline version. This action deletes all the deployment requests in the pipeline.

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
request_id = 'request_id_example' # str 
version = 'version_example' # str 

# Delete a pipeline version request
api_instance.pipeline_version_requests_delete(project_name, pipeline_name, request_id, version)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 
 **version** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_get**
> PipelineRequestSingleDetail pipeline_version_requests_get(project_name, pipeline_name, request_id, version, metadata_only=metadata_only)

Get a pipeline version request

## Description
Get a request for a pipeline version. With this method, the result of a request may be retrieved.

### Optional Parameters
The following parameters should be given as query parameters:

- `metadata_only`: A boolean value that indicates whether the response should include the request data and result. The default value is False.

### Response Structure
A dictionary containing the details of the pipeline version request with the following fields:

- `id`: Unique identifier for the pipeline version request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request was made
- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'.
- `success`: A boolean value that indicates whether the pipeline version request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed
- `request_data`: A dictionary (structured input type) or string (plain input type) containing the data that was sent when the request was created
- `deployment_requests`: A list of requests of the deployments in the pipeline. With the deployment request ids provided in this list, it's possible to collect the results of the deployment requests separately.
- `result`: A dictionary (structured output type) or string (plain output type) containing the data connected to the pipeline end
- `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
- `created_by`: The email of the user that created the request. In case the request is created by a service, the field will have a "UbiOps" value.
- `notification_group`: Name of a notification group to send notifications (e.g., emails) when the request is completed

## Response Examples

```
{
  "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
  "pipeline": "pipeline-1",
  "version": "v1",
  "status": "pending",
  "success": true,
  "time_created": "2020-03-28T20:00:26.613+00:00",
  "time_started": "2020-03-28T20:00:41.276+00:00",
  "time_completed": "2020-03-28T20:00:42.241+00:00",
  "request_data": {
    "input_field": 23.5
  },
  "deployment_requests": [
    {
      "id": "4b9c8a81-b3ef-437a-8d35-187490eda3e4",
      "pipeline_object": "deployment-1-v1-object",
      "deployment": "deployment-1",
      "version": "v1"
    }
  ],
  "result": {
    "output_field": 23.5
  },
  "error_message": null,
  "created_by": "my.example.user@ubiops.com",
  "notification_group": "notification-group-1"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
request_id = 'request_id_example' # str 
version = 'version_example' # str 
metadata_only = True # bool  (optional)

# Get a pipeline version request
api_response = api_instance.pipeline_version_requests_get(project_name, pipeline_name, request_id, version, metadata_only=metadata_only)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **request_id** | **str** | 
 **version** | **str** | 
 **metadata_only** | **bool** | [optional] 

### Return type

[**PipelineRequestSingleDetail**](PipelineRequestSingleDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_version_requests_list**
> list[PipelineRequestList] pipeline_version_requests_list(project_name, pipeline_name, version, status=status, success=success, limit=limit, offset=offset, sort=sort, start_date=start_date, end_date=end_date, search_id=search_id)

List pipeline version requests

## Description
List all requests for a pipeline version

### Optional Parameters
The following parameters should be given as query parameters:

- `status`: Status of the request. Can be 'pending', 'processing', 'failed' or 'completed'.
- `success`: A boolean value that indicates whether the pipeline version request was successful
- `limit`: The maximum number of requests given back, default is 50
- `offset`: The number which forms the starting point of the requests given back. If offset equals 2, then the first 2 requests will be omitted from the list.
- `sort`: Direction of sorting according to the creation date of the request, can be 'asc' or 'desc'. The default sorting is done in descending order.
- `start_date`: Start date of the interval for which the requests are retrieved, looking at the creation date of the request
- `end_date`: End date of the interval for which the requests are retrieved, looking at the creation date of the request
- `search_id`: A string to search inside request ids. It will filter all request ids that contain this string

If no start or end date is provided, the most recent requests are returned.

### Response Structure
A list of dictionaries containing the details of the pipeline version requests with the following fields:

- `id`: Unique identifier for the pipeline version request
- `pipeline`: Name of the pipeline for which the request is made
- `version`: Name of the pipeline version for which the request was made
- `status`: Status of the request
- `success`: A boolean value that indicates whether the pipeline version request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
version = 'version_example' # str 
status = 'status_example' # str  (optional)
success = True # bool  (optional)
limit = 56 # int  (optional)
offset = 56 # int  (optional)
sort = 'sort_example' # str  (optional)
start_date = 'start_date_example' # str  (optional)
end_date = 'end_date_example' # str  (optional)
search_id = 'search_id_example' # str  (optional)

# List pipeline version requests
api_response = api_instance.pipeline_version_requests_list(project_name, pipeline_name, version, status=status, success=success, limit=limit, offset=offset, sort=sort, start_date=start_date, end_date=end_date, search_id=search_id)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 
 **status** | **str** | [optional] 
 **success** | **bool** | [optional] 
 **limit** | **int** | [optional] 
 **offset** | **int** | [optional] 
 **sort** | **str** | [optional] 
 **start_date** | **str** | [optional] 
 **end_date** | **str** | [optional] 
 **search_id** | **str** | [optional] 

### Return type

[**list[PipelineRequestList]**](PipelineRequestList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_versions_create**
> PipelineVersionDetail pipeline_versions_create(project_name, pipeline_name, data)

Create pipeline versions

## Description
Create a version for a pipeline. The first version of a pipeline is set as default.
Provide the parameter 'monitoring' as the name of a notification group to send monitoring notifications to. A notification will be sent in the case of a failed/recovered request. Pass `null` to switch off monitoring notifications for this version.
Provide the parameter 'default_notification_group' as the name of a notification group to send notifications when requests for the version are completed. Pass `null` to switch off request notifications for this version.

### Required Parameters

- `version`: Name of the version of the pipeline

### Optional Parameters

- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version. It defaults to 604800 seconds (1 week).
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored
- `objects`: List of pipeline version objects
- `attachments`: List of pipeline version object attachments

## Request Examples

```
{
  "version": "v1"
}
```


```
{
  "version": "v1",
  "description": "my description",
  "labels": {
    "type": "production"
  },
  "monitoring": "notification-group-1",
  "request_retention_time": 604800,
  "request_retention_mode": "full"
}
```

A pipeline version with objects and attachments

```
{
  "version": "v1",
  "description": "my description",
  "labels": {
    "type": "production"
  },
  "monitoring": ["test@example.com"],
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [
    {
      "name": "object-1",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1"
    }
  ],
  "attachments": [
    {
      "destination_name": "object-1",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    }
  ]
}
```

### Response Structure
Details of the created pipeline version

- `id`: Unique identifier for the pipeline version (UUID)
- `pipeline`: Name of the pipeline to which the version is associated
- `version`: Name of the version of the pipeline
- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline version was created
- `last_updated`: The date when the pipeline version was last updated
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following: *none*, *metadata* or *full*.
- `objects`: List of pipeline version objects
- `attachments`: List of pipeline version object attachments

## Response Examples

```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": "notification-group-1",
  "default_notification_group": null,
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [],
  "attachments": []
}
```


```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": ["test@example.com"],
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [
    {
      "id": "38549ff5-5bf0-4803-8571-236077c77e62",
      "name": "object-1",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1",
      "input_type": "structured",
      "output_type": "structured",
      "configuration": {},
      "input_fields": [
        {
          "name": "input",
          "data_type": "int"
        }
      ],
      "output_fields": [
        {
          "name": "output",
          "data_type": "int"
        }
      ]
    }
  ],
  "attachments": [
    {
      "destination_name": "object-1",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    }
  ]
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
data = ubiops.PipelineVersionCreate() # PipelineVersionCreate 

# Create pipeline versions
api_response = api_instance.pipeline_versions_create(project_name, pipeline_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **data** | [**PipelineVersionCreate**](PipelineVersionCreate.md) | 

### Return type

[**PipelineVersionDetail**](PipelineVersionDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_versions_delete**
> pipeline_versions_delete(project_name, pipeline_name, version)

Delete pipeline version

## Description
Delete a pipeline version. This will also delete all objects and attachments in the pipeline version.

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
version = 'version_example' # str 

# Delete pipeline version
api_instance.pipeline_versions_delete(project_name, pipeline_name, version)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_versions_get**
> PipelineVersionDetail pipeline_versions_get(project_name, pipeline_name, version)

Get pipeline version

## Description
Get the details of a single pipeline version

### Response Structure
Details of the pipeline version

- `id`: Unique identifier for the pipeline version (UUID)
- `pipeline`: Name of the pipeline to which the version is associated
- `version`: Name of the version of the pipeline
- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline version was created
- `last_updated`: The date when the pipeline version was last updated
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored
- `objects`: List of pipeline version objects
- `attachments`: List of pipeline version object attachments

## Response Examples

```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": "notification-group-1",
  "default_notification_group": null,
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [],
  "attachments": []
}
```


```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": ["test@example.com"],
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [
    {
      "id": "38549ff5-5bf0-4803-8571-236077c77e62",
      "name": "object-1",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1",
      "input_type": "structured",
      "output_type": "structured",
      "configuration": {},
      "input_fields": [
        {
          "name": "input",
          "data_type": "int"
        }
      ],
      "output_fields": [
        {
          "name": "output",
          "data_type": "int"
        }
      ]
    }
  ],
  "attachments": [
    {
      "destination_name": "object-1",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    }
  ]
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
version = 'version_example' # str 

# Get pipeline version
api_response = api_instance.pipeline_versions_get(project_name, pipeline_name, version)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 

### Return type

[**PipelineVersionDetail**](PipelineVersionDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_versions_list**
> list[PipelineVersionList] pipeline_versions_list(project_name, pipeline_name, labels=labels)

List pipeline versions

## Description
Pipeline versions can be filtered according to the labels they have by giving labels as a query parameter. Pipeline versions that have at least one of the labels on which is filtered, are returned.

### Optional Parameters

- `labels`: Filter on labels of the pipeline version. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.

### Response Structure
A list of details of the versions of the pipeline

- `id`: Unique identifier for the pipeline version (UUID)
- `pipeline`: Name of the pipeline to which the version is associated
- `version`: Name of the version of the pipeline
- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline version was created
- `last_updated`: The date when the pipeline version was last updated
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored

## Response Examples

```
[
  {
    "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
    "pipeline": "pipeline-1",
    "version": "v1",
    "description": "my description",
    "labels": {
      "tag": "production"
    },
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z",
    "monitoring": "notification-group-1",
    "default_notification_group": null,
    "request_retention_time": 604800,
    "request_retention_mode": "full"
  },
  {
    "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
    "pipeline": "pipeline-1",
    "version": "v1",
    "description": "my description",
    "labels": {
      "tag": "production"
    },
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z",
    "monitoring": "notification-group-2",
    "default_notification_group": "notification-group-2",
    "request_retention_time": 86400,
    "request_retention_mode": "metadata"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
labels = 'labels_example' # str  (optional)

# List pipeline versions
api_response = api_instance.pipeline_versions_list(project_name, pipeline_name, labels=labels)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **labels** | **str** | [optional] 

### Return type

[**list[PipelineVersionList]**](PipelineVersionList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipeline_versions_update**
> PipelineVersionDetail pipeline_versions_update(project_name, pipeline_name, version, data)

Update pipeline version

## Description
Update a pipeline version. When updating labels, the labels will replace the existing value for labels.
Provide the parameter 'monitoring' as the name of a notification group to send monitoring notifications to. A notification will be sent in the case of a failed/recovered request. Pass `null` to switch off monitoring notifications for this version.
Provide the parameter 'default_notification_group' as the name of a notification group to send notifications when requests for the version are completed. Pass `null` to switch off request notifications for this version.

**Attention:** *In case either the `objects` or `attachments` parameter is null or an empty list, all of the objects or attachments of the pipeline will be removed.*

### Optional Parameters

- `version`: Name of the version of the pipeline
- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following:
    - *none* - the requests will not be stored
    - *metadata* - only the metadata of the requests will be stored
    - *full* - both the metadata and input/output of the requests will be stored
- `objects`: List of pipeline version objects
- `attachments`: List of pipeline version object attachments

## Request Examples

```
{
  "version": "v1",
  "description": "my description",
  "labels": {
    "type": "production"
  },
  "monitoring": "notification-group-1"
}
```

Updating a pipeline version with new objects and attachments

```
{
  "version": "v1",
  "description": "my description",
  "labels": {
    "type": "production"
  },
  "monitoring": ["test@example.com"],
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [
    {
      "name": "object-1",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1"
    }
  ],
  "attachments": [
    {
      "destination_name": "object-1",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    }
  ]
}
```

Updating a pipeline version by removing objects and attachments

```
{
  "version": "v1",
  "description": "my description",
  "labels": {
    "type": "production"
  },
  "monitoring": ["test@example.com"],
  "objects": null,
  "attachments": null
}
```

### Response Structure
Details of the created pipeline

- `id`: Unique identifier for the pipeline version (UUID)
- `pipeline`: Name of the pipeline to which the version is associated
- `version`: Name of the version of the pipeline
- `description`: Description of the pipeline version
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline version was created
- `last_updated`: The date when the pipeline version was last updated
- `monitoring`: Name of a notification group which contain contacts to send monitoring notifications
- `default_notification_group`: Name of a notification group which contain contacts to send notifications when requests for the version are completed
- `request_retention_time`: Number of seconds to store requests to the pipeline version
- `request_retention_mode`: Mode of request retention for requests to the pipeline version. It can be one of the following: *none*, *metadata* or *full*.
- `objects`: List of pipeline version objects
- `attachments`: List of pipeline version object attachments

## Response Examples

```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": "notification-group-1",
  "default_notification_group": null,
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [],
  "attachments": []
}
```


```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "pipeline": "pipeline-1",
  "version": "v1",
  "description": "my description",
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-06-22T18:04:76.123754Z",
  "monitoring": ["test@example.com"],
  "request_retention_time": 604800,
  "request_retention_mode": "full",
  "objects": [
    {
      "id": "38549ff5-5bf0-4803-8571-236077c77e62",
      "name": "object-1",
      "reference_name": "deployment-1",
      "reference_type": "deployment",
      "version": "v1",
      "input_type": "structured",
      "output_type": "structured",
      "configuration": {},
      "input_fields": [
        {
          "name": "input",
          "data_type": "int"
        }
      ],
      "output_fields": [
        {
          "name": "output",
          "data_type": "int"
        }
      ]
    }
  ],
  "attachments": [
    {
      "destination_name": "object-1",
      "sources": [
        {
          "source_name": "pipeline_start",
          "mapping": [
            {
              "source_field_name": "pipeline-input",
              "destination_field_name": "input"
            }
          ]
        }
      ]
    }
  ]
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
version = 'version_example' # str 
data = ubiops.PipelineVersionUpdate() # PipelineVersionUpdate 

# Update pipeline version
api_response = api_instance.pipeline_versions_update(project_name, pipeline_name, version, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **version** | **str** | 
 **data** | [**PipelineVersionUpdate**](PipelineVersionUpdate.md) | 

### Return type

[**PipelineVersionDetail**](PipelineVersionDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipelines_create**
> PipelineCreateResponse pipelines_create(project_name, data)

Create pipelines

## Description
Create a pipeline in a project.

The input_fields represent the fields that the input data for pipeline requests should contain. When an object is attached to the pipeline, it means that the input data will be forwarded to these objects.

### Required Parameters

- `name`: Name of the pipeline. It is unique within a project.
- `input_type`: Type of the pipeline input. It can be either structured or plain.
- `input_fields`: A list of input fields with name, data_type and (optional) widget. In case of plain pipelines, the input_fields should be omitted or given as an empty list. For structured pipelines, it is possible to leave this field empty.
- `output_type`: Type of the pipeline output. It can be either structured or plain.
- `output_fields`: A list of output fields with name, data_type and (optional) widget. In case of plain pipelines, the output_fields should be omitted or given as an empty list. For structured pipelines, it is possible to leave this field empty.

### Optional Parameters

- `description`: Description of the pipeline
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Request Examples
A structured pipeline

```
{
  "name": "pipeline-1",
  "input_type": "structured",
  "input_fields": [
    {
      "name": "field-1",
      "data_type": "int"
    },
    {
      "name": "field-2",
      "data_type": "double"
    }
  ],
  "output_type": "structured",
  "output_fields": [
    {
      "name": "field-1",
      "data_type": "int"
    },
    {
      "name": "field-2",
      "data_type": "double"
    }
  ]
}
```

A plain pipeline

```
{
  "name": "pipeline-2",
  "input_type": "plain",
  "output_type": "plain",
  "description": "my description"
}
```

A structured pipeline with input/output field widgets

```
{
  "name": "pipeline-1",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "field-1",
      "data_type": "int",
      "widget": {
        "type": "slider",
        "configuration": {"min": 0, "max": 10, "default": 4, "step": 2}
      }
    },
    {
      "name": "field-2",
      "data_type": "double",
      "widget": {
        "type": "numberbox",
        "configuration": {"min": 0, "max": 1, "default": 0.5, "step": 0.1}
      }
    }
  ],
  "output_fields": [
    {
      "name": "field-1",
      "data_type": "double",
      "widget": {
        "type": "textbox",
        "configuration": {}
      }
    },
    {
      "name": "field-2",
      "data_type": "double",
      "widget": {
        "type": "textbox",
        "configuration": {}
      }
    }
  ]
}
```

### Response Structure
Details of the created pipeline

- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `description`: Description of the pipeline
- `project`: Project name in which the pipeline is created
- `input_type`: Type of the pipeline input
- `input_fields`: A list of pipeline input fields with name, data_type and widget
- `output_type`: Type of the pipeline output
- `output_fields`: A list of pipeline output fields with name, data_type and widget
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated

## Response Examples

```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "name": "pipeline-1",
  "project": "project-1",
  "description": "my description",
  "input_type": "structured",
  "input_fields": [
    {
      "name": "field-1",
      "data_type": "int",
      "widget": {}
    },
    {
      "name": "field-2",
      "data_type": "double",
      "widget": {}
    }
  ],
  "output_type": "structured",
  "output_fields": [
    {
      "name": "field-1",
      "data_type": "int",
      "widget": {}
    },
    {
      "name": "field-2",
      "data_type": "double",
      "widget": {}
    }
  ],
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-03-24T09:43:51.791253Z",
  "last_updated": "2020-03-24T09:43:51.791253Z"
}
```


```
{
  "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
  "name": "pipeline-2",
  "project": "project-1",
  "description": "my description",
  "input_type": "plain",
  "input_fields": [],
  "output_type": "plain",
  "output_fields": [],
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-05-12T16:23:15.456812Z"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
data = ubiops.PipelineCreate() # PipelineCreate 

# Create pipelines
api_response = api_instance.pipelines_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**PipelineCreate**](PipelineCreate.md) | 

### Return type

[**PipelineCreateResponse**](PipelineCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipelines_delete**
> pipelines_delete(project_name, pipeline_name)

Delete a pipeline

## Description
Delete a pipeline. This will also delete all versions of the pipeline.

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 

# Delete a pipeline
api_instance.pipelines_delete(project_name, pipeline_name)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipelines_get**
> PipelineDetail pipelines_get(project_name, pipeline_name)

Get details of a pipeline

## Description
Get the details of a single pipeline

### Response Structure
Details of the pipeline

- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `description` Description of the pipeline
- `project`: Project name in which the pipeline is defined
- `input_type`: Type of the pipeline input
- `input_fields`: A list of pipeline input fields with name, data_type and widget
- `output_type`: Type of the pipeline output
- `output_fields`: A list of pipeline output fields with name, data_type and widget
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated
- `default_version`: Default version of the pipeline.  If it does not have a default version, it is not set.

## Response Examples

```
{
  "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
  "name": "pipeline-2",
  "project": "project-1",
  "description": "my description",
  "input_type": "plain",
  "input_fields": [],
  "output_type": "plain",
  "output_fields": [],
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-03-24T09:43:51.791253Z",
  "last_updated": "2020-05-19T11:52:21.163270Z",
  "default_version": "v1"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 

# Get details of a pipeline
api_response = api_instance.pipelines_get(project_name, pipeline_name)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 

### Return type

[**PipelineDetail**](PipelineDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipelines_list**
> list[PipelineList] pipelines_list(project_name, labels=labels)

List pipelines

## Description
Pipelines can be filtered according to the labels they have by giving labels as a query parameter. Pipelines that have at least one of the labels on which is filtered, are returned.

### Optional Parameters

- `labels`: Filter on labels of the pipeline. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.

### Response Structure
A list of details of the pipelines in the project

- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `project`: Project name in which the pipeline is defined
- `description`: Description of the pipeline
- `input_type`: Type of the pipeline input
- `input_fields`: A list of pipeline input fields with name and data_type
- `output_type`: Type of the pipeline output
- `output_fields`: A list of pipeline output fields with name and data_type
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated

## Response Examples

```
[
  {
    "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
    "name": "pipeline-1",
    "project": "project-1",
    "description": "my description",
    "input_type": "structured",
    "input_fields": [
      {
        "name": "field-1",
        "data_type": "int"
      },
      {
        "name": "field-2",
        "data_type": "double"
      }
    ],
    "output_type": "structured",
    "output_fields": [
      {
        "name": "field-1",
        "data_type": "int"
      },
      {
        "name": "field-2",
        "data_type": "double"
      }
    ],
    "labels": {
      "tag": "production"
    },
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-06-22T18:04:76.123754Z"
  },
  {
    "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
    "name": "pipeline-2",
    "project": "project-1",
    "description": "my description",
    "input_type": "plain",
    "input_fields": [],
    "output_type": "plain",
    "output_fields": [],
    "labels": {
      "tag": "production"
    },
    "creation_date": "2020-03-24T09:43:51.791253Z",
    "last_updated": "2020-05-19T11:52:21.163270Z"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
labels = 'labels_example' # str  (optional)

# List pipelines
api_response = api_instance.pipelines_list(project_name, labels=labels)
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

[**list[PipelineList]**](PipelineList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **pipelines_update**
> PipelineDetail pipelines_update(project_name, pipeline_name, data)

Update a pipeline

## Description
Update a pipeline. All necessary fields are validated again. When updating labels, the labels will replace the existing value for labels.

### Optional Parameters

- `name`: New name for the pipeline
- `description`: New description for the pipeline
- `labels`: New dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label. The new labels will replace the existing value for labels.
- `input_type`: New type for the pipeline input. It is possible to change the type from plain to structured and vice versa.
- `input_fields`: New input fields for the pipeline
- `output_type`: New type for the pipeline output. It is possible to change the type from plain to structured and vice versa.
- `output_fields`: New output fields for the pipeline
- `default_version`: Name of a version of this pipeline which will be assigned as default

If the input type of pipeline is updated to plain, the input fields are deleted. In this case, input_fields should either be omitted or provided as en empty list.
If the input type of pipeline is updated to structured, the old input fields are deleted, if there existed any. The new fields are created, if any is provided. If one or more old fields need to be kept, they must be provided again.
The same goes for updating the pipeline output.

**To delete the input/output fields of a pipeline**, provide an empty list for input_fields/output_fields field.

## Request Examples

```
{
  "name": "new-pipeline-name"
}
```


```
{
  "description": "New pipeline description",
  "labels": {
    "tag": "production"
  }
}
```


```
{
  "input_type": "plain"
}
```

```
{
  "input_type": "structured",
  "input_fields": [
    {
      "name": "new-field-1",
      "data_type": "array_double",
      "widget": {}
    },
    {
      "name": "new-field-2",
      "data_type": "array_string",
      "widget": {}
    }
  ]
}
```

```
{
  "input_type": "structured",
  "input_fields": []
}
```

```
{
  "output_type": "structured",
  "output_fields": [
    {
      "name": "new-field-1",
      "data_type": "array_double",
      "widget": {}
    },
    {
      "name": "new-field-2",
      "data_type": "array_string",
      "widget": {}
    }
  ]
}
```

### Response Structure
Details of the updated pipeline

- `id`: Unique identifier for the pipeline (UUID)
- `name`: Name of the pipeline
- `project`: Project name in which the pipeline is defined
- `description`: Description for the pipeline
- `input_type`: Type of the pipeline input
- `input_fields`: A list of pipeline input fields with name, data_type and widget
- `output_type`: Type of the pipeline output
- `output_fields`: A list of pipeline output fields with name, data_type and widget
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the pipeline was created
- `last_updated`: The date when the pipeline was last updated
- `default_version`: Default version of the pipeline.  If it does not have a default version, it is not set.

## Response Examples

```
{
  "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
  "name": "new-pipeline-name",
  "project": "project-1",
  "description": "my description",
  "input_type": "structured",
  "input_fields": [
    {
      "name": "new-field-1",
      "data_type": "array_double",
      "widget": {}
    },
    {
      "name": "new-field-2",
      "data_type": "array_string",
      "widget": {}
    }
  ],
  "output_type": "structured",
  "output_fields": [
    {
      "name": "new-field-1",
      "data_type": "array_double",
      "widget": {}
    },
    {
      "name": "new-field-2",
      "data_type": "array_string",
      "widget": {}
    }
  ],
  "labels": {
    "tag": "production"
  },
  "creation_date": "2020-03-24T09:43:51.791253Z",
  "last_updated": "2020-05-19T11:52:21.163270Z",
  "default_version": "v1"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
pipeline_name = 'pipeline_name_example' # str 
data = ubiops.PipelineUpdate() # PipelineUpdate 

# Update a pipeline
api_response = api_instance.pipelines_update(project_name, pipeline_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **pipeline_name** | **str** | 
 **data** | [**PipelineUpdate**](PipelineUpdate.md) | 

### Return type

[**PipelineDetail**](PipelineDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_audit_events_list**
> list[AuditList] project_audit_events_list(project_name, action=action, limit=limit, offset=offset)

List audit events in a project

## Description
List all audit events in a project including all objects

### Optional Parameters
The following parameters should be given as query parameters:

- `action`: Type of action. It can be one of: create, update, delete, info.
- `limit`: The maximum number of audit events given back, default is 50
- `offset`: The number which forms the starting point of the audit events given back. If offset equals 2, then the first 2 events will be omitted from the list.

### Response Structure
A list of details of the audit events in the project

- `id`: Unique identifier for the audit event (UUID)
- `date`: The date when the action was performed
- `action`: Type of action. It can be one of: create, update, delete, info. *info* action denotes that the action does not fall into create, update or delete categories.
- `user`: Email of the user who performed the action
- `event`: Description of the event
- `object_type`: Type of the object on which the action was performed
- `object_name`: Name of the object on which the action was performed. If the object is deleted at the time of listing audit events, this field is empty.

## Response Examples

```
[
  {
    "id": "54c1ea23-5773-4821-8fd7-1b577cc301bc",
    "date": "2020-05-23T11:53:02.873+00:00",
    "action": "create",
    "user": "user@example.com",
    "event": "Created project test-project",
    "object_type": "project",
    "object_name": "test-project"
  },
  {
    "id": "764e254c-7402-4445-ac79-009d08b21caa",
    "date": "2020-05-23T11:57:20.072+00:00",
    "action": "create",
    "user": "user@example.com",
    "event": "Created deployment deployment-1",
    "object_type": "deployment",
    "object_name": "deployment-1"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
action = 'action_example' # str  (optional)
limit = 56 # int  (optional)
offset = 56 # int  (optional)

# List audit events in a project
api_response = api_instance.project_audit_events_list(project_name, action=action, limit=limit, offset=offset)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **action** | **str** | [optional] 
 **limit** | **int** | [optional] 
 **offset** | **int** | [optional] 

### Return type

[**list[AuditList]**](AuditList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_environment_variables_create**
> EnvironmentVariableList project_environment_variables_create(project_name, data)

Create project environment variable

## Description
Create an environment variable for the project. This variable will be inherited by all deployments in this project.

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users.

## Request Examples

```
{
  "name": "database_schema",
  "value": "public",
  "secret": false
}
```


```
{
  "name": "database_password",
  "value": "password",
  "secret": true
}
```

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

```
{
  "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
  "name": "database_schema",
  "value": "public",
  "secret": false
}
```


```
{
  "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
  "name": "database_password",
  "value": null,
  "secret": true
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate 

# Create project environment variable
api_response = api_instance.project_environment_variables_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md) | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_environment_variables_delete**
> project_environment_variables_delete(project_name, id)

Delete project environment variable

## Description
Delete an environment variable of the project

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
id = 'id_example' # str 

# Delete project environment variable
api_instance.project_environment_variables_delete(project_name, id)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_environment_variables_get**
> EnvironmentVariableList project_environment_variables_get(project_name, id)

Get project environment variable

## Description
Retrieve details of a project environment variable.

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
id = 'id_example' # str 

# Get project environment variable
api_response = api_instance.project_environment_variables_get(project_name, id)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **id** | **str** | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_environment_variables_list**
> list[EnvironmentVariableList] project_environment_variables_list(project_name)

List project environment variables

## Description
List the environment variables defined for the project. These are the variables that are inherited by all deployments in this project.

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 

# List project environment variables
api_response = api_instance.project_environment_variables_list(project_name)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 

### Return type

[**list[EnvironmentVariableList]**](EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_environment_variables_update**
> EnvironmentVariableList project_environment_variables_update(project_name, id, data)

Update project environment variable

## Description
Update an environment variable for the projects

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed from your deployment code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string.
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users. Can be updated from false to true, but not from true to false (i.e. secrets will stay secrets).

## Request Examples

```
{
  "name": "database_schema",
  "value": "new+schema",
  "secret": false
}
```

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

```
{
  "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
  "name": "database_schema",
  "value": "new_schema",
  "secret": false
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
id = 'id_example' # str 
data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate 

# Update project environment variable
api_response = api_instance.project_environment_variables_update(project_name, id, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **id** | **str** | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md) | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_requests_list**
> list[RequestsOverview] project_requests_list(project_name, object_type)

List requests in project

## Description
List the deployment/pipeline requests of the given project

### Required Parameters

- `object_type`: The type of the object. It can be either deployment or pipeline.

### Optional Parameters

- `status`: Status of the request. Can be 'pending', 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `success`: A boolean value that indicates whether the deployment request was successful
- `limit`: The maximum number of requests given back, default is 50
- `offset`: The number which forms the starting point of the requests given back. If offset equals 2, then the first 2 requests will be omitted from the list.
- `sort`: Direction of sorting according to the creation date of the request, can be 'asc' or 'desc'. The default sorting is done in descending order.
- `pipeline`: A boolean value that indicates whether the deployment request was part of a pipeline request
- `start_date`: Start date of the interval for which the requests are retrieved, looking at the creation date of the request
- `end_date`: End date of the interval for which the requests are retrieved, looking at the creation date of the request
- `search_id`: A string to search inside request ids. It will filter all request ids that contain this string

### Response Structure
A list of dictionaries containing the metadata of the deployment/pipeline requests with the following fields:

- `id`: The UUID of the object
- `deployment`: Name of the deployment the request was made to (Optional: in case it's a deployment request. Else NULL)
- `pipeline`: Name of the pipeline the request was made to (Optional: in case it's a pipeline request. Else NULL)
- `version`: Name of the version the request was made to
- `status`: Status of the request
- `success`: A boolean value that indicates whether the deployment/pipeline request was successful. NULL if the request is not yet finished.
- `time_created`: Server time that the request was made (current time)
- `time_started`: Server time that the processing of the request was started
- `time_completed`: Server time that the processing of the request was completed

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "deployment": "deployment-1",
    "pipeline": null,
    "version": "v1",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "deployment": null,
    "pipeline": "pipeline-1",
    "version": "v1",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
object_type = 'object_type_example' # str 

# List requests in project
api_response = api_instance.project_requests_list(project_name, object_type)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **object_type** | **str** | 

### Return type

[**list[RequestsOverview]**](RequestsOverview.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_users_create**
> ProjectUserList project_users_create(project_name, data)

Add user to a project

## Description
Add a user to a project. The user making the request must be admin of the organization. The user can later be assigned roles in the project, such as project-admin, project-viewer etc.

### Required Parameters

- `user_id`: UUID of the user

## Request Examples

```
{
  "user_id": "bd3e25a3-f77a-4cb5-92df-a7e614106e95"
}
```

### Response Structure
Details of the added user

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

## Response Examples

```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
data = ubiops.ProjectUserCreate() # ProjectUserCreate 

# Add user to a project
api_response = api_instance.project_users_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**ProjectUserCreate**](ProjectUserCreate.md) | 

### Return type

[**ProjectUserList**](ProjectUserList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_users_delete**
> project_users_delete(project_name, user_id)

Delete user from a project

## Description
Delete a user from a project. The user making the request must be admin of the organization.

**When a user is deleted from a project, all his roles defined in the scope of the project are also deleted.**

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
user_id = 'user_id_example' # str 

# Delete user from a project
api_instance.project_users_delete(project_name, user_id)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **user_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_users_get**
> ProjectUserList project_users_get(project_name, user_id)

Get user in a project

## Description
Get the details of a user in a project. The user making the request must also be a project user.

### Response Structure
Details of the user

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

## Response Examples

```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
user_id = 'user_id_example' # str 

# Get user in a project
api_response = api_instance.project_users_get(project_name, user_id)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **user_id** | **str** | 

### Return type

[**ProjectUserList**](ProjectUserList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **project_users_list**
> list[ProjectUserList] project_users_list(project_name, user_type=user_type)

List users in a project

## Description
List users and their details in a project. The user making the request must also be a project user.

### Response Structure
List of users

- `id`: Unique identifier for the user (UUID)

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

## Response Examples

```
[
  {
    "id": "54977bc3-2c3b-4d8f-97c7-aff89a95bf21",
    "email": "user@example.com",
    "name": "user",
    "surname": "name"
  },
  {
    "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
    "email": "user2@example.com",
    "name": "user",
    "surname": "name"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
user_type = 'user_type_example' # str  (optional)

# List users in a project
api_response = api_instance.project_users_list(project_name, user_type=user_type)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **user_type** | **str** | [optional] 

### Return type

[**list[ProjectUserList]**](ProjectUserList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **projects_create**
> ProjectDetail projects_create(data)

Create projects

## Description
Create a new project with the provided name.
**Only the organization admins have permission to make this request.** When a new project is created, the current organization admins are assigned project-admin role for the created project.

### Required Parameters

- `name`: Name of the project. The name is globally unique. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter.
- `organization_name`: Name of the organization in which the project is going to be created

### Optional Parameters

- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project. It defaults to False.
- `credits`: Maximum usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours they are running. It defaults to null, meaning that there are no limits.

## Request Examples

```
{
  "name": "project-1",
  "organization_name": "organization-1"
}
```

### Response Structure
Details of the created project

- `id`: Unique identifier for the project (UUID)
- `name`: Name of the project
- `creation_date`: Time the project was created
- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project
- `organization_name`: Name of the organization in which the project is created
- `credits`: Maximum usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours they are running
- `suspended`: A boolean indicating whether the project is suspended due to going over the credits limit
- `suspended_reason`: Description explaining why the project is suspended

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "advanced_permissions": false,
  "organization_name": "organization-1",
  "credits": null,
  "suspended": false,
  "suspended_reason": null
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

data = ubiops.ProjectCreate() # ProjectCreate 

# Create projects
api_response = api_instance.projects_create(data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **data** | [**ProjectCreate**](ProjectCreate.md) | 

### Return type

[**ProjectDetail**](ProjectDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **projects_delete**
> projects_delete(project_name)

Delete a project

## Description
Delete a project. The user making the request must have appropriate permissions.
**When project is deleted, all the deployments and pipelines defined in it are also deleted.**

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 

# Delete a project
api_instance.projects_delete(project_name)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **projects_get**
> ProjectDetail projects_get(project_name)

Get details of a project

## Description
Get the details of a single project. The user making the request must have appropriate permissions.

### Response Structure
Details of a project

- `id`: Unique identifier for the project (UUID)
- `name`: Name of the project
- `creation_date`: Time the project was created
- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project
- `organization_name`: Name of the organization in which the project is created
- `credits`: Maximum usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours they are running
- `suspended`: A boolean indicating whether the project is suspended due to going over the credits limit
- `suspended_reason`: Description explaining why the project is suspended

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "advanced_permissions": false,
  "organization_name": "organization-1",
  "credits": 10000,
  "suspended": false,
  "suspended_reason": null
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 

# Get details of a project
api_response = api_instance.projects_get(project_name)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 

### Return type

[**ProjectDetail**](ProjectDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **projects_list**
> list[ProjectList] projects_list(organization=organization)

List projects

## Description
List all projects to which the user making request has access. The projects in organizations to which the user belongs are shown.

### Response Structure
A list of details of the projects

- `id`: Unique identifier for the project (UUID)

- `name`: Name of the project

- `creation_date`: Time the project was created

- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project

- `organization_name`: Name of the organization in which the project is created

### Optional Parameters
These parameters should be given as query parameters

- `organization`: Name of the organization whose projects should be obtained

## Response Examples

```
[
  {
    "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
    "name": "project-1",
    "creation_date": "2018-10-26",
    "advanced_permissions": false,
    "organization_name": "organization-1"
  },
  {
    "id": "e6a85cd7-94cc-44cf-9fa0-4b462d5a71ab",
    "name": "project-2",
    "creation_date": "2019-06-20",
    "advanced_permissions": false,
    "organization_name": "organization-2"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

organization = 'organization_example' # str  (optional)

# List projects
api_response = api_instance.projects_list(organization=organization)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **organization** | **str** | [optional] 

### Return type

[**list[ProjectList]**](ProjectList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **projects_log_list**
> list[Logs] projects_log_list(project_name, data=data)

List logs for a project

## Description
Retrieve the logs of all objects in a project, including deployments, pipelines and requests. Using filters you can filter the logs on the objects and information of your choice.

### Optional Parameters

- `filters`: A dictionary containing information to filter logs on. It may contain zero or more of the following fields:

    - `deployment_name`: name of a deployment

    - `deployment_version`: name of a deployment version. If this field is present in the request, deployment_name must also be given. The deployment versions are only meaningful in combination with the deployments they are defined for.

    - `build_id`: the UUID of a build. It does not have to be given in combination with the version and deployment name.

    - `pipeline_name`: name of a pipeline

    - `pipeline_version`: name of a pipeline version. If this field is present in the request, pipeline_name must also be given. The pipeline versions are only meaningful in combination with the pipelines they are defined for.

    - `pipeline_object_name`: name of a pipeline object. If this field is present in the request, pipeline_name and pipeline_version must also be given. The pipeline objects are only meaningful in combination with the pipeline versions they are defined in.

    - `deployment_request_id`: the UUID of a deployment request

    - `pipeline_request_id`: the UUID of a pipeline request

    - `system`: whether the log was generated by the system or user code (true / false)

    - `level`: the level of the log (info / error)


Any combination of filters may be given in the request. For example, if only a deployment_name is provided, all logs for that deployment are returned. These logs can contain information from all the pipelines that deployment is referenced in. If the filters dictionary is empty, all logs for all objects in the project are returned.
Either `date` or `id` should be provided, as they both refer to a starting point of the logs. If no `date` or `id` is specified, the API will use the current time as a starting point and try to fetch the logs starting from now minus date range seconds into the past.

- `date`: Starting date for the logs. If it is not provided and the `id` parameter is not set, the most recent logs are returned. It should be provided in ISO 8601 format. The results are inclusive of the given date.

- `id`: identifier for log lines. If specified, it will act as a starting point for the interval in which to query the logs. This can be useful when making multiple queries to obtain consecutive logs

    It will include the log having the log id equal to the id value in the response, regardless of whether the date_range is positive or negative.
- `limit`: Limit for the logs response. If specified, it will limit the total number of logs returned from the query to the specified number. Defaults to 50, the maximum is 500.

- `date_range`: The date range parameter sets the interval of time in which to query the logs, specified in seconds. It may be a positive or a negative value.

    If it is positive, logs starting from the specified date / log id (both inclusive) plus date range seconds towards the present time are returned.

    Otherwise, logs starting from the specified date / log id (both inclusive) minus date range seconds towards the past are returned.

    The default value is -21600 (6 hours). The maximum value is -/+ 86400 seconds (24 hours).

## Request Examples

```
{
  "filters": {
    "deployment_name": "deployment-1",
    "deployment_version": "v1"
  },
  "date": "2020-01-01T00:00:00.000000Z"
}
```


```
{
  "filters": {
    "pipeline_name": "pipeline-1",
    "pipeline_version": "v1"
  },
  "id": "41d7a7c5cd025e3501a00000",
  "date_range": -100
}
```


```
{
  "filters": {
    "pipeline_name": "pipeline-1",
    "pipeline_version": "v1",
    "deployment_name": "deployment-1",
    "deployment_version": "v1"
  },
  "date": "2020-01-01T00:00:00.000000Z",
  "date_range": -86400,
  "limit": 5
}
```

### Response Structure
A list of log details

- `id`: Unique UUID of the log line

- `log`: Log line text

- `date`: Time the log line was created

The following fields will be returned on response if they are set for the log line:
- `deployment_name`:  The deployment which the log is related to

- `deployment_version`:  The deployment version which the log is related to

- `build_id`: The UUID of the build

- `pipeline_name`: The pipeline which the log is related to

- `pipeline_version`: The pipeline version which the log is related to

- `pipeline_object_name`: The pipeline object which the log is related to

- `deployment_request_id`:  The deployment request the log is related to

- `pipeline_request_id`:  The pipeline request the log is related to

- `system`:  Whether the log was generated by the system (true / false)

- `level`: The level of the log (info / error)

## Response Examples
Logs for a specific deployment and version

```
[
  {
    "id": "5dcad12ba76a2c6e4331f180",
    "deployment_name": "deployment-1",
    "deployment_version": "v1",
    "date": "2020-01-01T00:00:00.000000Z",
    "log": "[Info] Prediction result 0.14981"
  },
  {
    "id": "5dcad12ba76a2c6e4331f181",
    "deployment_name": "deployment-1",
    "deployment_version": "v1",
    "deployment_request_id": "ee63f938-ba81-438e-8482-9ac76037895f",
    "pipeline_name": "pipeline-2",
    "pipeline_version": "v2",
    "pipeline_object_name": "deployment-1-v1-object",
    "pipeline_request_id": "8bb6ed79-8606-4acf-acd2-90507130523c",
    "date": "2020-01-01T00:00:01.000000Z",
    "log": "[Error] Deployment call result (failed)"
  }
]
```

Logs for a specific pipeline

```
[
  {
    "id": "5dcad12ba76a2c6e4331f192",
    "deployment_name": "deployment-2",
    "deployment_version": "v2",
    "deployment_request_id": "6ee941d3-9905-49f5-95b4-cd9c4c23bb03",
    "pipeline_name": "pipeline-1",
    "pipeline_version": "v1",
    "pipeline_object_name": "deployment-2-v2-object",
    "pipeline_request_id": "4f75b10d-6012-47ab-ae68-cc9e69f35841",
    "date": "2020-01-01T00:00:00.000000Z",
    "log": "[Info] Deployment call result (success): 0.2316"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
data = ubiops.LogsCreate() # LogsCreate  (optional)

# List logs for a project
api_response = api_instance.projects_log_list(project_name, data=data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**LogsCreate**](LogsCreate.md) | [optional] 

### Return type

[**list[Logs]**](Logs.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **projects_resource_usage**
> ProjectResourceUsage projects_resource_usage(project_name)

List resource usage of a project

## Description
List the total number of resources used in a project

### Response Structure
A list containing the number of

- deployments

- deployment_versions

- pipelines

- pipeline_versions

currently defined in the project.

## Response Examples

```
{
  "deployments": 30,
  "deployment_versions": 47,
  "pipelines": 2,
  "pipeline_versions": 4
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 

# List resource usage of a project
api_response = api_instance.projects_resource_usage(project_name)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 

### Return type

[**ProjectResourceUsage**](ProjectResourceUsage.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **projects_update**
> ProjectDetail projects_update(project_name, data)

Update a project

## Description
Update the name of a single project. The user making the request must have appropriate permissions.

### Optional Parameters

- `name`: New project name
- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project
- `credits`: Maximum usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours they are running
- `suspend`: A boolean to suspend and activate projects. If the project is already suspended by UbiOps, it is not possible to suspend/activate the project.

## Request Examples

```
{
  "name": "project-name-example"
}
```

### Response Structure
Details of a project

- `id`: Unique identifier for the project (UUID)
- `name`: Name of the project
- `creation_date`: Time the project was created
- `advanced_permissions`: A boolean to enable/disable advanced permissions for the project
- `organization_name`: Name of the organization in which the project is created
- `credits`: Maximum usage of credits, calculated by multiplying the credit rate of a deployment instance type by the number of hours they are running
- `suspended`: A boolean indicating whether the project is suspended due to going over the credits limit
- `suspended_reason`: Description explaining why the project is suspended

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "advanced_permissions": false,
  "organization_name": "organization-1",
  "credits": 10000,
  "suspended": false,
  "suspended_reason": null
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
data = ubiops.ProjectUpdate() # ProjectUpdate 

# Update a project
api_response = api_instance.projects_update(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**ProjectUpdate**](ProjectUpdate.md) | 

### Return type

[**ProjectDetail**](ProjectDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **projects_usage_get**
> list[Usage] projects_usage_get(project_name, start_date=start_date, end_date=end_date, interval=interval)

Get resource usage

## Description
Get resource usage for the project. It contains **the details of each metric aggregated per month.**

### Optional Parameters

- `start_date`: date indicating the start date to fetch usage data from. If omitted, results are generated for current subscription period.
- `end_date`: date indicating the end date to fetch usage data until. If omitted, results are generated for current subscription period.
- `interval`: interval for which the usage data is fetched. It can be 'day' or 'month'. It defaults to 'month'.

If no **start_date** or **end_date** is given, the current subscription period is used, e.g. if the usage details are requested on 01-12-2020 and the subscription started on 20-11-2020, the results will contain data from 20-11-2020 to 20-12-2020.
When **start_date** and **end_date** are given, this month period is used, e.g. if 12-11-2020 is given as start date and 12-12-2020 as end date, the results will contain data from 12-11-2020 to 12-12-2020.

### Response Structure

- `metric`: Metric name
- `object_type`: Type of object the metric was measured for (deployment_version or pipeline_version)
- `usage`: an array of objects each containing the following:
  - `start_date`: Timestamp denoting the start of the current subscription period or the provided date
  - `end_date`: Timestamp denoting the end of the current subscription period or the provided date
  - `value`: Aggregated metric value for the given unit over the given month

## Response Examples
2019-08-01 as start date and 2019-09-01 as end date

```
[
  {
    "object_type": "deployment_version",
    "metric": "credits",
    "usage": [
      {
        "start_date": "2019-08-01T00:00:00Z",
        "end_date": "2019-09-01T00:00:00Z",
        "value": 13543
      } 
    ]
  },
  {
    "object_type": "deployment_version",
    "metric": "input_volume",
    "usage": [
      {
        "start_date": "2019-08-01T00:00:00Z",
        "end_date": "2019-09-01T00:00:00Z",
        "value": 136
      } 
    ]
  },
  {
    "object_type": "deployment_version",
    "metric": "output_volume",
    "usage": [
      {
        "start_date": "2019-08-01T00:00:00Z",
        "end_date": "2019-09-01T00:00:00Z",
        "value": 468
      } 
    ]
  },
  {
    "object_type": "pipeline_version",
    "metric": "input_volume",
    "usage": [
      {
        "start_date": "2019-08-01T00:00:00Z",
        "end_date": "2019-09-01T00:00:00Z",
        "value": 125
      } 
    ]
  },
  {
    "object_type": "pipeline_version",
    "metric": "output_volume",
    "usage": [
      {
        "start_date": "2019-08-01T00:00:00Z",
        "end_date": "2019-09-01T00:00:00Z",
        "value": 135
      } 
    ]
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
start_date = str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')) # datetime  (optional)
end_date = str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')) # datetime  (optional)
interval = 'month' # str  (optional) (default to 'month')

# Get resource usage
api_response = api_instance.projects_usage_get(project_name, start_date=start_date, end_date=end_date, interval=interval)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **start_date** | **datetime** | [optional] 
 **end_date** | **datetime** | [optional] 
 **interval** | **str** | [optional] [default to &#39;month&#39;]

### Return type

[**list[Usage]**](Usage.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **request_schedules_create**
> ScheduleList request_schedules_create(project_name, data)

Create request schedules

## Description
Create a new request schedule with the provided name

### Required Parameters

- `name`: Name of the request. The name is unique per project. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter.

- `object_type`: Type of object for which the request is made. Can be either 'deployment' or 'pipeline'.

- `object_name`: Name of deployment or pipeline for which the request is made

- `schedule`: Schedule in crontab format

### Optional Parameters

- `version`: Name of version for which the request schedule is made. If not provided, default version of the deployment/pipeline will be used.

- `request_data`: Input data for the request schedule. For structured deployments/pipelines, it must be a dictionary.

- `timeout`: Timeout of the request in seconds. The maximum and default values depend on the object (deployment or pipeline) and the type of request (batch or direct).
- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled. Default is 'True'.

- `description`: Description of the request schedule

- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Request Examples

```
{
  "name": "test-request",
  "object_type": "deployment",
  "object_name": "test-deployment",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "timeout": 300,
  "enabled": true,
  "description": "Daily request schedule",
  "labels": {
    "type": "daily"
  }
}
```

### Response Structure
Details of the created request schedule

- `name`: Name of the request

- `object_type`: Type of object for which the request is made

- `object_name`: Name of deployment/pipeline for which the request schedule is made

- `schedule`: Schedule in crontab format

- `version`: Name of version for which the request schedule is made

- `request_data`: Input data for the request schedule

- `timeout`: Timeout of the request in seconds

- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled

- `creation_date`: The date when the request schedule was created

- `description`: Description of the request schedule

- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Response Examples

```
{
  "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
  "name": "test-request",
  "object_type": "deployment",
  "object_name": "test-deployment",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "timeout": 300,
  "enabled": true,
  "creation_date": "2020-09-16T08:06:34.457679Z",
  "description": "Daily request schedule",
  "labels": {
    "type": "daily"
  }
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
data = ubiops.ScheduleCreate() # ScheduleCreate 

# Create request schedules
api_response = api_instance.request_schedules_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**ScheduleCreate**](ScheduleCreate.md) | 

### Return type

[**ScheduleList**](ScheduleList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **request_schedules_delete**
> request_schedules_delete(project_name, schedule_name)

Delete a request schedule

## Description
Delete the request schedule from the project.

If you want to temporarily disable a request schedule, update the request with `enabled` set to False.

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
schedule_name = 'schedule_name_example' # str 

# Delete a request schedule
api_instance.request_schedules_delete(project_name, schedule_name)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **schedule_name** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **request_schedules_get**
> ScheduleList request_schedules_get(project_name, schedule_name)

Get details of a request schedule

## Description
Retrieve details of a single request schedule

### Response Structure
Details of a request schedule

- `name`: Name of the request

- `object_type`: Type of object for which the request is made

- `object_name`: Name of deployment/pipeline for which the request is made

- `schedule`: Schedule in crontab format

- `version`: Name of version for which the request schedule is made

- `request_data`: Input data for the request schedule

- `timeout`: Timeout of the request in seconds

- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled

- `creation_date`: The date when the request schedule was created

- `description`: Description of the request schedule

- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Response Examples

```
{
  "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
  "name": "test-request",
  "object_type": "deployment",
  "object_name": "test-deployment",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "timeout": 200,
  "enabled": true,
  "creation_date": "2020-09-16T08:06:34.457679Z",
  "description": "Daily request schedule",
  "labels": {
    "type": "daily"
  }
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
schedule_name = 'schedule_name_example' # str 

# Get details of a request schedule
api_response = api_instance.request_schedules_get(project_name, schedule_name)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **schedule_name** | **str** | 

### Return type

[**ScheduleList**](ScheduleList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **request_schedules_list**
> list[ScheduleList] request_schedules_list(project_name, labels=labels)

List request schedules

## Description
List the request schedules in a project. The user has to have 'requests.list' permission on either 'deployments.versions' or 'pipelines.versions' to list the request schedules.

### Optional Parameters

- `labels`: Filter on labels of the request schedules. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.

### Response Structure
A list of details of all request schedules in a project

- `name`: Name of the request

- `object_type`: Type of object for which the request is made

- `object_name`: Name of deployment/pipeline for which the request is made

- `schedule`: Schedule in crontab format

- `version`: Name of version for which the request schedule is made 

- `request_data`: Input data for the request schedule

- `timeout`: Timeout of the request in seconds

- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled

- `creation_date`: The date when the request schedule was created

- `description`: Description of the request schedule

- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Response Examples

```
[
  {
    "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
    "name": "test-request",
    "object_type": "deployment",
    "object_name": "test-deployment",
    "version": "v1",
    "schedule": "0 * 3 * *",
    "request_data": {
      "input_field_1": 2345,
      "input_field_2": 8765
    },
    "timeout": 200",
    "enabled": true,
    "creation_date": "2020-09-16T08:06:34.457679Z",
    "description": "Daily request schedule",
    "labels": {
      "type": "daily"
    }
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
labels = 'labels_example' # str  (optional)

# List request schedules
api_response = api_instance.request_schedules_list(project_name, labels=labels)
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

[**list[ScheduleList]**](ScheduleList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **request_schedules_update**
> ScheduleList request_schedules_update(project_name, schedule_name, data)

Update a request schedule

## Description
Update a request schedule in a project. Create permissions on the object are necessary for this action.

### Optional Parameters

- `name`: Name of the request. The name is unique per project. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter.

- `schedule`: Schedule in crontab format

- `request_data`: Input data for the request schedule. For structured deployments/pipelines, it must be a dictionary.

- `timeout`: Timeout of the request in seconds. The maximum and default values depend on the object (deployment or pipeline) and the type of request (batch or direct).

- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled. Default is 'True'.

- `description`: Description of the request schedule

- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Request Examples

```
{
  "name": "test-request",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "timeout": 360,
  "enabled": false
}
```

### Response Structure
Details of the updated request schedule

- `name`: Name of the request

- `object_type`: Type of object for which the request is made

- `object_name`: Name of deployment/pipeline for which the request is made

- `schedule`: Schedule in crontab format

- `version`: Name of version for which the request schedule is made

- `request_data`: Input data for the request schedule

- `timeout`: Timeout of the request in seconds

- `enabled`: Boolean value indicating whether the request schedule is enabled or disabled

- `creation_date`: The date when the request schedule was created

- `description`: Description of the request schedule

- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Response Examples

```
{
  "id": "b4a06aed-f7ab-48b3-b579-b12b62db8058",
  "name": "test-request",
  "object_type": "deployment",
  "object_name": "test-deployment",
  "version": "v1",
  "schedule": "0 * 3 * *",
  "request_data": {
    "input_field_1": 2345,
    "input_field_2": 8765
  },
  "timeout": 360,
  "enabled": true,
  "creation_date": "2020-09-16T08:06:34.457679Z",
  "description": "Daily request schedule",
  "labels": {
    "type": "daily"
  }
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
schedule_name = 'schedule_name_example' # str 
data = ubiops.ScheduleUpdate() # ScheduleUpdate 

# Update a request schedule
api_response = api_instance.request_schedules_update(project_name, schedule_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **schedule_name** | **str** | 
 **data** | [**ScheduleUpdate**](ScheduleUpdate.md) | 

### Return type

[**ScheduleList**](ScheduleList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **revisions_file_download**
> file revisions_file_download(project_name, deployment_name, revision_id, version)

Download deployment file

## Description
Download the deployment file of a revision of a version

### Response Structure

- `file`: Deployment file of the version

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
revision_id = 'revision_id_example' # str 
version = 'version_example' # str 

# Download deployment file
with api_instance.revisions_file_download(project_name, deployment_name, revision_id, version) as response:
    filename = response.getfilename()
    content = response.read()

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **revision_id** | **str** | 
 **version** | **str** | 

### Return type

**file**

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **revisions_file_upload**
> RevisionCreate revisions_file_upload(project_name, deployment_name, version, file=file, source_deployment=source_deployment, source_version=source_version, template_deployment_id=template_deployment_id)

Upload deployment file

## Description
Upload a deployment file for a version. Uploading a deployment file will create a new revision and trigger a build.
This file should contain the deployment that will be run. It should be provided as a zip and a template can be found on https://github.com/UbiOps/deployment-template. The file is saved under a directory in the storage specified in the settings.

It is **also possible** to provide a source version from which the deployment file will be copied. This will also create a new revision and trigger a build.

### Optional Parameters

- `file`: Deployment file
- `source_deployment`: Name of the deployment from which the deployment file will be copied
- `source_version`: Version from which the deployment file will be copied
- `template_deployment_id`: UUID of a template deployment which will be used as the source of the deployment file

Either **file** or **source_deployment** and **source_version** must be provided. source_deployment and source_version must be provided together.

### Response Structure

- `success`: Boolean indicating whether the deployment file upload/copy succeeded or not
- `revision`: UUID of the created revision for the file upload
- `build`: UUID of the build created for the file upload

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
version = 'version_example' # str 
file = '/path/to/file' # file  (optional)
source_deployment = 'source_deployment_example' # str  (optional)
source_version = 'source_version_example' # str  (optional)
template_deployment_id = 'template_deployment_id_example' # str  (optional)

# Upload deployment file
api_response = api_instance.revisions_file_upload(project_name, deployment_name, version, file=file, source_deployment=source_deployment, source_version=source_version, template_deployment_id=template_deployment_id)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 
 **file** | **file** | [optional] 
 **source_deployment** | **str** | [optional] 
 **source_version** | **str** | [optional] 
 **template_deployment_id** | **str** | [optional] 

### Return type

[**RevisionCreate**](RevisionCreate.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **revisions_get**
> RevisionList revisions_get(project_name, deployment_name, revision_id, version)

Get revision

## Description
Retrieve details of a single revision of a version

### Response Structure
A dictionary containing details of the build

- `id`: Unique identifier for the revision (UUID)
- `version`: Version to which the revision is linked
- `creation_date`: The date when the revision was created
- `created_by`: The email of the user that uploaded the deployment file. In case the revision is created by a service, the field will have a "UbiOps" value.

## Response Examples

```
{
  "id": "a009d7c9-67e4-4d3c-89fd-d3c8b07c7242",
  "version": "v1",
  "creation_date": "2020-12-23T16:35:13.069+00:00",
  "created_by": "test@example.com"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
revision_id = 'revision_id_example' # str 
version = 'version_example' # str 

# Get revision
api_response = api_instance.revisions_get(project_name, deployment_name, revision_id, version)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **revision_id** | **str** | 
 **version** | **str** | 

### Return type

[**RevisionList**](RevisionList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **revisions_list**
> list[RevisionList] revisions_list(project_name, deployment_name, version)

List revisions

## Description
List all revisions associated with a version. A new revision is created every time a new deployment file is uploaded for a version.

### Response Structure
A list of details of the revisions

- `id`: Unique identifier for the revision (UUID)
- `version`: Version to which the revision is linked
- `creation_date`: The date when the revision was created
- `created_by`: The email of the user that uploaded the deployment file. In case the revision is created by a service, the field will have a "UbiOps" value.

## Response Examples

```
[
  {
    "id": "7ead8a18-c1d2-4751-80d2-d8e0e0e2fed6",
    "version": "v1",
    "creation_date": "2020-12-23T16:15:11.181+00:00",
    "created_by": "UbiOps"
  },
  {
    "id": "a009d7c9-67e4-4d3c-89fd-d3c8b07c7242",
    "version": "v1",
    "creation_date": "2020-12-23T16:35:13.069+00:00",
    "created_by": "test@example.com"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
deployment_name = 'deployment_name_example' # str 
version = 'version_example' # str 

# List revisions
api_response = api_instance.revisions_list(project_name, deployment_name, version)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **deployment_name** | **str** | 
 **version** | **str** | 

### Return type

[**list[RevisionList]**](RevisionList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **role_assignments_create**
> RoleAssignmentList role_assignments_create(project_name, data)

Assign role to user/object

## Description
Assign a role to a user or an object in the scope of a project. This role can be assigned on either project level or on object level, which can be a deployment, pipeline or bucket.

### Required Parameters

- `user_id`: Unique identifier for the user (UUID)

- `role`: Name of the role to be assigned to the user

- `assignee`: UUID of the user or the name of the object for which the role will be assigned

- `assignee_type`: Type of the assignee. It can be user or deployment.
- `resource`: Name of the object for which the role will be assigned

- `resource_type`: Type of the object for which the role will be assigned. It can be project, deployment, pipeline or bucket.

**resource and resource_type must be provided together. If neither of them is provided, the role is set on project level.**

## Request Examples
Setting the role deployment-admin on project level for user with id 02b77d8f-b312-47ef-990f-4685a7ab9363

```
{
  "assignee": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "assignee_type": "user",
  "role": "deployment-admin"
}
```

Setting the role deployment-viewer on deployment-1 for user with id 02b77d8f-b312-47ef-990f-4685a7ab9363

```
{
  "assignee": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "assignee_type": "user",
  "role": "deployment-viewer",
  "resource": "deployment-1",
  "resource_type": "deployment"
}
```

Setting the role files-reader on bucket-1 for deployment-1

```
{
  "assignee": "deployment-1",
  "assignee_type": "deployment",
  "role": "file-reader",
  "resource": "bucket-1",
  "resource_type": "bucket"
}
```

### Response Structure
Details of the created role assignment

- `id`: Unique identifier for the role assignment (UUID)
- `assignee`: UUID of the user or the name of the object
- `assignee_type`: Type of the assignee
- `role`: Name of the role assigned to the user
- `resource`: Name of the object for which the role is assigned
- `resource_type`: Type of the object for which the role is assigned

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "assignee": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "assignee_type": "user",
  "role": "deployment-admin",
  "resource": "project-1",
  "resource_type": "project"
}
```


```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "assignee": "deployment-1",
  "assignee_type": "deployment",
  "role": "file-reader",
  "resource": "bucket-1",
  "resource_type": "bucket"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
data = ubiops.RoleAssignmentCreate() # RoleAssignmentCreate 

# Assign role to user/object
api_response = api_instance.role_assignments_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**RoleAssignmentCreate**](RoleAssignmentCreate.md) | 

### Return type

[**RoleAssignmentList**](RoleAssignmentList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **role_assignments_delete**
> role_assignments_delete(project_name, id)

Delete role of user

## Description
Delete a role of a user.  It is possible for a user to delete their own role if they have permissions to do so.

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
id = 'id_example' # str 

# Delete role of user
api_instance.role_assignments_delete(project_name, id)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **role_assignments_get**
> RoleAssignmentList role_assignments_get(project_name, id)

Get role assignment

## Description
Get the details of a role assignment of a user/deployment.

### Response Structure
Details of the role assignment

- `id`: Unique identifier for the role assignment (UUID)
- `assignee`: UUID of the user or the name of the object
- `assignee_type`: Type of the assignee
- `role`: Name of the role assigned to the user/object
- `resource`: Name of the object for which the role is assigned
- `resource_type`: Type of the object for which the role is assigned

## Response Examples

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "assignee": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "assignee_type": "user",
  "role": "deployment-admin",
  "resource": "project-1",
  "resource_type": "project"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
id = 'id_example' # str 

# Get role assignment
api_response = api_instance.role_assignments_get(project_name, id)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **id** | **str** | 

### Return type

[**RoleAssignmentList**](RoleAssignmentList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **role_assignments_per_object_list**
> list[RoleAssignmentList] role_assignments_per_object_list(project_name, resource=resource, resource_type=resource_type, assignee=assignee, assignee_type=assignee_type)

List roles on object/user

## Description
List the roles assigned to a user or on an object in the scope of a project.

### Optional Parameters
These parameters should be given as query parameters

- `resource`: Name of the object on which the assigned roles will be listed
- `resource_type`: Type of the object on which the assigned roles will be listed
- `assignee`: UUID of the user or the name of the object for which the assigned roles will be listed
- `assignee_type`: Type of the assignee for which the assigned roles will be listed

### Response Structure

- `id`: Unique identifier for the role assignment (UUID)
- `assignee`: UUID of the user or the name of the object
- `assignee_type`: Type of the assignee
- `role`: Name of the role assigned to the user/object
- `resource`: Name of the object for which the role is assigned
- `resource_type`: Type of the object for which the role is assigned

## Response Examples
Roles assigned to user with id 02b77d8f-b312-47ef-990f-4685a7ab9363

```
[
  {
    "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
    "assignee": "02b77d8f-b312-47ef-990f-4685a7ab9363",
    "assignee_type": "user",
    "role": "deployment-admin",
    "resource": "project-1",
    "resource_type": "project"
  },
  {
    "id": "13cf9dd7-7356-4797-b453-e0cb6b416162",
    "assignee": "02b77d8f-b312-47ef-990f-4685a7ab9363",
    "assignee_type": "user",
    "role": "pipeline-admin",
    "resource": "pipeline-1",
    "resource_type": "pipeline"
  }
]
```

Roles assigned on deployment with name deployment-1

```
[
  {
    "id": "a24aabc2-c7df-4f7b-b177-f80827aea1bb",
    "assignee": "258771bb-1bc4-4f2f-a3f4-9309cc64d1dd",
    "assignee_type": "user",
    "role": "deployment-admin",
    "resource": "deployment-1",
    "resource_type": "deployment"
  },
  {
    "id": "dfd4e714-9c2d-446e-ae96-4db18f91d3de",
    "assignee": "0ca8a61d-962e-48e3-b558-61e8ca2dae88",
    "assignee_type": "user",
    "role": "deployment-viewer",
    "resource": "deployment-1",
    "resource_type": "deployment"
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
resource = 'resource_example' # str  (optional)
resource_type = 'resource_type_example' # str  (optional)
assignee = 'assignee_example' # str  (optional)
assignee_type = 'assignee_type_example' # str  (optional)

# List roles on object/user
api_response = api_instance.role_assignments_per_object_list(project_name, resource=resource, resource_type=resource_type, assignee=assignee, assignee_type=assignee_type)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **resource** | **str** | [optional] 
 **resource_type** | **str** | [optional] 
 **assignee** | **str** | [optional] 
 **assignee_type** | **str** | [optional] 

### Return type

[**list[RoleAssignmentList]**](RoleAssignmentList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **roles_create**
> RoleDetailList roles_create(project_name, data)

Create a custom role scoped in a project

## Description
Create a custom role in the scope of a project. This role is not accessible from other projects.
The user making the request must have appropriate permissions.

### Required Parameters

- `name`: Name of the role which will be created. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter.

- `permissions`: A list of permissions which the role will contain. The list of available permissions can be obtained with */permissions* endpoint.

## Request Examples

```
{
  "name": "custom-deployment-editor-role",
  "permissions": [
    "deployments.list",
    "deployments.get",
    "deployments.delete"
  ]
}
```

### Response Structure
Details of the created role

- `id`: Unique identifier for the created role (UUID)

- `name`: Name of the created role

- `default`: A boolean value that indicates whether the role is a default role or not

- `permissions`: A list of permissions which the role contains

## Response Examples

```
{
  "id": "18a4a60d-d5f0-4099-9c6e-543bf2fd5a1d",
  "name": "custom-deployment-editor-role",
  "default": false,
  "permissions": [
    "deployments.list",
    "deployments.get",
    "deployments.delete"
  ]
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
data = ubiops.RoleCreate() # RoleCreate 

# Create a custom role scoped in a project
api_response = api_instance.roles_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**RoleCreate**](RoleCreate.md) | 

### Return type

[**RoleDetailList**](RoleDetailList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **roles_delete**
> roles_delete(project_name, role_name)

Delete a role from a project

## Description
Delete a role from a project. The user making the request must have appropriate permissions.
**Default roles cannot be deleted.**

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
role_name = 'role_name_example' # str 

# Delete a role from a project
api_instance.roles_delete(project_name, role_name)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **role_name** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **roles_get**
> RoleDetailList roles_get(project_name, role_name)

Get details of a role

## Description
Get the details of a role. The user making the request must have appropriate permissions.

### Response Structure
Details of the role

- `id`: Unique identifier for the role (UUID)

- `name`: Name of the role

- `default`: A boolean value that indicates whether the role is a default role or not

- `permissions`: A list of permissions which the role contains

## Response Examples

```
{
  "id": "18a4a60d-d5f0-4099-9c6e-543bf2fd5a1d",
  "name": "custom-deployment-editor-role",
  "default": false,
  "permissions": [
    "deployments.list",
    "deployments.get",
    "deployments.delete"
  ]
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
role_name = 'role_name_example' # str 

# Get details of a role
api_response = api_instance.roles_get(project_name, role_name)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **role_name** | **str** | 

### Return type

[**RoleDetailList**](RoleDetailList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **roles_list**
> list[RoleList] roles_list(project_name)

List the available roles in a project

## Description
List the roles available in the scope of a project. Information on which permissions each role contains, can be obtained with a call to get details of a single role.

### Response Structure

- `id`: Unique identifier for the role (UUID)

- `name`: Name of the role

- `default`: A boolean value that indicates whether the role is a default role or not

## Response Examples

```
[
  {
    "id": "34e53855-9b50-47bc-b516-6cb971b1949c",
    "name": "project-admin",
    "default": true
  },
  {
    "id": "00132911-b5dd-4017-b399-85f3ffd2a7c3",
    "name": "project-editor",
    "default": true
  },
  {
    "id": "bf0d5823-8062-40f6-bbd2-21bc732f3c3b",
    "name": "project-viewer",
    "default": true
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 

# List the available roles in a project
api_response = api_instance.roles_list(project_name)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 

### Return type

[**list[RoleList]**](RoleList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **roles_update**
> RoleDetailList roles_update(project_name, role_name, data)

Update a role in a project

## Description
Update a role in a project. The user making the request must have appropriate permissions.
**Default roles cannot be updated.**

### Optional Parameters

- `name`: New name for the role. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter.

- `permissions`: A new list of permissions which the role will contain. The previous permissions will be replaced with the given ones. The list of available permissions can be obtained with */permissions* endpoint.

## Request Examples

```
{
  "name": "new-deployment-editor-role",
  "permissions": [
    "deployments.list",
    "deployments.get"
  ]
}
```

### Response Structure
Details of the updated role

- `id`: Unique identifier for the role (UUID)

- `name`: Name of the updated role

- `default`: A boolean value that indicates whether the role is a default role or not

- `permissions`: A list of permissions which the role contains

## Response Examples

```
{
  "id": "18a4a60d-d5f0-4099-9c6e-543bf2fd5a1d",
  "name": "new-deployment-editor-role",
  "default": false,
  "permissions": [
    "deployments.list",
    "deployments.get"
  ]
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
role_name = 'role_name_example' # str 
data = ubiops.RoleUpdate() # RoleUpdate 

# Update a role in a project
api_response = api_instance.roles_update(project_name, role_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **role_name** | **str** | 
 **data** | [**RoleUpdate**](RoleUpdate.md) | 

### Return type

[**RoleDetailList**](RoleDetailList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **service_status**
> Status service_status()

Service status

## Description
Request the API status. It can be used to determine whether the API is online. You do not have to be authenticated to access this method.

### Response Structure

- `status`: API status, either ok or fail. The database connection is tested at each status request, to make sure that the API is online.

## Response Examples

```	
{
  "status": "ok"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)


# Service status
api_response = api_instance.service_status()
print(api_response)

# Close the connection
api_client.close()
```


### Parameters

This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **service_users_create**
> ServiceUserTokenDetail service_users_create(project_name, data)

Create a new service user

## Description
Create a new service user. A unique email is generated for the service user. Additionally, a token for this service user is generated. This token can be used to authorize requests sent to our API. It is possible to set an expiry date for this token.
In addition, allowed cors origins can be configured for the service user. The service user will be allowed to make a deployment or pipeline request from these origins.

The token is **ONLY** returned on creation and will not be accessible afterwards.

### Optional Parameters

- `name`: Name of the service user

- `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from

- `expiry_date`: Date when the service user account expires (UTC). If null is passed, the account will never expire.

## Request Examples

```
{
  "name": "service-user-1"
}
```


```
{
  "name": "service-user-1",
  "allowed_cors_origins": [
    "https://test.com"
  ]
}
```


```
{
  "name": "service-user-1",
  "expiry_date": "2020-01-01T00:00:00.000Z"
}
```

### Response Structure
Details of the created service user

- `id`: Unique identifier for the service user (UUID)

- `email`: Email of the service user 

- `token`: The API token for the created service user 

- `name`: Name of the service user

- `creation_date`: Date when the service user was created

- `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from

- `expiry_date`: Date when the service user account will expire (UTC)

## Response Examples

```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
  "token": "e962d9190348af7fa8d233d75cff7385b4335f81",
  "name": "service-user-1",
  "creation_date": "2020-03-24T09:16:27.504+00:00",
  "allowed_cors_origins": [
    "https://test.com"
  ],
  "expiry_date": "2021-03-24T00:00:00.000+00:00"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
data = ubiops.ServiceUserCreate() # ServiceUserCreate 

# Create a new service user
api_response = api_instance.service_users_create(project_name, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**ServiceUserCreate**](ServiceUserCreate.md) | 

### Return type

[**ServiceUserTokenDetail**](ServiceUserTokenDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **service_users_delete**
> service_users_delete(project_name, service_user_id)

Delete service user

## Description
Delete a service user from a project

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
service_user_id = 'service_user_id_example' # str 

# Delete service user
api_instance.service_users_delete(project_name, service_user_id)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_user_id** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **service_users_get**
> ServiceUserList service_users_get(project_name, service_user_id)

Retrieve details of a service user

## Description
Retrieve details of a service user

### Response Structure
Details of the service user

- `id`: Unique identifier for the service user (UUID)

- `email`: Email of the service user 

- `name`: Name of the service user

- `creation_date`: Date when the service user was created

- `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from

- `expiry_date`: Date when the service user account will expire (UTC)

## Response Examples

```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
  "name": "new-service-user-name",
  "creation_date": "2020-03-26T12:18:43.123+00:00",
  "allowed_cors_origins": [
    "https://test.com"
  ],
  "expiry_date": null
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
service_user_id = 'service_user_id_example' # str 

# Retrieve details of a service user
api_response = api_instance.service_users_get(project_name, service_user_id)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_user_id** | **str** | 

### Return type

[**ServiceUserList**](ServiceUserList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **service_users_list**
> list[ServiceUserList] service_users_list(project_name)

List service users

## Description
List service users defined in a project

### Response Structure
List of details of the service users:

- `id`: Unique identifier for the service user (UUID)

- `email`: Email of the service user

- `name`: Name of the service user

- `creation_date`: Date when the service user was created

- `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from

- `expiry_date`: Date when the service user account will expire (UTC)

## Response Examples

```
[
  {
    "id": "537bca64-5ab6-43eb-a7ef-1638bc30b6ed",
    "email": "537bca64-5ab6-43eb-a7ef-1638bc30b6ed.project1@serviceuser.ubiops.com",
    "name": "service-user-1",
    "creation_date": "2020-03-24T09:16:27.504+00:00",
    "allowed_cors_origins": [
      "https://test.com"
    ],
    "expiry_date": "2021-03-24T00:00:00.000+00:00"
  },
  {
    "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
    "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
    "name": "service-user-2",
    "creation_date": "2020-03-26T12:18:43.123+00:00",
    "allowed_cors_origins": [
      "https://test.com"
    ],
    "expiry_date": null
  }
]
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 

# List service users
api_response = api_instance.service_users_list(project_name)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 

### Return type

[**list[ServiceUserList]**](ServiceUserList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **service_users_token**
> ServiceUserTokenList service_users_token(project_name, service_user_id, data=data)

Reset the token of a service user

## Description
Reset the token of a service user. The old token will be deleted and a new one will be created for the service user. No data should be sent in the body of the request.

It is not possible to reset the token of a service user whose expiry date has been reached.

### Response Structure
Details of the new token for the service user

- `token`: The new API token for the service user

## Response Examples

```
{
  "token": "e962d9190348af7fa8d233d75cff7385b4335f81"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
service_user_id = 'service_user_id_example' # str 
data = None # object  (optional)

# Reset the token of a service user
api_response = api_instance.service_users_token(project_name, service_user_id, data=data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_user_id** | **str** | 
 **data** | **object** | [optional] 

### Return type

[**ServiceUserTokenList**](ServiceUserTokenList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **service_users_update**
> ServiceUserList service_users_update(project_name, service_user_id, data)

Update service user details

## Description
Update the name, expiry date and cors allowed origins of a service user. The new value for the cors_allowed_origin will replace the old value.
Leave as an empty list to remove the previous list of allowed origins.

It is not possible to update a service user whose expiry date has been reached.

### Optional Parameters

- `name`: Name of the service user

- `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from

- `expiry_date`: Date when the service user account will expire (UTC). If null is passed, the account will never expire.

## Request Examples


```
{
  "name": "new-service-user-name",
}
```


```
{
  "name": "service-user-1",
  "allowed_cors_origins": [
    "https://test.com"
  ]
}
```


```
{
  "expiry_date": "2020-01-01T00:00:00.000Z"
}
```

### Response Structure
Details of the updated service user

- `id`: Unique identifier for the service user (UUID)

- `email`: Email of the service user 

- `name`: Name of the service user

- `creation_date`: Date when the service user was created

- `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from

- `expiry_date`: Date when the service user account will expire (UTC)

## Response Examples

```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com",
  "name": "new-service-user-name",
  "creation_date": "2020-03-26T12:18:43.123+00:00",
  "allowed_cors_origins": [
    "https://test.com"
  ],
  "expiry_date": null
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

project_name = 'project_name_example' # str 
service_user_id = 'service_user_id_example' # str 
data = ubiops.ServiceUserCreate() # ServiceUserCreate 

# Update service user details
api_response = api_instance.service_users_update(project_name, service_user_id, data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **service_user_id** | **str** | 
 **data** | [**ServiceUserCreate**](ServiceUserCreate.md) | 

### Return type

[**ServiceUserList**](ServiceUserList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **user_create**
> UserPendingDetail user_create(data)

Create a new user

## Description
Create a new user with the given details - email, password, name and surname. After creation, an email is send to the email address to activate the account.
The user is required to accept the terms and conditions. The password needs to be at least 8 characters long.

### Required Parameters

- `email`: Email of the user. This is a unique field.

- `password`: Password of the user

- `terms_conditions`: Boolean field. Pass True to accept terms and conditions.

### Optional Parameters

- `name`: Name of the user

- `surname`: Surname of the user

- `newsletter`: Boolean field. Pass True to subscribe to the newsletters.

## Request Examples

```
{
  "email": "test@example.com",
  "password": "secret-password",
  "name": "User name",
  "surname": "User surname",
  "terms_conditions": true,
  "newsletter": false
}
```


```
{
  "email": "test@example.com",
  "password": "secret-password",
  "terms_conditions": true,
  "newsletter": false

}
```

### Response Structure
Details of the created user

- `email`: Email of the user

- `name`: Name of the user

- `surname`: Surname of the user

## Response Examples

```
{
  "email": "test@example.com",
  "name": "User name",
  "surname": "User surname"
}
```

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)

data = ubiops.UserPendingCreate() # UserPendingCreate 

# Create a new user
api_response = api_instance.user_create(data)
print(api_response)

# Close the connection
api_client.close()
```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **data** | [**UserPendingCreate**](UserPendingCreate.md) | 

### Return type

[**UserPendingDetail**](UserPendingDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **user_delete**
> user_delete()

Delete user

## Description
Delete the user that makes the request

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

# Create an instance of the API class
api_instance = ubiops.CoreApi(api_client)


# Delete user
api_instance.user_delete()

# Close the connection
api_client.close()
```


### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


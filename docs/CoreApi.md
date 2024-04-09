# ubiops.CoreApi

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blobs_create**](./Blobs.md#blobs_create) | **POST** /projects/{project_name}/blobs | Upload a blob
[**blobs_delete**](./Blobs.md#blobs_delete) | **DELETE** /projects/{project_name}/blobs/{blob_id} | Delete a blob
[**blobs_get**](./Blobs.md#blobs_get) | **GET** /projects/{project_name}/blobs/{blob_id} | Get a blob
[**blobs_list**](./Blobs.md#blobs_list) | **GET** /projects/{project_name}/blobs | List blobs
[**blobs_update**](./Blobs.md#blobs_update) | **PUT** /projects/{project_name}/blobs/{blob_id} | Update a blob
[**batch_deployment_requests_create**](./DeploymentRequests.md#batch_deployment_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/batch | Create a batch deployment request
[**batch_deployment_version_requests_create**](./DeploymentRequests.md#batch_deployment_version_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/batch | Create a batch deployment version request
[**deployment_requests_batch_delete**](./DeploymentRequests.md#deployment_requests_batch_delete) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/delete | Delete multiple deployment requests
[**deployment_requests_batch_get**](./DeploymentRequests.md#deployment_requests_batch_get) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests/collect | Retrieve multiple deployment requests
[**deployment_requests_create**](./DeploymentRequests.md#deployment_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/requests | Create a direct deployment request
[**deployment_requests_delete**](./DeploymentRequests.md#deployment_requests_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Delete a deployment request
[**deployment_requests_get**](./DeploymentRequests.md#deployment_requests_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Get a deployment request
[**deployment_requests_list**](./DeploymentRequests.md#deployment_requests_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/requests | List deployment requests
[**deployment_requests_update**](./DeploymentRequests.md#deployment_requests_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/requests/{request_id} | Update a deployment request
[**deployment_version_requests_batch_delete**](./DeploymentRequests.md#deployment_version_requests_batch_delete) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/delete | Delete multiple deployment version requests
[**deployment_version_requests_batch_get**](./DeploymentRequests.md#deployment_version_requests_batch_get) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/collect | Retrieve multiple deployment version requests
[**deployment_version_requests_create**](./DeploymentRequests.md#deployment_version_requests_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests | Create a direct deployment version request
[**deployment_version_requests_delete**](./DeploymentRequests.md#deployment_version_requests_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Delete a deployment version request
[**deployment_version_requests_get**](./DeploymentRequests.md#deployment_version_requests_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Get a deployment version request
[**deployment_version_requests_list**](./DeploymentRequests.md#deployment_version_requests_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests | List deployment version requests
[**deployment_version_requests_update**](./DeploymentRequests.md#deployment_version_requests_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/requests/{request_id} | Update a deployment version request
[**builds_get**](./Deployments.md#builds_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/builds/{build_id} | Get build
[**deployment_audit_events_list**](./Deployments.md#deployment_audit_events_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/audit | List audit events for a deployment
[**deployment_environment_variables_copy**](./Deployments.md#deployment_environment_variables_copy) | **POST** /projects/{project_name}/deployments/{deployment_name}/copy-environment-variables | Copy deployment environment variable
[**deployment_environment_variables_create**](./Deployments.md#deployment_environment_variables_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/environment-variables | Create deployment environment variable
[**deployment_environment_variables_delete**](./Deployments.md#deployment_environment_variables_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Delete deployment environment variable
[**deployment_environment_variables_get**](./Deployments.md#deployment_environment_variables_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Get deployment environment variable
[**deployment_environment_variables_list**](./Deployments.md#deployment_environment_variables_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/environment-variables | List deployment environment variables
[**deployment_environment_variables_update**](./Deployments.md#deployment_environment_variables_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/environment-variables/{id} | Update deployment environment variable
[**deployment_version_environment_variables_copy**](./Deployments.md#deployment_version_environment_variables_copy) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/copy-environment-variables | Copy deployment version environment variable
[**deployment_version_environment_variables_create**](./Deployments.md#deployment_version_environment_variables_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables | Create deployment version environment variable
[**deployment_version_environment_variables_delete**](./Deployments.md#deployment_version_environment_variables_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Delete deployment version environment variable
[**deployment_version_environment_variables_get**](./Deployments.md#deployment_version_environment_variables_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Get deployment version environment variable
[**deployment_version_environment_variables_list**](./Deployments.md#deployment_version_environment_variables_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables | List deployment version environment variables
[**deployment_version_environment_variables_update**](./Deployments.md#deployment_version_environment_variables_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/environment-variables/{id} | Update deployment version environment variable
[**deployment_versions_create**](./Deployments.md#deployment_versions_create) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions | Create deployment versions
[**deployment_versions_delete**](./Deployments.md#deployment_versions_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Delete deployment version
[**deployment_versions_get**](./Deployments.md#deployment_versions_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Get deployment version
[**deployment_versions_list**](./Deployments.md#deployment_versions_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions | List deployment versions
[**deployment_versions_update**](./Deployments.md#deployment_versions_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name}/versions/{version} | Update deployment version
[**deployments_create**](./Deployments.md#deployments_create) | **POST** /projects/{project_name}/deployments | Create deployments
[**deployments_delete**](./Deployments.md#deployments_delete) | **DELETE** /projects/{project_name}/deployments/{deployment_name} | Delete a deployment
[**deployments_get**](./Deployments.md#deployments_get) | **GET** /projects/{project_name}/deployments/{deployment_name} | Get details of a deployment
[**deployments_list**](./Deployments.md#deployments_list) | **GET** /projects/{project_name}/deployments | List deployments
[**deployments_update**](./Deployments.md#deployments_update) | **PATCH** /projects/{project_name}/deployments/{deployment_name} | Update a deployment
[**revisions_file_download**](./Deployments.md#revisions_file_download) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions/{revision_id}/download | Download deployment file
[**revisions_file_upload**](./Deployments.md#revisions_file_upload) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions | Upload deployment file
[**revisions_get**](./Deployments.md#revisions_get) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions/{revision_id} | Get revision
[**revisions_list**](./Deployments.md#revisions_list) | **GET** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions | List revisions
[**revisions_rebuild**](./Deployments.md#revisions_rebuild) | **POST** /projects/{project_name}/deployments/{deployment_name}/versions/{version}/revisions/{revision_id}/rebuild | Rebuild revision
[**template_deployments_list**](./Deployments.md#template_deployments_list) | **GET** /template-deployments | List template deployments
[**environment_build_dependencies_list**](./Environments.md#environment_build_dependencies_list) | **GET** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id}/builds/{build_id}/dependency-files | List dependency files
[**environment_builds_get**](./Environments.md#environment_builds_get) | **GET** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id}/builds/{build_id} | Get build
[**environment_builds_list**](./Environments.md#environment_builds_list) | **GET** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id}/builds | List builds
[**environment_builds_update**](./Environments.md#environment_builds_update) | **PATCH** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id}/builds/{build_id} | Update build
[**environment_revisions_file_download**](./Environments.md#environment_revisions_file_download) | **GET** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id}/download | Download environment file
[**environment_revisions_file_upload**](./Environments.md#environment_revisions_file_upload) | **POST** /projects/{project_name}/environments/{environment_name}/revisions | Upload environment file
[**environment_revisions_get**](./Environments.md#environment_revisions_get) | **GET** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id} | Get revision
[**environment_revisions_list**](./Environments.md#environment_revisions_list) | **GET** /projects/{project_name}/environments/{environment_name}/revisions | List revisions
[**environment_revisions_rebuild**](./Environments.md#environment_revisions_rebuild) | **POST** /projects/{project_name}/environments/{environment_name}/revisions/{revision_id}/rebuild | Rebuild revision
[**environments_create**](./Environments.md#environments_create) | **POST** /projects/{project_name}/environments | Create environments
[**environments_delete**](./Environments.md#environments_delete) | **DELETE** /projects/{project_name}/environments/{environment_name} | Delete environment
[**environments_get**](./Environments.md#environments_get) | **GET** /projects/{project_name}/environments/{environment_name} | Get environment
[**environments_list**](./Environments.md#environments_list) | **GET** /projects/{project_name}/environments | List environments
[**environments_update**](./Environments.md#environments_update) | **PATCH** /projects/{project_name}/environments/{environment_name} | Update environment
[**environments_usage**](./Environments.md#environments_usage) | **GET** /projects/{project_name}/environments/{environment_name}/usage | List usage of environment
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
[**exports_create**](./ImportsAndExports.md#exports_create) | **POST** /projects/{project_name}/exports | Create an export
[**exports_delete**](./ImportsAndExports.md#exports_delete) | **DELETE** /projects/{project_name}/exports/{export_id} | Delete an export
[**exports_download**](./ImportsAndExports.md#exports_download) | **GET** /projects/{project_name}/exports/{export_id}/download | Download an export
[**exports_get**](./ImportsAndExports.md#exports_get) | **GET** /projects/{project_name}/exports/{export_id} | Get an export
[**exports_list**](./ImportsAndExports.md#exports_list) | **GET** /projects/{project_name}/exports | List exports
[**imports_create**](./ImportsAndExports.md#imports_create) | **POST** /projects/{project_name}/imports | Create an import
[**imports_delete**](./ImportsAndExports.md#imports_delete) | **DELETE** /projects/{project_name}/imports/{import_id} | Delete an import
[**imports_download**](./ImportsAndExports.md#imports_download) | **GET** /projects/{project_name}/imports/{import_id}/download | Download an import
[**imports_get**](./ImportsAndExports.md#imports_get) | **GET** /projects/{project_name}/imports/{import_id} | Get an import
[**imports_list**](./ImportsAndExports.md#imports_list) | **GET** /projects/{project_name}/imports | List imports
[**imports_update**](./ImportsAndExports.md#imports_update) | **PATCH** /projects/{project_name}/imports/{import_id} | Confirm an import
[**metrics_create**](./Metrics.md#metrics_create) | **POST** /projects/{project_name}/metrics | Create metrics
[**metrics_delete**](./Metrics.md#metrics_delete) | **DELETE** /projects/{project_name}/metrics/{metric_name} | Delete metric
[**metrics_get**](./Metrics.md#metrics_get) | **GET** /projects/{project_name}/metrics/{metric_name} | Get metric
[**metrics_list**](./Metrics.md#metrics_list) | **GET** /projects/{project_name}/metrics | List metrics
[**metrics_update**](./Metrics.md#metrics_update) | **PATCH** /projects/{project_name}/metrics/{metric_name} | Update metric
[**time_series_data_aggregate**](./Metrics.md#time_series_data_aggregate) | **POST** /projects/{project_name}/time-series/aggregate | Aggregate metric data
[**time_series_data_create**](./Metrics.md#time_series_data_create) | **POST** /projects/{project_name}/time-series/data | Create metric data
[**time_series_data_list**](./Metrics.md#time_series_data_list) | **GET** /projects/{project_name}/time-series/data | List time series data
[**time_series_delete**](./Metrics.md#time_series_delete) | **DELETE** /projects/{project_name}/time-series/{time_series_id} | Delete time series
[**time_series_search**](./Metrics.md#time_series_search) | **GET** /projects/{project_name}/time-series/search | Search time series
[**notification_groups_create**](./Monitoring.md#notification_groups_create) | **POST** /projects/{project_name}/monitoring/notification-groups | Create notification groups
[**notification_groups_delete**](./Monitoring.md#notification_groups_delete) | **DELETE** /projects/{project_name}/monitoring/notification-groups/{notification_group_name} | Delete notification group
[**notification_groups_get**](./Monitoring.md#notification_groups_get) | **GET** /projects/{project_name}/monitoring/notification-groups/{notification_group_name} | Get notification group
[**notification_groups_list**](./Monitoring.md#notification_groups_list) | **GET** /projects/{project_name}/monitoring/notification-groups | List notification groups
[**notification_groups_update**](./Monitoring.md#notification_groups_update) | **PATCH** /projects/{project_name}/monitoring/notification-groups/{notification_group_name} | Update notification group
[**organization_users_create**](./Organizations.md#organization_users_create) | **POST** /organizations/{organization_name}/users | Add a user to an organization
[**organization_users_delete**](./Organizations.md#organization_users_delete) | **DELETE** /organizations/{organization_name}/users/{user_id} | Delete a user from an organization
[**organization_users_get**](./Organizations.md#organization_users_get) | **GET** /organizations/{organization_name}/users/{user_id} | Get details of a user in an organization
[**organization_users_list**](./Organizations.md#organization_users_list) | **GET** /organizations/{organization_name}/users | List the users in an organization
[**organization_users_update**](./Organizations.md#organization_users_update) | **PATCH** /organizations/{organization_name}/users/{user_id} | Update details of a user in an organization
[**organizations_create**](./Organizations.md#organizations_create) | **POST** /organizations | Create organizations
[**organizations_get**](./Organizations.md#organizations_get) | **GET** /organizations/{organization_name} | Get details of an organization
[**organizations_list**](./Organizations.md#organizations_list) | **GET** /organizations | List organizations
[**organizations_resource_usage**](./Organizations.md#organizations_resource_usage) | **GET** /organizations/{organization_name}/resources | Get resource usage
[**organizations_update**](./Organizations.md#organizations_update) | **PATCH** /organizations/{organization_name} | Update details of an organization
[**organizations_usage_get**](./Organizations.md#organizations_usage_get) | **GET** /organizations/{organization_name}/usage | Get organization usage
[**vouchers_get**](./Organizations.md#vouchers_get) | **GET** /vouchers/{code} | Get voucher
[**batch_pipeline_requests_create**](./PipelineRequests.md#batch_pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/batch | Create a batch pipeline request
[**batch_pipeline_version_requests_create**](./PipelineRequests.md#batch_pipeline_version_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/batch | Create a batch pipeline version request
[**pipeline_requests_batch_delete**](./PipelineRequests.md#pipeline_requests_batch_delete) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/delete | Delete multiple pipeline requests
[**pipeline_requests_batch_get**](./PipelineRequests.md#pipeline_requests_batch_get) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests/collect | Retrieve multiple pipeline requests
[**pipeline_requests_create**](./PipelineRequests.md#pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/requests | Create a pipeline request
[**pipeline_requests_delete**](./PipelineRequests.md#pipeline_requests_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/requests/{request_id} | Delete a pipeline request
[**pipeline_requests_get**](./PipelineRequests.md#pipeline_requests_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/requests/{request_id} | Get a pipeline request
[**pipeline_requests_list**](./PipelineRequests.md#pipeline_requests_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/requests | List pipeline requests
[**pipeline_version_object_requests_get**](./PipelineRequests.md#pipeline_version_object_requests_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/object-requests/{request_id} | Get an operator request
[**pipeline_version_requests_batch_delete**](./PipelineRequests.md#pipeline_version_requests_batch_delete) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/delete | Delete multiple pipeline version requests
[**pipeline_version_requests_batch_get**](./PipelineRequests.md#pipeline_version_requests_batch_get) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/collect | Retrieve multiple pipeline version requests
[**pipeline_version_requests_create**](./PipelineRequests.md#pipeline_version_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests | Create a pipeline version request
[**pipeline_version_requests_delete**](./PipelineRequests.md#pipeline_version_requests_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/{request_id} | Delete a pipeline version request
[**pipeline_version_requests_get**](./PipelineRequests.md#pipeline_version_requests_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests/{request_id} | Get a pipeline version request
[**pipeline_version_requests_list**](./PipelineRequests.md#pipeline_version_requests_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/requests | List pipeline version requests
[**expressions_evaluate**](./Pipelines.md#expressions_evaluate) | **POST** /expressions/evaluate | Evaluate expression
[**pipeline_audit_events_list**](./Pipelines.md#pipeline_audit_events_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/audit | List audit events for a pipeline
[**pipeline_version_object_environment_variables_list**](./Pipelines.md#pipeline_version_object_environment_variables_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version}/objects/{name}/environment-variables | List pipeline object environment variables
[**pipeline_versions_create**](./Pipelines.md#pipeline_versions_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/versions | Create pipeline versions
[**pipeline_versions_delete**](./Pipelines.md#pipeline_versions_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Delete pipeline version
[**pipeline_versions_get**](./Pipelines.md#pipeline_versions_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Get pipeline version
[**pipeline_versions_list**](./Pipelines.md#pipeline_versions_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/versions | List pipeline versions
[**pipeline_versions_update**](./Pipelines.md#pipeline_versions_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name}/versions/{version} | Update pipeline version
[**pipelines_create**](./Pipelines.md#pipelines_create) | **POST** /projects/{project_name}/pipelines | Create pipelines
[**pipelines_delete**](./Pipelines.md#pipelines_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name} | Delete a pipeline
[**pipelines_get**](./Pipelines.md#pipelines_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name} | Get details of a pipeline
[**pipelines_list**](./Pipelines.md#pipelines_list) | **GET** /projects/{project_name}/pipelines | List pipelines
[**pipelines_update**](./Pipelines.md#pipelines_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name} | Update a pipeline
[**instance_types_list**](./Projects.md#instance_types_list) | **GET** /projects/{project_name}/instance-types | List instance types
[**project_audit_events_list**](./Projects.md#project_audit_events_list) | **GET** /projects/{project_name}/audit | List audit events in a project
[**project_environment_variables_create**](./Projects.md#project_environment_variables_create) | **POST** /projects/{project_name}/environment-variables | Create project environment variable
[**project_environment_variables_delete**](./Projects.md#project_environment_variables_delete) | **DELETE** /projects/{project_name}/environment-variables/{id} | Delete project environment variable
[**project_environment_variables_get**](./Projects.md#project_environment_variables_get) | **GET** /projects/{project_name}/environment-variables/{id} | Get project environment variable
[**project_environment_variables_list**](./Projects.md#project_environment_variables_list) | **GET** /projects/{project_name}/environment-variables | List project environment variables
[**project_environment_variables_update**](./Projects.md#project_environment_variables_update) | **PATCH** /projects/{project_name}/environment-variables/{id} | Update project environment variable
[**project_requests_list**](./Projects.md#project_requests_list) | **GET** /projects/{project_name}/requests | List requests in project
[**project_users_create**](./Projects.md#project_users_create) | **POST** /projects/{project_name}/users | Add user to a project
[**project_users_delete**](./Projects.md#project_users_delete) | **DELETE** /projects/{project_name}/users/{user_id} | Delete user from a project
[**project_users_get**](./Projects.md#project_users_get) | **GET** /projects/{project_name}/users/{user_id} | Get user in a project
[**project_users_list**](./Projects.md#project_users_list) | **GET** /projects/{project_name}/users | List users in a project
[**projects_create**](./Projects.md#projects_create) | **POST** /projects | Create projects
[**projects_delete**](./Projects.md#projects_delete) | **DELETE** /projects/{project_name} | Delete a project
[**projects_get**](./Projects.md#projects_get) | **GET** /projects/{project_name} | Get details of a project
[**projects_list**](./Projects.md#projects_list) | **GET** /projects | List projects
[**projects_log_list**](./Projects.md#projects_log_list) | **POST** /projects/{project_name}/logs | List logs for a project
[**projects_resource_usage**](./Projects.md#projects_resource_usage) | **GET** /projects/{project_name}/resources | List resource usage of a project
[**projects_update**](./Projects.md#projects_update) | **PATCH** /projects/{project_name} | Update a project
[**projects_usage_get**](./Projects.md#projects_usage_get) | **GET** /projects/{project_name}/usage | Get resource usage
[**quotas_list**](./Projects.md#quotas_list) | **GET** /projects/{project_name}/quotas | List quotas
[**request_schedules_create**](./RequestSchedules.md#request_schedules_create) | **POST** /projects/{project_name}/schedules | Create request schedules
[**request_schedules_delete**](./RequestSchedules.md#request_schedules_delete) | **DELETE** /projects/{project_name}/schedules/{schedule_name} | Delete a request schedule
[**request_schedules_get**](./RequestSchedules.md#request_schedules_get) | **GET** /projects/{project_name}/schedules/{schedule_name} | Get details of a request schedule
[**request_schedules_list**](./RequestSchedules.md#request_schedules_list) | **GET** /projects/{project_name}/schedules | List request schedules
[**request_schedules_update**](./RequestSchedules.md#request_schedules_update) | **PATCH** /projects/{project_name}/schedules/{schedule_name} | Update a request schedule
[**permissions_list**](./Roles.md#permissions_list) | **GET** /permissions | List the available permissions
[**role_assignments_create**](./Roles.md#role_assignments_create) | **POST** /projects/{project_name}/role-assignments | Assign role to user/object
[**role_assignments_delete**](./Roles.md#role_assignments_delete) | **DELETE** /projects/{project_name}/role-assignments/{id} | Delete role of user
[**role_assignments_get**](./Roles.md#role_assignments_get) | **GET** /projects/{project_name}/role-assignments/{id} | Get role assignment
[**role_assignments_per_object_list**](./Roles.md#role_assignments_per_object_list) | **GET** /projects/{project_name}/role-assignments | List roles on object/user
[**roles_create**](./Roles.md#roles_create) | **POST** /projects/{project_name}/roles | Create a custom role scoped in a project
[**roles_delete**](./Roles.md#roles_delete) | **DELETE** /projects/{project_name}/roles/{role_name} | Delete a role from a project
[**roles_get**](./Roles.md#roles_get) | **GET** /projects/{project_name}/roles/{role_name} | Get details of a role
[**roles_list**](./Roles.md#roles_list) | **GET** /projects/{project_name}/roles | List the available roles in a project
[**roles_update**](./Roles.md#roles_update) | **PATCH** /projects/{project_name}/roles/{role_name} | Update a role in a project
[**service_users_create**](./ServiceUsers.md#service_users_create) | **POST** /projects/{project_name}/service-users | Create a new service user
[**service_users_delete**](./ServiceUsers.md#service_users_delete) | **DELETE** /projects/{project_name}/service-users/{service_user_id} | Delete service user
[**service_users_get**](./ServiceUsers.md#service_users_get) | **GET** /projects/{project_name}/service-users/{service_user_id} | Retrieve details of a service user
[**service_users_list**](./ServiceUsers.md#service_users_list) | **GET** /projects/{project_name}/service-users | List service users
[**service_users_token**](./ServiceUsers.md#service_users_token) | **PUT** /projects/{project_name}/service-users/{service_user_id}/token | Reset the token of a service user
[**service_users_update**](./ServiceUsers.md#service_users_update) | **PATCH** /projects/{project_name}/service-users/{service_user_id} | Update service user details
[**service_status**](./Status.md#service_status) | **GET** /status | Service status
[**user_create**](./User.md#user_create) | **POST** /user | Create a new user
[**user_delete**](./User.md#user_delete) | **DELETE** /user | Delete user
[**webhook_tests_create**](./Webhooks.md#webhook_tests_create) | **POST** /projects/{project_name}/webhooks-tests | Create webhook tests
[**webhook_tests_get**](./Webhooks.md#webhook_tests_get) | **GET** /projects/{project_name}/webhooks-tests/{test_id} | Get webhook test
[**webhooks_create**](./Webhooks.md#webhooks_create) | **POST** /projects/{project_name}/webhooks | Create webhooks
[**webhooks_delete**](./Webhooks.md#webhooks_delete) | **DELETE** /projects/{project_name}/webhooks/{webhook_name} | Delete a webhook
[**webhooks_get**](./Webhooks.md#webhooks_get) | **GET** /projects/{project_name}/webhooks/{webhook_name} | Get webhook
[**webhooks_list**](./Webhooks.md#webhooks_list) | **GET** /projects/{project_name}/webhooks | List webhooks
[**webhooks_update**](./Webhooks.md#webhooks_update) | **PATCH** /projects/{project_name}/webhooks/{webhook_name} | Update a webhook


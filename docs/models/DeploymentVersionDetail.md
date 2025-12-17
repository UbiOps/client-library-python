# DeploymentVersionDetail

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**id** | **str** | [optional] [readonly]
**deployment** | **str** |
**version** | **str** |
**default** | **bool** | [optional]
**description** | **str** | [optional]
**environment** | **str** | [optional]
**environment_display_name** | **str** | [optional]
**status** | **str** | [optional] [readonly]
**active_revision** | **str** | [optional] [readonly]
**latest_revision** | **str** | [optional] [readonly]
**maximum_instances** | **int** | [optional]
**minimum_instances** | **int** | [optional]
**maximum_idle_time** | **int** | [optional]
**labels** | **dict(str, str)** | [optional]
**creation_date** | **datetime** | [optional]
**last_updated** | **datetime** | [optional]
**request_retention_time** | **int** | [optional]
**request_retention_mode** | **str** | [optional]
**maximum_queue_size** | **int** | [optional]
**static_ip** | **bool** | [optional]
**restart_request_interruption** | **bool** | [optional]
**ports** | [**list[DeploymentVersionPort]**](DeploymentVersionPort.md) | [optional]
**instance_type** | **str** | [optional] [readonly]
**scaling_strategy** | **str** | [optional]
**instance_processes** | **int** | [optional]
**instance_type_group_id** | **str** | [optional] [readonly]
**instance_type_group_name** | **str** | [optional] [readonly]
**last_file_upload** | **datetime** | [optional] [readonly]
**has_request_method** | **bool** | [optional] [readonly]
**has_requests_method** | **bool** | [optional] [readonly]



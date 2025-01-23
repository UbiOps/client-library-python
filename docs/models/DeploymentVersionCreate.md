# DeploymentVersionCreate

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**version** | **str** |
**environment** | **str** | [optional]
**instance_type** | **str** | [optional]
**instance_type_group_id** | **str** | [optional]
**instance_type_group_name** | **str** | [optional]
**maximum_instances** | **int** | [optional]
**minimum_instances** | **int** | [optional]
**maximum_idle_time** | **int** | [optional]
**description** | **str** | [optional]
**labels** | **dict(str, str)** | [optional]
**request_retention_time** | **int** | [optional]
**request_retention_mode** | **str** | [optional]
**maximum_queue_size_express** | **int** | [optional]
**maximum_queue_size_batch** | **int** | [optional]
**static_ip** | **bool** | [optional]
**restart_request_interruption** | **bool** | [optional]
**ports** | [**list[DeploymentVersionPort]**](DeploymentVersionPort.md) | [optional]
**scaling_strategy** | **str** | [optional]
**instance_processes** | **int** | [optional]



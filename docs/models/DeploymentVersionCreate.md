# DeploymentVersionCreate

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**version** | **str** | 
**language** | **str** | [optional] 
**environment** | **str** | [optional] [default to 'python3-10']
**instance_type** | **str** | [optional] 
**maximum_instances** | **int** | [optional] 
**minimum_instances** | **int** | [optional] 
**maximum_idle_time** | **int** | [optional] 
**description** | **str** | [optional] 
**labels** | **dict(str, str)** | [optional] 
**monitoring** | **str** | [optional] 
**request_retention_time** | **int** | [optional] 
**request_retention_mode** | **str** | [optional] [default to 'full']
**default_notification_group** | **str** | [optional] 
**maximum_queue_size_express** | **int** | [optional] 
**maximum_queue_size_batch** | **int** | [optional] 
**static_ip** | **bool** | [optional] [default to False]
**restart_request_interruption** | **bool** | [optional] [default to False]



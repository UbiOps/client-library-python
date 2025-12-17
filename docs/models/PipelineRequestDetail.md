# PipelineRequestDetail

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**id** | **str** |
**pipeline** | **str** | [optional]
**version** | **str** |
**status** | **str** |
**success** | **bool** | [optional] [deprecated]
**time_created** | **datetime** |
**time_started** | **datetime** | [optional]
**time_completed** | **datetime** | [optional]
**request_data** | **str** or **dict(str, str)** | [optional] [deprecated]
**result** | **str** or **dict(str, str)** | [optional] [deprecated]
**error_message** | **str** | [optional]
**pipeline_timeout** | **int** | [optional]
**deployment_timeout** | **int** | [optional]
**input_size** | **int** | [optional]
**output_size** | **int** | [optional]
**deployment_requests** | [**list[PipelineRequestDeploymentRequest]**](PipelineRequestDeploymentRequest.md) |
**operator_requests** | [**list[PipelineRequestOperatorRequest]**](PipelineRequestOperatorRequest.md) |
**pipeline_requests** | [**list[PipelineRequestPipelineRequest]**](PipelineRequestPipelineRequest.md) |



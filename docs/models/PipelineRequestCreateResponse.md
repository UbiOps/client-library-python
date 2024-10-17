# PipelineRequestCreateResponse

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**id** | **str** |
**pipeline** | **str** | [optional]
**version** | **str** |
**deployment_requests** | [**list[PipelineRequestDeploymentRequest]**](PipelineRequestDeploymentRequest.md) |
**operator_requests** | [**list[PipelineRequestOperatorRequest]**](PipelineRequestOperatorRequest.md) |
**pipeline_requests** | [**list[PipelineRequestPipelineRequest]**](PipelineRequestPipelineRequest.md) |
**result** | **str** or **dict(str, str)** | [optional]
**status** | **str** |
**success** | **bool** | [optional] [deprecated]
**error_message** | **str** | [optional]
**pipeline_timeout** | **int** | [optional]
**deployment_timeout** | **int** | [optional]



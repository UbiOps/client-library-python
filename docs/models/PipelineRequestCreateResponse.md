# PipelineRequestCreateResponse

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**id** | **str** |
**pipeline** | **str** | [optional]
**version** | **str** |
**deployment_requests** | [**list[DirectPipelineRequestDeploymentRequest]**](DirectPipelineRequestDeploymentRequest.md) |
**operator_requests** | [**list[DirectPipelineRequestOperatorRequest]**](DirectPipelineRequestOperatorRequest.md) |
**pipeline_requests** | [**list[DirectPipelineRequestPipelineRequest]**](DirectPipelineRequestPipelineRequest.md) |
**result** | **str** or **dict(str, str)** | [optional]
**status** | **str** |
**success** | **bool** | [optional] [deprecated]
**error_message** | **str** | [optional]
**pipeline_timeout** | **int** | [optional]
**deployment_timeout** | **int** | [optional]



# DeploymentRequestSingleDetail

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**id** | **str** |
**deployment** | **str** | [optional]
**version** | **str** |
**status** | **str** |
**success** | **bool** | [optional] [deprecated]
**time_created** | **datetime** |
**time_started** | **datetime** | [optional]
**time_completed** | **datetime** | [optional]
**input_size** | **int** | [optional]
**output_size** | **int** | [optional]
**error_message** | **str** | [optional]
**timeout** | **int** | [optional]
**request_data** | **str** or **dict(str, str)** | [optional] [deprecated]
**result** | **str** or **dict(str, str)** | [optional] [deprecated]
**additional_data** | [**AdditionalData**](AdditionalData.md) | [optional]
**origin** | **dict(str, str)** | [optional]



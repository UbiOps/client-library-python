# ServiceDetail

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**id** | **str** |
**name** | **str** |
**deployment** | **str** |
**version** | **str** | [optional]
**port** | **int** |
**time_created** | **datetime** |
**time_updated** | **datetime** |
**labels** | **dict(str, str)** | [optional]
**authentication_required** | **bool** | [optional]
**description** | **str** | [optional]
**authentication_method_token_enabled** | **bool** | [optional]
**request_logging_excluded_paths** | **str** | [optional]
**request_logging_excluded_extensions** | **list[str]** | [optional]
**health_check** | [**HealthCheck**](HealthCheck.md) | [optional]
**rate_limit_token** | **int** | [optional]
**endpoint** | **str** | [optional] [readonly]



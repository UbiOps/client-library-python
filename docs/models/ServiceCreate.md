# ServiceCreate

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**name** | **str** |
**deployment** | **str** |
**version** | **str** | [optional]
**port** | **int** |
**description** | **str** | [optional]
**labels** | **dict(str, str)** | [optional]
**authentication_required** | **bool** | [optional]
**authentication_method_token_enabled** | **bool** | [optional]
**request_logging_excluded_paths** | **str** | [optional]
**request_logging_excluded_extensions** | **list[str]** | [optional]
**health_check** | [**HealthCheck**](HealthCheck.md) | [optional]
**rate_limit_token** | **int** | [optional]



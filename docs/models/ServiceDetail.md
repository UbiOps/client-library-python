# ServiceDetail

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**id** | **str** | [optional] [readonly]
**name** | **str** |
**deployment** | **str** |
**version** | **str** | [optional]
**port** | **int** |
**time_created** | **datetime** | [optional] [readonly]
**time_updated** | **datetime** | [optional] [readonly]
**labels** | **dict(str, str)** | [optional]
**authentication_required** | **bool** | [optional]
**description** | **str** | [optional]
**authentication_method_token_enabled** | **bool** | [optional]
**authentication_header_pass_through** | **bool** | [optional]
**request_logging_excluded_paths** | **str** | [optional]
**request_logging_excluded_extensions** | **list[str]** | [optional]
**rate_limit** | **int** | [optional]
**rate_limit_user_default** | **int** | [optional]
**concurrency_limit** | **int** | [optional]
**concurrency_limit_user_default** | **int** | [optional]
**endpoint** | **str** | [optional] [readonly]



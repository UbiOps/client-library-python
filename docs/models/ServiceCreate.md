# ServiceCreate

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**name** | **str** |
**description** | **str** | [optional]
**labels** | **dict(str, str)** | [optional]
**port** | **int** |
**authentication_required** | **bool** | [optional]
**authentication_method_token_enabled** | **bool** | [optional]
**authentication_header_pass_through** | **bool** | [optional]
**request_logging_excluded_paths** | **str** | [optional]
**request_logging_excluded_extensions** | **list[str]** | [optional]
**deployment** | **str** | [optional]
**version** | **str** | [optional]
**rate_limit** | **int** | [optional]
**rate_limit_user_default** | **int** | [optional]
**concurrency_limit** | **int** | [optional]
**concurrency_limit_user_default** | **int** | [optional]
**type** | **str** | [optional]
**cache_aware_llm_routing** | **bool** | [optional]
**imported_name** | **str** | [optional]
**imported_namespace** | **str** | [optional]
**imported_cluster_domain** | **str** | [optional]



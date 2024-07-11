# WebhookDetail

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**id** | **str** | [optional] [readonly]
**name** | **str** |
**object_type** | **str** | [optional] [readonly]
**object_name** | **str** | [optional] [readonly]
**version** | **str** | [optional] [readonly]
**url** | **str** |
**headers** | [**list[WebhookHeader]**](WebhookHeader.md) | [optional] [readonly]
**event** | **str** |
**creation_date** | **datetime** | [optional]
**last_updated** | **datetime** | [optional]
**description** | **str** | [optional]
**labels** | **dict(str, str)** | [optional]
**timeout** | **int** | [optional]
**enabled** | **bool** | [optional]
**retry** | **bool** | [optional]
**include_result** | **bool** | [optional]



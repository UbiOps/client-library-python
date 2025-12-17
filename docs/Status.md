# Status

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_status**](./Status.md#service_status) | **GET** /status | Service status


# **service_status**
> Status service_status()

Service status

## Description
Request the API status. It can be used to determine whether the API is online. You do not have to be authenticated to access this method.

### Response Structure

- `status`: API status, either ok or fail. The database connection is tested at each status request, to make sure that the API is online.

## Response Examples

```
{
  "status": "ok"
}
```

### Example

Initialize [**core_api**](./CoreApi.md#example) using your credentials.

```python

# Service status
api_response = core_api.service_status()
print(api_response)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Status**](./models/Status.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


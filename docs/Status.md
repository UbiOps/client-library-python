# Status

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_status**](Status.md#service_status) | **GET** /status | Service status


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

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()


    # Service status
    api_response = core_api.service_status()
    print(api_response)

    # Close the connection
    core_api.api_client.close()
    ```

- Use authorization parameters
    ```python
    import ubiops

    configuration = ubiops.Configuration()
    # Configure API token authorization
    configuration.api_key['Authorization'] = "Token <YOUR_API_TOKEN>"
    # Defining host is optional and default to "https://api.ubiops.com/v2.1"
    configuration.host = "https://api.ubiops.com/v2.1"

    api_client = ubiops.ApiClient(configuration)
    core_api = ubiops.CoreApi(api_client)


    # Service status
    api_response = core_api.service_status()
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters

This endpoint does not need any parameter.

### Return type

[**Status**](./models/Status.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


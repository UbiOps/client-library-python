# Webhooks

All URIs are relative to *https://api.ubiops.com/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_tests_create**](./Webhooks.md#webhook_tests_create) | **POST** /projects/{project_name}/webhooks-tests | Create webhook tests
[**webhook_tests_get**](./Webhooks.md#webhook_tests_get) | **GET** /projects/{project_name}/webhooks-tests/{test_id} | Get webhook test
[**webhooks_create**](./Webhooks.md#webhooks_create) | **POST** /projects/{project_name}/webhooks | Create webhooks
[**webhooks_delete**](./Webhooks.md#webhooks_delete) | **DELETE** /projects/{project_name}/webhooks/{webhook_name} | Delete a webhook
[**webhooks_get**](./Webhooks.md#webhooks_get) | **GET** /projects/{project_name}/webhooks/{webhook_name} | Get webhook
[**webhooks_list**](./Webhooks.md#webhooks_list) | **GET** /projects/{project_name}/webhooks | List webhooks
[**webhooks_update**](./Webhooks.md#webhooks_update) | **PATCH** /projects/{project_name}/webhooks/{webhook_name} | Update a webhook


# **webhook_tests_create**
> WebhookTestDetail webhook_tests_create(project_name, data)

Create webhook tests

## Description
Test a webhook

### Required Parameters

- `url`: Callback url to send event payloads to
- `object_type`: Type of object for which the webhook will be tested. It can be either 'deployment' or 'pipeline'.
- `object_name`: Name of deployment or pipeline for which the webhook will be tested
- `event`: Event that triggers the webhook

### Optional Parameters

- `headers`: Request headers to use when calling the webhook
- `version`: Name of deployment/pipeline version for which the webhook will be tested. If not provided, the default version of the deployment/pipeline will be used.
- `timeout`: Timeout in seconds on the call to webhook. It defaults to 10 seconds and the maximum value is 30 seconds.
- `retry`: Boolean value indicating whether the calls to the webhook should be retried if they fail (network timeout or non 2xx or 3xx HTTP response). It defaults to False.
- `include_result`: Boolean indicating whether the result of a request should be included in the webhook call. It defaults to False.

## Request Examples

```
{
  "url": "https://callback-url-webhook-1.com",
  "object_type": "deployment",
  "object_name": "deployment-1",
  "event": "deployment_request_finished"
}
```

### Response Structure
Details of the test

- `id`: Unique identifier for the test (UUID)
- `status`: Status of the test. It can be one of the following: 'pending', 'completed' or 'failed'.
- `error_message`: An error message explaining why the test has failed

## Response Examples

```
{
  "id": "ed64752b-5f05-4c26-9c4f-f1aba5ce38e1",
  "status": "pending",
  "error_message": null
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

    project_name = 'project_name_example' # str
    data = ubiops.WebhookTestCreate() # WebhookTestCreate

    # Create webhook tests
    api_response = core_api.webhook_tests_create(project_name, data)
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

    project_name = 'project_name_example' # str
    data = ubiops.WebhookTestCreate() # WebhookTestCreate

    # Create webhook tests
    api_response = core_api.webhook_tests_create(project_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**WebhookTestCreate**](./models/WebhookTestCreate.md) | 

### Return type

[**WebhookTestDetail**](./models/WebhookTestDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **webhook_tests_get**
> WebhookTestDetail webhook_tests_get(project_name, test_id)

Get webhook test

## Description
Retrieve details of a webhook test in a project

### Response Structure
Details of a test

- `id`: Unique identifier for the test (UUID)
- `status`: Status of the test. It can be one of the following: 'pending', 'completed' or 'failed'.
- `error_message`: An error message explaining why the test has failed

## Response Examples

Pending test

```
{
  "id": "ed64752b-5f05-4c26-9c4f-f1aba5ce38e1",
  "status": "pending",
  "error_message": null
}
```

Completed test

```
{
  "id": "ed64752b-5f05-4c26-9c4f-f1aba5ce38e1",
  "status": "completed",
  "error_message": null
}
```

Failed test

```
{
  "id": "ed64752b-5f05-4c26-9c4f-f1aba5ce38e1",
  "status": "failed",
  "error_message": "Connection error"
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

    project_name = 'project_name_example' # str
    test_id = 'test_id_example' # str

    # Get webhook test
    api_response = core_api.webhook_tests_get(project_name, test_id)
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

    project_name = 'project_name_example' # str
    test_id = 'test_id_example' # str

    # Get webhook test
    api_response = core_api.webhook_tests_get(project_name, test_id)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **test_id** | **str** | 

### Return type

[**WebhookTestDetail**](./models/WebhookTestDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **webhooks_create**
> WebhookDetail webhooks_create(project_name, data)

Create webhooks

## Description
Create a webhook

### Required Parameters

- `name`: Name of the webhook. It is unique within a project.
- `url`: Callback url to send event payloads to
- `object_type`: Type of object for which the webhook will be created. It can be either 'deployment' or 'pipeline'.
- `object_name`: Name of deployment or pipeline for which the webhook will be created
- `event`: Event that triggers the webhook

### Optional Parameters

- `headers`: Request headers to use when calling the webhook. It defaults to an empty list.
- `description`: Description of the webhook
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `version`: Name of deployment/pipeline version for which the webhook will be created. If not provided, the default version of the deployment/pipeline will be used.
- `timeout`: Timeout in seconds on the call to webhook. It defaults to 10 seconds and the maximum value is 30 seconds.
- `enabled`: Boolean value indicating whether the webhook is enabled or disabled. It defaults to True.
- `retry`: Boolean value indicating whether the calls to the webhook should be retried if they fail (network timeout or non 2xx or 3xx HTTP response). It defaults to False.
- `include_result`: Boolean indicating whether the result of a request should be included in the webhook call. It defaults to False.

## Request Examples

```
{
  "name": "webhook-1",
  "url": "https://callback-url-webhook-1.com",
  "headers": [
    {
      "key": "Authorization",
      "value": "Token 123",
      "protected": true
    }
  ],
  "object_type": "deployment",
  "object_name": "deployment-1",
  "version": "v1",
  "event": "deployment_request_finished"
}
```

### Response Structure
Details of the created webhook

- `id`: Unique identifier for the webhook (UUID)
- `name`: Name of the webhook
- `url`: Callback url to send event payloads to
- `headers`: Request headers to use when calling the webhook
- `object_type`: Type of object for which the webhook is created
- `object_name`: Name of deployment or pipeline for which the webhook is created
- `version`: Name of deployment/pipeline version for which the webhook is created
- `description`: Description of the webhook
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `event`: Event that triggers the webhook
- `timeout`: Timeout in seconds on the call to webhook
- `enabled`: Boolean value indicating whether the webhook is enabled or disabled
- `retry`: Boolean value indicating whether the calls to webhook should be retried if they fail

## Response Examples

```
{
  "id": "e54251d8-e518-424f-bf7d-c45aaf26f72c",
  "name": "webhook-1",
  "url": "https://callback-url-webhook-1.com",
  "headers": [
    {
      "key": "Authorization",
      "value": "Token 123",
      "protected": true
  ],
  "object_type": "deployment",
  "object_name": "deployment-1",
  "version": "v1",
  "description": "",
  "labels": {
    "event-type": "request-finished"
  },
  "event": "deployment_request_finished",
  "timeout": 10,
  "enabled": true,
  "retry": false,
  "include_result": false
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

    project_name = 'project_name_example' # str
    data = ubiops.WebhookCreate() # WebhookCreate

    # Create webhooks
    api_response = core_api.webhooks_create(project_name, data)
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

    project_name = 'project_name_example' # str
    data = ubiops.WebhookCreate() # WebhookCreate

    # Create webhooks
    api_response = core_api.webhooks_create(project_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **data** | [**WebhookCreate**](./models/WebhookCreate.md) | 

### Return type

[**WebhookDetail**](./models/WebhookDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **webhooks_delete**
> webhooks_delete(project_name, webhook_name)

Delete a webhook

## Description
Delete a webhook

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    webhook_name = 'webhook_name_example' # str

    # Delete a webhook
    core_api.webhooks_delete(project_name, webhook_name)

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

    project_name = 'project_name_example' # str
    webhook_name = 'webhook_name_example' # str

    # Delete a webhook
    core_api.webhooks_delete(project_name, webhook_name)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **webhook_name** | **str** | 

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **webhooks_get**
> WebhookDetail webhooks_get(project_name, webhook_name)

Get webhook

## Description
Retrieve details of a webhook in a project

### Response Structure
Details of a webhook

- `id`: Unique identifier for the webhook (UUID)
- `name`: Name of the webhook
- `url`: Callback url to send event payloads to
- `headers`: Request headers to use when calling the webhook
- `object_type`: Type of object for which the webhook is created
- `object_name`: Name of deployment or pipeline for which the webhook is created
- `version`: Name of deployment/pipeline version for which the webhook is created
- `description`: Description of the webhook
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `event`: Event that triggers the webhook
- `timeout`: Timeout in seconds on the call to webhook
- `enabled`: Boolean value indicating whether the webhook is enabled or disabled
- `retry`: Boolean value indicating whether the calls to webhook should be retried if they fail
- `include_result`: Boolean indicating whether the result of a request should be included in the webhook call

## Response Examples

```
{
  "id": "e54251d8-e518-424f-bf7d-c45aaf26f72c",
  "name": "webhook-1",
  "url": "https://callback-url-webhook-1.com",
  "headers": [],
  "object_type": "deployment",
  "object_name": "deployment-1",
  "version": "v1",
  "description": "",
  "labels": {
    "event-type": "request-finished"
  },
  "event": "deployment_request_finished",
  "timeout": 10,
  "enabled": true,
  "retry": false,
  "include_result": false
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

    project_name = 'project_name_example' # str
    webhook_name = 'webhook_name_example' # str

    # Get webhook
    api_response = core_api.webhooks_get(project_name, webhook_name)
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

    project_name = 'project_name_example' # str
    webhook_name = 'webhook_name_example' # str

    # Get webhook
    api_response = core_api.webhooks_get(project_name, webhook_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **webhook_name** | **str** | 

### Return type

[**WebhookDetail**](./models/WebhookDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **webhooks_list**
> list[WebhookDetail] webhooks_list(project_name, labels=labels, object_type=object_type, event=event)

List webhooks

## Description
List the webhooks in a project

### Response Structure
A list of details of the webhooks in the project

- `id`: Unique identifier for the webhook (UUID)
- `name`: Name of the webhook
- `url`: Callback url to send event payloads to
- `headers`: Request headers to use when calling the webhook
- `object_type`: Type of object for which the webhook is created
- `object_name`: Name of deployment or pipeline for which the webhook is created
- `version`: Name of deployment/pipeline version for which the webhook is created
- `description`: Description of the webhook
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `event`: Event that triggers the webhook
- `timeout`: Timeout in seconds on the call to webhook
- `enabled`: Boolean value indicating whether the webhook is enabled or disabled
- `retry`: Boolean value indicating whether the calls to webhook should be retried if they fail
- `include_result`: Boolean indicating whether the result of a request should be included in the webhook call

## Response Examples

```
[
  {
    "id": "e54251d8-e518-424f-bf7d-c45aaf26f72c",
    "name": "webhook-1",
    "url": "https://callback-url-webhook-1.com",
    "headers": [],
    "object_type": "deployment",
    "object_name": "deployment-1",
    "version": "v1",
    "description": "",
    "labels": {
      "event-type": "request-finished"
    },
    "event": "deployment_request_finished",
    "timeout": 10,
    "enabled": true,
    "retry": false,
    "include_result": false
  },
  {
    "id": "cbfb3944-bbcb-4e18-907a-54d2f792a136",
    "name": "webhook-2",
    "url": "https://callback-url-webook-2.com",
    "headers": [],
    "object_type": "deployment",
    "object_name": "deployment-2",
    "version": null,
    "description": "",
    "labels": {
      "event-type": "request-failed"
    },
    "event": "deployment_request_failed",
    "timeout": 15,
    "enabled": true,
    "retry": false,
    "include_result": false
  },
]
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    core_api = ubiops.CoreApi()

    project_name = 'project_name_example' # str
    labels = 'labels_example' # str (optional)
    object_type = 'object_type_example' # str (optional)
    event = 'event_example' # str (optional)

    # List webhooks
    api_response = core_api.webhooks_list(project_name, labels=labels, object_type=object_type, event=event)
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

    project_name = 'project_name_example' # str
    labels = 'labels_example' # str (optional)
    object_type = 'object_type_example' # str (optional)
    event = 'event_example' # str (optional)

    # List webhooks
    api_response = core_api.webhooks_list(project_name, labels=labels, object_type=object_type, event=event)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **labels** | **str** | [optional] 
 **object_type** | **str** | [optional] 
 **event** | **str** | [optional] 

### Return type

[**list[WebhookDetail]**](./models/WebhookDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **webhooks_update**
> WebhookDetail webhooks_update(project_name, webhook_name, data)

Update a webhook

## Description
Update a webhook

### Optional Parameters

- `name`: Name for the webhook
- `url`: Callback url to send event payloads to
- `headers`: Request headers to use when calling the webhook. Use *value* None to not update the values of protected headers.
- `description`: Description of the webhook
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `event`: Event that triggers the webhook
- `timeout`: Timeout in seconds on the call to webhook
- `enabled`: Boolean value indicating whether the webhook is enabled or disabled
- `retry`: Boolean value indicating whether the calls to webhook should be retried if they fail
- `include_result`: Boolean indicating whether the result of a request should be included in the webhook call

## Request Examples

```
{
  "name": "new-webhook-name"
}
```

### Response Structure
Details of a webhook

- `id`: Unique identifier for the webhook (UUID)
- `name`: Name of the webhook
- `url`: Callback url to send event payloads to
- `headers`: Request headers to use when calling the webhook
- `object_type`: Type of object for which the webhook is created
- `object_name`: Name of deployment or pipeline for which the webhook is created
- `version`: Name of deployment/pipeline version for which the webhook is created
- `description`: Description of the webhook
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `event`: Event that triggers the webhook
- `timeout`: Timeout in seconds on the call to webhook
- `enabled`: Boolean value indicating whether the webhook is enabled or disabled
- `retry`: Boolean value indicating whether the calls to webhook should be retried if they fail
- `include_result`: Boolean indicating whether the result of a request should be included in the webhook call

## Response Examples

```
{
  "id": "e54251d8-e518-424f-bf7d-c45aaf26f72c",
  "name": "new-webhook-name",
  "url": "https://callback-url-webhook-1.com",
  "headers": [],
  "object_type": "deployment",
  "object_name": "deployment-1",
  "version": "v1",
  "description": "",
  "labels": {
    "event-type": "request-finished"
  },
  "event": "deployment_request_finished",
  "timeout": 10,
  "enabled": true,
  "retry": false,
  "include_result": false
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

    project_name = 'project_name_example' # str
    webhook_name = 'webhook_name_example' # str
    data = ubiops.WebhookUpdate() # WebhookUpdate

    # Update a webhook
    api_response = core_api.webhooks_update(project_name, webhook_name, data)
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

    project_name = 'project_name_example' # str
    webhook_name = 'webhook_name_example' # str
    data = ubiops.WebhookUpdate() # WebhookUpdate

    # Update a webhook
    api_response = core_api.webhooks_update(project_name, webhook_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


Name | Type | Notes
------------- | ------------- | -------------
 **project_name** | **str** | 
 **webhook_name** | **str** | 
 **data** | [**WebhookUpdate**](./models/WebhookUpdate.md) | 

### Return type

[**WebhookDetail**](./models/WebhookDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)


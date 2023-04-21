# RunLocal

Function(s) to run a deployment locally

| Method                                 | Description              |
|----------------------------------------|--------------------------|
| [**run_local**](RunLocal.md#run_local) | Run a deployment locally |

# **run_local**

> run_local(deployment_directory, data, init_context=dummy_init_context, request_context=dummy_request_context)

Calls the request(s) function of a deployment locally. See [dummy init context](#dummy-context) for the context
data that is passed to the init function. See [dummy request context](#dummy-context) for the context data that
is passed to the request(s) function.

## Description

Helper function to run a deployment locally. It calls the request(s) function of the deployment in the same way as would
happen when running it on UbiOps.

See [dummy init context](#dummy-context) for the context data that is passed to the init function. See
[dummy request context](#dummy-context) for the context data that is passed to the request(s) function. The
deployment will be run in the current Python environment.


### Example

```python
from ubiops import utils

request_data = {"input": 123}
result = utils.run_local("deployment_package", request_data)

print("Result:")
print(result)
```

### Parameters

| Name                     | Type                | Notes                                                                                                                   |
|--------------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------|
| **deployment_directory** | **str**             | The name of the deployment directory, absolute or relative to the current working directory, e.g. 'deployment_package'  |
| **data**                 | **dict** or **str** | Input data of the deployment request function                                                                           |
| **init_context**         | **dict**            | [optional] Context data of the deployment init function, defaults to [Dummy init context](#dummy-context)               |
| **request_context**      | **dict**            | [optional] Context data of the deployment request function, defaults to [Dummy request context](#dummy-context)         |

#### Dummy context

```python
dummy_init_context = {
    'project': 'run-local',
    'project_id': '123',
    'deployment_id': '456',
    'deployment': 'My Deployment',
    'version_id': '789',
    'version': 'v1',
    'input_type': 'structured',
    'output_type': 'structured',
    'input_fields': ['input_field_1', 'input_field_2', 'input_field_3'],
    'output_fields': ['output_field_1', 'output_field_2', 'output_field_3'],
    'language': 'python',
    'environment_variables': {
        'ENV_VAR': 'abc123'
    }
}

dummy_request_context = {
    'id': "a64c1dfb-d9bb-4e23-b66f-3795e67bb6cf",
    'request_mode': 'express',
    'user_id': "d9e30331-3edc-4a88-b8c3-027412e8baeb"
}
```

### Return type

**dict** for structured output type, or **str** for plain output type

[[Back to top]](#)

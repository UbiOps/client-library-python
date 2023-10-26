# Training

Helper functions for training.

| Method                                                                                               | Description                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------|
| [**experiments_create**](./Training.md#experiments_create)                                           | Create experiment                      |
| [**experiments_delete**](./Training.md#experiments_delete)                                           | Delete experiment                      |
| [**experiments_get**](./Training.md#experiments_get)                                                 | Get experiment                         |
| [**experiments_list**](./Training.md#experiments_list)                                               | List experiments                       |
| [**experiments_update**](./Training.md#experiments_update)                                           | Update experiment                      |
| [**experiment_runs_create**](./Training.md#experiment_runs_create)                                   | Create experiment run                  |
| [**experiment_runs_delete**](./Training.md#experiment_runs_delete)                                   | Delete experiment run                  |
| [**experiment_runs_get**](./Training.md#experiment_runs_get)                                         | Get experiment run                     |
| [**experiment_runs_list**](./Training.md#experiment_runs_list)                                       | List experiment runs                   |
| [**experiment_runs_update**](./Training.md#experiment_runs_update)                                   | Update experiment run                  |
| [**experiment_environment_variables_create**](./Training.md#experiment_environment_variables_create) | Create experiment environment variable |
| [**experiment_environment_variables_delete**](./Training.md#experiment_environment_variables_delete) | Delete experiment environment variable |
| [**experiment_environment_variables_get**](./Training.md#experiment_environment_variables_get)       | Get experiment environment variable    |
| [**experiment_environment_variables_list**](./Training.md#experiment_environment_variables_list)     | List experiment environment variables  |
| [**experiment_environment_variables_update**](./Training.md#experiment_environment_variables_update) | Update experiment environment variable |


# **experiments_create**
> ExperimentList experiments_create(project_name, data)

Create a training experiment

## Description
Helper function to create a training experiment

### Required Parameters
- `name`: The name of the experiment to create
- `environment`: The name of the runtime environment to use

### Optional Parameters
- `default_bucket`: In which bucket to store the in- and output artifacts of the training experiment
- `description`: Description of the experiment
- `instance_type`: The instance type to allocate for this experiment
- `request_retention_time`: The request retention time for this experiment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label

## Request Examples

```
{
  "name": "my-experiment",
  "environment": "python3-8"
}
```

```
{
  "name": "my-experiment",
  "description": "A training experiment",
  "environment": "python3-8",
  "instance_type": "4096mb",
  "default_bucket": "default",
  "labels": {
    "type": "pytorch"
  }
}
```

### Response Structure
Details of the created experiment

- `id`: Unique identifier for the experiment (UUID)
- `name`: Experiment name
- `environment`: Environment of the experiment
- `environment_display_name`: Human readable name of the environment
- `status`: The status of the experiment 
- `active_revision`: UUID of the active revision of the experiment
- `latest_revision`: UUID of the latest revision of the experiment
- `instance_type`: The instance type for the experiment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the experiment was created
- `last_updated`: The date when the experiment was last updated

## Response Examples

```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "name": "training-experiment",
  "environment": "python3-8",
  "environment_display_name": "Python 3.8",
  "status": "available",
  "active_revision": "7169cac3-74eb-4189-99d7-322bc71f070b",
  "latest_revision": "7169cac3-74eb-4189-99d7-322bc71f070b",
  "instance_type": "4069mb",
  "labels": {
    "type": "pytorch"
  },
  "creation_date": "2020-05-12T16:23:15.456812Z",
  "last_updated": "2020-05-12T16:23:15.456812Z"
}
```
### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    training = ubiops.Training()

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str

    # Create experiment
    api_response = training.experiments_create(
        project_name=project_name,
        data=ubiops.ExperimentCreate(
            name=experiment_name,
            instance_type='4069mb',
            description='A training experiment',
            environment='python3-8',
            default_bucket='default',
            labels={"type": "pytorch"}
        )
    )
    print(api_response)

    # Close the connection
    training.api_client.close()
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
    training = ubiops.Training(api_client)

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str

    # Create experiment
    api_response = training.experiments_create(
        project_name=project_name,
        data=ubiops.ExperimentCreate(
            name=experiment_name,
            instance_type='4069mb',
            description='A training experiment',
            environment='python3-8',
            default_bucket='default',
            labels={"type": "pytorch"}
        )
    )
    print(api_response)

    # Close the connection
    api_client.close()
    ```

### Parameters


| Name                | Type                                          | Notes |
|---------------------|-----------------------------------------------|-------|
| **project_name**    | **str**                                       |       |
| **data**            | [**ExperimentCreate**](./ExperimentCreate.md) |       |

### Return type

[**ExperimentList**](./ExperimentList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **experiments_delete**
> experiments_delete(project_name, experiment_name)

Delete a training experiment

## Description
Helper function to delete a training experiment

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    training = ubiops.Training()

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str

    # Delete experiment
    training.experiments_delete(project_name=project_name, experiment_name=experiment_name)

    # Close the connection
    training.api_client.close()
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
    training = ubiops.Training(api_client)

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str

    # Delete experiment
    training.experiments_delete(project_name=project_name, experiment_name=experiment_name)

    # Close the connection
    api_client.close()
    ```

### Parameters


| Name                | Type                                          | Notes |
|---------------------|-----------------------------------------------|-------|
| **project_name**    | **str**                                       |       |
| **experiment_name** | **str**                                       |       |

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **experiments_get**
> ExperimentDetail experiments_get(project_name, experiment_name)

Get the details of a training experiment

## Description
Helper function to get the details of a training experiment

### Response Structure
Get the details of an experiment

- `id`: Unique identifier for the experiment (UUID)
- `name`: Experiment name
- `description`: Description of the experiment
- `environment`: Environment of the experiment
- `environment_display_name`: Human readable name of the environment
- `status`: The status of the experiment
- `active_revision`: UUID of the active revision of the experiment
- `latest_revision`: UUID of the latest revision of the experiment
- `instance_type`: The instance type for the experiment
- `maximum_instances`: Upper bound of number of experiment pods running in parallel
- `minimum_instances`: Lower bound of number of experiment pods running in parallel
- `maximum_idle_time`: Maximum time in seconds a experiment stays idle before it is stopped
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the experiment was created
- `last_updated`: The date when the experiment was last updated
- `monitoring`: Name of a notification group which contains contacts to send notifications when runs for the experiment fail and recover
- `default_notification_group`: Name of a notification group which contains contacts to send notifications when runs for the experiment are completed
- `request_retention_time`: Number of seconds to store runs of the experiment
- `request_retention_mode`: Mode of retention for runs to the experiment. It can be one of the following:
    - *none* - the runs will not be stored
    - *metadata* - only the metadata of the runs will be stored
    - *full* - both the metadata and input/output of the runs will be stored
- `maximum_queue_size_express`: Maximum number of queued express runs for all instances of this experiment
- `maximum_queue_size_batch`: Maximum number of queued batch runs for all instances of this experiment
- `has_request_method`: Whether the latest revision of the experiment has a 'request' method
- `has_requests_method`: Whether the latest revision of the experiment has a 'requests' method
- `static_ip`: A boolean indicating whether the experiment should get a static IP
- `restart_request_interruption`: A boolean indicating whether the runs should be restarted in case of an interruption
- `default_bucket`: Indicates in which bucket input and output artifacts of the training job will be stored

## Response Examples

```
{
  "active_revision": "7169cac3-74eb-4189-99d7-322bc71f070b",
  "creation_date": "2021-06-15T10:12:11.554682Z",
  "default_bucket": "default",
  "default_notification_group": None,
  "description": "An experiment with Python 3.7",
  "environment": "python3-7",
  "environment_display_name": "Python 3.7",
  "has_request_method": True,
  "has_requests_method": False,
  "id": "49d7d195-2296-43c0-8eab-84b0acd6e5bc",
  "instance_type": "2048mb",
  "labels": {},
  "last_updated": 2021-06-15T10:12:11.554682Z,
  "latest_revision": "7169cac3-74eb-4189-99d7-322bc71f070b",
  "maximum_idle_time": 300,
  "maximum_instances": 10,
  "maximum_queue_size_batch": 100000,
  "maximum_queue_size_express": 100,
  "minimum_instances": 0,
  "monitoring": None,
  "name": "training-experiment",
  "request_retention_mode": "full",
  "request_retention_time": 31536000,
  "restart_request_interruption": False,
  "static_ip": False,
  "status": "available"
}
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    training = ubiops.Training()

    project_name = 'project_name_example' # str
    experiment_name = "experiment_name_example" # str

    # Get experiment details
    api_response = training.experiments_get(project_name=project_name, experiment_name=experiment_name)
    print(api_response)

    # Close the connection
    training.api_client.close()
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
    training = ubiops.Training(api_client)

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str

    # Get experiment details
    api_response = training.experiments_list(project_name=project_name, experiment_name=experiment_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```

### Parameters


| Name                | Type    | Notes |
|---------------------|---------|-------|
| **project_name**    | **str** |       |
| **experiment_name** | **str** |       |

### Return type

[**[ExperimentDetail]**](./ExperimentDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **experiments_list**
> list[ExperimentList] experiments_list(project_name)

List training experiments

## Description
Helper function to list training experiments

### Response Structure
A list of details of the experiments

- `id`: Unique identifier for the experiment (UUID)
- `name`: Experiment name
- `environment`: Environment of the experiment
- `environment_display_name`: Human readable name of the environment
- `status`: The status of the experiment 
- `active_revision`: UUID of the active revision of the experiment
- `latest_revision`: UUID of the latest revision of the experiment
- `instance_type`: The instance type for the experiment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the experiment was created
- `last_updated`: The date when the experiment was last updated

## Response Examples

```
[
  {
    "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
    "name": "experiment_name_example_1",
    "environment": "python3-8",
    "environment_display_name": "Python 3.8",
    "status": "available",
    "active_revision": "7169cac3-74eb-4189-99d7-322bc71f070b",
    "latest_revision": "7169cac3-74eb-4189-99d7-322bc71f070b",
    "instance_type": "4069mb",
    "labels": {
      "type": "pytorch"
    },
    "creation_date": "2020-05-12T16:23:15.456812Z",
    "last_updated": "2020-05-12T16:23:15.456812Z"
  },
  {
    "id": "536b4b33-b1db-4446-b07c-986806478654",
    "name": "experiment_name_example_2",
    "environment": "python3-7",
    "environment_display_name": "Python 3.7",
    "status": "available",
    "active_revision": "cd2244a7-5953-4d31-add8-e88cf5f4bb30",
    "latest_revision": "cd2244a7-5953-4d31-add8-e88cf5f4bb30",
    "instance_type": "16384mb",
    "labels": {
      "type": "tensorflow"
    },
    "creation_date": "2021-06-15T10:12:11.554682Z",
    "last_updated": "2021-06-15T10:12:11.554682Z"
  }
]
```
### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    training = ubiops.Training()

    project_name = 'project_name_example' # str

    # List experiments
    api_response = training.experiments_list(project_name=project_name)
    print(api_response)

    # Close the connection
    training.api_client.close()
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
    training = ubiops.Training(api_client)

    project_name = 'project_name_example' # str

    # List experiments
    api_response = training.experiments_list(project_name=project_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```

### Parameters


| Name                | Type                                          | Notes |
|---------------------|-----------------------------------------------|-------|
| **project_name**    | **str**                                       |       |

### Return type

[**list[ExperimentList]**](./ExperimentList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **experiments_update**
> ExperimentDetail experiments_update(project_name, experiment_name, data)

Update a training experiment

## Description
Helper function to update a training experiment

### Optional Parameters
- `name`: New name for the experiment
- `environment`: New environment for the experiment. It can be either a base or a custom environment.
- `default_bucket`: New default bucket for the experiment
- `description`: New description for the experiment
- `instance_type`: New instance type for the experiment
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label. The new labels will replace the existing value for labels.

## Request Examples

```
{
  "name": "my-experiment-new-name",
  "environment": "python3.8"
}
```

```
{
  "name": "my-experiment-new-name",
  "description": "My new description",
  "environment": "python3.7",
  "instance_type": "4096mb",
  "default_bucket": "default",
  "labels": {
    "type": "pytorch"
  }
}
```

### Response Structure
The details of the experiment

- `id`: Unique identifier for the experiment (UUID)
- `name`: Experiment name
- `description`: Description of the experiment
- `environment`: Environment of the experiment
- `environment_display_name`: Human readable name of the environment
- `status`: The status of the experiment
- `active_revision`: UUID of the active revision of the experiment
- `latest_revision`: UUID of the latest revision of the experiment
- `instance_type`: The reserved instance type for the experiment
- `maximum_instances`: Upper bound of number of experiment pods running in parallel
- `minimum_instances`: Lower bound of number of experiment pods running in parallel
- `maximum_idle_time`: Maximum time in seconds a experiment stays idle before it is stopped
- `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label
- `creation_date`: The date when the experiment was created
- `last_updated`: The date when the experiment was last updated
- `monitoring`: Name of a notification group which contains contacts to send notifications when runs for the experiment fail and recover
- `default_notification_group`: Name of a notification group which contains contacts to send notifications when runs for the experiment are completed
- `request_retention_time`: Number of seconds to store runs of the experiment
- `request_retention_mode`: Mode of retention for runs to the experiment. It can be one of the following:
    - *none* - the runs will not be stored
    - *metadata* - only the metadata of the runs will be stored
    - *full* - both the metadata and input/output of the runs will be stored
- `maximum_queue_size_express`: Maximum number of queued express runs for all instances of this experiment
- `maximum_queue_size_batch`: Maximum number of queued batch runs for all instances of this experiment
- `has_request_method`: Whether the latest revision of the experiment has a 'request' method
- `has_requests_method`: Whether the latest revision of the experiment has a 'requests' method
- `static_ip`: A boolean indicating whether the experiment should get a static IP
- `restart_request_interruption`: A boolean indicating whether the runs should be restarted in case of an interruption
- `default_bucket`: Indicates in which bucket input and output artifacts of the training job will be stored

## Response Examples

```
{
  "active_revision": "7169cac3-74eb-4189-99d7-322bc71f070b",
  "creation_date": "2021-06-15T10:12:11.554682Z",
  "default_bucket": "default",
  "default_notification_group": None,
  "description": "An experiment with Python 3.7",
  "environment": "python3-7",
  "environment_display_name": "Python 3.7",
  "has_request_method": True,
  "has_requests_method": False,
  "id": "49d7d195-2296-43c0-8eab-84b0acd6e5bc",
  "instance_type": "2048mb",
  "labels": {},
  "last_updated": 2021-06-15T10:12:11.554682Z,
  "latest_revision": "7169cac3-74eb-4189-99d7-322bc71f070b",
  "maximum_idle_time": 300,
  "maximum_instances": 10,
  "maximum_queue_size_batch": 100000,
  "maximum_queue_size_express": 100,
  "minimum_instances": 0,
  "monitoring": None,
  "name": "training-experiment",
  "request_retention_mode": "full",
  "request_retention_time": 31536000,
  "restart_request_interruption": False,
  "static_ip": False,
  "status": "available"
}
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    training = ubiops.Training()

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str
    new_experiment_name = 'experiment_new_name_example' # str

    # Update experiment
    api_response = training.experiments_update(
        project_name=project_name,
        experiment_name=experiment_name,
        data=ubiops.ExperimentUpdate(name=new_experiment_name)
    )
    print(api_response)

    # Close the connection
    training.api_client.close()
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
    training = ubiops.Training(api_client)

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str
    new_experiment_name = 'experiment_new_name_example' # str

    # Update experiment
    api_response = training.experiments_update(
        project_name=project_name,
        experiment_name=experiment_name,
        data=ubiops.ExperimentUpdate(name=new_experiment_name)
    )
    print(api_response)

    # Close the connection
    api_client.close()
    ```

### Parameters


| Name                | Type                                          | Notes |
|---------------------|-----------------------------------------------|-------|
| **project_name**    | **str**                                       |       |
| **experiment_name** | **str**                                       |       |
| **data**            | [**ExperimentUpdate**](./ExperimentUpdate.md) |       |

### Return type

[**ExperimentDetail**](./ExperimentDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **experiment_runs_create**
> ExperimentRunCreateResponse experiment_runs_create(project_name, experiment_name, data)

Create an experiment run

## Description
Helper function to create an experiment run

### Required Parameters
- `name`: The name of the experiment run
- `training_code`: A reference to a location containing the training code. Can be an UbiOps file uri, directory or file

### Optional Parameters
- `description`: Description of the experiment run
- `training_data`: A reference to a location containing the training data. Can be an UbiOps file uri, directory or file
- `parameters`: Dictionary containing key/value pairs with training parameters

## Request Examples

```
{
  "name": "my-run",
  "training_code": "train.py"
}
```

```
{
  "name": "my-run",
  "training_code": "ubiops-file://default/train.py",
  "training_data": "my-training-data-directory",
  "parameters = {
    "nr_epochs": 15,
    "batch_size": 32
  }
}
```

### Response Structure
Details of the created run

- `id`: Unique identifier for the run (UUID)
- `experiment`: Experiment name for which the run was created
- `status`: The status of the run
- `time_created`: The date when the run was created

## Response Examples

```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "experiment": "my-experiment-name",
  "status": "pending",
  "time_created": "2020-05-12T16:23:15.456812Z"
}
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    training = ubiops.Training()

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str

    # Create run
    api_response = training.experiment_runs_create(
        project_name=project_name,
        experiment_name=experiment_name,
        data=ubiops.ExperimentRunCreate(
            name="my-run",
            training_code="./train.py"
        )
    )
    print(api_response)

    # Close the connection
    training.api_client.close()
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
    training = ubiops.Training(api_client)

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str

    # Create run
    api_response = training.experiment_runs_create(
        project_name=project_name,
        experiment_name=experiment_name,
        data=ubiops.ExperimentRunCreate(
            name="my-run",
            training_code="./train.py"
        )
    )
    print(api_response)

    # Close the connection
    api_client.close()
    ```

### Parameters


| Name                | Type                                                | Notes |
|---------------------|-----------------------------------------------------|-------|
| **project_name**    | **str**                                             |       |
| **experiment_name** | **str**                                             |       | 
| **data**            | [**ExperimentRunCreate**](./ExperimentRunCreate.md) |       |

### Return type

[**ExperimentRunCreateResponse**](./ExperimentRunCreateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **experiment_runs_delete**
> experiment_runs_delete(project_name, experiment_name, run_id)

Delete an experiment run

## Description
Helper function to delete an experiment run

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    training = ubiops.Training()

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str
    run_id = "9eaee2b8-daf9-49fc-b958-be31f6ac48e3" # str

    # Delete run
    training.experiment_runs_delete(
        project_name=project_name,
        experiment_name=experiment_name,
        run_id=run_id
    )

    # Close the connection
    training.api_client.close()
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
    training = ubiops.Training(api_client)

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str
    run_id = "9eaee2b8-daf9-49fc-b958-be31f6ac48e3" # str

    # Delete run
    training.experiment_runs_delete(
        project_name=project_name,
        experiment_name=experiment_name,
        run_id=run_id,
    )

    # Close the connection
    api_client.close()
    ```

### Parameters


| Name                | Type                                                | Notes |
|---------------------|-----------------------------------------------------|-------|
| **project_name**    | **str**                                             |       |
| **experiment_name** | **str**                                             |       | 
| **run_id**          | **str**                                             |       |

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **experiment_runs_get**
> ExperimentRunDetail experiment_runs_get(project_name, experiment_name, run_id)

Get an experiment run

## Description
Helper function to get an experiment run details

### Response Structure
Get the details of an experiment run

- `id`: Unique identifier for the run
- `experiment`: Experiment name for which the run was created
- `status`: Status of the run. Can be 'pending', 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `success`: A boolean value that indicates whether the run was successful. NULL if the run is not yet finished.
- `time_created`: Server time that the run was made (current time)
- `time_started`: Server time that the processing of the run was started
- `time_completed`: Server time that the processing of the run was completed
- `error_message`: An error message explaining why the run has failed. NULL if the run was successful.
- `retries`: Number of times that the run has been retried
- `request_data`: A dictionary containing the data that was sent when the run was created
- `result`: Run result. NULL if the run is 'pending', 'processing' or 'failed'.
- `notification_group`: Name of a notification group to send notifications (e.g., emails) when the run is completed
- `origin`: A dictionary containing the information on where the run originated from. It contains:
  - `created_by` field indicating the user that created the run

## Response Examples

```
{
  "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
  "experiment": "my-experiment-name",
  "status": "completed",
  "success": True,
  "time_created": "2020-03-29T08:09:10.729+00:00",
  "time_started": "2020-03-28T20:00:41.276+00:00",
  "time_completed": "2020-03-28T20:00:42.241+00:00",
  "error_message": None,
  "retries": 0,
  "request_data": {
    "name": "my-experiment-run-name",
    "training_code": "ubiops-file://default/training_code.zip",
    "parameters": {
      "batch_size": 32,
      "nr_epochs": 15
    }
  },
  "result": {
    "artifact": "ubiops-file://default/a83f4004-412b-4cd9-be05-55a2789438e8/model.pkl",
    "metadata": None,
    "metrics": {"accuracy": 1.0, "loss": 0.0}
  },
  "notification_group": None,
  "origin": {
    "created_by": "my.example.user@ubiops.com",
  }
}
```

```
{
  "id": "2f909aeb-5c7e-4974-970d-cd0a6a073aca",
  "experiment": "my-experiment-name",
  "status": "completed",
  "success": False,
  "time_created": "2020-03-29T08:09:10.729+00:00",
  "time_started": "2020-03-28T20:00:41.276+00:00",
  "time_completed": "2020-03-28T20:00:42.241+00:00",
  "error_message": "An exception occurred in the request. See the logs for details.",
  "retries": 0,
  "request_data": {
    "name": "my-experiment-run-name",
    "training_code": "ubiops-file://default/training_code.zip",
  },
  "result": None,
  "notification_group": None,
  "origin": {
    "created_by": "my.example.user@ubiops.com",
  }
}
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    training = ubiops.Training()

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str
    run_id = "9eaee2b8-daf9-49fc-b958-be31f6ac48e3" # str

    # Get experiment run
    api_response = training.experiment_runs_get(
        project_name=project_name,
        experiment_name=experiment_name,
        run_id=run_id
    )
    print(api_response)

    # Close the connection
    training.api_client.close()
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
    training = ubiops.Training(api_client)

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str
    run_id = "9eaee2b8-daf9-49fc-b958-be31f6ac48e3" # str

    # Get experiment run
    api_response = training.experiment_runs_get(
        project_name=project_name,
        experiment_name=experiment_name,
        run_id=run_id
    )
    print(api_response)

    # Close the connection
    api_client.close()
    ```

### Parameters


| Name                | Type    | Notes |
|---------------------|---------|-------|
| **project_name**    | **str** |       |
| **experiment_name** | **str** |       |
| **run_id**          | **str** |       | 

### Return type

[**ExperimentRunDetail**](./ExperimentRunDetail.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **experiment_runs_list**
> list[ExperimentRunList] experiment_runs_list(project_name, experiment_name)

List experiment runs

## Description
Helper function to list experiment runs

### Response Structure
A list of details of the experiment runs

- `id`: Unique identifier for the run (UUID)
- `experiment`: Experiment name for which the run was created
- `status`: Status of the run. Can be 'pending', 'processing', 'failed', 'completed', 'cancelled' or 'cancelled_pending'.
- `success`: A boolean value that indicates whether the run was successful. NULL if the run is not yet finished.
- `time_created`: Server time that the run was made (current time)
- `time_started`: Server time that the processing of the run was started
- `time_completed`: Server time that the processing of the run was completed

## Response Examples

```
[
  {
    "id": "69eca481-8576-49e8-8e20-ea56f2005bcb",
    "experiment": "my-experiment-name",
    "status": "pending",
    "success": false,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  },
  {
    "id": "2521378e-263e-4e2e-85e9-a96254b36536",
    "experiment": "my-experiment-name",
    "status": "completed",
    "success": true,
    "time_created": "2020-03-28T20:00:26.613+00:00",
    "time_started": "2020-03-28T20:00:41.276+00:00",
    "time_completed": "2020-03-28T20:00:42.241+00:00"
  }
]
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    training = ubiops.Training()

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str

    # List runs
    api_response = training.experiment_runs_list(
        project_name=project_name,
        experiment_name=experiment_name
    )
    print(api_response)

    # Close the connection
    training.api_client.close()
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
    training = ubiops.Training(api_client)

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str

    # Create run
    api_response = training.experiment_runs_list(
        project_name=project_name,
        experiment_name=experiment_name
    )
    print(api_response)

    # Close the connection
    api_client.close()
    ```

### Parameters


| Name                | Type                                                | Notes |
|---------------------|-----------------------------------------------------|-------|
| **project_name**    | **str**                                             |       |
| **experiment_name** | **str**                                             |       |

### Return type

[**list[ExperimentRunList]**](./ExperimentRunList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **experiment_runs_update**
> ExperimentRunUpdateResponse experiment_runs_update(project_name, experiment_name, run_id, data)

Cancel an experiment run

## Description
Helper function to cancel an experiment run

### Required Parameters

- `status`: Status that the run will be updated to. It can only be `cancelled`.

## Request Examples

```
{
  "status": "cancelled"
}
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    training = ubiops.Training()

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str

    # Update a run
    api_response = training.experiment_runs_update(
        project_name=project_name,
        experiment_name=experiment_name,
        run_id="9eaee2b8-daf9-49fc-b958-be31f6ac48e3",
        data=ubiops.ExperimentRunUpdate(
            status="cancelled"
        )
    )
    print(api_response)

    # Close the connection
    training.api_client.close()
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
    training = ubiops.Training(api_client)

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str
    run_id = "9eaee2b8-daf9-49fc-b958-be31f6ac48e3" # str

    # Update a run
    api_response = training.experiment_runs_update(
        project_name=project_name,
        experiment_name=experiment_name,
        run_id=run_id,
        data=ubiops.ExperimentRunUpdate(
            status="cancelled"
        )
    )
    print(api_response)

    # Close the connection
    api_client.close()
    ```

### Parameters


| Name                | Type                                                | Notes |
|---------------------|-----------------------------------------------------|-------|
| **project_name**    | **str**                                             |       |
| **experiment_name** | **str**                                             |       |
| **run_id**          | **str**                                             |       |
| **data**            | [**ExperimentRunUpdate**](./ExperimentRunUpdate.md) |       |

### Return type

[**ExperimentRunUpdateResponse**](./ExperimentRunUpdateResponse.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **experiment_environment_variables_create**
> EnvironmentVariableList experiment_environment_variables_create(project_name, experiment_name, data)

Create experiment environment variable

## Description
Create an environment variable for the experiment. Variables inherited from the project can be shadowed by creating a variable with the same name.

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed from your training code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users.

## Request Examples

```
{
  "name": "experiment_variable",
  "value": "another one",
  "secret": false
}
```

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

```
{
  "id": "54e94fbe-507e-4fae-981d-227c28a2dab0",
  "name": "experiment_variable",
  "value": "another one",
  "secret": false
}
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    training = ubiops.Training()

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str
    data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate

    # Create experiment environment variable
    api_response = training.experiment_environment_variables_create(project_name, experiment_name, data)
    print(api_response)

    # Close the connection
    training.api_client.close()
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
    training = ubiops.Training(api_client)

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str
    data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate

    # Create experiment environment variable
    api_response = training.experiment_environment_variables_create(project_name, experiment_name, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters


| Name                | Type                                                                    | Notes |
|---------------------|-------------------------------------------------------------------------|-------|
| **project_name**    | **str**                                                                 |       |
| **experiment_name** | **str**                                                                 |       |
| **data**            | [**EnvironmentVariableCreate**](../models/EnvironmentVariableCreate.md) |       |

### Return type

[**EnvironmentVariableList**](../models/EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **experiment_environment_variables_delete**
> experiment_environment_variables_delete(project_name, experiment_name, id)

Delete experiment environment variable

## Description
Delete an environment variable of a experiment

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    training = ubiops.Training()

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str
    id = 'id_example' # str

    # Delete experiment environment variable
    training.experiment_environment_variables_delete(project_name, experiment_name, id)

    # Close the connection
    training.api_client.close()
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
    training = ubiops.Training(api_client)

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str
    id = 'id_example' # str

    # Delete experiment environment variable
    training.experiment_environment_variables_delete(project_name, experiment_name, id)

    # Close the connection
    api_client.close()
    ```


### Parameters

| Name                | Type    | Notes |
|---------------------|---------|-------|
| **project_name**    | **str** |       |
| **experiment_name** | **str** |       |
| **id**              | **str** |       |

### Return type

void (empty response body)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **experiment_environment_variables_get**
> EnvironmentVariableList experiment_environment_variables_get(project_name, experiment_name, id)

Get experiment environment variable

## Description
Retrieve details of a experiment environment variable. This cannot be used to retrieve details of inherited variables.

### Response Structure
The details of the environment variable:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

```
{
  "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
  "name": "database_schema",
  "value": "public",
  "secret": false
}
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    training = ubiops.Training()

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str
    id = 'id_example' # str

    # Get experiment environment variable
    api_response = training.experiment_environment_variables_get(project_name, experiment_name, id)
    print(api_response)

    # Close the connection
    training.api_client.close()
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
    training = ubiops.Training(api_client)

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str
    id = 'id_example' # str

    # Get experiment environment variable
    api_response = training.experiment_environment_variables_get(project_name, experiment_name, id)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters

| Name                | Type    | Notes |
|---------------------|---------|-------|
| **project_name**    | **str** |       |
| **experiment_name** | **str** |       |
| **id**              | **str** |       |

### Return type

[**EnvironmentVariableList**](../models/EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **experiment_environment_variables_list**
> list[InheritedEnvironmentVariableList] experiment_environment_variables_list(project_name, experiment_name)

List experiment environment variables

## Description
List the environment variables defined for the experiment. Includes environment variables defined at project level.

### Response Structure
A list of variables described by the following fields:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information
- `inheritance_type`: Type of parent object that this variable is inherited from - can be `project`, or null if the variable was defined for the experiment directly
- `inheritance_name`: Name of the parent object that this variable is inherited from - will be null if the variable was defined for the experiment directly

## Response Examples

```
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "experiment_variable",
    "value": "some_value",
    "secret": false,
    "inheritance_type": null,
    "inheritance_name": null
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": "project",
    "inheritance_name": "project_name"
  }
]
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    training = ubiops.Training()

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str

    # List experiment environment variables
    api_response = training.experiment_environment_variables_list(project_name, experiment_name)
    print(api_response)

    # Close the connection
    training.api_client.close()
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
    training = ubiops.Training(api_client)

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str

    # List experiment environment variables
    api_response = training.experiment_environment_variables_list(project_name, experiment_name)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters

| Name                 | Type    | Notes |
|----------------------|---------|-------|
| **project_name**     | **str** |       |
| **dexperiment_name** | **str** |       |

### Return type

[**list[InheritedEnvironmentVariableList]**](../models/InheritedEnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)

# **experiment_environment_variables_update**
> EnvironmentVariableList experiment_environment_variables_update(project_name, experiment_name, id, data)

Update experiment environment variable

## Description
Update an environment variable for the experiment. This cannot be used to update inherited variables; to change an inherited variable for a specific experiment you can create a variable with the same name for the experiment.

### Required Parameters

- `name`: The name of the variable. The variable will have this name when accessed from your training code. The variable name should contain only letters and underscores, and not start or end with an underscore.
- `value`: The value of the variable as a string. It may be an empty string ("").
- `secret`: If this variable contains sensitive information, set this to true to hide it from other users. Can be updated from false to true, but not from true to false (i.e. secrets will stay secrets).

## Request Examples

```
{
  "name": "experiment_variable",
  "value": "yet another one",
  "secret": false
}
```

### Response Structure
The details of the environment variable:

- `id`: Unique identifier for the environment variable
- `name`: Variable name
- `value`: Variable value (will be null for secret variables)
- `secret`: Boolean that indicates if this variable contains sensitive information

## Response Examples

```
{
  "id": "54e94fbe-507e-4fae-981d-227c28a2dab0",
  "name": "experiment_variable",
  "value": "yet another one",
  "secret": false
}
```

### Example

- Use system environment variables
    ```python
    import ubiops

    # Set environment variables
    # - UBIOPS_API_TOKEN: "Token <YOUR_API_TOKEN>"
    # - UBIOPS_API_HOST: optional - default to "https://api.ubiops.com/v2.1"
    training = ubiops.Training()

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str
    id = 'id_example' # str
    data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate

    # Update experiment environment variable
    api_response = training.experiment_environment_variables_update(project_name, experiment_name, id, data)
    print(api_response)

    # Close the connection
    training.api_client.close()
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
    training = ubiops.Training(api_client)

    project_name = 'project_name_example' # str
    experiment_name = 'experiment_name_example' # str
    id = 'id_example' # str
    data = ubiops.EnvironmentVariableCreate() # EnvironmentVariableCreate

    # Update experiment environment variable
    api_response = training.experiment_environment_variables_update(project_name, experiment_name, id, data)
    print(api_response)

    # Close the connection
    api_client.close()
    ```


### Parameters

| Name                | Type                                                                    | Notes |
|---------------------|-------------------------------------------------------------------------|-------|
| **project_name**    | **str**                                                                 |       |
| **experiment_name** | **str**                                                                 |       |
| **id**              | **str**                                                                 |       |
| **data**            | [**EnvironmentVariableCreate**](../models/EnvironmentVariableCreate.md) |       |

### Return type

[**EnvironmentVariableList**](../models/EnvironmentVariableList.md)

### Authorization

[API token](https://ubiops.com/docs/organizations/service-users)

[[Back to top]](#)




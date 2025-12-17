# ExperimentDetail

## Properties
| Name                             | Type               | Notes                 |
|----------------------------------|--------------------|-----------------------|
| **id**                           | **str**            | [optional] [readonly] |
| **name**                         | **str**            |                       |
| **description**                  | **str**            | [optional]            |
| **environment**                  | **str**            | [optional]            |
| **environment_display_name**     | **str**            | [optional]            |
| **status**                       | **str**            | [optional] [readonly] |
| **active_revision**              | **str**            | [optional] [readonly] |
| **latest_revision**              | **str**            | [optional] [readonly] |
| **instance_type**                | **str**            | [optional] [readonly] |
| **instance_type_group_id**       | **str**            | [optional] [readonly] |
| **instance_type_group_name**     | **str**            | [optional] [readonly] |
| **maximum_instances**            | **int**            | [optional]            |
| **minimum_instances**            | **int**            | [optional]            |
| **maximum_idle_time**            | **int**            | [optional]            |
| **labels**                       | **dict(str, str)** | [optional]            |
| **creation_date**                | **datetime**       | [optional]            |
| **last_updated**                 | **datetime**       | [optional]            |
| **request_retention_time**       | **int**            | [optional]            |
| **request_retention_mode**       | **str**            |                       |
| **maximum_queue_size**           | **int**            | [optional]            |
| **has_request_method**           | **bool**           | [optional] [readonly] |
| **has_requests_method**          | **bool**           | [optional] [readonly] |
| **static_ip**                    | **bool**           | [optional]            |
| **restart_request_interruption** | **bool**           | [optional]            |
| **default_bucket**               | **str**            | [optional]            |

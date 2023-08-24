# Validate

Helper functions for local file validation for the UbiOps infrastructure.

| Method                                                                     | Description                        |
|----------------------------------------------------------------------------|------------------------------------|
| [**validate_requirements_file**](./Validate.md#validate_requirements_file) | Validate a `requirements.txt` file |
| [**validate_yaml_file**](./Validate.md#validate_yaml_file)                 | Validate an `ubiops.yaml` file     |

# **validate_requirements_file**

> validate_requirements_file(requirements_path)

Validate a `requirements.txt` file

## Description

A function that goes through every line of a `requirements.txt` file and checks this line. The found
inconsistencies/errors will be logged (likely in the console) with the corresponding line numbers. True will be returned
if no errors were found, False otherwise.

The following will be checked:

- If the package name specified can be found on PyPi
- If a valid version can be found on PyPi for the package version
- If the line structure is correct
    - [Package name] [[specifiers] [version], ...]

Note that the following will not be checked:

- Options (e.g. -i or --extra-index-url)
- Dependencies
- Git/URL packages

DISCLAIMER:<br/>
Please note that this function aims to catch as many inconsistencies/errors as possible, but may not include all of
them. For a complete check, create an environment in UbiOps and upload the `requirements.txt`.

### Example

```python
from ubiops import utils

# Validate the given requirements.txt
requirements_file_name = "requirements.txt"
return_value = utils.validate_requirements_file(file_path=requirements_file_name)
print("Return value of requirements validation:", return_value)
```

### Parameters

| Name          | Type    | Notes                                                 |
|---------------|---------|-------------------------------------------------------|
| **file_path** | **str** | Absolute/relative path to the `requirements.txt` file |

### Return type

**bool**

[[Back to top]](#)

# **validate_yaml_file**

> validate_yaml_file(file_path)

Validate an ubiops.yaml file

## Description

A function that validates the structure of an `ubiops.yaml` file. The found inconsistencies/errors will be logged
(likely in the console) with the corresponding line numbers. A message will be printed to the console when the
validation is finished. True will be returned if no errors were found, False otherwise.

The structure is expected to be as follows:

```yaml
"environment_variables":
  - ...
"apt":
  "keys":
    "urls":
      - https://...
    "items":
      - ...
      - ...
  "sources":
    "urls":
      - https://...
    "items":
      - ...
  "packages":
    - ...
    - ...
```

### Example

```python
from ubiops import utils

# Validate the given ubiops.yaml
file_path = "ubiops.yaml"
return_value = utils.validate_yaml_file(file_path=file_path)
print("Return value of yaml validation", return_value)
```

### Parameters

| Name          | Type    | Notes                                            |
|---------------|---------|--------------------------------------------------|
| **file_path** | **str** | Absolute/relative path to the `ubiops.yaml` file |

### Return type

**bool**

[[Back to top]](#)

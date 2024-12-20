import logging
import re
import yaml

from schema import Schema, And, Optional, SchemaError

from .exceptions import ValidateError, ValidateSkip, ValidateWarning
from .validators import validate_requirement_line


logger = logging.getLogger("Validate")

regex_env_var = re.compile(r"^[A-Z_][A-Z0-9_]*=.*$")
regex_url = re.compile(r"^(http|https)\:\/\/.*$")

ubiops_config_schema = Schema(
    {
        Optional("environment_variables"): [
            And(
                str,
                regex_env_var.match,
                error="Environment variable definition must be in format 'VAR_NAME=Value'",
            )
        ],
        Optional("apt"): {
            Optional("keys"): {
                Optional("urls"): [
                    And(
                        str,
                        regex_url.match,
                        error="Key URL must be in format 'https://example.com/path'",
                    )
                ],
                Optional("items"): [And(str, lambda x: len(x) > 0, error="Item must be a non-empty string")],
            },
            Optional("sources"): {
                Optional("urls"): [
                    And(
                        str,
                        regex_url.match,
                        error="Source URL must be in format 'https://example.com/path'",
                    )
                ],
                Optional("items"): [And(str, lambda x: len(x) > 0, error="Item must be a non-empty string")],
            },
            "packages": [And(str, lambda x: len(x) > 0, error="Package must be a non-empty string")],
        },
    }
)


def validate_requirements_file(file_path):
    """
    Validates the requirements.txt file with data from PyPi. Logs error/warning/info messages. Returns True if the file
    is valid, False if not.

    :param str file_path: the path to the requirements.txt file
    """

    return_value = True
    with open(file_path, "r") as f:
        for index, line in enumerate(f):
            try:
                validate_requirement_line(index=index, line=line)
            except ValidateError as e:
                logger.error(f"Line {index + 1}, {e}")
                return_value = False
            except ValidateWarning as e:
                logger.warning(f"Line {index + 1}, {e}")
            except ValidateSkip as e:
                logger.info(f"Line {index + 1}, {e}")

    return return_value


def validate_yaml_file(file_path):
    """
    Validate ubiops.yaml. Check if correct keys are provided with the correct structure and data type.
    See https://ubiops.com/docs/deployments/deployment-package/ubiops-yaml for more information.
    The structure is expected to be the following:
    "environment_variables": list[strings]
    "apt": dict
        "keys": dict
            "urls": list[strings]
            "items": list[strings]
        "sources": dict
            "urls": list[strings]
            "items": list[strings]
        "packages": list[strings]

    Logs error/warning/info messages.
    Returns True if the line is valid, False if not.

    :param str file_path: path to ubiops.yaml file
    """

    with open(file_path, encoding="utf-8") as config_file:
        try:
            config = yaml.safe_load(config_file)
            ubiops_config_schema.validate({} if config is None else config)
        except yaml.MarkedYAMLError as e:
            if e.problem is not None and "\\t" in e.problem and e.problem_mark is not None:
                logger.error(f"Tab characters are invalid for indentation in line {e.problem_mark.line}")
            else:
                logger.error(f"Invalid yaml file, can't continue validation: {e}")
            return False
        except yaml.YAMLError as e:
            logger.error(f"Invalid yaml file, can't continue validation: {e}")
            return False
        except SchemaError as e:
            logger.error(f"Invalid ubiops.yaml file schema: {e.code}")
            return False

    return True

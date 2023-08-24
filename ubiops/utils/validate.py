import logging

import yaml

from .exceptions import ValidateError, ValidateSkip, ValidateWarning
from .validators import validate_requirement_line, validate_yaml_apt, validate_yaml_env_vars


logger = logging.getLogger("Validate")


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

    with open(file_path) as config_file:
        try:
            config = yaml.safe_load(config_file)
        except yaml.YAMLError:
            logger.error("Invalid yaml file, can't continue validation")
            return False

        if not isinstance(config, dict):
            logger.error("ubiops.yaml must contain a dictionary, can't continue validation")
            return False

        if not all(item in ["environment_variables", "apt"] for item in config):
            logger.error("ubiops.yaml file must contain environment_variables and/or apt, can't continue validation")
            return False

        return_value = True

        # Validate provided environment variables
        try:
            validate_yaml_env_vars(config)
        except ValidateError as e:
            logger.error(e)
            return_value = False

        # Validate provided apt packages
        try:
            validate_yaml_apt(config)
        except ValidateError as e:
            logger.error(e)
            return_value = False

    return return_value

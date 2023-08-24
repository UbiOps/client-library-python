from ..exceptions import ValidateError


def validate_yaml_env_vars(config):
    """
    Validate environment variables in ubiops.yaml. Check if correct keys are provided with the correct structure and
     data type.
    See https://ubiops.com/docs/deployments/deployment-package/ubiops-yaml for more information.
    The structure is expected to be the following:
    "environment_variables": list[strings]

    Raises exception to be handled by the caller if the validation fails.

    :param dict config: config dictionary
    """

    if "environment_variables" in config and config["environment_variables"]:
        if not isinstance(config["environment_variables"], list):
            raise ValidateError("environment_variables should be a list")

        for item in config["environment_variables"]:
            if not isinstance(item, str):
                raise ValidateError("Item in environment_variables should be a string")


def validate_yaml_apt(config):
    """
    Validate apt in ubiops.yaml. Check if correct keys are provided with the correct structure and data type.
    See https://ubiops.com/docs/deployments/deployment-package/ubiops-yaml for more information.
    The structure is expected to be the following:
    "apt": dict
        "keys": dict
            "urls": list[strings]
            "items": list[strings]
        "sources": dict
            "urls": list[strings]
            "items": list[strings]
        "packages": list[strings]

    Raises exception to be handled by the caller if the validation fails.

    :param dict config: config dictionary
    """

    if "apt" in config and config["apt"]:
        if not isinstance(config["apt"], dict):
            raise ValidateError("apt must be a dictionary")

        if not all(item in ["keys", "sources", "packages"] for item in config["apt"]):
            raise ValidateError("item in apt must contain keys, sources or packages")

        # Validate keys
        if "keys" in config["apt"] and config["apt"]["keys"]:
            if not all(item in ["urls", "items"] for item in config["apt"]["keys"]):
                raise ValidateError("keys must contain urls and items")

            if "urls" in config["apt"]["keys"] and config["apt"]["keys"]["urls"]:
                if not isinstance(config["apt"]["keys"]["urls"], list):
                    raise ValidateError("urls must be a list")

            if "items" in config["apt"]["keys"] and config["apt"]["keys"]["items"]:
                if not isinstance(config["apt"]["keys"]["items"], list):
                    raise ValidateError("items must be a list")

        # Validate sources
        if "sources" in config["apt"] and config["apt"]["sources"]:
            if not all(item in ["urls", "items"] for item in config["apt"]["sources"]):
                raise ValidateError("sources must contain urls or items")

            if "urls" in config["apt"]["sources"] and config["apt"]["sources"]["urls"]:
                if not isinstance(config["apt"]["sources"]["urls"], list):
                    raise ValidateError("urls must be a list")

            if "items" in config["apt"]["sources"] and config["apt"]["sources"]["items"]:
                if not isinstance(config["apt"]["sources"]["items"], list):
                    raise ValidateError("items must be a list")

        # Validate packages
        if "packages" in config["apt"] and config["apt"]["packages"]:
            if not isinstance(config["apt"]["packages"], list):
                raise ValidateError("packages must be a list")

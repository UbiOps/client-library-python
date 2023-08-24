# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.
"""

from ubiops.models.deployment_version_create import DeploymentVersionCreate


class ExperimentCreate(DeploymentVersionCreate):
    openapi_types = {
        "name": "str",
        "environment": "str",
        "instance_type": "str",
        "description": "str",
        "labels": "dict(str, str)",
        "request_retention_time": "int",
        "default_bucket": "str",
    }

    attribute_map = {
        "name": "name",
        "environment": "environment",
        "instance_type": "instance_type",
        "description": "description",
        "labels": "labels",
        "request_retention_time": "request_retention_time",
        "default_bucket": "default_bucket",
    }

    def __init__(
        self,
        name=None,
        environment="python3-7",
        instance_type=None,
        description=None,
        labels=None,
        request_retention_time=31536000,
        default_bucket=None,
        **kwargs,
    ):
        """
        ExperimentCreate
        """

        kwargs.pop("version", None)  # To make sure we don't pass the version twice

        super().__init__(
            version=name,  # Convert name to version
            environment=environment,
            instance_type=instance_type,
            description=description,
            labels=labels,
            request_retention_time=request_retention_time,
            **kwargs,
        )

        self._name = None
        self._default_bucket = None

        self.name = name
        if default_bucket is not None:
            self.default_bucket = default_bucket

    @property
    def name(self):
        """
        Gets the name of this ExperimentCreate

        :return: The name of this ExperimentCreate
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExperimentCreate

        :param name: The name of this ExperimentCreate
        :type: str
        """
        if self.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if self.client_side_validation and (name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")

        if self.client_side_validation and (name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def default_bucket(self):
        """
        Gets the default_bucket of this ExperimentCreate

        :return: The default_bucket of this ExperimentCreate
        :rtype: str
        """
        return self._default_bucket

    @default_bucket.setter
    def default_bucket(self, default_bucket):
        """
        Sets the default_bucket of this ExperimentCreate

        :param default_bucket: The default_bucket of this ExperimentCreate
        :type: str
        """
        if self.client_side_validation and (default_bucket is not None and not isinstance(default_bucket, str)):
            raise ValueError("Parameter `default_bucket` must be a string")

        if self.client_side_validation and (default_bucket is not None and len(default_bucket) < 1):
            raise ValueError("Invalid value for `default_bucket`, length must be greater than or equal to `1`")

        self._default_bucket = default_bucket

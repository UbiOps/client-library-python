# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.
"""


from ubiops.models.deployment_version_list import DeploymentVersionList


class ExperimentList(DeploymentVersionList):
    openapi_types = {
        "id": "str",
        "name": "str",
        "environment": "str",
        "environment_display_name": "str",
        "status": "str",
        "active_revision": "str",
        "latest_revision": "str",
        "instance_type": "str",
        "labels": "dict(str, str)",
        "creation_date": "datetime",
        "last_updated": "datetime",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "environment": "environment",
        "environment_display_name": "environment_display_name",
        "status": "status",
        "active_revision": "active_revision",
        "latest_revision": "latest_revision",
        "instance_type": "instance_type",
        "labels": "labels",
        "creation_date": "creation_date",
        "last_updated": "last_updated",
    }

    def __init__(
        self,
        id=None,
        name=None,
        environment=None,
        environment_display_name=None,
        status=None,
        active_revision=None,
        latest_revision=None,
        instance_type=None,
        labels=None,
        creation_date=None,
        last_updated=None,
        **kwargs,
    ):
        """
        ExperimentList
        """

        kwargs.pop("version", None)  # To make sure we don't pass the version twice

        super().__init__(
            id=id,
            version=name,  # Convert name to version
            environment=environment,
            environment_display_name=environment_display_name,
            status=status,
            active_revision=active_revision,
            latest_revision=latest_revision,
            instance_type=instance_type,
            labels=labels,
            creation_date=creation_date,
            last_updated=last_updated,
            **kwargs,
        )

        self._name = None

        self.name = name

    @property
    def name(self):
        """
        Gets the name of this ExperimentList

        :return: The name of this ExperimentList
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExperimentList

        :param name: The name of this ExperimentList
        :type: str
        """
        if self.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if self.client_side_validation and (name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")

        if self.client_side_validation and (name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

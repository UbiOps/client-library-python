# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.
"""

from ubiops.models.deployment_version_detail import DeploymentVersionDetail


class ExperimentDetail(DeploymentVersionDetail):
    openapi_types = {
        "id": "str",
        "name": "str",
        "description": "str",
        "environment": "str",
        "environment_display_name": "str",
        "status": "str",
        "active_revision": "str",
        "latest_revision": "str",
        "instance_type": "str",
        "maximum_instances": "int",
        "minimum_instances": "int",
        "maximum_idle_time": "int",
        "labels": "dict(str, str)",
        "creation_date": "datetime",
        "last_updated": "datetime",
        "monitoring": "str",
        "request_retention_time": "int",
        "request_retention_mode": "str",
        "default_notification_group": "str",
        "maximum_queue_size_express": "int",
        "maximum_queue_size_batch": "int",
        "has_request_method": "bool",
        "has_requests_method": "bool",
        "static_ip": "bool",
        "restart_request_interruption": "bool",
        "default_bucket": "str",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "description": "description",
        "environment": "environment",
        "environment_display_name": "environment_display_name",
        "status": "status",
        "active_revision": "active_revision",
        "latest_revision": "latest_revision",
        "instance_type": "instance_type",
        "maximum_instances": "maximum_instances",
        "minimum_instances": "minimum_instances",
        "maximum_idle_time": "maximum_idle_time",
        "labels": "labels",
        "creation_date": "creation_date",
        "last_updated": "last_updated",
        "monitoring": "monitoring",
        "request_retention_time": "request_retention_time",
        "request_retention_mode": "request_retention_mode",
        "default_notification_group": "default_notification_group",
        "maximum_queue_size_express": "maximum_queue_size_express",
        "maximum_queue_size_batch": "maximum_queue_size_batch",
        "has_request_method": "has_request_method",
        "has_requests_method": "has_requests_method",
        "static_ip": "static_ip",
        "restart_request_interruption": "restart_request_interruption",
        "default_bucket": "default_bucket",
    }

    def __init__(
        self,
        id=None,
        name=None,
        description=None,
        environment=None,
        environment_display_name=None,
        status=None,
        active_revision=None,
        latest_revision=None,
        instance_type=None,
        maximum_instances=None,
        minimum_instances=None,
        maximum_idle_time=None,
        labels=None,
        creation_date=None,
        last_updated=None,
        monitoring=None,
        request_retention_time=None,
        request_retention_mode=None,
        default_notification_group=None,
        maximum_queue_size_express=None,
        maximum_queue_size_batch=None,
        has_request_method=None,
        has_requests_method=None,
        static_ip=None,
        restart_request_interruption=None,
        default_bucket=None,
        **kwargs,
    ):
        """
        ExperimentDetail
        """

        kwargs.pop("version", None)  # To make sure we don't pass the version twice

        super().__init__(
            id=id,
            version=name,  # Convert name to version
            description=description,
            environment=environment,
            environment_display_name=environment_display_name,
            status=status,
            active_revision=active_revision,
            latest_revision=latest_revision,
            instance_type=instance_type,
            maximum_instances=maximum_instances,
            minimum_instances=minimum_instances,
            maximum_idle_time=maximum_idle_time,
            labels=labels,
            creation_date=creation_date,
            last_updated=last_updated,
            monitoring=monitoring,
            request_retention_time=request_retention_time,
            request_retention_mode=request_retention_mode,
            default_notification_group=default_notification_group,
            maximum_queue_size_express=maximum_queue_size_express,
            maximum_queue_size_batch=maximum_queue_size_batch,
            has_request_method=has_request_method,
            has_requests_method=has_requests_method,
            static_ip=static_ip,
            restart_request_interruption=restart_request_interruption,
            default_bucket=default_bucket,
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
        Gets the name of this ExperimentDetail

        :return: The name of this ExperimentDetail
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExperimentDetail

        :param name: The name of this ExperimentDetail
        :type: str
        """
        if self.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if self.client_side_validation and (name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")

        if self.client_side_validation and (name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")
        if self.client_side_validation and (name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def default_bucket(self):
        """
        Gets the default_bucket of this ExperimentDetail

        :return: The default_bucket of this ExperimentDetail
        :rtype: str
        """
        return self._default_bucket

    @default_bucket.setter
    def default_bucket(self, default_bucket):
        """
        Sets the default_bucket of this ExperimentDetail

        :param default_bucket: The default_bucket of this ExperimentDetail
        :type: str
        """
        if self.client_side_validation and default_bucket is None:
            raise ValueError("Invalid value for `default_bucket`, must not be `None`")
        if self.client_side_validation and (default_bucket is not None and not isinstance(default_bucket, str)):
            raise ValueError("Parameter `default_bucket` must be a string")

        if self.client_side_validation and (default_bucket is not None and len(default_bucket) < 1):
            raise ValueError("Invalid value for `default_bucket`, length must be greater than or equal to `1`")

        self._default_bucket = default_bucket

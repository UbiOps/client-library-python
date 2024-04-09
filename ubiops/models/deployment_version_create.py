# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class DeploymentVersionCreate(object):
    """
    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name and the value is attribute type
      attribute_map (dict): The key is attribute name and the value is json key in definition
    """

    openapi_types = {
        "version": "str",
        "environment": "str",
        "instance_type": "str",
        "maximum_instances": "int",
        "minimum_instances": "int",
        "maximum_idle_time": "int",
        "description": "str",
        "labels": "dict(str, str)",
        "monitoring": "str",
        "request_retention_time": "int",
        "request_retention_mode": "str",
        "default_notification_group": "str",
        "maximum_queue_size_express": "int",
        "maximum_queue_size_batch": "int",
        "static_ip": "bool",
        "restart_request_interruption": "bool",
        "ports": "list[DeploymentVersionPort]",
    }

    attribute_map = {
        "version": "version",
        "environment": "environment",
        "instance_type": "instance_type",
        "maximum_instances": "maximum_instances",
        "minimum_instances": "minimum_instances",
        "maximum_idle_time": "maximum_idle_time",
        "description": "description",
        "labels": "labels",
        "monitoring": "monitoring",
        "request_retention_time": "request_retention_time",
        "request_retention_mode": "request_retention_mode",
        "default_notification_group": "default_notification_group",
        "maximum_queue_size_express": "maximum_queue_size_express",
        "maximum_queue_size_batch": "maximum_queue_size_batch",
        "static_ip": "static_ip",
        "restart_request_interruption": "restart_request_interruption",
        "ports": "ports",
    }

    def __init__(
        self,
        version=None,
        environment="python3-10",
        instance_type=None,
        maximum_instances=None,
        minimum_instances=None,
        maximum_idle_time=None,
        description=None,
        labels=None,
        monitoring=None,
        request_retention_time=None,
        request_retention_mode="full",
        default_notification_group=None,
        maximum_queue_size_express=None,
        maximum_queue_size_batch=None,
        static_ip=False,
        restart_request_interruption=False,
        ports=None,
        **kwargs,
    ):
        """
        DeploymentVersionCreate - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._version = None
        self._environment = None
        self._instance_type = None
        self._maximum_instances = None
        self._minimum_instances = None
        self._maximum_idle_time = None
        self._description = None
        self._labels = None
        self._monitoring = None
        self._request_retention_time = None
        self._request_retention_mode = None
        self._default_notification_group = None
        self._maximum_queue_size_express = None
        self._maximum_queue_size_batch = None
        self._static_ip = None
        self._restart_request_interruption = None
        self._ports = None
        self.discriminator = None

        self.version = version
        if environment is not None:
            self.environment = environment
        if instance_type is not None:
            self.instance_type = instance_type
        if maximum_instances is not None:
            self.maximum_instances = maximum_instances
        if minimum_instances is not None:
            self.minimum_instances = minimum_instances
        if maximum_idle_time is not None:
            self.maximum_idle_time = maximum_idle_time
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        self.monitoring = monitoring
        if request_retention_time is not None:
            self.request_retention_time = request_retention_time
        if request_retention_mode is not None:
            self.request_retention_mode = request_retention_mode
        self.default_notification_group = default_notification_group
        if maximum_queue_size_express is not None:
            self.maximum_queue_size_express = maximum_queue_size_express
        if maximum_queue_size_batch is not None:
            self.maximum_queue_size_batch = maximum_queue_size_batch
        if static_ip is not None:
            self.static_ip = static_ip
        if restart_request_interruption is not None:
            self.restart_request_interruption = restart_request_interruption
        if ports is not None:
            self.ports = ports

    @property
    def version(self):
        """
        Gets the version of this DeploymentVersionCreate

        :return: the version of this DeploymentVersionCreate
        :rtype: str
        """

        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DeploymentVersionCreate

        :param version: the version of this DeploymentVersionCreate
        :type: str
        """

        if self.client_side_validation and version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")
        if self.client_side_validation and (version is not None and not isinstance(version, str)):
            raise ValueError("Parameter `version` must be a string")

        if self.client_side_validation and (version is not None and len(version) < 1):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")

        self._version = version

    @property
    def environment(self):
        """
        Gets the environment of this DeploymentVersionCreate

        :return: the environment of this DeploymentVersionCreate
        :rtype: str
        """

        return self._environment

    @environment.setter
    def environment(self, environment):
        """
        Sets the environment of this DeploymentVersionCreate

        :param environment: the environment of this DeploymentVersionCreate
        :type: str
        """

        if self.client_side_validation and (environment is not None and not isinstance(environment, str)):
            raise ValueError("Parameter `environment` must be a string")

        if self.client_side_validation and (environment is not None and len(environment) < 1):
            raise ValueError("Invalid value for `environment`, length must be greater than or equal to `1`")

        self._environment = environment

    @property
    def instance_type(self):
        """
        Gets the instance_type of this DeploymentVersionCreate

        :return: the instance_type of this DeploymentVersionCreate
        :rtype: str
        """

        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """
        Sets the instance_type of this DeploymentVersionCreate

        :param instance_type: the instance_type of this DeploymentVersionCreate
        :type: str
        """

        if self.client_side_validation and (instance_type is not None and not isinstance(instance_type, str)):
            raise ValueError("Parameter `instance_type` must be a string")

        if self.client_side_validation and (instance_type is not None and len(instance_type) < 1):
            raise ValueError("Invalid value for `instance_type`, length must be greater than or equal to `1`")

        self._instance_type = instance_type

    @property
    def maximum_instances(self):
        """
        Gets the maximum_instances of this DeploymentVersionCreate

        :return: the maximum_instances of this DeploymentVersionCreate
        :rtype: int
        """

        return self._maximum_instances

    @maximum_instances.setter
    def maximum_instances(self, maximum_instances):
        """
        Sets the maximum_instances of this DeploymentVersionCreate

        :param maximum_instances: the maximum_instances of this DeploymentVersionCreate
        :type: int
        """

        if self.client_side_validation and (maximum_instances is not None and not isinstance(maximum_instances, int)):
            raise ValueError("Parameter `maximum_instances` must be an integer")

        self._maximum_instances = maximum_instances

    @property
    def minimum_instances(self):
        """
        Gets the minimum_instances of this DeploymentVersionCreate

        :return: the minimum_instances of this DeploymentVersionCreate
        :rtype: int
        """

        return self._minimum_instances

    @minimum_instances.setter
    def minimum_instances(self, minimum_instances):
        """
        Sets the minimum_instances of this DeploymentVersionCreate

        :param minimum_instances: the minimum_instances of this DeploymentVersionCreate
        :type: int
        """

        if self.client_side_validation and (minimum_instances is not None and not isinstance(minimum_instances, int)):
            raise ValueError("Parameter `minimum_instances` must be an integer")

        self._minimum_instances = minimum_instances

    @property
    def maximum_idle_time(self):
        """
        Gets the maximum_idle_time of this DeploymentVersionCreate

        :return: the maximum_idle_time of this DeploymentVersionCreate
        :rtype: int
        """

        return self._maximum_idle_time

    @maximum_idle_time.setter
    def maximum_idle_time(self, maximum_idle_time):
        """
        Sets the maximum_idle_time of this DeploymentVersionCreate

        :param maximum_idle_time: the maximum_idle_time of this DeploymentVersionCreate
        :type: int
        """

        if self.client_side_validation and (maximum_idle_time is not None and not isinstance(maximum_idle_time, int)):
            raise ValueError("Parameter `maximum_idle_time` must be an integer")

        self._maximum_idle_time = maximum_idle_time

    @property
    def description(self):
        """
        Gets the description of this DeploymentVersionCreate

        :return: the description of this DeploymentVersionCreate
        :rtype: str
        """

        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeploymentVersionCreate

        :param description: the description of this DeploymentVersionCreate
        :type: str
        """

        if self.client_side_validation and (description is not None and not isinstance(description, str)):
            raise ValueError("Parameter `description` must be a string")

        self._description = description

    @property
    def labels(self):
        """
        Gets the labels of this DeploymentVersionCreate

        :return: the labels of this DeploymentVersionCreate
        :rtype: dict(str, str)
        """

        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this DeploymentVersionCreate

        :param labels: the labels of this DeploymentVersionCreate
        :type: dict(str, str)
        """

        if self.client_side_validation and (labels is not None and not isinstance(labels, dict)):
            raise ValueError("Parameter `labels` must be a dictionary")

        self._labels = labels

    @property
    def monitoring(self):
        """
        Gets the monitoring of this DeploymentVersionCreate

        :return: the monitoring of this DeploymentVersionCreate
        :rtype: str
        """

        return self._monitoring

    @monitoring.setter
    def monitoring(self, monitoring):
        """
        Sets the monitoring of this DeploymentVersionCreate

        :param monitoring: the monitoring of this DeploymentVersionCreate
        :type: str
        """

        if self.client_side_validation and (monitoring is not None and not isinstance(monitoring, str)):
            raise ValueError("Parameter `monitoring` must be a string")

        if self.client_side_validation and (monitoring is not None and len(monitoring) < 1):
            raise ValueError("Invalid value for `monitoring`, length must be greater than or equal to `1`")

        self._monitoring = monitoring

    @property
    def request_retention_time(self):
        """
        Gets the request_retention_time of this DeploymentVersionCreate

        :return: the request_retention_time of this DeploymentVersionCreate
        :rtype: int
        """

        return self._request_retention_time

    @request_retention_time.setter
    def request_retention_time(self, request_retention_time):
        """
        Sets the request_retention_time of this DeploymentVersionCreate

        :param request_retention_time: the request_retention_time of this DeploymentVersionCreate
        :type: int
        """

        if self.client_side_validation and (
            request_retention_time is not None and not isinstance(request_retention_time, int)
        ):
            raise ValueError("Parameter `request_retention_time` must be an integer")

        self._request_retention_time = request_retention_time

    @property
    def request_retention_mode(self):
        """
        Gets the request_retention_mode of this DeploymentVersionCreate

        :return: the request_retention_mode of this DeploymentVersionCreate
        :rtype: str
        """

        return self._request_retention_mode

    @request_retention_mode.setter
    def request_retention_mode(self, request_retention_mode):
        """
        Sets the request_retention_mode of this DeploymentVersionCreate

        :param request_retention_mode: the request_retention_mode of this DeploymentVersionCreate
        :type: str
        """

        if self.client_side_validation and (
            request_retention_mode is not None and not isinstance(request_retention_mode, str)
        ):
            raise ValueError("Parameter `request_retention_mode` must be a string")

        self._request_retention_mode = request_retention_mode

    @property
    def default_notification_group(self):
        """
        Gets the default_notification_group of this DeploymentVersionCreate

        :return: the default_notification_group of this DeploymentVersionCreate
        :rtype: str
        """

        return self._default_notification_group

    @default_notification_group.setter
    def default_notification_group(self, default_notification_group):
        """
        Sets the default_notification_group of this DeploymentVersionCreate

        :param default_notification_group: the default_notification_group of this DeploymentVersionCreate
        :type: str
        """

        if self.client_side_validation and (
            default_notification_group is not None and not isinstance(default_notification_group, str)
        ):
            raise ValueError("Parameter `default_notification_group` must be a string")

        if self.client_side_validation and (
            default_notification_group is not None and len(default_notification_group) < 1
        ):
            raise ValueError(
                "Invalid value for `default_notification_group`, length must be greater than or equal to `1`"
            )

        self._default_notification_group = default_notification_group

    @property
    def maximum_queue_size_express(self):
        """
        Gets the maximum_queue_size_express of this DeploymentVersionCreate

        :return: the maximum_queue_size_express of this DeploymentVersionCreate
        :rtype: int
        """

        return self._maximum_queue_size_express

    @maximum_queue_size_express.setter
    def maximum_queue_size_express(self, maximum_queue_size_express):
        """
        Sets the maximum_queue_size_express of this DeploymentVersionCreate

        :param maximum_queue_size_express: the maximum_queue_size_express of this DeploymentVersionCreate
        :type: int
        """

        if self.client_side_validation and (
            maximum_queue_size_express is not None and not isinstance(maximum_queue_size_express, int)
        ):
            raise ValueError("Parameter `maximum_queue_size_express` must be an integer")

        self._maximum_queue_size_express = maximum_queue_size_express

    @property
    def maximum_queue_size_batch(self):
        """
        Gets the maximum_queue_size_batch of this DeploymentVersionCreate

        :return: the maximum_queue_size_batch of this DeploymentVersionCreate
        :rtype: int
        """

        return self._maximum_queue_size_batch

    @maximum_queue_size_batch.setter
    def maximum_queue_size_batch(self, maximum_queue_size_batch):
        """
        Sets the maximum_queue_size_batch of this DeploymentVersionCreate

        :param maximum_queue_size_batch: the maximum_queue_size_batch of this DeploymentVersionCreate
        :type: int
        """

        if self.client_side_validation and (
            maximum_queue_size_batch is not None and not isinstance(maximum_queue_size_batch, int)
        ):
            raise ValueError("Parameter `maximum_queue_size_batch` must be an integer")

        self._maximum_queue_size_batch = maximum_queue_size_batch

    @property
    def static_ip(self):
        """
        Gets the static_ip of this DeploymentVersionCreate

        :return: the static_ip of this DeploymentVersionCreate
        :rtype: bool
        """

        return self._static_ip

    @static_ip.setter
    def static_ip(self, static_ip):
        """
        Sets the static_ip of this DeploymentVersionCreate

        :param static_ip: the static_ip of this DeploymentVersionCreate
        :type: bool
        """

        if self.client_side_validation and (static_ip is not None and not isinstance(static_ip, bool)):
            raise ValueError("Parameter `static_ip` must be a boolean")

        self._static_ip = static_ip

    @property
    def restart_request_interruption(self):
        """
        Gets the restart_request_interruption of this DeploymentVersionCreate

        :return: the restart_request_interruption of this DeploymentVersionCreate
        :rtype: bool
        """

        return self._restart_request_interruption

    @restart_request_interruption.setter
    def restart_request_interruption(self, restart_request_interruption):
        """
        Sets the restart_request_interruption of this DeploymentVersionCreate

        :param restart_request_interruption: the restart_request_interruption of this DeploymentVersionCreate
        :type: bool
        """

        if self.client_side_validation and (
            restart_request_interruption is not None and not isinstance(restart_request_interruption, bool)
        ):
            raise ValueError("Parameter `restart_request_interruption` must be a boolean")

        self._restart_request_interruption = restart_request_interruption

    @property
    def ports(self):
        """
        Gets the ports of this DeploymentVersionCreate

        :return: the ports of this DeploymentVersionCreate
        :rtype: list[DeploymentVersionPort]
        """

        return self._ports

    @ports.setter
    def ports(self, ports):
        """
        Sets the ports of this DeploymentVersionCreate

        :param ports: the ports of this DeploymentVersionCreate
        :type: list[DeploymentVersionPort]
        """

        if self.client_side_validation and (ports is not None and not isinstance(ports, list)):
            raise ValueError("Parameter `ports` must be a list")
        if self.client_side_validation and ports is not None:
            from ubiops.models.deployment_version_port import DeploymentVersionPort

            ports = [DeploymentVersionPort(**item) if isinstance(item, dict) else item for item in ports]

        self._ports = ports

    def to_dict(self):
        """
        Returns the model properties as a dict
        """

        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """

        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """

        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """

        if not isinstance(other, DeploymentVersionCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, DeploymentVersionCreate):
            return True

        return self.to_dict() != other.to_dict()

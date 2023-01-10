# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.  # noqa: E501

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ubiops.configuration import Configuration


class DeploymentVersionList(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'deployment': 'str',
        'version': 'str',
        'description': 'str',
        'language': 'str',
        'language_description': 'str',
        'status': 'str',
        'active_revision': 'str',
        'latest_build': 'str',
        'memory_allocation': 'int',
        'instance_type': 'str',
        'maximum_instances': 'int',
        'minimum_instances': 'int',
        'maximum_idle_time': 'int',
        'labels': 'dict(str, str)',
        'creation_date': 'datetime',
        'last_updated': 'datetime',
        'request_retention_time': 'int',
        'request_retention_mode': 'str',
        'monitoring': 'str',
        'default_notification_group': 'str',
        'maximum_queue_size_express': 'int',
        'maximum_queue_size_batch': 'int',
        'static_ip': 'bool',
        'restart_request_interruption': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'deployment': 'deployment',
        'version': 'version',
        'description': 'description',
        'language': 'language',
        'language_description': 'language_description',
        'status': 'status',
        'active_revision': 'active_revision',
        'latest_build': 'latest_build',
        'memory_allocation': 'memory_allocation',
        'instance_type': 'instance_type',
        'maximum_instances': 'maximum_instances',
        'minimum_instances': 'minimum_instances',
        'maximum_idle_time': 'maximum_idle_time',
        'labels': 'labels',
        'creation_date': 'creation_date',
        'last_updated': 'last_updated',
        'request_retention_time': 'request_retention_time',
        'request_retention_mode': 'request_retention_mode',
        'monitoring': 'monitoring',
        'default_notification_group': 'default_notification_group',
        'maximum_queue_size_express': 'maximum_queue_size_express',
        'maximum_queue_size_batch': 'maximum_queue_size_batch',
        'static_ip': 'static_ip',
        'restart_request_interruption': 'restart_request_interruption'
    }

    def __init__(self, id=None, deployment=None, version=None, description=None, language=None, language_description=None, status=None, active_revision=None, latest_build=None, memory_allocation=None, instance_type=None, maximum_instances=None, minimum_instances=None, maximum_idle_time=None, labels=None, creation_date=None, last_updated=None, request_retention_time=None, request_retention_mode=None, monitoring=None, default_notification_group=None, maximum_queue_size_express=None, maximum_queue_size_batch=None, static_ip=None, restart_request_interruption=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """DeploymentVersionList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._deployment = None
        self._version = None
        self._description = None
        self._language = None
        self._language_description = None
        self._status = None
        self._active_revision = None
        self._latest_build = None
        self._memory_allocation = None
        self._instance_type = None
        self._maximum_instances = None
        self._minimum_instances = None
        self._maximum_idle_time = None
        self._labels = None
        self._creation_date = None
        self._last_updated = None
        self._request_retention_time = None
        self._request_retention_mode = None
        self._monitoring = None
        self._default_notification_group = None
        self._maximum_queue_size_express = None
        self._maximum_queue_size_batch = None
        self._static_ip = None
        self._restart_request_interruption = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.deployment = deployment
        self.version = version
        if description is not None:
            self.description = description
        if language is not None:
            self.language = language
        if language_description is not None:
            self.language_description = language_description
        if status is not None:
            self.status = status
        if active_revision is not None:
            self.active_revision = active_revision
        if latest_build is not None:
            self.latest_build = latest_build
        if memory_allocation is not None:
            self.memory_allocation = memory_allocation
        self.instance_type = instance_type
        if maximum_instances is not None:
            self.maximum_instances = maximum_instances
        if minimum_instances is not None:
            self.minimum_instances = minimum_instances
        if maximum_idle_time is not None:
            self.maximum_idle_time = maximum_idle_time
        self.labels = labels
        if creation_date is not None:
            self.creation_date = creation_date
        if last_updated is not None:
            self.last_updated = last_updated
        if request_retention_time is not None:
            self.request_retention_time = request_retention_time
        self.request_retention_mode = request_retention_mode
        if monitoring is not None:
            self.monitoring = monitoring
        if default_notification_group is not None:
            self.default_notification_group = default_notification_group
        if maximum_queue_size_express is not None:
            self.maximum_queue_size_express = maximum_queue_size_express
        if maximum_queue_size_batch is not None:
            self.maximum_queue_size_batch = maximum_queue_size_batch
        if static_ip is not None:
            self.static_ip = static_ip
        if restart_request_interruption is not None:
            self.restart_request_interruption = restart_request_interruption

    @property
    def id(self):
        """Gets the id of this DeploymentVersionList.  # noqa: E501


        :return: The id of this DeploymentVersionList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeploymentVersionList.


        :param id: The id of this DeploymentVersionList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")  # noqa: E501

        self._id = id

    @property
    def deployment(self):
        """Gets the deployment of this DeploymentVersionList.  # noqa: E501


        :return: The deployment of this DeploymentVersionList.  # noqa: E501
        :rtype: str
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """Sets the deployment of this DeploymentVersionList.


        :param deployment: The deployment of this DeploymentVersionList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and deployment is None:  # noqa: E501
            raise ValueError("Invalid value for `deployment`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                deployment is not None and not isinstance(deployment, str)):
            raise ValueError("Parameter `deployment` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                deployment is not None and len(deployment) < 1):
            raise ValueError("Invalid value for `deployment`, length must be greater than or equal to `1`")  # noqa: E501

        self._deployment = deployment

    @property
    def version(self):
        """Gets the version of this DeploymentVersionList.  # noqa: E501


        :return: The version of this DeploymentVersionList.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DeploymentVersionList.


        :param version: The version of this DeploymentVersionList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and not isinstance(version, str)):
            raise ValueError("Parameter `version` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) > 64):
            raise ValueError("Invalid value for `version`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) < 1):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501

        self._version = version

    @property
    def description(self):
        """Gets the description of this DeploymentVersionList.  # noqa: E501


        :return: The description of this DeploymentVersionList.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeploymentVersionList.


        :param description: The description of this DeploymentVersionList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not isinstance(description, str)):
            raise ValueError("Parameter `description` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 400):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `400`")  # noqa: E501

        self._description = description

    @property
    def language(self):
        """Gets the language of this DeploymentVersionList.  # noqa: E501


        :return: The language of this DeploymentVersionList.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this DeploymentVersionList.


        :param language: The language of this DeploymentVersionList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                language is not None and not isinstance(language, str)):
            raise ValueError("Parameter `language` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                language is not None and len(language) > 30):
            raise ValueError("Invalid value for `language`, length must be less than or equal to `30`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                language is not None and len(language) < 1):
            raise ValueError("Invalid value for `language`, length must be greater than or equal to `1`")  # noqa: E501

        self._language = language

    @property
    def language_description(self):
        """Gets the language_description of this DeploymentVersionList.  # noqa: E501


        :return: The language_description of this DeploymentVersionList.  # noqa: E501
        :rtype: str
        """
        return self._language_description

    @language_description.setter
    def language_description(self, language_description):
        """Sets the language_description of this DeploymentVersionList.


        :param language_description: The language_description of this DeploymentVersionList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                language_description is not None and not isinstance(language_description, str)):
            raise ValueError("Parameter `language_description` must be a string")  # noqa: E501

        self._language_description = language_description

    @property
    def status(self):
        """Gets the status of this DeploymentVersionList.  # noqa: E501


        :return: The status of this DeploymentVersionList.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeploymentVersionList.


        :param status: The status of this DeploymentVersionList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                status is not None and not isinstance(status, str)):
            raise ValueError("Parameter `status` must be a string")  # noqa: E501

        self._status = status

    @property
    def active_revision(self):
        """Gets the active_revision of this DeploymentVersionList.  # noqa: E501


        :return: The active_revision of this DeploymentVersionList.  # noqa: E501
        :rtype: str
        """
        return self._active_revision

    @active_revision.setter
    def active_revision(self, active_revision):
        """Sets the active_revision of this DeploymentVersionList.


        :param active_revision: The active_revision of this DeploymentVersionList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                active_revision is not None and not isinstance(active_revision, str)):
            raise ValueError("Parameter `active_revision` must be a string")  # noqa: E501

        self._active_revision = active_revision

    @property
    def latest_build(self):
        """Gets the latest_build of this DeploymentVersionList.  # noqa: E501


        :return: The latest_build of this DeploymentVersionList.  # noqa: E501
        :rtype: str
        """
        return self._latest_build

    @latest_build.setter
    def latest_build(self, latest_build):
        """Sets the latest_build of this DeploymentVersionList.


        :param latest_build: The latest_build of this DeploymentVersionList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                latest_build is not None and not isinstance(latest_build, str)):
            raise ValueError("Parameter `latest_build` must be a string")  # noqa: E501

        self._latest_build = latest_build

    @property
    def memory_allocation(self):
        """Gets the memory_allocation of this DeploymentVersionList.  # noqa: E501


        :return: The memory_allocation of this DeploymentVersionList.  # noqa: E501
        :rtype: int
        """
        return self._memory_allocation

    @memory_allocation.setter
    def memory_allocation(self, memory_allocation):
        """Sets the memory_allocation of this DeploymentVersionList.


        :param memory_allocation: The memory_allocation of this DeploymentVersionList.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                memory_allocation is not None and not isinstance(memory_allocation, int)):
            raise ValueError("Parameter `memory_allocation` must be an integer")  # noqa: E501

        self._memory_allocation = memory_allocation

    @property
    def instance_type(self):
        """Gets the instance_type of this DeploymentVersionList.  # noqa: E501


        :return: The instance_type of this DeploymentVersionList.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this DeploymentVersionList.


        :param instance_type: The instance_type of this DeploymentVersionList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and instance_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instance_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instance_type is not None and not isinstance(instance_type, str)):
            raise ValueError("Parameter `instance_type` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                instance_type is not None and len(instance_type) < 1):
            raise ValueError("Invalid value for `instance_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._instance_type = instance_type

    @property
    def maximum_instances(self):
        """Gets the maximum_instances of this DeploymentVersionList.  # noqa: E501


        :return: The maximum_instances of this DeploymentVersionList.  # noqa: E501
        :rtype: int
        """
        return self._maximum_instances

    @maximum_instances.setter
    def maximum_instances(self, maximum_instances):
        """Sets the maximum_instances of this DeploymentVersionList.


        :param maximum_instances: The maximum_instances of this DeploymentVersionList.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_instances is not None and not isinstance(maximum_instances, int)):
            raise ValueError("Parameter `maximum_instances` must be an integer")  # noqa: E501

        self._maximum_instances = maximum_instances

    @property
    def minimum_instances(self):
        """Gets the minimum_instances of this DeploymentVersionList.  # noqa: E501


        :return: The minimum_instances of this DeploymentVersionList.  # noqa: E501
        :rtype: int
        """
        return self._minimum_instances

    @minimum_instances.setter
    def minimum_instances(self, minimum_instances):
        """Sets the minimum_instances of this DeploymentVersionList.


        :param minimum_instances: The minimum_instances of this DeploymentVersionList.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                minimum_instances is not None and not isinstance(minimum_instances, int)):
            raise ValueError("Parameter `minimum_instances` must be an integer")  # noqa: E501

        self._minimum_instances = minimum_instances

    @property
    def maximum_idle_time(self):
        """Gets the maximum_idle_time of this DeploymentVersionList.  # noqa: E501


        :return: The maximum_idle_time of this DeploymentVersionList.  # noqa: E501
        :rtype: int
        """
        return self._maximum_idle_time

    @maximum_idle_time.setter
    def maximum_idle_time(self, maximum_idle_time):
        """Sets the maximum_idle_time of this DeploymentVersionList.


        :param maximum_idle_time: The maximum_idle_time of this DeploymentVersionList.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_idle_time is not None and not isinstance(maximum_idle_time, int)):
            raise ValueError("Parameter `maximum_idle_time` must be an integer")  # noqa: E501

        self._maximum_idle_time = maximum_idle_time

    @property
    def labels(self):
        """Gets the labels of this DeploymentVersionList.  # noqa: E501


        :return: The labels of this DeploymentVersionList.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this DeploymentVersionList.


        :param labels: The labels of this DeploymentVersionList.  # noqa: E501
        :type: dict(str, str)
        """
        if (self.local_vars_configuration.client_side_validation and
                labels is not None and not isinstance(labels, dict)):
            raise ValueError("Parameter `labels` must be a dictionary")  # noqa: E501

        self._labels = labels

    @property
    def creation_date(self):
        """Gets the creation_date of this DeploymentVersionList.  # noqa: E501


        :return: The creation_date of this DeploymentVersionList.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this DeploymentVersionList.


        :param creation_date: The creation_date of this DeploymentVersionList.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def last_updated(self):
        """Gets the last_updated of this DeploymentVersionList.  # noqa: E501


        :return: The last_updated of this DeploymentVersionList.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this DeploymentVersionList.


        :param last_updated: The last_updated of this DeploymentVersionList.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def request_retention_time(self):
        """Gets the request_retention_time of this DeploymentVersionList.  # noqa: E501


        :return: The request_retention_time of this DeploymentVersionList.  # noqa: E501
        :rtype: int
        """
        return self._request_retention_time

    @request_retention_time.setter
    def request_retention_time(self, request_retention_time):
        """Sets the request_retention_time of this DeploymentVersionList.


        :param request_retention_time: The request_retention_time of this DeploymentVersionList.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                request_retention_time is not None and not isinstance(request_retention_time, int)):
            raise ValueError("Parameter `request_retention_time` must be an integer")  # noqa: E501

        self._request_retention_time = request_retention_time

    @property
    def request_retention_mode(self):
        """Gets the request_retention_mode of this DeploymentVersionList.  # noqa: E501


        :return: The request_retention_mode of this DeploymentVersionList.  # noqa: E501
        :rtype: str
        """
        return self._request_retention_mode

    @request_retention_mode.setter
    def request_retention_mode(self, request_retention_mode):
        """Sets the request_retention_mode of this DeploymentVersionList.


        :param request_retention_mode: The request_retention_mode of this DeploymentVersionList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and request_retention_mode is None:  # noqa: E501
            raise ValueError("Invalid value for `request_retention_mode`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                request_retention_mode is not None and not isinstance(request_retention_mode, str)):
            raise ValueError("Parameter `request_retention_mode` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                request_retention_mode is not None and len(request_retention_mode) < 1):
            raise ValueError("Invalid value for `request_retention_mode`, length must be greater than or equal to `1`")  # noqa: E501

        self._request_retention_mode = request_retention_mode

    @property
    def monitoring(self):
        """Gets the monitoring of this DeploymentVersionList.  # noqa: E501


        :return: The monitoring of this DeploymentVersionList.  # noqa: E501
        :rtype: str
        """
        return self._monitoring

    @monitoring.setter
    def monitoring(self, monitoring):
        """Sets the monitoring of this DeploymentVersionList.


        :param monitoring: The monitoring of this DeploymentVersionList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                monitoring is not None and not isinstance(monitoring, str)):
            raise ValueError("Parameter `monitoring` must be a string")  # noqa: E501

        self._monitoring = monitoring

    @property
    def default_notification_group(self):
        """Gets the default_notification_group of this DeploymentVersionList.  # noqa: E501


        :return: The default_notification_group of this DeploymentVersionList.  # noqa: E501
        :rtype: str
        """
        return self._default_notification_group

    @default_notification_group.setter
    def default_notification_group(self, default_notification_group):
        """Sets the default_notification_group of this DeploymentVersionList.


        :param default_notification_group: The default_notification_group of this DeploymentVersionList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                default_notification_group is not None and not isinstance(default_notification_group, str)):
            raise ValueError("Parameter `default_notification_group` must be a string")  # noqa: E501

        self._default_notification_group = default_notification_group

    @property
    def maximum_queue_size_express(self):
        """Gets the maximum_queue_size_express of this DeploymentVersionList.  # noqa: E501


        :return: The maximum_queue_size_express of this DeploymentVersionList.  # noqa: E501
        :rtype: int
        """
        return self._maximum_queue_size_express

    @maximum_queue_size_express.setter
    def maximum_queue_size_express(self, maximum_queue_size_express):
        """Sets the maximum_queue_size_express of this DeploymentVersionList.


        :param maximum_queue_size_express: The maximum_queue_size_express of this DeploymentVersionList.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_queue_size_express is not None and not isinstance(maximum_queue_size_express, int)):
            raise ValueError("Parameter `maximum_queue_size_express` must be an integer")  # noqa: E501

        self._maximum_queue_size_express = maximum_queue_size_express

    @property
    def maximum_queue_size_batch(self):
        """Gets the maximum_queue_size_batch of this DeploymentVersionList.  # noqa: E501


        :return: The maximum_queue_size_batch of this DeploymentVersionList.  # noqa: E501
        :rtype: int
        """
        return self._maximum_queue_size_batch

    @maximum_queue_size_batch.setter
    def maximum_queue_size_batch(self, maximum_queue_size_batch):
        """Sets the maximum_queue_size_batch of this DeploymentVersionList.


        :param maximum_queue_size_batch: The maximum_queue_size_batch of this DeploymentVersionList.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_queue_size_batch is not None and not isinstance(maximum_queue_size_batch, int)):
            raise ValueError("Parameter `maximum_queue_size_batch` must be an integer")  # noqa: E501

        self._maximum_queue_size_batch = maximum_queue_size_batch

    @property
    def static_ip(self):
        """Gets the static_ip of this DeploymentVersionList.  # noqa: E501


        :return: The static_ip of this DeploymentVersionList.  # noqa: E501
        :rtype: bool
        """
        return self._static_ip

    @static_ip.setter
    def static_ip(self, static_ip):
        """Sets the static_ip of this DeploymentVersionList.


        :param static_ip: The static_ip of this DeploymentVersionList.  # noqa: E501
        :type: bool
        """
        if (self.local_vars_configuration.client_side_validation and
                static_ip is not None and not isinstance(static_ip, bool)):
            raise ValueError("Parameter `static_ip` must be a boolean")  # noqa: E501

        self._static_ip = static_ip

    @property
    def restart_request_interruption(self):
        """Gets the restart_request_interruption of this DeploymentVersionList.  # noqa: E501


        :return: The restart_request_interruption of this DeploymentVersionList.  # noqa: E501
        :rtype: bool
        """
        return self._restart_request_interruption

    @restart_request_interruption.setter
    def restart_request_interruption(self, restart_request_interruption):
        """Sets the restart_request_interruption of this DeploymentVersionList.


        :param restart_request_interruption: The restart_request_interruption of this DeploymentVersionList.  # noqa: E501
        :type: bool
        """
        if (self.local_vars_configuration.client_side_validation and
                restart_request_interruption is not None and not isinstance(restart_request_interruption, bool)):
            raise ValueError("Parameter `restart_request_interruption` must be a boolean")  # noqa: E501

        self._restart_request_interruption = restart_request_interruption

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeploymentVersionList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeploymentVersionList):
            return True

        return self.to_dict() != other.to_dict()

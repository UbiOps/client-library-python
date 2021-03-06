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


class DeploymentVersionDetail(object):
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
        'status': 'str',
        'active_revision': 'str',
        'latest_build': 'str',
        'memory_allocation': 'int',
        'maximum_instances': 'int',
        'minimum_instances': 'int',
        'maximum_idle_time': 'int',
        'labels': 'object',
        'creation_date': 'datetime',
        'last_updated': 'datetime',
        'last_file_upload': 'datetime',
        'request_retention_time': 'int',
        'request_retention_mode': 'str'
    }

    attribute_map = {
        'id': 'id',
        'deployment': 'deployment',
        'version': 'version',
        'description': 'description',
        'language': 'language',
        'status': 'status',
        'active_revision': 'active_revision',
        'latest_build': 'latest_build',
        'memory_allocation': 'memory_allocation',
        'maximum_instances': 'maximum_instances',
        'minimum_instances': 'minimum_instances',
        'maximum_idle_time': 'maximum_idle_time',
        'labels': 'labels',
        'creation_date': 'creation_date',
        'last_updated': 'last_updated',
        'last_file_upload': 'last_file_upload',
        'request_retention_time': 'request_retention_time',
        'request_retention_mode': 'request_retention_mode'
    }

    def __init__(self, id=None, deployment=None, version=None, description=None, language=None, status=None, active_revision=None, latest_build=None, memory_allocation=None, maximum_instances=None, minimum_instances=None, maximum_idle_time=None, labels=None, creation_date=None, last_updated=None, last_file_upload=None, request_retention_time=None, request_retention_mode=None, local_vars_configuration=None):  # noqa: E501
        """DeploymentVersionDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._deployment = None
        self._version = None
        self._description = None
        self._language = None
        self._status = None
        self._active_revision = None
        self._latest_build = None
        self._memory_allocation = None
        self._maximum_instances = None
        self._minimum_instances = None
        self._maximum_idle_time = None
        self._labels = None
        self._creation_date = None
        self._last_updated = None
        self._last_file_upload = None
        self._request_retention_time = None
        self._request_retention_mode = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.deployment = deployment
        self.version = version
        if description is not None:
            self.description = description
        self.language = language
        if status is not None:
            self.status = status
        if active_revision is not None:
            self.active_revision = active_revision
        if latest_build is not None:
            self.latest_build = latest_build
        if memory_allocation is not None:
            self.memory_allocation = memory_allocation
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
        if last_file_upload is not None:
            self.last_file_upload = last_file_upload
        if request_retention_time is not None:
            self.request_retention_time = request_retention_time
        self.request_retention_mode = request_retention_mode

    @property
    def id(self):
        """Gets the id of this DeploymentVersionDetail.  # noqa: E501


        :return: The id of this DeploymentVersionDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeploymentVersionDetail.


        :param id: The id of this DeploymentVersionDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")  # noqa: E501

        self._id = id

    @property
    def deployment(self):
        """Gets the deployment of this DeploymentVersionDetail.  # noqa: E501


        :return: The deployment of this DeploymentVersionDetail.  # noqa: E501
        :rtype: str
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """Sets the deployment of this DeploymentVersionDetail.


        :param deployment: The deployment of this DeploymentVersionDetail.  # noqa: E501
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
        """Gets the version of this DeploymentVersionDetail.  # noqa: E501


        :return: The version of this DeploymentVersionDetail.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DeploymentVersionDetail.


        :param version: The version of this DeploymentVersionDetail.  # noqa: E501
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
        """Gets the description of this DeploymentVersionDetail.  # noqa: E501


        :return: The description of this DeploymentVersionDetail.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeploymentVersionDetail.


        :param description: The description of this DeploymentVersionDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not isinstance(description, str)):
            raise ValueError("Parameter `description` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 200):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501

        self._description = description

    @property
    def language(self):
        """Gets the language of this DeploymentVersionDetail.  # noqa: E501


        :return: The language of this DeploymentVersionDetail.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this DeploymentVersionDetail.


        :param language: The language of this DeploymentVersionDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and language is None:  # noqa: E501
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                language is not None and not isinstance(language, str)):
            raise ValueError("Parameter `language` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                language is not None and len(language) < 1):
            raise ValueError("Invalid value for `language`, length must be greater than or equal to `1`")  # noqa: E501

        self._language = language

    @property
    def status(self):
        """Gets the status of this DeploymentVersionDetail.  # noqa: E501


        :return: The status of this DeploymentVersionDetail.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeploymentVersionDetail.


        :param status: The status of this DeploymentVersionDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                status is not None and not isinstance(status, str)):
            raise ValueError("Parameter `status` must be a string")  # noqa: E501

        self._status = status

    @property
    def active_revision(self):
        """Gets the active_revision of this DeploymentVersionDetail.  # noqa: E501


        :return: The active_revision of this DeploymentVersionDetail.  # noqa: E501
        :rtype: str
        """
        return self._active_revision

    @active_revision.setter
    def active_revision(self, active_revision):
        """Sets the active_revision of this DeploymentVersionDetail.


        :param active_revision: The active_revision of this DeploymentVersionDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                active_revision is not None and not isinstance(active_revision, str)):
            raise ValueError("Parameter `active_revision` must be a string")  # noqa: E501

        self._active_revision = active_revision

    @property
    def latest_build(self):
        """Gets the latest_build of this DeploymentVersionDetail.  # noqa: E501


        :return: The latest_build of this DeploymentVersionDetail.  # noqa: E501
        :rtype: str
        """
        return self._latest_build

    @latest_build.setter
    def latest_build(self, latest_build):
        """Sets the latest_build of this DeploymentVersionDetail.


        :param latest_build: The latest_build of this DeploymentVersionDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                latest_build is not None and not isinstance(latest_build, str)):
            raise ValueError("Parameter `latest_build` must be a string")  # noqa: E501

        self._latest_build = latest_build

    @property
    def memory_allocation(self):
        """Gets the memory_allocation of this DeploymentVersionDetail.  # noqa: E501


        :return: The memory_allocation of this DeploymentVersionDetail.  # noqa: E501
        :rtype: int
        """
        return self._memory_allocation

    @memory_allocation.setter
    def memory_allocation(self, memory_allocation):
        """Sets the memory_allocation of this DeploymentVersionDetail.


        :param memory_allocation: The memory_allocation of this DeploymentVersionDetail.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                memory_allocation is not None and not isinstance(memory_allocation, int)):
            raise ValueError("Parameter `memory_allocation` must be an integer")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                memory_allocation is not None and memory_allocation > 1048576):  # noqa: E501
            raise ValueError("Invalid value for `memory_allocation`, must be a value less than or equal to `1048576`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                memory_allocation is not None and memory_allocation < 256):  # noqa: E501
            raise ValueError("Invalid value for `memory_allocation`, must be a value greater than or equal to `256`")  # noqa: E501

        self._memory_allocation = memory_allocation

    @property
    def maximum_instances(self):
        """Gets the maximum_instances of this DeploymentVersionDetail.  # noqa: E501


        :return: The maximum_instances of this DeploymentVersionDetail.  # noqa: E501
        :rtype: int
        """
        return self._maximum_instances

    @maximum_instances.setter
    def maximum_instances(self, maximum_instances):
        """Sets the maximum_instances of this DeploymentVersionDetail.


        :param maximum_instances: The maximum_instances of this DeploymentVersionDetail.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_instances is not None and not isinstance(maximum_instances, int)):
            raise ValueError("Parameter `maximum_instances` must be an integer")  # noqa: E501

        self._maximum_instances = maximum_instances

    @property
    def minimum_instances(self):
        """Gets the minimum_instances of this DeploymentVersionDetail.  # noqa: E501


        :return: The minimum_instances of this DeploymentVersionDetail.  # noqa: E501
        :rtype: int
        """
        return self._minimum_instances

    @minimum_instances.setter
    def minimum_instances(self, minimum_instances):
        """Sets the minimum_instances of this DeploymentVersionDetail.


        :param minimum_instances: The minimum_instances of this DeploymentVersionDetail.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                minimum_instances is not None and not isinstance(minimum_instances, int)):
            raise ValueError("Parameter `minimum_instances` must be an integer")  # noqa: E501

        self._minimum_instances = minimum_instances

    @property
    def maximum_idle_time(self):
        """Gets the maximum_idle_time of this DeploymentVersionDetail.  # noqa: E501


        :return: The maximum_idle_time of this DeploymentVersionDetail.  # noqa: E501
        :rtype: int
        """
        return self._maximum_idle_time

    @maximum_idle_time.setter
    def maximum_idle_time(self, maximum_idle_time):
        """Sets the maximum_idle_time of this DeploymentVersionDetail.


        :param maximum_idle_time: The maximum_idle_time of this DeploymentVersionDetail.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_idle_time is not None and not isinstance(maximum_idle_time, int)):
            raise ValueError("Parameter `maximum_idle_time` must be an integer")  # noqa: E501

        self._maximum_idle_time = maximum_idle_time

    @property
    def labels(self):
        """Gets the labels of this DeploymentVersionDetail.  # noqa: E501


        :return: The labels of this DeploymentVersionDetail.  # noqa: E501
        :rtype: object
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this DeploymentVersionDetail.


        :param labels: The labels of this DeploymentVersionDetail.  # noqa: E501
        :type: object
        """

        self._labels = labels

    @property
    def creation_date(self):
        """Gets the creation_date of this DeploymentVersionDetail.  # noqa: E501


        :return: The creation_date of this DeploymentVersionDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this DeploymentVersionDetail.


        :param creation_date: The creation_date of this DeploymentVersionDetail.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def last_updated(self):
        """Gets the last_updated of this DeploymentVersionDetail.  # noqa: E501


        :return: The last_updated of this DeploymentVersionDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this DeploymentVersionDetail.


        :param last_updated: The last_updated of this DeploymentVersionDetail.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def last_file_upload(self):
        """Gets the last_file_upload of this DeploymentVersionDetail.  # noqa: E501


        :return: The last_file_upload of this DeploymentVersionDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._last_file_upload

    @last_file_upload.setter
    def last_file_upload(self, last_file_upload):
        """Sets the last_file_upload of this DeploymentVersionDetail.


        :param last_file_upload: The last_file_upload of this DeploymentVersionDetail.  # noqa: E501
        :type: datetime
        """

        self._last_file_upload = last_file_upload

    @property
    def request_retention_time(self):
        """Gets the request_retention_time of this DeploymentVersionDetail.  # noqa: E501


        :return: The request_retention_time of this DeploymentVersionDetail.  # noqa: E501
        :rtype: int
        """
        return self._request_retention_time

    @request_retention_time.setter
    def request_retention_time(self, request_retention_time):
        """Sets the request_retention_time of this DeploymentVersionDetail.


        :param request_retention_time: The request_retention_time of this DeploymentVersionDetail.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                request_retention_time is not None and not isinstance(request_retention_time, int)):
            raise ValueError("Parameter `request_retention_time` must be an integer")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                request_retention_time is not None and request_retention_time > 2.4192E+6):  # noqa: E501
            raise ValueError("Invalid value for `request_retention_time`, must be a value less than or equal to `2.4192E+6`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                request_retention_time is not None and request_retention_time < 3.6E+3):  # noqa: E501
            raise ValueError("Invalid value for `request_retention_time`, must be a value greater than or equal to `3.6E+3`")  # noqa: E501

        self._request_retention_time = request_retention_time

    @property
    def request_retention_mode(self):
        """Gets the request_retention_mode of this DeploymentVersionDetail.  # noqa: E501


        :return: The request_retention_mode of this DeploymentVersionDetail.  # noqa: E501
        :rtype: str
        """
        return self._request_retention_mode

    @request_retention_mode.setter
    def request_retention_mode(self, request_retention_mode):
        """Sets the request_retention_mode of this DeploymentVersionDetail.


        :param request_retention_mode: The request_retention_mode of this DeploymentVersionDetail.  # noqa: E501
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
        if not isinstance(other, DeploymentVersionDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeploymentVersionDetail):
            return True

        return self.to_dict() != other.to_dict()

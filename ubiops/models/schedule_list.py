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


class ScheduleList(object):
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
        'name': 'str',
        'object_type': 'str',
        'object_name': 'str',
        'version': 'str',
        'schedule': 'str',
        'request_data': 'object',
        'timeout': 'int',
        'enabled': 'bool',
        'creation_date': 'datetime',
        'description': 'str',
        'labels': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'object_type': 'object_type',
        'object_name': 'object_name',
        'version': 'version',
        'schedule': 'schedule',
        'request_data': 'request_data',
        'timeout': 'timeout',
        'enabled': 'enabled',
        'creation_date': 'creation_date',
        'description': 'description',
        'labels': 'labels'
    }

    def __init__(self, id=None, name=None, object_type=None, object_name=None, version=None, schedule=None, request_data=None, timeout=None, enabled=None, creation_date=None, description=None, labels=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """ScheduleList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._object_type = None
        self._object_name = None
        self._version = None
        self._schedule = None
        self._request_data = None
        self._timeout = None
        self._enabled = None
        self._creation_date = None
        self._description = None
        self._labels = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if object_type is not None:
            self.object_type = object_type
        if object_name is not None:
            self.object_name = object_name
        if version is not None:
            self.version = version
        if schedule is not None:
            self.schedule = schedule
        self.request_data = request_data
        self.timeout = timeout
        self.enabled = enabled
        if creation_date is not None:
            self.creation_date = creation_date
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels

    @property
    def id(self):
        """Gets the id of this ScheduleList.  # noqa: E501


        :return: The id of this ScheduleList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScheduleList.


        :param id: The id of this ScheduleList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this ScheduleList.  # noqa: E501


        :return: The name of this ScheduleList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScheduleList.


        :param name: The name of this ScheduleList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def object_type(self):
        """Gets the object_type of this ScheduleList.  # noqa: E501


        :return: The object_type of this ScheduleList.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ScheduleList.


        :param object_type: The object_type of this ScheduleList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                object_type is not None and not isinstance(object_type, str)):
            raise ValueError("Parameter `object_type` must be a string")  # noqa: E501

        self._object_type = object_type

    @property
    def object_name(self):
        """Gets the object_name of this ScheduleList.  # noqa: E501


        :return: The object_name of this ScheduleList.  # noqa: E501
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """Sets the object_name of this ScheduleList.


        :param object_name: The object_name of this ScheduleList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                object_name is not None and not isinstance(object_name, str)):
            raise ValueError("Parameter `object_name` must be a string")  # noqa: E501

        self._object_name = object_name

    @property
    def version(self):
        """Gets the version of this ScheduleList.  # noqa: E501


        :return: The version of this ScheduleList.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ScheduleList.


        :param version: The version of this ScheduleList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                version is not None and not isinstance(version, str)):
            raise ValueError("Parameter `version` must be a string")  # noqa: E501

        self._version = version

    @property
    def schedule(self):
        """Gets the schedule of this ScheduleList.  # noqa: E501


        :return: The schedule of this ScheduleList.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this ScheduleList.


        :param schedule: The schedule of this ScheduleList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                schedule is not None and not isinstance(schedule, str)):
            raise ValueError("Parameter `schedule` must be a string")  # noqa: E501

        self._schedule = schedule

    @property
    def request_data(self):
        """Gets the request_data of this ScheduleList.  # noqa: E501


        :return: The request_data of this ScheduleList.  # noqa: E501
        :rtype: object
        """
        return self._request_data

    @request_data.setter
    def request_data(self, request_data):
        """Sets the request_data of this ScheduleList.


        :param request_data: The request_data of this ScheduleList.  # noqa: E501
        :type: object
        """

        self._request_data = request_data

    @property
    def timeout(self):
        """Gets the timeout of this ScheduleList.  # noqa: E501


        :return: The timeout of this ScheduleList.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ScheduleList.


        :param timeout: The timeout of this ScheduleList.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                timeout is not None and not isinstance(timeout, int)):
            raise ValueError("Parameter `timeout` must be an integer")  # noqa: E501

        self._timeout = timeout

    @property
    def enabled(self):
        """Gets the enabled of this ScheduleList.  # noqa: E501


        :return: The enabled of this ScheduleList.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ScheduleList.


        :param enabled: The enabled of this ScheduleList.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                enabled is not None and not isinstance(enabled, bool)):
            raise ValueError("Parameter `enabled` must be a boolean")  # noqa: E501

        self._enabled = enabled

    @property
    def creation_date(self):
        """Gets the creation_date of this ScheduleList.  # noqa: E501


        :return: The creation_date of this ScheduleList.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ScheduleList.


        :param creation_date: The creation_date of this ScheduleList.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def description(self):
        """Gets the description of this ScheduleList.  # noqa: E501


        :return: The description of this ScheduleList.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ScheduleList.


        :param description: The description of this ScheduleList.  # noqa: E501
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
    def labels(self):
        """Gets the labels of this ScheduleList.  # noqa: E501


        :return: The labels of this ScheduleList.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ScheduleList.


        :param labels: The labels of this ScheduleList.  # noqa: E501
        :type: dict(str, str)
        """
        if (self.local_vars_configuration.client_side_validation and
                labels is not None and not isinstance(labels, dict)):
            raise ValueError("Parameter `labels` must be a dictionary")  # noqa: E501

        self._labels = labels

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
        if not isinstance(other, ScheduleList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduleList):
            return True

        return self.to_dict() != other.to_dict()

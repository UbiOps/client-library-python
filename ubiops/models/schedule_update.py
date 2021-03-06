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


class ScheduleUpdate(object):
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
        'name': 'str',
        'schedule': 'str',
        'request_data': 'object',
        'batch': 'bool',
        'timeout': 'int',
        'enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'schedule': 'schedule',
        'request_data': 'request_data',
        'batch': 'batch',
        'timeout': 'timeout',
        'enabled': 'enabled'
    }

    def __init__(self, name=None, schedule=None, request_data=None, batch=None, timeout=None, enabled=None, local_vars_configuration=None):  # noqa: E501
        """ScheduleUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._schedule = None
        self._request_data = None
        self._batch = None
        self._timeout = None
        self._enabled = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if schedule is not None:
            self.schedule = schedule
        self.request_data = request_data
        if batch is not None:
            self.batch = batch
        if timeout is not None:
            self.timeout = timeout
        if enabled is not None:
            self.enabled = enabled

    @property
    def name(self):
        """Gets the name of this ScheduleUpdate.  # noqa: E501


        :return: The name of this ScheduleUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScheduleUpdate.


        :param name: The name of this ScheduleUpdate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def schedule(self):
        """Gets the schedule of this ScheduleUpdate.  # noqa: E501


        :return: The schedule of this ScheduleUpdate.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this ScheduleUpdate.


        :param schedule: The schedule of this ScheduleUpdate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                schedule is not None and not isinstance(schedule, str)):
            raise ValueError("Parameter `schedule` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                schedule is not None and len(schedule) < 1):
            raise ValueError("Invalid value for `schedule`, length must be greater than or equal to `1`")  # noqa: E501

        self._schedule = schedule

    @property
    def request_data(self):
        """Gets the request_data of this ScheduleUpdate.  # noqa: E501


        :return: The request_data of this ScheduleUpdate.  # noqa: E501
        :rtype: object
        """
        return self._request_data

    @request_data.setter
    def request_data(self, request_data):
        """Sets the request_data of this ScheduleUpdate.


        :param request_data: The request_data of this ScheduleUpdate.  # noqa: E501
        :type: object
        """

        self._request_data = request_data

    @property
    def batch(self):
        """Gets the batch of this ScheduleUpdate.  # noqa: E501


        :return: The batch of this ScheduleUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._batch

    @batch.setter
    def batch(self, batch):
        """Sets the batch of this ScheduleUpdate.


        :param batch: The batch of this ScheduleUpdate.  # noqa: E501
        :type: bool
        """
        if (self.local_vars_configuration.client_side_validation and
                batch is not None and not isinstance(batch, bool)):
            raise ValueError("Parameter `batch` must be a boolean")  # noqa: E501

        self._batch = batch

    @property
    def timeout(self):
        """Gets the timeout of this ScheduleUpdate.  # noqa: E501


        :return: The timeout of this ScheduleUpdate.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ScheduleUpdate.


        :param timeout: The timeout of this ScheduleUpdate.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                timeout is not None and not isinstance(timeout, int)):
            raise ValueError("Parameter `timeout` must be an integer")  # noqa: E501

        self._timeout = timeout

    @property
    def enabled(self):
        """Gets the enabled of this ScheduleUpdate.  # noqa: E501


        :return: The enabled of this ScheduleUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ScheduleUpdate.


        :param enabled: The enabled of this ScheduleUpdate.  # noqa: E501
        :type: bool
        """
        if (self.local_vars_configuration.client_side_validation and
                enabled is not None and not isinstance(enabled, bool)):
            raise ValueError("Parameter `enabled` must be a boolean")  # noqa: E501

        self._enabled = enabled

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
        if not isinstance(other, ScheduleUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduleUpdate):
            return True

        return self.to_dict() != other.to_dict()

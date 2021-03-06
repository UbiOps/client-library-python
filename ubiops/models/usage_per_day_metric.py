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


class UsagePerDayMetric(object):
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
        'day': 'datetime',
        'value': 'float'
    }

    attribute_map = {
        'day': 'day',
        'value': 'value'
    }

    def __init__(self, day=None, value=None, local_vars_configuration=None):  # noqa: E501
        """UsagePerDayMetric - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._day = None
        self._value = None
        self.discriminator = None

        self.day = day
        self.value = value

    @property
    def day(self):
        """Gets the day of this UsagePerDayMetric.  # noqa: E501


        :return: The day of this UsagePerDayMetric.  # noqa: E501
        :rtype: datetime
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this UsagePerDayMetric.


        :param day: The day of this UsagePerDayMetric.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and day is None:  # noqa: E501
            raise ValueError("Invalid value for `day`, must not be `None`")  # noqa: E501

        self._day = day

    @property
    def value(self):
        """Gets the value of this UsagePerDayMetric.  # noqa: E501


        :return: The value of this UsagePerDayMetric.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UsagePerDayMetric.


        :param value: The value of this UsagePerDayMetric.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                value is not None and not isinstance(value, float)):
            raise ValueError("Parameter `value` must be a float")  # noqa: E501

        self._value = value

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
        if not isinstance(other, UsagePerDayMetric):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsagePerDayMetric):
            return True

        return self.to_dict() != other.to_dict()

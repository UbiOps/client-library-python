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


class Metrics(object):
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
        'value': 'float',
        'start_date': 'datetime',
        'end_date': 'datetime'
    }

    attribute_map = {
        'value': 'value',
        'start_date': 'start_date',
        'end_date': 'end_date'
    }

    def __init__(self, value=None, start_date=None, end_date=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """Metrics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def value(self):
        """Gets the value of this Metrics.  # noqa: E501


        :return: The value of this Metrics.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Metrics.


        :param value: The value of this Metrics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and (
            value is not None and not isinstance(value, float)
        ):
            raise ValueError("Parameter `value` must be a float")  # noqa: E501

        self._value = value

    @property
    def start_date(self):
        """Gets the start_date of this Metrics.  # noqa: E501


        :return: The start_date of this Metrics.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Metrics.


        :param start_date: The start_date of this Metrics.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Metrics.  # noqa: E501


        :return: The end_date of this Metrics.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Metrics.


        :param end_date: The end_date of this Metrics.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

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
        if not isinstance(other, Metrics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Metrics):
            return True

        return self.to_dict() != other.to_dict()

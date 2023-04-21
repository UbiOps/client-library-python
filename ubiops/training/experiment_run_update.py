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


class ExperimentRunUpdate(object):
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
        'status': 'str',
        'notification_group': 'str'
    }

    attribute_map = {
        'status': 'status',
        'notification_group': 'notification_group'
    }

    def __init__(self, status=None, notification_group=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """ExperimentRunUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._notification_group = None
        self.discriminator = None

        if status is not None:
            self.status = status
        self.notification_group = notification_group

    @property
    def status(self):
        """Gets the status of this ExperimentRunUpdate.  # noqa: E501


        :return: The status of this ExperimentRunUpdate.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExperimentRunUpdate.


        :param status: The status of this ExperimentRunUpdate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and (
            status is not None and not isinstance(status, str)
        ):
            raise ValueError("Parameter `status` must be a string")  # noqa: E501
        allowed_values = ["cancelled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def notification_group(self):
        """Gets the notification_group of this ExperimentRunUpdate.  # noqa: E501


        :return: The notification_group of this ExperimentRunUpdate.  # noqa: E501
        :rtype: str
        """
        return self._notification_group

    @notification_group.setter
    def notification_group(self, notification_group):
        """Sets the notification_group of this ExperimentRunUpdate.


        :param notification_group: The notification_group of this ExperimentRunUpdate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and (
            notification_group is not None and not isinstance(notification_group, str)
        ):
            raise ValueError("Parameter `notification_group` must be a string")  # noqa: E501

        if self.local_vars_configuration.client_side_validation and (
            notification_group is not None and len(notification_group) < 1
        ):
            raise ValueError("Invalid value for `notification_group`, length must be greater than or equal to `1`")  # noqa: E501

        self._notification_group = notification_group

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
        if not isinstance(other, ExperimentRunUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExperimentRunUpdate):
            return True

        return self.to_dict() != other.to_dict()

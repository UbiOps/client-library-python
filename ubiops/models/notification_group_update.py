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


class NotificationGroupUpdate(object):
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
        'contacts': 'list[NotificationGroupContact]'
    }

    attribute_map = {
        'name': 'name',
        'contacts': 'contacts'
    }

    def __init__(self, name=None, contacts=None, local_vars_configuration=None):  # noqa: E501
        """NotificationGroupUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._contacts = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if contacts is not None:
            self.contacts = contacts

    @property
    def name(self):
        """Gets the name of this NotificationGroupUpdate.  # noqa: E501


        :return: The name of this NotificationGroupUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NotificationGroupUpdate.


        :param name: The name of this NotificationGroupUpdate.  # noqa: E501
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
    def contacts(self):
        """Gets the contacts of this NotificationGroupUpdate.  # noqa: E501


        :return: The contacts of this NotificationGroupUpdate.  # noqa: E501
        :rtype: list[NotificationGroupContact]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this NotificationGroupUpdate.


        :param contacts: The contacts of this NotificationGroupUpdate.  # noqa: E501
        :type: list[NotificationGroupContact]
        """
        if (self.local_vars_configuration.client_side_validation and
                contacts is not None and not isinstance(contacts, list)):
            raise ValueError("Parameter `contacts` must be a list")  # noqa: E501
        if self.local_vars_configuration.client_side_validation and contacts is not None:
            from ubiops.models.notification_group_contact import NotificationGroupContact

            contacts = [
                NotificationGroupContact(**item) if isinstance(item, dict) else item  # noqa: E501
                for item in contacts
            ]

        self._contacts = contacts

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
        if not isinstance(other, NotificationGroupUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationGroupUpdate):
            return True

        return self.to_dict() != other.to_dict()
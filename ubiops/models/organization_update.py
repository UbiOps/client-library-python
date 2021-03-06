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


class OrganizationUpdate(object):
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
        'subscription': 'str',
        'subscription_agreed': 'bool',
        'subscription_end_date': 'date'
    }

    attribute_map = {
        'name': 'name',
        'subscription': 'subscription',
        'subscription_agreed': 'subscription_agreed',
        'subscription_end_date': 'subscription_end_date'
    }

    def __init__(self, name=None, subscription=None, subscription_agreed=None, subscription_end_date=None, local_vars_configuration=None):  # noqa: E501
        """OrganizationUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._subscription = None
        self._subscription_agreed = None
        self._subscription_end_date = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if subscription is not None:
            self.subscription = subscription
        if subscription_agreed is not None:
            self.subscription_agreed = subscription_agreed
        self.subscription_end_date = subscription_end_date

    @property
    def name(self):
        """Gets the name of this OrganizationUpdate.  # noqa: E501


        :return: The name of this OrganizationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationUpdate.


        :param name: The name of this OrganizationUpdate.  # noqa: E501
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
    def subscription(self):
        """Gets the subscription of this OrganizationUpdate.  # noqa: E501


        :return: The subscription of this OrganizationUpdate.  # noqa: E501
        :rtype: str
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this OrganizationUpdate.


        :param subscription: The subscription of this OrganizationUpdate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                subscription is not None and not isinstance(subscription, str)):
            raise ValueError("Parameter `subscription` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                subscription is not None and len(subscription) < 1):
            raise ValueError("Invalid value for `subscription`, length must be greater than or equal to `1`")  # noqa: E501

        self._subscription = subscription

    @property
    def subscription_agreed(self):
        """Gets the subscription_agreed of this OrganizationUpdate.  # noqa: E501


        :return: The subscription_agreed of this OrganizationUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._subscription_agreed

    @subscription_agreed.setter
    def subscription_agreed(self, subscription_agreed):
        """Sets the subscription_agreed of this OrganizationUpdate.


        :param subscription_agreed: The subscription_agreed of this OrganizationUpdate.  # noqa: E501
        :type: bool
        """
        if (self.local_vars_configuration.client_side_validation and
                subscription_agreed is not None and not isinstance(subscription_agreed, bool)):
            raise ValueError("Parameter `subscription_agreed` must be a boolean")  # noqa: E501

        self._subscription_agreed = subscription_agreed

    @property
    def subscription_end_date(self):
        """Gets the subscription_end_date of this OrganizationUpdate.  # noqa: E501


        :return: The subscription_end_date of this OrganizationUpdate.  # noqa: E501
        :rtype: date
        """
        return self._subscription_end_date

    @subscription_end_date.setter
    def subscription_end_date(self, subscription_end_date):
        """Sets the subscription_end_date of this OrganizationUpdate.


        :param subscription_end_date: The subscription_end_date of this OrganizationUpdate.  # noqa: E501
        :type: date
        """

        self._subscription_end_date = subscription_end_date

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
        if not isinstance(other, OrganizationUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationUpdate):
            return True

        return self.to_dict() != other.to_dict()

# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class OrganizationUpdate(object):
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
        "name": "str",
        "subscription": "str",
        "subscription_end_date": "date",
        "subscription_start_date": "date",
        "two_factor_authentication_forced": "bool",
    }

    attribute_map = {
        "name": "name",
        "subscription": "subscription",
        "subscription_end_date": "subscription_end_date",
        "subscription_start_date": "subscription_start_date",
        "two_factor_authentication_forced": "two_factor_authentication_forced",
    }

    def __init__(
        self,
        name=None,
        subscription=None,
        subscription_end_date=None,
        subscription_start_date=None,
        two_factor_authentication_forced=None,
        **kwargs,
    ):
        """
        OrganizationUpdate - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._name = None
        self._subscription = None
        self._subscription_end_date = None
        self._subscription_start_date = None
        self._two_factor_authentication_forced = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if subscription is not None:
            self.subscription = subscription
        self.subscription_end_date = subscription_end_date
        self.subscription_start_date = subscription_start_date
        if two_factor_authentication_forced is not None:
            self.two_factor_authentication_forced = two_factor_authentication_forced

    @property
    def name(self):
        """
        Gets the name of this OrganizationUpdate

        :return: the name of this OrganizationUpdate
        :rtype: str
        """

        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OrganizationUpdate

        :param name: the name of this OrganizationUpdate
        :type: str
        """

        if self.client_side_validation and (name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")

        if self.client_side_validation and (name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def subscription(self):
        """
        Gets the subscription of this OrganizationUpdate

        :return: the subscription of this OrganizationUpdate
        :rtype: str
        """

        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """
        Sets the subscription of this OrganizationUpdate

        :param subscription: the subscription of this OrganizationUpdate
        :type: str
        """

        if self.client_side_validation and (subscription is not None and not isinstance(subscription, str)):
            raise ValueError("Parameter `subscription` must be a string")

        if self.client_side_validation and (subscription is not None and len(subscription) < 1):
            raise ValueError("Invalid value for `subscription`, length must be greater than or equal to `1`")

        self._subscription = subscription

    @property
    def subscription_end_date(self):
        """
        Gets the subscription_end_date of this OrganizationUpdate

        :return: the subscription_end_date of this OrganizationUpdate
        :rtype: date
        """

        return self._subscription_end_date

    @subscription_end_date.setter
    def subscription_end_date(self, subscription_end_date):
        """
        Sets the subscription_end_date of this OrganizationUpdate

        :param subscription_end_date: the subscription_end_date of this OrganizationUpdate
        :type: date
        """

        self._subscription_end_date = subscription_end_date

    @property
    def subscription_start_date(self):
        """
        Gets the subscription_start_date of this OrganizationUpdate

        :return: the subscription_start_date of this OrganizationUpdate
        :rtype: date
        """

        return self._subscription_start_date

    @subscription_start_date.setter
    def subscription_start_date(self, subscription_start_date):
        """
        Sets the subscription_start_date of this OrganizationUpdate

        :param subscription_start_date: the subscription_start_date of this OrganizationUpdate
        :type: date
        """

        self._subscription_start_date = subscription_start_date

    @property
    def two_factor_authentication_forced(self):
        """
        Gets the two_factor_authentication_forced of this OrganizationUpdate

        :return: the two_factor_authentication_forced of this OrganizationUpdate
        :rtype: bool
        """

        return self._two_factor_authentication_forced

    @two_factor_authentication_forced.setter
    def two_factor_authentication_forced(self, two_factor_authentication_forced):
        """
        Sets the two_factor_authentication_forced of this OrganizationUpdate

        :param two_factor_authentication_forced: the two_factor_authentication_forced of this OrganizationUpdate
        :type: bool
        """

        if self.client_side_validation and (
            two_factor_authentication_forced is not None and not isinstance(two_factor_authentication_forced, bool)
        ):
            raise ValueError("Parameter `two_factor_authentication_forced` must be a boolean")

        self._two_factor_authentication_forced = two_factor_authentication_forced

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

        if not isinstance(other, OrganizationUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, OrganizationUpdate):
            return True

        return self.to_dict() != other.to_dict()

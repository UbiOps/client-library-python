# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class Node(object):
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

    openapi_types = {"ipv4_address": "str", "ipv6_address": "str"}

    attribute_map = {"ipv4_address": "ipv4_address", "ipv6_address": "ipv6_address"}

    def __init__(self, ipv4_address=None, ipv6_address=None, **kwargs):
        """
        Node - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._ipv4_address = None
        self._ipv6_address = None
        self.discriminator = None

        self.ipv4_address = ipv4_address
        self.ipv6_address = ipv6_address

    @property
    def ipv4_address(self):
        """
        Gets the ipv4_address of this Node

        :return: the ipv4_address of this Node
        :rtype: str
        """

        return self._ipv4_address

    @ipv4_address.setter
    def ipv4_address(self, ipv4_address):
        """
        Sets the ipv4_address of this Node

        :param ipv4_address: the ipv4_address of this Node
        :type: str
        """

        if self.client_side_validation and (ipv4_address is not None and not isinstance(ipv4_address, str)):
            raise ValueError("Parameter `ipv4_address` must be a string")

        if self.client_side_validation and (ipv4_address is not None and len(ipv4_address) < 1):
            raise ValueError("Invalid value for `ipv4_address`, length must be greater than or equal to `1`")

        self._ipv4_address = ipv4_address

    @property
    def ipv6_address(self):
        """
        Gets the ipv6_address of this Node

        :return: the ipv6_address of this Node
        :rtype: str
        """

        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        """
        Sets the ipv6_address of this Node

        :param ipv6_address: the ipv6_address of this Node
        :type: str
        """

        if self.client_side_validation and (ipv6_address is not None and not isinstance(ipv6_address, str)):
            raise ValueError("Parameter `ipv6_address` must be a string")

        if self.client_side_validation and (ipv6_address is not None and len(ipv6_address) < 1):
            raise ValueError("Invalid value for `ipv6_address`, length must be greater than or equal to `1`")

        self._ipv6_address = ipv6_address

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

        if not isinstance(other, Node):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, Node):
            return True

        return self.to_dict() != other.to_dict()
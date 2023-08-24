# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class RoleDetailList(object):
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

    openapi_types = {"id": "str", "name": "str", "default": "str", "permissions": "list[str]"}

    attribute_map = {"id": "id", "name": "name", "default": "default", "permissions": "permissions"}

    def __init__(self, id=None, name=None, default=None, permissions=None, **kwargs):
        """
        RoleDetailList - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._id = None
        self._name = None
        self._default = None
        self._permissions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if default is not None:
            self.default = default
        if permissions is not None:
            self.permissions = permissions

    @property
    def id(self):
        """
        Gets the id of this RoleDetailList

        :return: the id of this RoleDetailList
        :rtype: str
        """

        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RoleDetailList

        :param id: the id of this RoleDetailList
        :type: str
        """

        if self.client_side_validation and (id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this RoleDetailList

        :return: the name of this RoleDetailList
        :rtype: str
        """

        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RoleDetailList

        :param name: the name of this RoleDetailList
        :type: str
        """

        if self.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if self.client_side_validation and (name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")

        if self.client_side_validation and (name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")
        if self.client_side_validation and (name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def default(self):
        """
        Gets the default of this RoleDetailList

        :return: the default of this RoleDetailList
        :rtype: str
        """

        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this RoleDetailList

        :param default: the default of this RoleDetailList
        :type: str
        """

        if self.client_side_validation and (default is not None and not isinstance(default, str)):
            raise ValueError("Parameter `default` must be a string")

        self._default = default

    @property
    def permissions(self):
        """
        Gets the permissions of this RoleDetailList

        :return: the permissions of this RoleDetailList
        :rtype: list[str]
        """

        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this RoleDetailList

        :param permissions: the permissions of this RoleDetailList
        :type: list[str]
        """

        if self.client_side_validation and (permissions is not None and not isinstance(permissions, list)):
            raise ValueError("Parameter `permissions` must be a list")

        self._permissions = permissions

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

        if not isinstance(other, RoleDetailList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, RoleDetailList):
            return True

        return self.to_dict() != other.to_dict()

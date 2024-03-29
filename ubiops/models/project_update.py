# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class ProjectUpdate(object):
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
        "advanced_permissions": "bool",
        "credits": "float",
        "suspend": "bool",
        "cors_origins": "list[str]",
    }

    attribute_map = {
        "name": "name",
        "advanced_permissions": "advanced_permissions",
        "credits": "credits",
        "suspend": "suspend",
        "cors_origins": "cors_origins",
    }

    def __init__(self, name=None, advanced_permissions=None, credits=None, suspend=None, cors_origins=None, **kwargs):
        """
        ProjectUpdate - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._name = None
        self._advanced_permissions = None
        self._credits = None
        self._suspend = None
        self._cors_origins = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if advanced_permissions is not None:
            self.advanced_permissions = advanced_permissions
        self.credits = credits
        if suspend is not None:
            self.suspend = suspend
        if cors_origins is not None:
            self.cors_origins = cors_origins

    @property
    def name(self):
        """
        Gets the name of this ProjectUpdate

        :return: the name of this ProjectUpdate
        :rtype: str
        """

        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProjectUpdate

        :param name: the name of this ProjectUpdate
        :type: str
        """

        if self.client_side_validation and (name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")

        if self.client_side_validation and (name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def advanced_permissions(self):
        """
        Gets the advanced_permissions of this ProjectUpdate

        :return: the advanced_permissions of this ProjectUpdate
        :rtype: bool
        """

        return self._advanced_permissions

    @advanced_permissions.setter
    def advanced_permissions(self, advanced_permissions):
        """
        Sets the advanced_permissions of this ProjectUpdate

        :param advanced_permissions: the advanced_permissions of this ProjectUpdate
        :type: bool
        """

        if self.client_side_validation and (
            advanced_permissions is not None and not isinstance(advanced_permissions, bool)
        ):
            raise ValueError("Parameter `advanced_permissions` must be a boolean")

        self._advanced_permissions = advanced_permissions

    @property
    def credits(self):
        """
        Gets the credits of this ProjectUpdate

        :return: the credits of this ProjectUpdate
        :rtype: float
        """

        return self._credits

    @credits.setter
    def credits(self, credits):
        """
        Sets the credits of this ProjectUpdate

        :param credits: the credits of this ProjectUpdate
        :type: float
        """

        if self.client_side_validation and (credits is not None and not isinstance(credits, (int, float))):
            raise ValueError("Parameter `credits` must be a float")

        self._credits = credits

    @property
    def suspend(self):
        """
        Gets the suspend of this ProjectUpdate

        :return: the suspend of this ProjectUpdate
        :rtype: bool
        """

        return self._suspend

    @suspend.setter
    def suspend(self, suspend):
        """
        Sets the suspend of this ProjectUpdate

        :param suspend: the suspend of this ProjectUpdate
        :type: bool
        """

        if self.client_side_validation and (suspend is not None and not isinstance(suspend, bool)):
            raise ValueError("Parameter `suspend` must be a boolean")

        self._suspend = suspend

    @property
    def cors_origins(self):
        """
        Gets the cors_origins of this ProjectUpdate

        :return: the cors_origins of this ProjectUpdate
        :rtype: list[str]
        """

        return self._cors_origins

    @cors_origins.setter
    def cors_origins(self, cors_origins):
        """
        Sets the cors_origins of this ProjectUpdate

        :param cors_origins: the cors_origins of this ProjectUpdate
        :type: list[str]
        """

        if self.client_side_validation and (cors_origins is not None and not isinstance(cors_origins, list)):
            raise ValueError("Parameter `cors_origins` must be a list")

        self._cors_origins = cors_origins

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

        if not isinstance(other, ProjectUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, ProjectUpdate):
            return True

        return self.to_dict() != other.to_dict()

# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class OrganizationUserCreate(object):
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

    openapi_types = {"email": "str", "admin": "bool"}

    attribute_map = {"email": "email", "admin": "admin"}

    def __init__(self, email=None, admin=False, **kwargs):
        """
        OrganizationUserCreate - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._email = None
        self._admin = None
        self.discriminator = None

        self.email = email
        if admin is not None:
            self.admin = admin

    @property
    def email(self):
        """
        Gets the email of this OrganizationUserCreate

        :return: the email of this OrganizationUserCreate
        :rtype: str
        """

        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this OrganizationUserCreate

        :param email: the email of this OrganizationUserCreate
        :type: str
        """

        if self.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")
        if self.client_side_validation and (email is not None and not isinstance(email, str)):
            raise ValueError("Parameter `email` must be a string")

        if self.client_side_validation and (email is not None and len(email) < 1):
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")

        self._email = email

    @property
    def admin(self):
        """
        Gets the admin of this OrganizationUserCreate

        :return: the admin of this OrganizationUserCreate
        :rtype: bool
        """

        return self._admin

    @admin.setter
    def admin(self, admin):
        """
        Sets the admin of this OrganizationUserCreate

        :param admin: the admin of this OrganizationUserCreate
        :type: bool
        """

        if self.client_side_validation and (admin is not None and not isinstance(admin, bool)):
            raise ValueError("Parameter `admin` must be a boolean")

        self._admin = admin

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

        if not isinstance(other, OrganizationUserCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, OrganizationUserCreate):
            return True

        return self.to_dict() != other.to_dict()

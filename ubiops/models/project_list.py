# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class ProjectList(object):
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
        "id": "str",
        "name": "str",
        "creation_date": "date",
        "advanced_permissions": "bool",
        "credits": "float",
        "organization_name": "str",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "creation_date": "creation_date",
        "advanced_permissions": "advanced_permissions",
        "credits": "credits",
        "organization_name": "organization_name",
    }

    def __init__(
        self,
        id=None,
        name=None,
        creation_date=None,
        advanced_permissions=None,
        credits=None,
        organization_name=None,
        **kwargs,
    ):
        """
        ProjectList - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._id = None
        self._name = None
        self._creation_date = None
        self._advanced_permissions = None
        self._credits = None
        self._organization_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if creation_date is not None:
            self.creation_date = creation_date
        if advanced_permissions is not None:
            self.advanced_permissions = advanced_permissions
        self.credits = credits
        self.organization_name = organization_name

    @property
    def id(self):
        """
        Gets the id of this ProjectList

        :return: the id of this ProjectList
        :rtype: str
        """

        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProjectList

        :param id: the id of this ProjectList
        :type: str
        """

        if self.client_side_validation and (id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ProjectList

        :return: the name of this ProjectList
        :rtype: str
        """

        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProjectList

        :param name: the name of this ProjectList
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
    def creation_date(self):
        """
        Gets the creation_date of this ProjectList

        :return: the creation_date of this ProjectList
        :rtype: date
        """

        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this ProjectList

        :param creation_date: the creation_date of this ProjectList
        :type: date
        """

        self._creation_date = creation_date

    @property
    def advanced_permissions(self):
        """
        Gets the advanced_permissions of this ProjectList

        :return: the advanced_permissions of this ProjectList
        :rtype: bool
        """

        return self._advanced_permissions

    @advanced_permissions.setter
    def advanced_permissions(self, advanced_permissions):
        """
        Sets the advanced_permissions of this ProjectList

        :param advanced_permissions: the advanced_permissions of this ProjectList
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
        Gets the credits of this ProjectList

        :return: the credits of this ProjectList
        :rtype: float
        """

        return self._credits

    @credits.setter
    def credits(self, credits):
        """
        Sets the credits of this ProjectList

        :param credits: the credits of this ProjectList
        :type: float
        """

        if self.client_side_validation and (credits is not None and not isinstance(credits, float)):
            raise ValueError("Parameter `credits` must be a float")

        self._credits = credits

    @property
    def organization_name(self):
        """
        Gets the organization_name of this ProjectList

        :return: the organization_name of this ProjectList
        :rtype: str
        """

        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """
        Sets the organization_name of this ProjectList

        :param organization_name: the organization_name of this ProjectList
        :type: str
        """

        if self.client_side_validation and organization_name is None:
            raise ValueError("Invalid value for `organization_name`, must not be `None`")
        if self.client_side_validation and (organization_name is not None and not isinstance(organization_name, str)):
            raise ValueError("Parameter `organization_name` must be a string")

        if self.client_side_validation and (organization_name is not None and len(organization_name) < 1):
            raise ValueError("Invalid value for `organization_name`, length must be greater than or equal to `1`")

        self._organization_name = organization_name

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

        if not isinstance(other, ProjectList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, ProjectList):
            return True

        return self.to_dict() != other.to_dict()

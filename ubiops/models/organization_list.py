# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class OrganizationList(object):
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
        "creation_date": "datetime",
        "status": "str",
        "two_factor_authentication_forced": "bool",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "creation_date": "creation_date",
        "status": "status",
        "two_factor_authentication_forced": "two_factor_authentication_forced",
    }

    def __init__(
        self, id=None, name=None, creation_date=None, status=None, two_factor_authentication_forced=None, **kwargs
    ):
        """
        OrganizationList - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._id = None
        self._name = None
        self._creation_date = None
        self._status = None
        self._two_factor_authentication_forced = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if creation_date is not None:
            self.creation_date = creation_date
        self.status = status
        if two_factor_authentication_forced is not None:
            self.two_factor_authentication_forced = two_factor_authentication_forced

    @property
    def id(self):
        """
        Gets the id of this OrganizationList

        :return: the id of this OrganizationList
        :rtype: str
        """

        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OrganizationList

        :param id: the id of this OrganizationList
        :type: str
        """

        if self.client_side_validation and (id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this OrganizationList

        :return: the name of this OrganizationList
        :rtype: str
        """

        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OrganizationList

        :param name: the name of this OrganizationList
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
        Gets the creation_date of this OrganizationList

        :return: the creation_date of this OrganizationList
        :rtype: datetime
        """

        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this OrganizationList

        :param creation_date: the creation_date of this OrganizationList
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def status(self):
        """
        Gets the status of this OrganizationList

        :return: the status of this OrganizationList
        :rtype: str
        """

        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this OrganizationList

        :param status: the status of this OrganizationList
        :type: str
        """

        if self.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        if self.client_side_validation and (status is not None and not isinstance(status, str)):
            raise ValueError("Parameter `status` must be a string")

        if self.client_side_validation and (status is not None and len(status) < 1):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")

        self._status = status

    @property
    def two_factor_authentication_forced(self):
        """
        Gets the two_factor_authentication_forced of this OrganizationList

        :return: the two_factor_authentication_forced of this OrganizationList
        :rtype: bool
        """

        return self._two_factor_authentication_forced

    @two_factor_authentication_forced.setter
    def two_factor_authentication_forced(self, two_factor_authentication_forced):
        """
        Sets the two_factor_authentication_forced of this OrganizationList

        :param two_factor_authentication_forced: the two_factor_authentication_forced of this OrganizationList
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

        if not isinstance(other, OrganizationList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, OrganizationList):
            return True

        return self.to_dict() != other.to_dict()

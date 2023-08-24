# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class ProjectUserList(object):
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

    openapi_types = {"id": "str", "email": "str", "name": "str", "surname": "str"}

    attribute_map = {"id": "id", "email": "email", "name": "name", "surname": "surname"}

    def __init__(self, id=None, email=None, name=None, surname=None, **kwargs):
        """
        ProjectUserList - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._id = None
        self._email = None
        self._name = None
        self._surname = None
        self.discriminator = None

        self.id = id
        self.email = email
        self.name = name
        self.surname = surname

    @property
    def id(self):
        """
        Gets the id of this ProjectUserList

        :return: the id of this ProjectUserList
        :rtype: str
        """

        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProjectUserList

        :param id: the id of this ProjectUserList
        :type: str
        """

        if self.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        if self.client_side_validation and (id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")

        self._id = id

    @property
    def email(self):
        """
        Gets the email of this ProjectUserList

        :return: the email of this ProjectUserList
        :rtype: str
        """

        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this ProjectUserList

        :param email: the email of this ProjectUserList
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
    def name(self):
        """
        Gets the name of this ProjectUserList

        :return: the name of this ProjectUserList
        :rtype: str
        """

        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProjectUserList

        :param name: the name of this ProjectUserList
        :type: str
        """

        if self.client_side_validation and (name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")

        self._name = name

    @property
    def surname(self):
        """
        Gets the surname of this ProjectUserList

        :return: the surname of this ProjectUserList
        :rtype: str
        """

        return self._surname

    @surname.setter
    def surname(self, surname):
        """
        Sets the surname of this ProjectUserList

        :param surname: the surname of this ProjectUserList
        :type: str
        """

        if self.client_side_validation and (surname is not None and not isinstance(surname, str)):
            raise ValueError("Parameter `surname` must be a string")

        self._surname = surname

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

        if not isinstance(other, ProjectUserList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, ProjectUserList):
            return True

        return self.to_dict() != other.to_dict()

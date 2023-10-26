# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class ImportList(object):
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
        "imported_by": "str",
        "creation_date": "datetime",
        "status": "str",
        "error_message": "str",
        "size": "int",
    }

    attribute_map = {
        "id": "id",
        "imported_by": "imported_by",
        "creation_date": "creation_date",
        "status": "status",
        "error_message": "error_message",
        "size": "size",
    }

    def __init__(
        self, id=None, imported_by=None, creation_date=None, status="pending", error_message=None, size=None, **kwargs
    ):
        """
        ImportList - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._id = None
        self._imported_by = None
        self._creation_date = None
        self._status = None
        self._error_message = None
        self._size = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if imported_by is not None:
            self.imported_by = imported_by
        if creation_date is not None:
            self.creation_date = creation_date
        if status is not None:
            self.status = status
        self.error_message = error_message
        self.size = size

    @property
    def id(self):
        """
        Gets the id of this ImportList

        :return: the id of this ImportList
        :rtype: str
        """

        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ImportList

        :param id: the id of this ImportList
        :type: str
        """

        if self.client_side_validation and (id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")

        self._id = id

    @property
    def imported_by(self):
        """
        Gets the imported_by of this ImportList

        :return: the imported_by of this ImportList
        :rtype: str
        """

        return self._imported_by

    @imported_by.setter
    def imported_by(self, imported_by):
        """
        Sets the imported_by of this ImportList

        :param imported_by: the imported_by of this ImportList
        :type: str
        """

        if self.client_side_validation and (imported_by is not None and not isinstance(imported_by, str)):
            raise ValueError("Parameter `imported_by` must be a string")

        self._imported_by = imported_by

    @property
    def creation_date(self):
        """
        Gets the creation_date of this ImportList

        :return: the creation_date of this ImportList
        :rtype: datetime
        """

        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this ImportList

        :param creation_date: the creation_date of this ImportList
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def status(self):
        """
        Gets the status of this ImportList

        :return: the status of this ImportList
        :rtype: str
        """

        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ImportList

        :param status: the status of this ImportList
        :type: str
        """

        if self.client_side_validation and (status is not None and not isinstance(status, str)):
            raise ValueError("Parameter `status` must be a string")

        self._status = status

    @property
    def error_message(self):
        """
        Gets the error_message of this ImportList

        :return: the error_message of this ImportList
        :rtype: str
        """

        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this ImportList

        :param error_message: the error_message of this ImportList
        :type: str
        """

        if self.client_side_validation and (error_message is not None and not isinstance(error_message, str)):
            raise ValueError("Parameter `error_message` must be a string")

        if self.client_side_validation and (error_message is not None and len(error_message) > 1024):
            raise ValueError("Invalid value for `error_message`, length must be less than or equal to `1024`")

        self._error_message = error_message

    @property
    def size(self):
        """
        Gets the size of this ImportList

        :return: the size of this ImportList
        :rtype: int
        """

        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this ImportList

        :param size: the size of this ImportList
        :type: int
        """

        if self.client_side_validation and (size is not None and not isinstance(size, int)):
            raise ValueError("Parameter `size` must be an integer")

        self._size = size

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

        if not isinstance(other, ImportList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, ImportList):
            return True

        return self.to_dict() != other.to_dict()

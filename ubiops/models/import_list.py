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


class ImportList(object):
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
        'id': 'str',
        'imported_by': 'str',
        'creation_date': 'datetime',
        'status': 'str',
        'error_message': 'str',
        'size': 'int'
    }

    attribute_map = {
        'id': 'id',
        'imported_by': 'imported_by',
        'creation_date': 'creation_date',
        'status': 'status',
        'error_message': 'error_message',
        'size': 'size'
    }

    def __init__(self, id=None, imported_by=None, creation_date=None, status='pending', error_message=None, size=None, local_vars_configuration=None):  # noqa: E501
        """ImportList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

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
        """Gets the id of this ImportList.  # noqa: E501


        :return: The id of this ImportList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImportList.


        :param id: The id of this ImportList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")  # noqa: E501

        self._id = id

    @property
    def imported_by(self):
        """Gets the imported_by of this ImportList.  # noqa: E501


        :return: The imported_by of this ImportList.  # noqa: E501
        :rtype: str
        """
        return self._imported_by

    @imported_by.setter
    def imported_by(self, imported_by):
        """Sets the imported_by of this ImportList.


        :param imported_by: The imported_by of this ImportList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                imported_by is not None and not isinstance(imported_by, str)):
            raise ValueError("Parameter `imported_by` must be a string")  # noqa: E501

        self._imported_by = imported_by

    @property
    def creation_date(self):
        """Gets the creation_date of this ImportList.  # noqa: E501


        :return: The creation_date of this ImportList.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ImportList.


        :param creation_date: The creation_date of this ImportList.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def status(self):
        """Gets the status of this ImportList.  # noqa: E501


        :return: The status of this ImportList.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ImportList.


        :param status: The status of this ImportList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                status is not None and not isinstance(status, str)):
            raise ValueError("Parameter `status` must be a string")  # noqa: E501
        allowed_values = ["pending", "scanning", "confirmation", "confirmation_pending", "processing", "completed", "failed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def error_message(self):
        """Gets the error_message of this ImportList.  # noqa: E501


        :return: The error_message of this ImportList.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ImportList.


        :param error_message: The error_message of this ImportList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                error_message is not None and not isinstance(error_message, str)):
            raise ValueError("Parameter `error_message` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                error_message is not None and len(error_message) > 1024):
            raise ValueError("Invalid value for `error_message`, length must be less than or equal to `1024`")  # noqa: E501

        self._error_message = error_message

    @property
    def size(self):
        """Gets the size of this ImportList.  # noqa: E501


        :return: The size of this ImportList.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ImportList.


        :param size: The size of this ImportList.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                size is not None and not isinstance(size, int)):
            raise ValueError("Parameter `size` must be an integer")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                size is not None and size > 9.223372036854776E+18):  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value less than or equal to `9.223372036854776E+18`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                size is not None and size < -9.223372036854776E+18):  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `-9.223372036854776E+18`")  # noqa: E501

        self._size = size

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
        if not isinstance(other, ImportList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportList):
            return True

        return self.to_dict() != other.to_dict()

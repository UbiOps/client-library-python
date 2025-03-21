# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class ExportList(object):
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
        "exported_by": "str",
        "creation_date": "datetime",
        "status": "str",
        "error_message": "str",
        "size": "int",
        "description": "str",
    }

    attribute_map = {
        "id": "id",
        "exported_by": "exported_by",
        "creation_date": "creation_date",
        "status": "status",
        "error_message": "error_message",
        "size": "size",
        "description": "description",
    }

    def __init__(
        self,
        id=None,
        exported_by=None,
        creation_date=None,
        status=None,
        error_message=None,
        size=None,
        description=None,
        **kwargs,
    ):
        """
        ExportList - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._id = None
        self._exported_by = None
        self._creation_date = None
        self._status = None
        self._error_message = None
        self._size = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if exported_by is not None:
            self.exported_by = exported_by
        if creation_date is not None:
            self.creation_date = creation_date
        if status is not None:
            self.status = status
        self.error_message = error_message
        self.size = size
        if description is not None:
            self.description = description

    @property
    def id(self):
        """
        Gets the id of this ExportList

        :return: the id of this ExportList
        :rtype: str
        """

        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExportList

        :param id: the id of this ExportList
        :type: str
        """

        if self.client_side_validation and (id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")

        self._id = id

    @property
    def exported_by(self):
        """
        Gets the exported_by of this ExportList

        :return: the exported_by of this ExportList
        :rtype: str
        """

        return self._exported_by

    @exported_by.setter
    def exported_by(self, exported_by):
        """
        Sets the exported_by of this ExportList

        :param exported_by: the exported_by of this ExportList
        :type: str
        """

        if self.client_side_validation and (exported_by is not None and not isinstance(exported_by, str)):
            raise ValueError("Parameter `exported_by` must be a string")

        self._exported_by = exported_by

    @property
    def creation_date(self):
        """
        Gets the creation_date of this ExportList

        :return: the creation_date of this ExportList
        :rtype: datetime
        """

        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this ExportList

        :param creation_date: the creation_date of this ExportList
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def status(self):
        """
        Gets the status of this ExportList

        :return: the status of this ExportList
        :rtype: str
        """

        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ExportList

        :param status: the status of this ExportList
        :type: str
        """

        if self.client_side_validation and (status is not None and not isinstance(status, str)):
            raise ValueError("Parameter `status` must be a string")

        self._status = status

    @property
    def error_message(self):
        """
        Gets the error_message of this ExportList

        :return: the error_message of this ExportList
        :rtype: str
        """

        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this ExportList

        :param error_message: the error_message of this ExportList
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
        Gets the size of this ExportList

        :return: the size of this ExportList
        :rtype: int
        """

        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this ExportList

        :param size: the size of this ExportList
        :type: int
        """

        if self.client_side_validation and (size is not None and not isinstance(size, int)):
            raise ValueError("Parameter `size` must be an integer")

        self._size = size

    @property
    def description(self):
        """
        Gets the description of this ExportList

        :return: the description of this ExportList
        :rtype: str
        """

        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ExportList

        :param description: the description of this ExportList
        :type: str
        """

        if self.client_side_validation and (description is not None and not isinstance(description, str)):
            raise ValueError("Parameter `description` must be a string")

        if self.client_side_validation and (description is not None and len(description) > 400):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `400`")

        self._description = description

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

        if not isinstance(other, ExportList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, ExportList):
            return True

        return self.to_dict() != other.to_dict()

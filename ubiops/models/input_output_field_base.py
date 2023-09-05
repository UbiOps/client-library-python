# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class InputOutputFieldBase(object):
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

    openapi_types = {"name": "str", "data_type": "str"}

    attribute_map = {"name": "name", "data_type": "data_type"}

    def __init__(self, name=None, data_type=None, **kwargs):
        """
        InputOutputFieldBase - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._name = None
        self._data_type = None
        self.discriminator = None

        self.name = name
        self.data_type = data_type

    @property
    def name(self):
        """
        Gets the name of this InputOutputFieldBase

        :return: the name of this InputOutputFieldBase
        :rtype: str
        """

        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InputOutputFieldBase

        :param name: the name of this InputOutputFieldBase
        :type: str
        """

        if self.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if self.client_side_validation and (name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")

        if self.client_side_validation and (name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def data_type(self):
        """
        Gets the data_type of this InputOutputFieldBase

        :return: the data_type of this InputOutputFieldBase
        :rtype: str
        """

        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this InputOutputFieldBase

        :param data_type: the data_type of this InputOutputFieldBase
        :type: str
        """

        if self.client_side_validation and data_type is None:
            raise ValueError("Invalid value for `data_type`, must not be `None`")
        if self.client_side_validation and (data_type is not None and not isinstance(data_type, str)):
            raise ValueError("Parameter `data_type` must be a string")

        self._data_type = data_type

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

        if not isinstance(other, InputOutputFieldBase):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, InputOutputFieldBase):
            return True

        return self.to_dict() != other.to_dict()

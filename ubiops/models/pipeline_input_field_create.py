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


class PipelineInputFieldCreate(object):
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
        'name': 'str',
        'data_type': 'str',
        'widget': 'InputFieldWidgetCreate'
    }

    attribute_map = {
        'name': 'name',
        'data_type': 'data_type',
        'widget': 'widget'
    }

    def __init__(self, name=None, data_type=None, widget=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """PipelineInputFieldCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._data_type = None
        self._widget = None
        self.discriminator = None

        self.name = name
        self.data_type = data_type
        if widget is not None:
            self.widget = widget

    @property
    def name(self):
        """Gets the name of this PipelineInputFieldCreate.  # noqa: E501


        :return: The name of this PipelineInputFieldCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelineInputFieldCreate.


        :param name: The name of this PipelineInputFieldCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def data_type(self):
        """Gets the data_type of this PipelineInputFieldCreate.  # noqa: E501


        :return: The data_type of this PipelineInputFieldCreate.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this PipelineInputFieldCreate.


        :param data_type: The data_type of this PipelineInputFieldCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and data_type is None:  # noqa: E501
            raise ValueError("Invalid value for `data_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                data_type is not None and not isinstance(data_type, str)):
            raise ValueError("Parameter `data_type` must be a string")  # noqa: E501
        allowed_values = ["int", "string", "double", "bool", "array_int", "array_double", "array_string", "blob", "file"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and data_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(data_type, allowed_values)
            )

        self._data_type = data_type

    @property
    def widget(self):
        """Gets the widget of this PipelineInputFieldCreate.  # noqa: E501


        :return: The widget of this PipelineInputFieldCreate.  # noqa: E501
        :rtype: InputFieldWidgetCreate
        """
        return self._widget

    @widget.setter
    def widget(self, widget):
        """Sets the widget of this PipelineInputFieldCreate.


        :param widget: The widget of this PipelineInputFieldCreate.  # noqa: E501
        :type: InputFieldWidgetCreate
        """

        if self.local_vars_configuration.client_side_validation and widget is not None:
            if isinstance(widget, dict):  # noqa: E501
                from ubiops.models.input_field_widget_create import InputFieldWidgetCreate

                widget = InputFieldWidgetCreate(**widget)  # noqa: E501

        self._widget = widget

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
        if not isinstance(other, PipelineInputFieldCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PipelineInputFieldCreate):
            return True

        return self.to_dict() != other.to_dict()

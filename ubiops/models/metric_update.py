# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class MetricUpdate(object):
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

    openapi_types = {"name": "str", "description": "str", "unit": "str", "labels": "list[str]"}

    attribute_map = {"name": "name", "description": "description", "unit": "unit", "labels": "labels"}

    def __init__(self, name=None, description=None, unit=None, labels=None, **kwargs):
        """
        MetricUpdate - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._name = None
        self._description = None
        self._unit = None
        self._labels = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if unit is not None:
            self.unit = unit
        if labels is not None:
            self.labels = labels

    @property
    def name(self):
        """
        Gets the name of this MetricUpdate

        :return: the name of this MetricUpdate
        :rtype: str
        """

        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MetricUpdate

        :param name: the name of this MetricUpdate
        :type: str
        """

        if self.client_side_validation and (name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")

        if self.client_side_validation and (name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this MetricUpdate

        :return: the description of this MetricUpdate
        :rtype: str
        """

        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MetricUpdate

        :param description: the description of this MetricUpdate
        :type: str
        """

        if self.client_side_validation and (description is not None and not isinstance(description, str)):
            raise ValueError("Parameter `description` must be a string")

        self._description = description

    @property
    def unit(self):
        """
        Gets the unit of this MetricUpdate

        :return: the unit of this MetricUpdate
        :rtype: str
        """

        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this MetricUpdate

        :param unit: the unit of this MetricUpdate
        :type: str
        """

        if self.client_side_validation and (unit is not None and not isinstance(unit, str)):
            raise ValueError("Parameter `unit` must be a string")

        if self.client_side_validation and (unit is not None and len(unit) > 32):
            raise ValueError("Invalid value for `unit`, length must be less than or equal to `32`")

        self._unit = unit

    @property
    def labels(self):
        """
        Gets the labels of this MetricUpdate

        :return: the labels of this MetricUpdate
        :rtype: list[str]
        """

        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this MetricUpdate

        :param labels: the labels of this MetricUpdate
        :type: list[str]
        """

        if self.client_side_validation and (labels is not None and not isinstance(labels, list)):
            raise ValueError("Parameter `labels` must be a list")

        self._labels = labels

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

        if not isinstance(other, MetricUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, MetricUpdate):
            return True

        return self.to_dict() != other.to_dict()

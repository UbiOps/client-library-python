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


class PipelineVersionObjectCreate(object):
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
        'reference_type': 'str',
        'reference_name': 'str',
        'version': 'str',
        'configuration': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'reference_type': 'reference_type',
        'reference_name': 'reference_name',
        'version': 'version',
        'configuration': 'configuration'
    }

    def __init__(self, name=None, reference_type='deployment', reference_name=None, version=None, configuration=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """PipelineVersionObjectCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._reference_type = None
        self._reference_name = None
        self._version = None
        self._configuration = None
        self.discriminator = None

        self.name = name
        if reference_type is not None:
            self.reference_type = reference_type
        self.reference_name = reference_name
        self.version = version
        if configuration is not None:
            self.configuration = configuration

    @property
    def name(self):
        """Gets the name of this PipelineVersionObjectCreate.  # noqa: E501


        :return: The name of this PipelineVersionObjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelineVersionObjectCreate.


        :param name: The name of this PipelineVersionObjectCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def reference_type(self):
        """Gets the reference_type of this PipelineVersionObjectCreate.  # noqa: E501


        :return: The reference_type of this PipelineVersionObjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type):
        """Sets the reference_type of this PipelineVersionObjectCreate.


        :param reference_type: The reference_type of this PipelineVersionObjectCreate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                reference_type is not None and not isinstance(reference_type, str)):
            raise ValueError("Parameter `reference_type` must be a string")  # noqa: E501
        allowed_values = ["deployment", "operator", "pipeline"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and reference_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `reference_type` ({0}), must be one of {1}"  # noqa: E501
                .format(reference_type, allowed_values)
            )

        self._reference_type = reference_type

    @property
    def reference_name(self):
        """Gets the reference_name of this PipelineVersionObjectCreate.  # noqa: E501


        :return: The reference_name of this PipelineVersionObjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._reference_name

    @reference_name.setter
    def reference_name(self, reference_name):
        """Sets the reference_name of this PipelineVersionObjectCreate.


        :param reference_name: The reference_name of this PipelineVersionObjectCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and reference_name is None:  # noqa: E501
            raise ValueError("Invalid value for `reference_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                reference_name is not None and not isinstance(reference_name, str)):
            raise ValueError("Parameter `reference_name` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                reference_name is not None and len(reference_name) < 1):
            raise ValueError("Invalid value for `reference_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._reference_name = reference_name

    @property
    def version(self):
        """Gets the version of this PipelineVersionObjectCreate.  # noqa: E501


        :return: The version of this PipelineVersionObjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PipelineVersionObjectCreate.


        :param version: The version of this PipelineVersionObjectCreate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                version is not None and not isinstance(version, str)):
            raise ValueError("Parameter `version` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) < 1):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501

        self._version = version

    @property
    def configuration(self):
        """Gets the configuration of this PipelineVersionObjectCreate.  # noqa: E501


        :return: The configuration of this PipelineVersionObjectCreate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this PipelineVersionObjectCreate.


        :param configuration: The configuration of this PipelineVersionObjectCreate.  # noqa: E501
        :type: dict(str, str)
        """
        if (self.local_vars_configuration.client_side_validation and
                configuration is not None and not isinstance(configuration, dict)):
            raise ValueError("Parameter `configuration` must be a dictionary")  # noqa: E501

        self._configuration = configuration

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
        if not isinstance(other, PipelineVersionObjectCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PipelineVersionObjectCreate):
            return True

        return self.to_dict() != other.to_dict()

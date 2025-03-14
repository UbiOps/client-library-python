# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class PipelineVersionObjectCreate(object):
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
        "name": "str",
        "reference_type": "str",
        "reference_name": "str",
        "version": "str",
        "configuration": "dict(str, str)",
        "metadata": "dict(str, str)",
    }

    attribute_map = {
        "name": "name",
        "reference_type": "reference_type",
        "reference_name": "reference_name",
        "version": "version",
        "configuration": "configuration",
        "metadata": "metadata",
    }

    def __init__(
        self,
        name=None,
        reference_type=None,
        reference_name=None,
        version=None,
        configuration=None,
        metadata=None,
        **kwargs,
    ):
        """
        PipelineVersionObjectCreate - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._name = None
        self._reference_type = None
        self._reference_name = None
        self._version = None
        self._configuration = None
        self._metadata = None
        self.discriminator = None

        self.name = name
        if reference_type is not None:
            self.reference_type = reference_type
        self.reference_name = reference_name
        self.version = version
        self.configuration = configuration
        self.metadata = metadata

    @property
    def name(self):
        """
        Gets the name of this PipelineVersionObjectCreate

        :return: the name of this PipelineVersionObjectCreate
        :rtype: str
        """

        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PipelineVersionObjectCreate

        :param name: the name of this PipelineVersionObjectCreate
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
    def reference_type(self):
        """
        Gets the reference_type of this PipelineVersionObjectCreate

        :return: the reference_type of this PipelineVersionObjectCreate
        :rtype: str
        """

        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type):
        """
        Sets the reference_type of this PipelineVersionObjectCreate

        :param reference_type: the reference_type of this PipelineVersionObjectCreate
        :type: str
        """

        if self.client_side_validation and (reference_type is not None and not isinstance(reference_type, str)):
            raise ValueError("Parameter `reference_type` must be a string")

        self._reference_type = reference_type

    @property
    def reference_name(self):
        """
        Gets the reference_name of this PipelineVersionObjectCreate

        :return: the reference_name of this PipelineVersionObjectCreate
        :rtype: str
        """

        return self._reference_name

    @reference_name.setter
    def reference_name(self, reference_name):
        """
        Sets the reference_name of this PipelineVersionObjectCreate

        :param reference_name: the reference_name of this PipelineVersionObjectCreate
        :type: str
        """

        if self.client_side_validation and reference_name is None:
            raise ValueError("Invalid value for `reference_name`, must not be `None`")
        if self.client_side_validation and (reference_name is not None and not isinstance(reference_name, str)):
            raise ValueError("Parameter `reference_name` must be a string")

        if self.client_side_validation and (reference_name is not None and len(reference_name) < 1):
            raise ValueError("Invalid value for `reference_name`, length must be greater than or equal to `1`")

        self._reference_name = reference_name

    @property
    def version(self):
        """
        Gets the version of this PipelineVersionObjectCreate

        :return: the version of this PipelineVersionObjectCreate
        :rtype: str
        """

        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PipelineVersionObjectCreate

        :param version: the version of this PipelineVersionObjectCreate
        :type: str
        """

        if self.client_side_validation and (version is not None and not isinstance(version, str)):
            raise ValueError("Parameter `version` must be a string")

        if self.client_side_validation and (version is not None and len(version) < 1):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")

        self._version = version

    @property
    def configuration(self):
        """
        Gets the configuration of this PipelineVersionObjectCreate

        :return: the configuration of this PipelineVersionObjectCreate
        :rtype: dict(str, str)
        """

        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this PipelineVersionObjectCreate

        :param configuration: the configuration of this PipelineVersionObjectCreate
        :type: dict(str, str)
        """

        if self.client_side_validation and (configuration is not None and not isinstance(configuration, dict)):
            raise ValueError("Parameter `configuration` must be a dictionary")

        self._configuration = configuration

    @property
    def metadata(self):
        """
        Gets the metadata of this PipelineVersionObjectCreate

        :return: the metadata of this PipelineVersionObjectCreate
        :rtype: dict(str, str)
        """

        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this PipelineVersionObjectCreate

        :param metadata: the metadata of this PipelineVersionObjectCreate
        :type: dict(str, str)
        """

        if self.client_side_validation and (metadata is not None and not isinstance(metadata, dict)):
            raise ValueError("Parameter `metadata` must be a dictionary")

        self._metadata = metadata

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

        if not isinstance(other, PipelineVersionObjectCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, PipelineVersionObjectCreate):
            return True

        return self.to_dict() != other.to_dict()

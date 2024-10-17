# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class PipelineVersionObjectList(object):
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
        "reference_name": "str",
        "reference_type": "str",
        "version": "str",
        "input_type": "str",
        "output_type": "str",
        "configuration": "PipelineVersionObjectConfigurationList",
        "metadata": "dict(str, str)",
        "input_fields": "list[InputOutputFieldBase]",
        "output_fields": "list[InputOutputFieldBase]",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "reference_name": "reference_name",
        "reference_type": "reference_type",
        "version": "version",
        "input_type": "input_type",
        "output_type": "output_type",
        "configuration": "configuration",
        "metadata": "metadata",
        "input_fields": "input_fields",
        "output_fields": "output_fields",
    }

    def __init__(
        self,
        id=None,
        name=None,
        reference_name=None,
        reference_type=None,
        version=None,
        input_type=None,
        output_type=None,
        configuration=None,
        metadata=None,
        input_fields=None,
        output_fields=None,
        **kwargs,
    ):
        """
        PipelineVersionObjectList - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._id = None
        self._name = None
        self._reference_name = None
        self._reference_type = None
        self._version = None
        self._input_type = None
        self._output_type = None
        self._configuration = None
        self._metadata = None
        self._input_fields = None
        self._output_fields = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.reference_name = reference_name
        if reference_type is not None:
            self.reference_type = reference_type
        self.version = version
        self.input_type = input_type
        self.output_type = output_type
        self.configuration = configuration
        self.metadata = metadata
        self.input_fields = input_fields
        self.output_fields = output_fields

    @property
    def id(self):
        """
        Gets the id of this PipelineVersionObjectList

        :return: the id of this PipelineVersionObjectList
        :rtype: str
        """

        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PipelineVersionObjectList

        :param id: the id of this PipelineVersionObjectList
        :type: str
        """

        if self.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        if self.client_side_validation and (id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this PipelineVersionObjectList

        :return: the name of this PipelineVersionObjectList
        :rtype: str
        """

        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PipelineVersionObjectList

        :param name: the name of this PipelineVersionObjectList
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
    def reference_name(self):
        """
        Gets the reference_name of this PipelineVersionObjectList

        :return: the reference_name of this PipelineVersionObjectList
        :rtype: str
        """

        return self._reference_name

    @reference_name.setter
    def reference_name(self, reference_name):
        """
        Sets the reference_name of this PipelineVersionObjectList

        :param reference_name: the reference_name of this PipelineVersionObjectList
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
    def reference_type(self):
        """
        Gets the reference_type of this PipelineVersionObjectList

        :return: the reference_type of this PipelineVersionObjectList
        :rtype: str
        """

        return self._reference_type

    @reference_type.setter
    def reference_type(self, reference_type):
        """
        Sets the reference_type of this PipelineVersionObjectList

        :param reference_type: the reference_type of this PipelineVersionObjectList
        :type: str
        """

        if self.client_side_validation and (reference_type is not None and not isinstance(reference_type, str)):
            raise ValueError("Parameter `reference_type` must be a string")

        if self.client_side_validation and (reference_type is not None and len(reference_type) < 1):
            raise ValueError("Invalid value for `reference_type`, length must be greater than or equal to `1`")

        self._reference_type = reference_type

    @property
    def version(self):
        """
        Gets the version of this PipelineVersionObjectList

        :return: the version of this PipelineVersionObjectList
        :rtype: str
        """

        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PipelineVersionObjectList

        :param version: the version of this PipelineVersionObjectList
        :type: str
        """

        if self.client_side_validation and (version is not None and not isinstance(version, str)):
            raise ValueError("Parameter `version` must be a string")

        self._version = version

    @property
    def input_type(self):
        """
        Gets the input_type of this PipelineVersionObjectList

        :return: the input_type of this PipelineVersionObjectList
        :rtype: str
        """

        return self._input_type

    @input_type.setter
    def input_type(self, input_type):
        """
        Sets the input_type of this PipelineVersionObjectList

        :param input_type: the input_type of this PipelineVersionObjectList
        :type: str
        """

        if self.client_side_validation and (input_type is not None and not isinstance(input_type, str)):
            raise ValueError("Parameter `input_type` must be a string")

        if self.client_side_validation and (input_type is not None and len(input_type) < 1):
            raise ValueError("Invalid value for `input_type`, length must be greater than or equal to `1`")

        self._input_type = input_type

    @property
    def output_type(self):
        """
        Gets the output_type of this PipelineVersionObjectList

        :return: the output_type of this PipelineVersionObjectList
        :rtype: str
        """

        return self._output_type

    @output_type.setter
    def output_type(self, output_type):
        """
        Sets the output_type of this PipelineVersionObjectList

        :param output_type: the output_type of this PipelineVersionObjectList
        :type: str
        """

        if self.client_side_validation and (output_type is not None and not isinstance(output_type, str)):
            raise ValueError("Parameter `output_type` must be a string")

        if self.client_side_validation and (output_type is not None and len(output_type) < 1):
            raise ValueError("Invalid value for `output_type`, length must be greater than or equal to `1`")

        self._output_type = output_type

    @property
    def configuration(self):
        """
        Gets the configuration of this PipelineVersionObjectList

        :return: the configuration of this PipelineVersionObjectList
        :rtype: PipelineVersionObjectConfigurationList
        """

        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this PipelineVersionObjectList

        :param configuration: the configuration of this PipelineVersionObjectList
        :type: PipelineVersionObjectConfigurationList
        """

        if self.client_side_validation and configuration is not None:
            if isinstance(configuration, dict):
                from ubiops.models.pipeline_version_object_configuration_list import (
                    PipelineVersionObjectConfigurationList,
                )

                configuration = PipelineVersionObjectConfigurationList(**configuration)

        self._configuration = configuration

    @property
    def metadata(self):
        """
        Gets the metadata of this PipelineVersionObjectList

        :return: the metadata of this PipelineVersionObjectList
        :rtype: dict(str, str)
        """

        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this PipelineVersionObjectList

        :param metadata: the metadata of this PipelineVersionObjectList
        :type: dict(str, str)
        """

        if self.client_side_validation and (metadata is not None and not isinstance(metadata, dict)):
            raise ValueError("Parameter `metadata` must be a dictionary")

        self._metadata = metadata

    @property
    def input_fields(self):
        """
        Gets the input_fields of this PipelineVersionObjectList

        :return: the input_fields of this PipelineVersionObjectList
        :rtype: list[InputOutputFieldBase]
        """

        return self._input_fields

    @input_fields.setter
    def input_fields(self, input_fields):
        """
        Sets the input_fields of this PipelineVersionObjectList

        :param input_fields: the input_fields of this PipelineVersionObjectList
        :type: list[InputOutputFieldBase]
        """

        if self.client_side_validation and (input_fields is not None and not isinstance(input_fields, list)):
            raise ValueError("Parameter `input_fields` must be a list")
        if self.client_side_validation and input_fields is not None:
            from ubiops.models.input_output_field_base import InputOutputFieldBase

            input_fields = [InputOutputFieldBase(**item) if isinstance(item, dict) else item for item in input_fields]

        self._input_fields = input_fields

    @property
    def output_fields(self):
        """
        Gets the output_fields of this PipelineVersionObjectList

        :return: the output_fields of this PipelineVersionObjectList
        :rtype: list[InputOutputFieldBase]
        """

        return self._output_fields

    @output_fields.setter
    def output_fields(self, output_fields):
        """
        Sets the output_fields of this PipelineVersionObjectList

        :param output_fields: the output_fields of this PipelineVersionObjectList
        :type: list[InputOutputFieldBase]
        """

        if self.client_side_validation and (output_fields is not None and not isinstance(output_fields, list)):
            raise ValueError("Parameter `output_fields` must be a list")
        if self.client_side_validation and output_fields is not None:
            from ubiops.models.input_output_field_base import InputOutputFieldBase

            output_fields = [InputOutputFieldBase(**item) if isinstance(item, dict) else item for item in output_fields]

        self._output_fields = output_fields

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

        if not isinstance(other, PipelineVersionObjectList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, PipelineVersionObjectList):
            return True

        return self.to_dict() != other.to_dict()

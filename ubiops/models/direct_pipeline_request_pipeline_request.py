# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class DirectPipelineRequestPipelineRequest(object):
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
        "pipeline_object": "str",
        "pipeline": "str",
        "version": "str",
        "success": "bool",
        "error_message": "str",
        "sequence_id": "str",
    }

    attribute_map = {
        "id": "id",
        "pipeline_object": "pipeline_object",
        "pipeline": "pipeline",
        "version": "version",
        "success": "success",
        "error_message": "error_message",
        "sequence_id": "sequence_id",
    }

    def __init__(
        self,
        id=None,
        pipeline_object=None,
        pipeline=None,
        version=None,
        success=None,
        error_message=None,
        sequence_id=None,
        **kwargs,
    ):
        """
        DirectPipelineRequestPipelineRequest - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._id = None
        self._pipeline_object = None
        self._pipeline = None
        self._version = None
        self._success = None
        self._error_message = None
        self._sequence_id = None
        self.discriminator = None

        self.id = id
        self.pipeline_object = pipeline_object
        self.pipeline = pipeline
        self.version = version
        self.success = success
        self.error_message = error_message
        self.sequence_id = sequence_id

    @property
    def id(self):
        """
        Gets the id of this DirectPipelineRequestPipelineRequest

        :return: the id of this DirectPipelineRequestPipelineRequest
        :rtype: str
        """

        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DirectPipelineRequestPipelineRequest

        :param id: the id of this DirectPipelineRequestPipelineRequest
        :type: str
        """

        if self.client_side_validation and (id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")

        self._id = id

    @property
    def pipeline_object(self):
        """
        Gets the pipeline_object of this DirectPipelineRequestPipelineRequest

        :return: the pipeline_object of this DirectPipelineRequestPipelineRequest
        :rtype: str
        """

        return self._pipeline_object

    @pipeline_object.setter
    def pipeline_object(self, pipeline_object):
        """
        Sets the pipeline_object of this DirectPipelineRequestPipelineRequest

        :param pipeline_object: the pipeline_object of this DirectPipelineRequestPipelineRequest
        :type: str
        """

        if self.client_side_validation and pipeline_object is None:
            raise ValueError("Invalid value for `pipeline_object`, must not be `None`")
        if self.client_side_validation and (pipeline_object is not None and not isinstance(pipeline_object, str)):
            raise ValueError("Parameter `pipeline_object` must be a string")

        if self.client_side_validation and (pipeline_object is not None and len(pipeline_object) < 1):
            raise ValueError("Invalid value for `pipeline_object`, length must be greater than or equal to `1`")

        self._pipeline_object = pipeline_object

    @property
    def pipeline(self):
        """
        Gets the pipeline of this DirectPipelineRequestPipelineRequest

        :return: the pipeline of this DirectPipelineRequestPipelineRequest
        :rtype: str
        """

        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """
        Sets the pipeline of this DirectPipelineRequestPipelineRequest

        :param pipeline: the pipeline of this DirectPipelineRequestPipelineRequest
        :type: str
        """

        if self.client_side_validation and (pipeline is not None and not isinstance(pipeline, str)):
            raise ValueError("Parameter `pipeline` must be a string")

        self._pipeline = pipeline

    @property
    def version(self):
        """
        Gets the version of this DirectPipelineRequestPipelineRequest

        :return: the version of this DirectPipelineRequestPipelineRequest
        :rtype: str
        """

        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DirectPipelineRequestPipelineRequest

        :param version: the version of this DirectPipelineRequestPipelineRequest
        :type: str
        """

        if self.client_side_validation and (version is not None and not isinstance(version, str)):
            raise ValueError("Parameter `version` must be a string")

        self._version = version

    @property
    def success(self):
        """
        Gets the success of this DirectPipelineRequestPipelineRequest

        :return: the success of this DirectPipelineRequestPipelineRequest
        :rtype: bool
        """

        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this DirectPipelineRequestPipelineRequest

        :param success: the success of this DirectPipelineRequestPipelineRequest
        :type: bool
        """

        if self.client_side_validation and success is None:
            raise ValueError("Invalid value for `success`, must not be `None`")
        if self.client_side_validation and (success is not None and not isinstance(success, bool)):
            raise ValueError("Parameter `success` must be a boolean")

        self._success = success

    @property
    def error_message(self):
        """
        Gets the error_message of this DirectPipelineRequestPipelineRequest

        :return: the error_message of this DirectPipelineRequestPipelineRequest
        :rtype: str
        """

        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this DirectPipelineRequestPipelineRequest

        :param error_message: the error_message of this DirectPipelineRequestPipelineRequest
        :type: str
        """

        if self.client_side_validation and (error_message is not None and not isinstance(error_message, str)):
            raise ValueError("Parameter `error_message` must be a string")

        self._error_message = error_message

    @property
    def sequence_id(self):
        """
        Gets the sequence_id of this DirectPipelineRequestPipelineRequest

        :return: the sequence_id of this DirectPipelineRequestPipelineRequest
        :rtype: str
        """

        return self._sequence_id

    @sequence_id.setter
    def sequence_id(self, sequence_id):
        """
        Sets the sequence_id of this DirectPipelineRequestPipelineRequest

        :param sequence_id: the sequence_id of this DirectPipelineRequestPipelineRequest
        :type: str
        """

        if self.client_side_validation and sequence_id is None:
            raise ValueError("Invalid value for `sequence_id`, must not be `None`")
        if self.client_side_validation and (sequence_id is not None and not isinstance(sequence_id, str)):
            raise ValueError("Parameter `sequence_id` must be a string")

        self._sequence_id = sequence_id

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

        if not isinstance(other, DirectPipelineRequestPipelineRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, DirectPipelineRequestPipelineRequest):
            return True

        return self.to_dict() != other.to_dict()

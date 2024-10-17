# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import warnings


class PipelineRequestDeploymentRequest(object):
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
        "deployment": "str",
        "version": "str",
        "status": "str",
        "success": "bool",
        "error_message": "str",
        "sequence_id": "str",
        "input_size": "int",
        "output_size": "int",
    }

    attribute_map = {
        "id": "id",
        "pipeline_object": "pipeline_object",
        "deployment": "deployment",
        "version": "version",
        "status": "status",
        "success": "success",
        "error_message": "error_message",
        "sequence_id": "sequence_id",
        "input_size": "input_size",
        "output_size": "output_size",
    }

    def __init__(
        self,
        id=None,
        pipeline_object=None,
        deployment=None,
        version=None,
        status=None,
        success=None,
        error_message=None,
        sequence_id=None,
        input_size=None,
        output_size=None,
        **kwargs,
    ):
        """
        PipelineRequestDeploymentRequest - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._id = None
        self._pipeline_object = None
        self._deployment = None
        self._version = None
        self._status = None
        self._success = None
        self._error_message = None
        self._sequence_id = None
        self._input_size = None
        self._output_size = None
        self.discriminator = None

        self.id = id
        self.pipeline_object = pipeline_object
        self.deployment = deployment
        self.version = version
        self.status = status
        self.success = success
        self.error_message = error_message
        self.sequence_id = sequence_id
        self.input_size = input_size
        self.output_size = output_size

    @property
    def id(self):
        """
        Gets the id of this PipelineRequestDeploymentRequest

        :return: the id of this PipelineRequestDeploymentRequest
        :rtype: str
        """

        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PipelineRequestDeploymentRequest

        :param id: the id of this PipelineRequestDeploymentRequest
        :type: str
        """

        if self.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        if self.client_side_validation and (id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")

        self._id = id

    @property
    def pipeline_object(self):
        """
        Gets the pipeline_object of this PipelineRequestDeploymentRequest

        :return: the pipeline_object of this PipelineRequestDeploymentRequest
        :rtype: str
        """

        return self._pipeline_object

    @pipeline_object.setter
    def pipeline_object(self, pipeline_object):
        """
        Sets the pipeline_object of this PipelineRequestDeploymentRequest

        :param pipeline_object: the pipeline_object of this PipelineRequestDeploymentRequest
        :type: str
        """

        if self.client_side_validation and (pipeline_object is not None and not isinstance(pipeline_object, str)):
            raise ValueError("Parameter `pipeline_object` must be a string")

        if self.client_side_validation and (pipeline_object is not None and len(pipeline_object) < 1):
            raise ValueError("Invalid value for `pipeline_object`, length must be greater than or equal to `1`")

        self._pipeline_object = pipeline_object

    @property
    def deployment(self):
        """
        Gets the deployment of this PipelineRequestDeploymentRequest

        :return: the deployment of this PipelineRequestDeploymentRequest
        :rtype: str
        """

        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """
        Sets the deployment of this PipelineRequestDeploymentRequest

        :param deployment: the deployment of this PipelineRequestDeploymentRequest
        :type: str
        """

        if self.client_side_validation and (deployment is not None and not isinstance(deployment, str)):
            raise ValueError("Parameter `deployment` must be a string")

        self._deployment = deployment

    @property
    def version(self):
        """
        Gets the version of this PipelineRequestDeploymentRequest

        :return: the version of this PipelineRequestDeploymentRequest
        :rtype: str
        """

        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PipelineRequestDeploymentRequest

        :param version: the version of this PipelineRequestDeploymentRequest
        :type: str
        """

        if self.client_side_validation and (version is not None and not isinstance(version, str)):
            raise ValueError("Parameter `version` must be a string")

        self._version = version

    @property
    def status(self):
        """
        Gets the status of this PipelineRequestDeploymentRequest

        :return: the status of this PipelineRequestDeploymentRequest
        :rtype: str
        """

        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PipelineRequestDeploymentRequest

        :param status: the status of this PipelineRequestDeploymentRequest
        :type: str
        """

        if self.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        if self.client_side_validation and (status is not None and not isinstance(status, str)):
            raise ValueError("Parameter `status` must be a string")

        self._status = status

    @property
    def success(self):
        """
        Gets the success of this PipelineRequestDeploymentRequest

        :return: the success of this PipelineRequestDeploymentRequest
        :rtype: bool
        """
        warnings.warn(
            message="success is deprecated and will be removed in a future version. Use status instead.",
            category=DeprecationWarning,
            stacklevel=2,
        )

        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this PipelineRequestDeploymentRequest

        :param success: the success of this PipelineRequestDeploymentRequest
        :type: bool
        """

        if self.client_side_validation and (success is not None and not isinstance(success, bool)):
            raise ValueError("Parameter `success` must be a boolean")

        self._success = success

    @property
    def error_message(self):
        """
        Gets the error_message of this PipelineRequestDeploymentRequest

        :return: the error_message of this PipelineRequestDeploymentRequest
        :rtype: str
        """

        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this PipelineRequestDeploymentRequest

        :param error_message: the error_message of this PipelineRequestDeploymentRequest
        :type: str
        """

        if self.client_side_validation and (error_message is not None and not isinstance(error_message, str)):
            raise ValueError("Parameter `error_message` must be a string")

        self._error_message = error_message

    @property
    def sequence_id(self):
        """
        Gets the sequence_id of this PipelineRequestDeploymentRequest

        :return: the sequence_id of this PipelineRequestDeploymentRequest
        :rtype: str
        """

        return self._sequence_id

    @sequence_id.setter
    def sequence_id(self, sequence_id):
        """
        Sets the sequence_id of this PipelineRequestDeploymentRequest

        :param sequence_id: the sequence_id of this PipelineRequestDeploymentRequest
        :type: str
        """

        if self.client_side_validation and sequence_id is None:
            raise ValueError("Invalid value for `sequence_id`, must not be `None`")
        if self.client_side_validation and (sequence_id is not None and not isinstance(sequence_id, str)):
            raise ValueError("Parameter `sequence_id` must be a string")

        self._sequence_id = sequence_id

    @property
    def input_size(self):
        """
        Gets the input_size of this PipelineRequestDeploymentRequest

        :return: the input_size of this PipelineRequestDeploymentRequest
        :rtype: int
        """

        return self._input_size

    @input_size.setter
    def input_size(self, input_size):
        """
        Sets the input_size of this PipelineRequestDeploymentRequest

        :param input_size: the input_size of this PipelineRequestDeploymentRequest
        :type: int
        """

        if self.client_side_validation and (input_size is not None and not isinstance(input_size, int)):
            raise ValueError("Parameter `input_size` must be an integer")

        self._input_size = input_size

    @property
    def output_size(self):
        """
        Gets the output_size of this PipelineRequestDeploymentRequest

        :return: the output_size of this PipelineRequestDeploymentRequest
        :rtype: int
        """

        return self._output_size

    @output_size.setter
    def output_size(self, output_size):
        """
        Sets the output_size of this PipelineRequestDeploymentRequest

        :param output_size: the output_size of this PipelineRequestDeploymentRequest
        :type: int
        """

        if self.client_side_validation and (output_size is not None and not isinstance(output_size, int)):
            raise ValueError("Parameter `output_size` must be an integer")

        self._output_size = output_size

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

        if not isinstance(other, PipelineRequestDeploymentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, PipelineRequestDeploymentRequest):
            return True

        return self.to_dict() != other.to_dict()

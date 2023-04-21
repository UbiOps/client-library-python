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


class DirectPipelineRequestDeploymentRequest(object):
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
        'pipeline_object': 'str',
        'deployment': 'str',
        'version': 'str',
        'success': 'bool',
        'error_message': 'str',
        'sequence_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'pipeline_object': 'pipeline_object',
        'deployment': 'deployment',
        'version': 'version',
        'success': 'success',
        'error_message': 'error_message',
        'sequence_id': 'sequence_id'
    }

    def __init__(self, id=None, pipeline_object=None, deployment=None, version=None, success=None, error_message=None, sequence_id=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """DirectPipelineRequestDeploymentRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._pipeline_object = None
        self._deployment = None
        self._version = None
        self._success = None
        self._error_message = None
        self._sequence_id = None
        self.discriminator = None

        self.id = id
        self.pipeline_object = pipeline_object
        self.deployment = deployment
        self.version = version
        self.success = success
        self.error_message = error_message
        self.sequence_id = sequence_id

    @property
    def id(self):
        """Gets the id of this DirectPipelineRequestDeploymentRequest.  # noqa: E501


        :return: The id of this DirectPipelineRequestDeploymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DirectPipelineRequestDeploymentRequest.


        :param id: The id of this DirectPipelineRequestDeploymentRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and (
            id is not None and not isinstance(id, str)
        ):
            raise ValueError("Parameter `id` must be a string")  # noqa: E501

        self._id = id

    @property
    def pipeline_object(self):
        """Gets the pipeline_object of this DirectPipelineRequestDeploymentRequest.  # noqa: E501


        :return: The pipeline_object of this DirectPipelineRequestDeploymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_object

    @pipeline_object.setter
    def pipeline_object(self, pipeline_object):
        """Sets the pipeline_object of this DirectPipelineRequestDeploymentRequest.


        :param pipeline_object: The pipeline_object of this DirectPipelineRequestDeploymentRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pipeline_object is None:  # noqa: E501
            raise ValueError("Invalid value for `pipeline_object`, must not be `None`")  # noqa: E501
        if self.local_vars_configuration.client_side_validation and (
            pipeline_object is not None and not isinstance(pipeline_object, str)
        ):
            raise ValueError("Parameter `pipeline_object` must be a string")  # noqa: E501

        if self.local_vars_configuration.client_side_validation and (
            pipeline_object is not None and len(pipeline_object) < 1
        ):
            raise ValueError("Invalid value for `pipeline_object`, length must be greater than or equal to `1`")  # noqa: E501

        self._pipeline_object = pipeline_object

    @property
    def deployment(self):
        """Gets the deployment of this DirectPipelineRequestDeploymentRequest.  # noqa: E501


        :return: The deployment of this DirectPipelineRequestDeploymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """Sets the deployment of this DirectPipelineRequestDeploymentRequest.


        :param deployment: The deployment of this DirectPipelineRequestDeploymentRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and (
            deployment is not None and not isinstance(deployment, str)
        ):
            raise ValueError("Parameter `deployment` must be a string")  # noqa: E501

        self._deployment = deployment

    @property
    def version(self):
        """Gets the version of this DirectPipelineRequestDeploymentRequest.  # noqa: E501


        :return: The version of this DirectPipelineRequestDeploymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DirectPipelineRequestDeploymentRequest.


        :param version: The version of this DirectPipelineRequestDeploymentRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and (
            version is not None and not isinstance(version, str)
        ):
            raise ValueError("Parameter `version` must be a string")  # noqa: E501

        self._version = version

    @property
    def success(self):
        """Gets the success of this DirectPipelineRequestDeploymentRequest.  # noqa: E501


        :return: The success of this DirectPipelineRequestDeploymentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this DirectPipelineRequestDeploymentRequest.


        :param success: The success of this DirectPipelineRequestDeploymentRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and success is None:  # noqa: E501
            raise ValueError("Invalid value for `success`, must not be `None`")  # noqa: E501
        if self.local_vars_configuration.client_side_validation and (
            success is not None and not isinstance(success, bool)
        ):
            raise ValueError("Parameter `success` must be a boolean")  # noqa: E501

        self._success = success

    @property
    def error_message(self):
        """Gets the error_message of this DirectPipelineRequestDeploymentRequest.  # noqa: E501


        :return: The error_message of this DirectPipelineRequestDeploymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this DirectPipelineRequestDeploymentRequest.


        :param error_message: The error_message of this DirectPipelineRequestDeploymentRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and (
            error_message is not None and not isinstance(error_message, str)
        ):
            raise ValueError("Parameter `error_message` must be a string")  # noqa: E501

        self._error_message = error_message

    @property
    def sequence_id(self):
        """Gets the sequence_id of this DirectPipelineRequestDeploymentRequest.  # noqa: E501


        :return: The sequence_id of this DirectPipelineRequestDeploymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._sequence_id

    @sequence_id.setter
    def sequence_id(self, sequence_id):
        """Sets the sequence_id of this DirectPipelineRequestDeploymentRequest.


        :param sequence_id: The sequence_id of this DirectPipelineRequestDeploymentRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sequence_id is None:  # noqa: E501
            raise ValueError("Invalid value for `sequence_id`, must not be `None`")  # noqa: E501
        if self.local_vars_configuration.client_side_validation and (
            sequence_id is not None and not isinstance(sequence_id, str)
        ):
            raise ValueError("Parameter `sequence_id` must be a string")  # noqa: E501

        self._sequence_id = sequence_id

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
        if not isinstance(other, DirectPipelineRequestDeploymentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DirectPipelineRequestDeploymentRequest):
            return True

        return self.to_dict() != other.to_dict()

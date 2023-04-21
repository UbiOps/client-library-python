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


class DeploymentRequestCreateResponse(object):
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
        'deployment': 'str',
        'version': 'str',
        'success': 'bool',
        'result': 'object',
        'error_message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'deployment': 'deployment',
        'version': 'version',
        'success': 'success',
        'result': 'result',
        'error_message': 'error_message'
    }

    def __init__(self, id=None, deployment=None, version=None, success=None, result=None, error_message=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """DeploymentRequestCreateResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._deployment = None
        self._version = None
        self._success = None
        self._result = None
        self._error_message = None
        self.discriminator = None

        self.id = id
        self.deployment = deployment
        self.version = version
        self.success = success
        self.result = result
        self.error_message = error_message

    @property
    def id(self):
        """Gets the id of this DeploymentRequestCreateResponse.  # noqa: E501


        :return: The id of this DeploymentRequestCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeploymentRequestCreateResponse.


        :param id: The id of this DeploymentRequestCreateResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if self.local_vars_configuration.client_side_validation and (
            id is not None and not isinstance(id, str)
        ):
            raise ValueError("Parameter `id` must be a string")  # noqa: E501

        self._id = id

    @property
    def deployment(self):
        """Gets the deployment of this DeploymentRequestCreateResponse.  # noqa: E501


        :return: The deployment of this DeploymentRequestCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """Sets the deployment of this DeploymentRequestCreateResponse.


        :param deployment: The deployment of this DeploymentRequestCreateResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and (
            deployment is not None and not isinstance(deployment, str)
        ):
            raise ValueError("Parameter `deployment` must be a string")  # noqa: E501

        self._deployment = deployment

    @property
    def version(self):
        """Gets the version of this DeploymentRequestCreateResponse.  # noqa: E501


        :return: The version of this DeploymentRequestCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DeploymentRequestCreateResponse.


        :param version: The version of this DeploymentRequestCreateResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and (
            version is not None and not isinstance(version, str)
        ):
            raise ValueError("Parameter `version` must be a string")  # noqa: E501

        self._version = version

    @property
    def success(self):
        """Gets the success of this DeploymentRequestCreateResponse.  # noqa: E501


        :return: The success of this DeploymentRequestCreateResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this DeploymentRequestCreateResponse.


        :param success: The success of this DeploymentRequestCreateResponse.  # noqa: E501
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
    def result(self):
        """Gets the result of this DeploymentRequestCreateResponse.  # noqa: E501


        :return: The result of this DeploymentRequestCreateResponse.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this DeploymentRequestCreateResponse.


        :param result: The result of this DeploymentRequestCreateResponse.  # noqa: E501
        :type: object
        """

        self._result = result

    @property
    def error_message(self):
        """Gets the error_message of this DeploymentRequestCreateResponse.  # noqa: E501


        :return: The error_message of this DeploymentRequestCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this DeploymentRequestCreateResponse.


        :param error_message: The error_message of this DeploymentRequestCreateResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and (
            error_message is not None and not isinstance(error_message, str)
        ):
            raise ValueError("Parameter `error_message` must be a string")  # noqa: E501

        self._error_message = error_message

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
        if not isinstance(other, DeploymentRequestCreateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeploymentRequestCreateResponse):
            return True

        return self.to_dict() != other.to_dict()

# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import warnings


class DeploymentRequestCreateResponse(object):
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
        "deployment": "str",
        "version": "str",
        "status": "str",
        "success": "bool",
        "result": "object",
        "error_message": "str",
        "timeout": "int",
    }

    attribute_map = {
        "id": "id",
        "deployment": "deployment",
        "version": "version",
        "status": "status",
        "success": "success",
        "result": "result",
        "error_message": "error_message",
        "timeout": "timeout",
    }

    def __init__(
        self,
        id=None,
        deployment=None,
        version=None,
        status=None,
        success=None,
        result=None,
        error_message=None,
        timeout=None,
        **kwargs,
    ):
        """
        DeploymentRequestCreateResponse - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._id = None
        self._deployment = None
        self._version = None
        self._status = None
        self._success = None
        self._result = None
        self._error_message = None
        self._timeout = None
        self.discriminator = None

        self.id = id
        self.deployment = deployment
        self.version = version
        self.status = status
        self.success = success
        self.result = result
        self.error_message = error_message
        self.timeout = timeout

    @property
    def id(self):
        """
        Gets the id of this DeploymentRequestCreateResponse

        :return: the id of this DeploymentRequestCreateResponse
        :rtype: str
        """

        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeploymentRequestCreateResponse

        :param id: the id of this DeploymentRequestCreateResponse
        :type: str
        """

        if self.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        if self.client_side_validation and (id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")

        self._id = id

    @property
    def deployment(self):
        """
        Gets the deployment of this DeploymentRequestCreateResponse

        :return: the deployment of this DeploymentRequestCreateResponse
        :rtype: str
        """

        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """
        Sets the deployment of this DeploymentRequestCreateResponse

        :param deployment: the deployment of this DeploymentRequestCreateResponse
        :type: str
        """

        if self.client_side_validation and (deployment is not None and not isinstance(deployment, str)):
            raise ValueError("Parameter `deployment` must be a string")

        self._deployment = deployment

    @property
    def version(self):
        """
        Gets the version of this DeploymentRequestCreateResponse

        :return: the version of this DeploymentRequestCreateResponse
        :rtype: str
        """

        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DeploymentRequestCreateResponse

        :param version: the version of this DeploymentRequestCreateResponse
        :type: str
        """

        if self.client_side_validation and (version is not None and not isinstance(version, str)):
            raise ValueError("Parameter `version` must be a string")

        self._version = version

    @property
    def status(self):
        """
        Gets the status of this DeploymentRequestCreateResponse

        :return: the status of this DeploymentRequestCreateResponse
        :rtype: str
        """

        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DeploymentRequestCreateResponse

        :param status: the status of this DeploymentRequestCreateResponse
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
        Gets the success of this DeploymentRequestCreateResponse

        :return: the success of this DeploymentRequestCreateResponse
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
        Sets the success of this DeploymentRequestCreateResponse

        :param success: the success of this DeploymentRequestCreateResponse
        :type: bool
        """

        if self.client_side_validation and (success is not None and not isinstance(success, bool)):
            raise ValueError("Parameter `success` must be a boolean")

        self._success = success

    @property
    def result(self):
        """
        Gets the result of this DeploymentRequestCreateResponse

        :return: the result of this DeploymentRequestCreateResponse
        :rtype: object
        """

        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this DeploymentRequestCreateResponse

        :param result: the result of this DeploymentRequestCreateResponse
        :type: object
        """

        self._result = result

    @property
    def error_message(self):
        """
        Gets the error_message of this DeploymentRequestCreateResponse

        :return: the error_message of this DeploymentRequestCreateResponse
        :rtype: str
        """

        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this DeploymentRequestCreateResponse

        :param error_message: the error_message of this DeploymentRequestCreateResponse
        :type: str
        """

        if self.client_side_validation and (error_message is not None and not isinstance(error_message, str)):
            raise ValueError("Parameter `error_message` must be a string")

        self._error_message = error_message

    @property
    def timeout(self):
        """
        Gets the timeout of this DeploymentRequestCreateResponse

        :return: the timeout of this DeploymentRequestCreateResponse
        :rtype: int
        """

        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """
        Sets the timeout of this DeploymentRequestCreateResponse

        :param timeout: the timeout of this DeploymentRequestCreateResponse
        :type: int
        """

        if self.client_side_validation and (timeout is not None and not isinstance(timeout, int)):
            raise ValueError("Parameter `timeout` must be an integer")

        self._timeout = timeout

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

        if not isinstance(other, DeploymentRequestCreateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, DeploymentRequestCreateResponse):
            return True

        return self.to_dict() != other.to_dict()

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


class PipelineRequestSingleDetail(object):
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
        'pipeline': 'str',
        'version': 'str',
        'status': 'str',
        'success': 'bool',
        'time_created': 'datetime',
        'time_started': 'datetime',
        'time_completed': 'datetime',
        'request_data': 'object',
        'result': 'object',
        'deployment_requests': 'list[PipelineRequestDeploymentRequest]',
        'operator_requests': 'list[PipelineRequestOperatorRequest]',
        'error_message': 'str',
        'notification_group': 'str',
        'origin': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'pipeline': 'pipeline',
        'version': 'version',
        'status': 'status',
        'success': 'success',
        'time_created': 'time_created',
        'time_started': 'time_started',
        'time_completed': 'time_completed',
        'request_data': 'request_data',
        'result': 'result',
        'deployment_requests': 'deployment_requests',
        'operator_requests': 'operator_requests',
        'error_message': 'error_message',
        'notification_group': 'notification_group',
        'origin': 'origin'
    }

    def __init__(self, id=None, pipeline=None, version=None, status=None, success=None, time_created=None, time_started=None, time_completed=None, request_data=None, result=None, deployment_requests=None, operator_requests=None, error_message=None, notification_group=None, origin=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """PipelineRequestSingleDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._pipeline = None
        self._version = None
        self._status = None
        self._success = None
        self._time_created = None
        self._time_started = None
        self._time_completed = None
        self._request_data = None
        self._result = None
        self._deployment_requests = None
        self._operator_requests = None
        self._error_message = None
        self._notification_group = None
        self._origin = None
        self.discriminator = None

        self.id = id
        self.pipeline = pipeline
        self.version = version
        self.status = status
        self.success = success
        self.time_created = time_created
        self.time_started = time_started
        self.time_completed = time_completed
        self.request_data = request_data
        self.result = result
        self.deployment_requests = deployment_requests
        self.operator_requests = operator_requests
        self.error_message = error_message
        self.notification_group = notification_group
        self.origin = origin

    @property
    def id(self):
        """Gets the id of this PipelineRequestSingleDetail.  # noqa: E501


        :return: The id of this PipelineRequestSingleDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PipelineRequestSingleDetail.


        :param id: The id of this PipelineRequestSingleDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")  # noqa: E501

        self._id = id

    @property
    def pipeline(self):
        """Gets the pipeline of this PipelineRequestSingleDetail.  # noqa: E501


        :return: The pipeline of this PipelineRequestSingleDetail.  # noqa: E501
        :rtype: str
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """Sets the pipeline of this PipelineRequestSingleDetail.


        :param pipeline: The pipeline of this PipelineRequestSingleDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pipeline is not None and not isinstance(pipeline, str)):
            raise ValueError("Parameter `pipeline` must be a string")  # noqa: E501

        self._pipeline = pipeline

    @property
    def version(self):
        """Gets the version of this PipelineRequestSingleDetail.  # noqa: E501


        :return: The version of this PipelineRequestSingleDetail.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PipelineRequestSingleDetail.


        :param version: The version of this PipelineRequestSingleDetail.  # noqa: E501
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
    def status(self):
        """Gets the status of this PipelineRequestSingleDetail.  # noqa: E501


        :return: The status of this PipelineRequestSingleDetail.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PipelineRequestSingleDetail.


        :param status: The status of this PipelineRequestSingleDetail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status is not None and not isinstance(status, str)):
            raise ValueError("Parameter `status` must be a string")  # noqa: E501
        allowed_values = ["pending", "processing", "completed", "failed", "cancelled_pending", "cancelled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def success(self):
        """Gets the success of this PipelineRequestSingleDetail.  # noqa: E501


        :return: The success of this PipelineRequestSingleDetail.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this PipelineRequestSingleDetail.


        :param success: The success of this PipelineRequestSingleDetail.  # noqa: E501
        :type: bool
        """
        if (self.local_vars_configuration.client_side_validation and
                success is not None and not isinstance(success, bool)):
            raise ValueError("Parameter `success` must be a boolean")  # noqa: E501

        self._success = success

    @property
    def time_created(self):
        """Gets the time_created of this PipelineRequestSingleDetail.  # noqa: E501


        :return: The time_created of this PipelineRequestSingleDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this PipelineRequestSingleDetail.


        :param time_created: The time_created of this PipelineRequestSingleDetail.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and time_created is None:  # noqa: E501
            raise ValueError("Invalid value for `time_created`, must not be `None`")  # noqa: E501

        self._time_created = time_created

    @property
    def time_started(self):
        """Gets the time_started of this PipelineRequestSingleDetail.  # noqa: E501


        :return: The time_started of this PipelineRequestSingleDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """Sets the time_started of this PipelineRequestSingleDetail.


        :param time_started: The time_started of this PipelineRequestSingleDetail.  # noqa: E501
        :type: datetime
        """

        self._time_started = time_started

    @property
    def time_completed(self):
        """Gets the time_completed of this PipelineRequestSingleDetail.  # noqa: E501


        :return: The time_completed of this PipelineRequestSingleDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._time_completed

    @time_completed.setter
    def time_completed(self, time_completed):
        """Sets the time_completed of this PipelineRequestSingleDetail.


        :param time_completed: The time_completed of this PipelineRequestSingleDetail.  # noqa: E501
        :type: datetime
        """

        self._time_completed = time_completed

    @property
    def request_data(self):
        """Gets the request_data of this PipelineRequestSingleDetail.  # noqa: E501


        :return: The request_data of this PipelineRequestSingleDetail.  # noqa: E501
        :rtype: object
        """
        return self._request_data

    @request_data.setter
    def request_data(self, request_data):
        """Sets the request_data of this PipelineRequestSingleDetail.


        :param request_data: The request_data of this PipelineRequestSingleDetail.  # noqa: E501
        :type: object
        """

        self._request_data = request_data

    @property
    def result(self):
        """Gets the result of this PipelineRequestSingleDetail.  # noqa: E501


        :return: The result of this PipelineRequestSingleDetail.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this PipelineRequestSingleDetail.


        :param result: The result of this PipelineRequestSingleDetail.  # noqa: E501
        :type: object
        """

        self._result = result

    @property
    def deployment_requests(self):
        """Gets the deployment_requests of this PipelineRequestSingleDetail.  # noqa: E501


        :return: The deployment_requests of this PipelineRequestSingleDetail.  # noqa: E501
        :rtype: list[PipelineRequestDeploymentRequest]
        """
        return self._deployment_requests

    @deployment_requests.setter
    def deployment_requests(self, deployment_requests):
        """Sets the deployment_requests of this PipelineRequestSingleDetail.


        :param deployment_requests: The deployment_requests of this PipelineRequestSingleDetail.  # noqa: E501
        :type: list[PipelineRequestDeploymentRequest]
        """
        if (self.local_vars_configuration.client_side_validation and
                deployment_requests is not None and not isinstance(deployment_requests, list)):
            raise ValueError("Parameter `deployment_requests` must be a list")  # noqa: E501
        if self.local_vars_configuration.client_side_validation and deployment_requests is not None:
            from ubiops.models.pipeline_request_deployment_request import PipelineRequestDeploymentRequest

            deployment_requests = [
                PipelineRequestDeploymentRequest(**item) if isinstance(item, dict) else item  # noqa: E501
                for item in deployment_requests
            ]

        self._deployment_requests = deployment_requests

    @property
    def operator_requests(self):
        """Gets the operator_requests of this PipelineRequestSingleDetail.  # noqa: E501


        :return: The operator_requests of this PipelineRequestSingleDetail.  # noqa: E501
        :rtype: list[PipelineRequestOperatorRequest]
        """
        return self._operator_requests

    @operator_requests.setter
    def operator_requests(self, operator_requests):
        """Sets the operator_requests of this PipelineRequestSingleDetail.


        :param operator_requests: The operator_requests of this PipelineRequestSingleDetail.  # noqa: E501
        :type: list[PipelineRequestOperatorRequest]
        """
        if (self.local_vars_configuration.client_side_validation and
                operator_requests is not None and not isinstance(operator_requests, list)):
            raise ValueError("Parameter `operator_requests` must be a list")  # noqa: E501
        if self.local_vars_configuration.client_side_validation and operator_requests is not None:
            from ubiops.models.pipeline_request_operator_request import PipelineRequestOperatorRequest

            operator_requests = [
                PipelineRequestOperatorRequest(**item) if isinstance(item, dict) else item  # noqa: E501
                for item in operator_requests
            ]

        self._operator_requests = operator_requests

    @property
    def error_message(self):
        """Gets the error_message of this PipelineRequestSingleDetail.  # noqa: E501


        :return: The error_message of this PipelineRequestSingleDetail.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this PipelineRequestSingleDetail.


        :param error_message: The error_message of this PipelineRequestSingleDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                error_message is not None and not isinstance(error_message, str)):
            raise ValueError("Parameter `error_message` must be a string")  # noqa: E501

        self._error_message = error_message

    @property
    def notification_group(self):
        """Gets the notification_group of this PipelineRequestSingleDetail.  # noqa: E501


        :return: The notification_group of this PipelineRequestSingleDetail.  # noqa: E501
        :rtype: str
        """
        return self._notification_group

    @notification_group.setter
    def notification_group(self, notification_group):
        """Sets the notification_group of this PipelineRequestSingleDetail.


        :param notification_group: The notification_group of this PipelineRequestSingleDetail.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                notification_group is not None and not isinstance(notification_group, str)):
            raise ValueError("Parameter `notification_group` must be a string")  # noqa: E501

        self._notification_group = notification_group

    @property
    def origin(self):
        """Gets the origin of this PipelineRequestSingleDetail.  # noqa: E501


        :return: The origin of this PipelineRequestSingleDetail.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this PipelineRequestSingleDetail.


        :param origin: The origin of this PipelineRequestSingleDetail.  # noqa: E501
        :type: dict(str, str)
        """
        if (self.local_vars_configuration.client_side_validation and
                origin is not None and not isinstance(origin, dict)):
            raise ValueError("Parameter `origin` must be a dictionary")  # noqa: E501

        self._origin = origin

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
        if not isinstance(other, PipelineRequestSingleDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PipelineRequestSingleDetail):
            return True

        return self.to_dict() != other.to_dict()

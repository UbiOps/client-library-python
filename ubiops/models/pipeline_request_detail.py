# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import warnings


class PipelineRequestDetail(object):
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
        "pipeline": "str",
        "version": "str",
        "status": "str",
        "success": "bool",
        "time_created": "datetime",
        "time_started": "datetime",
        "time_completed": "datetime",
        "request_data": "object",
        "result": "object",
        "deployment_requests": "list[PipelineRequestDeploymentRequest]",
        "operator_requests": "list[PipelineRequestOperatorRequest]",
        "pipeline_requests": "list[PipelineRequestPipelineRequest]",
        "error_message": "str",
        "pipeline_timeout": "int",
        "deployment_timeout": "int",
        "input_size": "int",
        "output_size": "int",
    }

    attribute_map = {
        "id": "id",
        "pipeline": "pipeline",
        "version": "version",
        "status": "status",
        "success": "success",
        "time_created": "time_created",
        "time_started": "time_started",
        "time_completed": "time_completed",
        "request_data": "request_data",
        "result": "result",
        "deployment_requests": "deployment_requests",
        "operator_requests": "operator_requests",
        "pipeline_requests": "pipeline_requests",
        "error_message": "error_message",
        "pipeline_timeout": "pipeline_timeout",
        "deployment_timeout": "deployment_timeout",
        "input_size": "input_size",
        "output_size": "output_size",
    }

    def __init__(
        self,
        id=None,
        pipeline=None,
        version=None,
        status=None,
        success=None,
        time_created=None,
        time_started=None,
        time_completed=None,
        request_data=None,
        result=None,
        deployment_requests=None,
        operator_requests=None,
        pipeline_requests=None,
        error_message=None,
        pipeline_timeout=None,
        deployment_timeout=None,
        input_size=None,
        output_size=None,
        **kwargs,
    ):
        """
        PipelineRequestDetail - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

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
        self._pipeline_requests = None
        self._error_message = None
        self._pipeline_timeout = None
        self._deployment_timeout = None
        self._input_size = None
        self._output_size = None
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
        self.pipeline_requests = pipeline_requests
        self.error_message = error_message
        self.pipeline_timeout = pipeline_timeout
        self.deployment_timeout = deployment_timeout
        self.input_size = input_size
        self.output_size = output_size

    @property
    def id(self):
        """
        Gets the id of this PipelineRequestDetail

        :return: the id of this PipelineRequestDetail
        :rtype: str
        """

        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PipelineRequestDetail

        :param id: the id of this PipelineRequestDetail
        :type: str
        """

        if self.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        if self.client_side_validation and (id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")

        self._id = id

    @property
    def pipeline(self):
        """
        Gets the pipeline of this PipelineRequestDetail

        :return: the pipeline of this PipelineRequestDetail
        :rtype: str
        """

        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """
        Sets the pipeline of this PipelineRequestDetail

        :param pipeline: the pipeline of this PipelineRequestDetail
        :type: str
        """

        if self.client_side_validation and (pipeline is not None and not isinstance(pipeline, str)):
            raise ValueError("Parameter `pipeline` must be a string")

        self._pipeline = pipeline

    @property
    def version(self):
        """
        Gets the version of this PipelineRequestDetail

        :return: the version of this PipelineRequestDetail
        :rtype: str
        """

        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PipelineRequestDetail

        :param version: the version of this PipelineRequestDetail
        :type: str
        """

        if self.client_side_validation and (version is not None and not isinstance(version, str)):
            raise ValueError("Parameter `version` must be a string")

        if self.client_side_validation and (version is not None and len(version) < 1):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")

        self._version = version

    @property
    def status(self):
        """
        Gets the status of this PipelineRequestDetail

        :return: the status of this PipelineRequestDetail
        :rtype: str
        """

        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PipelineRequestDetail

        :param status: the status of this PipelineRequestDetail
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
        Gets the success of this PipelineRequestDetail

        :return: the success of this PipelineRequestDetail
        :rtype: bool
        """
        warnings.warn(
            message="success is deprecated and will be removed after October 2024. Use status instead.",
            category=DeprecationWarning,
            stacklevel=2,
        )

        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this PipelineRequestDetail

        :param success: the success of this PipelineRequestDetail
        :type: bool
        """

        if self.client_side_validation and (success is not None and not isinstance(success, bool)):
            raise ValueError("Parameter `success` must be a boolean")

        self._success = success

    @property
    def time_created(self):
        """
        Gets the time_created of this PipelineRequestDetail

        :return: the time_created of this PipelineRequestDetail
        :rtype: datetime
        """

        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PipelineRequestDetail

        :param time_created: the time_created of this PipelineRequestDetail
        :type: datetime
        """

        if self.client_side_validation and time_created is None:
            raise ValueError("Invalid value for `time_created`, must not be `None`")

        self._time_created = time_created

    @property
    def time_started(self):
        """
        Gets the time_started of this PipelineRequestDetail

        :return: the time_started of this PipelineRequestDetail
        :rtype: datetime
        """

        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this PipelineRequestDetail

        :param time_started: the time_started of this PipelineRequestDetail
        :type: datetime
        """

        self._time_started = time_started

    @property
    def time_completed(self):
        """
        Gets the time_completed of this PipelineRequestDetail

        :return: the time_completed of this PipelineRequestDetail
        :rtype: datetime
        """

        return self._time_completed

    @time_completed.setter
    def time_completed(self, time_completed):
        """
        Sets the time_completed of this PipelineRequestDetail

        :param time_completed: the time_completed of this PipelineRequestDetail
        :type: datetime
        """

        self._time_completed = time_completed

    @property
    def request_data(self):
        """
        Gets the request_data of this PipelineRequestDetail

        :return: the request_data of this PipelineRequestDetail
        :rtype: object
        """

        return self._request_data

    @request_data.setter
    def request_data(self, request_data):
        """
        Sets the request_data of this PipelineRequestDetail

        :param request_data: the request_data of this PipelineRequestDetail
        :type: object
        """

        self._request_data = request_data

    @property
    def result(self):
        """
        Gets the result of this PipelineRequestDetail

        :return: the result of this PipelineRequestDetail
        :rtype: object
        """

        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this PipelineRequestDetail

        :param result: the result of this PipelineRequestDetail
        :type: object
        """

        self._result = result

    @property
    def deployment_requests(self):
        """
        Gets the deployment_requests of this PipelineRequestDetail

        :return: the deployment_requests of this PipelineRequestDetail
        :rtype: list[PipelineRequestDeploymentRequest]
        """

        return self._deployment_requests

    @deployment_requests.setter
    def deployment_requests(self, deployment_requests):
        """
        Sets the deployment_requests of this PipelineRequestDetail

        :param deployment_requests: the deployment_requests of this PipelineRequestDetail
        :type: list[PipelineRequestDeploymentRequest]
        """

        if self.client_side_validation and (
            deployment_requests is not None and not isinstance(deployment_requests, list)
        ):
            raise ValueError("Parameter `deployment_requests` must be a list")
        if self.client_side_validation and deployment_requests is not None:
            from ubiops.models.pipeline_request_deployment_request import PipelineRequestDeploymentRequest

            deployment_requests = [
                PipelineRequestDeploymentRequest(**item) if isinstance(item, dict) else item
                for item in deployment_requests
            ]

        self._deployment_requests = deployment_requests

    @property
    def operator_requests(self):
        """
        Gets the operator_requests of this PipelineRequestDetail

        :return: the operator_requests of this PipelineRequestDetail
        :rtype: list[PipelineRequestOperatorRequest]
        """

        return self._operator_requests

    @operator_requests.setter
    def operator_requests(self, operator_requests):
        """
        Sets the operator_requests of this PipelineRequestDetail

        :param operator_requests: the operator_requests of this PipelineRequestDetail
        :type: list[PipelineRequestOperatorRequest]
        """

        if self.client_side_validation and (operator_requests is not None and not isinstance(operator_requests, list)):
            raise ValueError("Parameter `operator_requests` must be a list")
        if self.client_side_validation and operator_requests is not None:
            from ubiops.models.pipeline_request_operator_request import PipelineRequestOperatorRequest

            operator_requests = [
                PipelineRequestOperatorRequest(**item) if isinstance(item, dict) else item for item in operator_requests
            ]

        self._operator_requests = operator_requests

    @property
    def pipeline_requests(self):
        """
        Gets the pipeline_requests of this PipelineRequestDetail

        :return: the pipeline_requests of this PipelineRequestDetail
        :rtype: list[PipelineRequestPipelineRequest]
        """

        return self._pipeline_requests

    @pipeline_requests.setter
    def pipeline_requests(self, pipeline_requests):
        """
        Sets the pipeline_requests of this PipelineRequestDetail

        :param pipeline_requests: the pipeline_requests of this PipelineRequestDetail
        :type: list[PipelineRequestPipelineRequest]
        """

        if self.client_side_validation and (pipeline_requests is not None and not isinstance(pipeline_requests, list)):
            raise ValueError("Parameter `pipeline_requests` must be a list")
        if self.client_side_validation and pipeline_requests is not None:
            from ubiops.models.pipeline_request_pipeline_request import PipelineRequestPipelineRequest

            pipeline_requests = [
                PipelineRequestPipelineRequest(**item) if isinstance(item, dict) else item for item in pipeline_requests
            ]

        self._pipeline_requests = pipeline_requests

    @property
    def error_message(self):
        """
        Gets the error_message of this PipelineRequestDetail

        :return: the error_message of this PipelineRequestDetail
        :rtype: str
        """

        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this PipelineRequestDetail

        :param error_message: the error_message of this PipelineRequestDetail
        :type: str
        """

        if self.client_side_validation and (error_message is not None and not isinstance(error_message, str)):
            raise ValueError("Parameter `error_message` must be a string")

        self._error_message = error_message

    @property
    def pipeline_timeout(self):
        """
        Gets the pipeline_timeout of this PipelineRequestDetail

        :return: the pipeline_timeout of this PipelineRequestDetail
        :rtype: int
        """

        return self._pipeline_timeout

    @pipeline_timeout.setter
    def pipeline_timeout(self, pipeline_timeout):
        """
        Sets the pipeline_timeout of this PipelineRequestDetail

        :param pipeline_timeout: the pipeline_timeout of this PipelineRequestDetail
        :type: int
        """

        if self.client_side_validation and (pipeline_timeout is not None and not isinstance(pipeline_timeout, int)):
            raise ValueError("Parameter `pipeline_timeout` must be an integer")

        self._pipeline_timeout = pipeline_timeout

    @property
    def deployment_timeout(self):
        """
        Gets the deployment_timeout of this PipelineRequestDetail

        :return: the deployment_timeout of this PipelineRequestDetail
        :rtype: int
        """

        return self._deployment_timeout

    @deployment_timeout.setter
    def deployment_timeout(self, deployment_timeout):
        """
        Sets the deployment_timeout of this PipelineRequestDetail

        :param deployment_timeout: the deployment_timeout of this PipelineRequestDetail
        :type: int
        """

        if self.client_side_validation and (deployment_timeout is not None and not isinstance(deployment_timeout, int)):
            raise ValueError("Parameter `deployment_timeout` must be an integer")

        self._deployment_timeout = deployment_timeout

    @property
    def input_size(self):
        """
        Gets the input_size of this PipelineRequestDetail

        :return: the input_size of this PipelineRequestDetail
        :rtype: int
        """

        return self._input_size

    @input_size.setter
    def input_size(self, input_size):
        """
        Sets the input_size of this PipelineRequestDetail

        :param input_size: the input_size of this PipelineRequestDetail
        :type: int
        """

        if self.client_side_validation and (input_size is not None and not isinstance(input_size, int)):
            raise ValueError("Parameter `input_size` must be an integer")

        self._input_size = input_size

    @property
    def output_size(self):
        """
        Gets the output_size of this PipelineRequestDetail

        :return: the output_size of this PipelineRequestDetail
        :rtype: int
        """

        return self._output_size

    @output_size.setter
    def output_size(self, output_size):
        """
        Sets the output_size of this PipelineRequestDetail

        :param output_size: the output_size of this PipelineRequestDetail
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

        if not isinstance(other, PipelineRequestDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, PipelineRequestDetail):
            return True

        return self.to_dict() != other.to_dict()

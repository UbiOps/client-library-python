# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import warnings


class PipelineRequestList(object):
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
        input_size=None,
        output_size=None,
        **kwargs,
    ):
        """
        PipelineRequestList - a model defined in OpenAPI
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
        self.input_size = input_size
        self.output_size = output_size

    @property
    def id(self):
        """
        Gets the id of this PipelineRequestList

        :return: the id of this PipelineRequestList
        :rtype: str
        """

        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PipelineRequestList

        :param id: the id of this PipelineRequestList
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
        Gets the pipeline of this PipelineRequestList

        :return: the pipeline of this PipelineRequestList
        :rtype: str
        """

        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """
        Sets the pipeline of this PipelineRequestList

        :param pipeline: the pipeline of this PipelineRequestList
        :type: str
        """

        if self.client_side_validation and (pipeline is not None and not isinstance(pipeline, str)):
            raise ValueError("Parameter `pipeline` must be a string")

        self._pipeline = pipeline

    @property
    def version(self):
        """
        Gets the version of this PipelineRequestList

        :return: the version of this PipelineRequestList
        :rtype: str
        """

        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PipelineRequestList

        :param version: the version of this PipelineRequestList
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
        Gets the status of this PipelineRequestList

        :return: the status of this PipelineRequestList
        :rtype: str
        """

        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PipelineRequestList

        :param status: the status of this PipelineRequestList
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
        Gets the success of this PipelineRequestList

        :return: the success of this PipelineRequestList
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
        Sets the success of this PipelineRequestList

        :param success: the success of this PipelineRequestList
        :type: bool
        """

        if self.client_side_validation and (success is not None and not isinstance(success, bool)):
            raise ValueError("Parameter `success` must be a boolean")

        self._success = success

    @property
    def time_created(self):
        """
        Gets the time_created of this PipelineRequestList

        :return: the time_created of this PipelineRequestList
        :rtype: datetime
        """

        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PipelineRequestList

        :param time_created: the time_created of this PipelineRequestList
        :type: datetime
        """

        if self.client_side_validation and time_created is None:
            raise ValueError("Invalid value for `time_created`, must not be `None`")

        self._time_created = time_created

    @property
    def time_started(self):
        """
        Gets the time_started of this PipelineRequestList

        :return: the time_started of this PipelineRequestList
        :rtype: datetime
        """

        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this PipelineRequestList

        :param time_started: the time_started of this PipelineRequestList
        :type: datetime
        """

        self._time_started = time_started

    @property
    def time_completed(self):
        """
        Gets the time_completed of this PipelineRequestList

        :return: the time_completed of this PipelineRequestList
        :rtype: datetime
        """

        return self._time_completed

    @time_completed.setter
    def time_completed(self, time_completed):
        """
        Sets the time_completed of this PipelineRequestList

        :param time_completed: the time_completed of this PipelineRequestList
        :type: datetime
        """

        self._time_completed = time_completed

    @property
    def input_size(self):
        """
        Gets the input_size of this PipelineRequestList

        :return: the input_size of this PipelineRequestList
        :rtype: int
        """

        return self._input_size

    @input_size.setter
    def input_size(self, input_size):
        """
        Sets the input_size of this PipelineRequestList

        :param input_size: the input_size of this PipelineRequestList
        :type: int
        """

        if self.client_side_validation and (input_size is not None and not isinstance(input_size, int)):
            raise ValueError("Parameter `input_size` must be an integer")

        self._input_size = input_size

    @property
    def output_size(self):
        """
        Gets the output_size of this PipelineRequestList

        :return: the output_size of this PipelineRequestList
        :rtype: int
        """

        return self._output_size

    @output_size.setter
    def output_size(self, output_size):
        """
        Sets the output_size of this PipelineRequestList

        :param output_size: the output_size of this PipelineRequestList
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

        if not isinstance(other, PipelineRequestList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, PipelineRequestList):
            return True

        return self.to_dict() != other.to_dict()

# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class RequestsOverview(object):
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
        "pipeline": "str",
        "version": "str",
        "status": "str",
        "time_created": "datetime",
        "time_started": "datetime",
        "time_completed": "datetime",
        "input_size": "int",
        "output_size": "int",
    }

    attribute_map = {
        "id": "id",
        "deployment": "deployment",
        "pipeline": "pipeline",
        "version": "version",
        "status": "status",
        "time_created": "time_created",
        "time_started": "time_started",
        "time_completed": "time_completed",
        "input_size": "input_size",
        "output_size": "output_size",
    }

    def __init__(
        self,
        id=None,
        deployment=None,
        pipeline=None,
        version=None,
        status=None,
        time_created=None,
        time_started=None,
        time_completed=None,
        input_size=None,
        output_size=None,
        **kwargs,
    ):
        """
        RequestsOverview - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._id = None
        self._deployment = None
        self._pipeline = None
        self._version = None
        self._status = None
        self._time_created = None
        self._time_started = None
        self._time_completed = None
        self._input_size = None
        self._output_size = None
        self.discriminator = None

        self.id = id
        self.deployment = deployment
        self.pipeline = pipeline
        self.version = version
        self.status = status
        self.time_created = time_created
        self.time_started = time_started
        self.time_completed = time_completed
        self.input_size = input_size
        self.output_size = output_size

    @property
    def id(self):
        """
        Gets the id of this RequestsOverview

        :return: the id of this RequestsOverview
        :rtype: str
        """

        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RequestsOverview

        :param id: the id of this RequestsOverview
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
        Gets the deployment of this RequestsOverview

        :return: the deployment of this RequestsOverview
        :rtype: str
        """

        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """
        Sets the deployment of this RequestsOverview

        :param deployment: the deployment of this RequestsOverview
        :type: str
        """

        if self.client_side_validation and (deployment is not None and not isinstance(deployment, str)):
            raise ValueError("Parameter `deployment` must be a string")

        self._deployment = deployment

    @property
    def pipeline(self):
        """
        Gets the pipeline of this RequestsOverview

        :return: the pipeline of this RequestsOverview
        :rtype: str
        """

        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """
        Sets the pipeline of this RequestsOverview

        :param pipeline: the pipeline of this RequestsOverview
        :type: str
        """

        if self.client_side_validation and (pipeline is not None and not isinstance(pipeline, str)):
            raise ValueError("Parameter `pipeline` must be a string")

        self._pipeline = pipeline

    @property
    def version(self):
        """
        Gets the version of this RequestsOverview

        :return: the version of this RequestsOverview
        :rtype: str
        """

        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this RequestsOverview

        :param version: the version of this RequestsOverview
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
        Gets the status of this RequestsOverview

        :return: the status of this RequestsOverview
        :rtype: str
        """

        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this RequestsOverview

        :param status: the status of this RequestsOverview
        :type: str
        """

        if self.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        if self.client_side_validation and (status is not None and not isinstance(status, str)):
            raise ValueError("Parameter `status` must be a string")

        self._status = status

    @property
    def time_created(self):
        """
        Gets the time_created of this RequestsOverview

        :return: the time_created of this RequestsOverview
        :rtype: datetime
        """

        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RequestsOverview

        :param time_created: the time_created of this RequestsOverview
        :type: datetime
        """

        if self.client_side_validation and time_created is None:
            raise ValueError("Invalid value for `time_created`, must not be `None`")

        self._time_created = time_created

    @property
    def time_started(self):
        """
        Gets the time_started of this RequestsOverview

        :return: the time_started of this RequestsOverview
        :rtype: datetime
        """

        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this RequestsOverview

        :param time_started: the time_started of this RequestsOverview
        :type: datetime
        """

        self._time_started = time_started

    @property
    def time_completed(self):
        """
        Gets the time_completed of this RequestsOverview

        :return: the time_completed of this RequestsOverview
        :rtype: datetime
        """

        return self._time_completed

    @time_completed.setter
    def time_completed(self, time_completed):
        """
        Sets the time_completed of this RequestsOverview

        :param time_completed: the time_completed of this RequestsOverview
        :type: datetime
        """

        self._time_completed = time_completed

    @property
    def input_size(self):
        """
        Gets the input_size of this RequestsOverview

        :return: the input_size of this RequestsOverview
        :rtype: int
        """

        return self._input_size

    @input_size.setter
    def input_size(self, input_size):
        """
        Sets the input_size of this RequestsOverview

        :param input_size: the input_size of this RequestsOverview
        :type: int
        """

        if self.client_side_validation and (input_size is not None and not isinstance(input_size, int)):
            raise ValueError("Parameter `input_size` must be an integer")

        self._input_size = input_size

    @property
    def output_size(self):
        """
        Gets the output_size of this RequestsOverview

        :return: the output_size of this RequestsOverview
        :rtype: int
        """

        return self._output_size

    @output_size.setter
    def output_size(self, output_size):
        """
        Sets the output_size of this RequestsOverview

        :param output_size: the output_size of this RequestsOverview
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

        if not isinstance(other, RequestsOverview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, RequestsOverview):
            return True

        return self.to_dict() != other.to_dict()

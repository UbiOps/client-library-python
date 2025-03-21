# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class PipelineVersionCreate(object):
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
        "version": "str",
        "description": "str",
        "labels": "dict(str, str)",
        "request_retention_time": "int",
        "request_retention_mode": "str",
        "objects": "list[PipelineVersionObjectCreate]",
        "attachments": "list[AttachmentsCreate]",
    }

    attribute_map = {
        "version": "version",
        "description": "description",
        "labels": "labels",
        "request_retention_time": "request_retention_time",
        "request_retention_mode": "request_retention_mode",
        "objects": "objects",
        "attachments": "attachments",
    }

    def __init__(
        self,
        version=None,
        description=None,
        labels=None,
        request_retention_time=None,
        request_retention_mode=None,
        objects=None,
        attachments=None,
        **kwargs,
    ):
        """
        PipelineVersionCreate - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._version = None
        self._description = None
        self._labels = None
        self._request_retention_time = None
        self._request_retention_mode = None
        self._objects = None
        self._attachments = None
        self.discriminator = None

        self.version = version
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        if request_retention_time is not None:
            self.request_retention_time = request_retention_time
        if request_retention_mode is not None:
            self.request_retention_mode = request_retention_mode
        if objects is not None:
            self.objects = objects
        if attachments is not None:
            self.attachments = attachments

    @property
    def version(self):
        """
        Gets the version of this PipelineVersionCreate

        :return: the version of this PipelineVersionCreate
        :rtype: str
        """

        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PipelineVersionCreate

        :param version: the version of this PipelineVersionCreate
        :type: str
        """

        if self.client_side_validation and version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")
        if self.client_side_validation and (version is not None and not isinstance(version, str)):
            raise ValueError("Parameter `version` must be a string")

        if self.client_side_validation and (version is not None and len(version) < 1):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")

        self._version = version

    @property
    def description(self):
        """
        Gets the description of this PipelineVersionCreate

        :return: the description of this PipelineVersionCreate
        :rtype: str
        """

        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PipelineVersionCreate

        :param description: the description of this PipelineVersionCreate
        :type: str
        """

        if self.client_side_validation and (description is not None and not isinstance(description, str)):
            raise ValueError("Parameter `description` must be a string")

        if self.client_side_validation and (description is not None and len(description) > 400):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `400`")

        self._description = description

    @property
    def labels(self):
        """
        Gets the labels of this PipelineVersionCreate

        :return: the labels of this PipelineVersionCreate
        :rtype: dict(str, str)
        """

        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this PipelineVersionCreate

        :param labels: the labels of this PipelineVersionCreate
        :type: dict(str, str)
        """

        if self.client_side_validation and (labels is not None and not isinstance(labels, dict)):
            raise ValueError("Parameter `labels` must be a dictionary")

        self._labels = labels

    @property
    def request_retention_time(self):
        """
        Gets the request_retention_time of this PipelineVersionCreate

        :return: the request_retention_time of this PipelineVersionCreate
        :rtype: int
        """

        return self._request_retention_time

    @request_retention_time.setter
    def request_retention_time(self, request_retention_time):
        """
        Sets the request_retention_time of this PipelineVersionCreate

        :param request_retention_time: the request_retention_time of this PipelineVersionCreate
        :type: int
        """

        if self.client_side_validation and (
            request_retention_time is not None and not isinstance(request_retention_time, int)
        ):
            raise ValueError("Parameter `request_retention_time` must be an integer")

        self._request_retention_time = request_retention_time

    @property
    def request_retention_mode(self):
        """
        Gets the request_retention_mode of this PipelineVersionCreate

        :return: the request_retention_mode of this PipelineVersionCreate
        :rtype: str
        """

        return self._request_retention_mode

    @request_retention_mode.setter
    def request_retention_mode(self, request_retention_mode):
        """
        Sets the request_retention_mode of this PipelineVersionCreate

        :param request_retention_mode: the request_retention_mode of this PipelineVersionCreate
        :type: str
        """

        if self.client_side_validation and (
            request_retention_mode is not None and not isinstance(request_retention_mode, str)
        ):
            raise ValueError("Parameter `request_retention_mode` must be a string")

        self._request_retention_mode = request_retention_mode

    @property
    def objects(self):
        """
        Gets the objects of this PipelineVersionCreate

        :return: the objects of this PipelineVersionCreate
        :rtype: list[PipelineVersionObjectCreate]
        """

        return self._objects

    @objects.setter
    def objects(self, objects):
        """
        Sets the objects of this PipelineVersionCreate

        :param objects: the objects of this PipelineVersionCreate
        :type: list[PipelineVersionObjectCreate]
        """

        if self.client_side_validation and (objects is not None and not isinstance(objects, list)):
            raise ValueError("Parameter `objects` must be a list")
        if self.client_side_validation and objects is not None:
            from ubiops.models.pipeline_version_object_create import PipelineVersionObjectCreate

            objects = [PipelineVersionObjectCreate(**item) if isinstance(item, dict) else item for item in objects]

        self._objects = objects

    @property
    def attachments(self):
        """
        Gets the attachments of this PipelineVersionCreate

        :return: the attachments of this PipelineVersionCreate
        :rtype: list[AttachmentsCreate]
        """

        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this PipelineVersionCreate

        :param attachments: the attachments of this PipelineVersionCreate
        :type: list[AttachmentsCreate]
        """

        if self.client_side_validation and (attachments is not None and not isinstance(attachments, list)):
            raise ValueError("Parameter `attachments` must be a list")
        if self.client_side_validation and attachments is not None:
            from ubiops.models.attachments_create import AttachmentsCreate

            attachments = [AttachmentsCreate(**item) if isinstance(item, dict) else item for item in attachments]

        self._attachments = attachments

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

        if not isinstance(other, PipelineVersionCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, PipelineVersionCreate):
            return True

        return self.to_dict() != other.to_dict()

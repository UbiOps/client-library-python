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


class PipelineVersionList(object):
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
        'version': 'str',
        'pipeline': 'str',
        'description': 'str',
        'labels': 'dict(str, str)',
        'creation_date': 'datetime',
        'last_updated': 'datetime',
        'monitoring': 'str',
        'request_retention_time': 'int',
        'request_retention_mode': 'str',
        'default_notification_group': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'pipeline': 'pipeline',
        'description': 'description',
        'labels': 'labels',
        'creation_date': 'creation_date',
        'last_updated': 'last_updated',
        'monitoring': 'monitoring',
        'request_retention_time': 'request_retention_time',
        'request_retention_mode': 'request_retention_mode',
        'default_notification_group': 'default_notification_group'
    }

    def __init__(self, id=None, version=None, pipeline=None, description=None, labels=None, creation_date=None, last_updated=None, monitoring=None, request_retention_time=None, request_retention_mode=None, default_notification_group=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """PipelineVersionList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._version = None
        self._pipeline = None
        self._description = None
        self._labels = None
        self._creation_date = None
        self._last_updated = None
        self._monitoring = None
        self._request_retention_time = None
        self._request_retention_mode = None
        self._default_notification_group = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.version = version
        self.pipeline = pipeline
        if description is not None:
            self.description = description
        self.labels = labels
        if creation_date is not None:
            self.creation_date = creation_date
        if last_updated is not None:
            self.last_updated = last_updated
        if monitoring is not None:
            self.monitoring = monitoring
        if request_retention_time is not None:
            self.request_retention_time = request_retention_time
        self.request_retention_mode = request_retention_mode
        if default_notification_group is not None:
            self.default_notification_group = default_notification_group

    @property
    def id(self):
        """Gets the id of this PipelineVersionList.  # noqa: E501


        :return: The id of this PipelineVersionList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PipelineVersionList.


        :param id: The id of this PipelineVersionList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")  # noqa: E501

        self._id = id

    @property
    def version(self):
        """Gets the version of this PipelineVersionList.  # noqa: E501


        :return: The version of this PipelineVersionList.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PipelineVersionList.


        :param version: The version of this PipelineVersionList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and not isinstance(version, str)):
            raise ValueError("Parameter `version` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) > 64):
            raise ValueError("Invalid value for `version`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) < 1):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501

        self._version = version

    @property
    def pipeline(self):
        """Gets the pipeline of this PipelineVersionList.  # noqa: E501


        :return: The pipeline of this PipelineVersionList.  # noqa: E501
        :rtype: str
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """Sets the pipeline of this PipelineVersionList.


        :param pipeline: The pipeline of this PipelineVersionList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pipeline is None:  # noqa: E501
            raise ValueError("Invalid value for `pipeline`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pipeline is not None and not isinstance(pipeline, str)):
            raise ValueError("Parameter `pipeline` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                pipeline is not None and len(pipeline) < 1):
            raise ValueError("Invalid value for `pipeline`, length must be greater than or equal to `1`")  # noqa: E501

        self._pipeline = pipeline

    @property
    def description(self):
        """Gets the description of this PipelineVersionList.  # noqa: E501


        :return: The description of this PipelineVersionList.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PipelineVersionList.


        :param description: The description of this PipelineVersionList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not isinstance(description, str)):
            raise ValueError("Parameter `description` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 400):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `400`")  # noqa: E501

        self._description = description

    @property
    def labels(self):
        """Gets the labels of this PipelineVersionList.  # noqa: E501


        :return: The labels of this PipelineVersionList.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this PipelineVersionList.


        :param labels: The labels of this PipelineVersionList.  # noqa: E501
        :type: dict(str, str)
        """
        if (self.local_vars_configuration.client_side_validation and
                labels is not None and not isinstance(labels, dict)):
            raise ValueError("Parameter `labels` must be a dictionary")  # noqa: E501

        self._labels = labels

    @property
    def creation_date(self):
        """Gets the creation_date of this PipelineVersionList.  # noqa: E501


        :return: The creation_date of this PipelineVersionList.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this PipelineVersionList.


        :param creation_date: The creation_date of this PipelineVersionList.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def last_updated(self):
        """Gets the last_updated of this PipelineVersionList.  # noqa: E501


        :return: The last_updated of this PipelineVersionList.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this PipelineVersionList.


        :param last_updated: The last_updated of this PipelineVersionList.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def monitoring(self):
        """Gets the monitoring of this PipelineVersionList.  # noqa: E501


        :return: The monitoring of this PipelineVersionList.  # noqa: E501
        :rtype: str
        """
        return self._monitoring

    @monitoring.setter
    def monitoring(self, monitoring):
        """Sets the monitoring of this PipelineVersionList.


        :param monitoring: The monitoring of this PipelineVersionList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                monitoring is not None and not isinstance(monitoring, str)):
            raise ValueError("Parameter `monitoring` must be a string")  # noqa: E501

        self._monitoring = monitoring

    @property
    def request_retention_time(self):
        """Gets the request_retention_time of this PipelineVersionList.  # noqa: E501


        :return: The request_retention_time of this PipelineVersionList.  # noqa: E501
        :rtype: int
        """
        return self._request_retention_time

    @request_retention_time.setter
    def request_retention_time(self, request_retention_time):
        """Sets the request_retention_time of this PipelineVersionList.


        :param request_retention_time: The request_retention_time of this PipelineVersionList.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                request_retention_time is not None and not isinstance(request_retention_time, int)):
            raise ValueError("Parameter `request_retention_time` must be an integer")  # noqa: E501

        self._request_retention_time = request_retention_time

    @property
    def request_retention_mode(self):
        """Gets the request_retention_mode of this PipelineVersionList.  # noqa: E501


        :return: The request_retention_mode of this PipelineVersionList.  # noqa: E501
        :rtype: str
        """
        return self._request_retention_mode

    @request_retention_mode.setter
    def request_retention_mode(self, request_retention_mode):
        """Sets the request_retention_mode of this PipelineVersionList.


        :param request_retention_mode: The request_retention_mode of this PipelineVersionList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and request_retention_mode is None:  # noqa: E501
            raise ValueError("Invalid value for `request_retention_mode`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                request_retention_mode is not None and not isinstance(request_retention_mode, str)):
            raise ValueError("Parameter `request_retention_mode` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                request_retention_mode is not None and len(request_retention_mode) < 1):
            raise ValueError("Invalid value for `request_retention_mode`, length must be greater than or equal to `1`")  # noqa: E501

        self._request_retention_mode = request_retention_mode

    @property
    def default_notification_group(self):
        """Gets the default_notification_group of this PipelineVersionList.  # noqa: E501


        :return: The default_notification_group of this PipelineVersionList.  # noqa: E501
        :rtype: str
        """
        return self._default_notification_group

    @default_notification_group.setter
    def default_notification_group(self, default_notification_group):
        """Sets the default_notification_group of this PipelineVersionList.


        :param default_notification_group: The default_notification_group of this PipelineVersionList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                default_notification_group is not None and not isinstance(default_notification_group, str)):
            raise ValueError("Parameter `default_notification_group` must be a string")  # noqa: E501

        self._default_notification_group = default_notification_group

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
        if not isinstance(other, PipelineVersionList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PipelineVersionList):
            return True

        return self.to_dict() != other.to_dict()

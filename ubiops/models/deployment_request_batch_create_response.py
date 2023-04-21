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


class DeploymentRequestBatchCreateResponse(object):
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
        'status': 'str',
        'time_created': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'deployment': 'deployment',
        'version': 'version',
        'status': 'status',
        'time_created': 'time_created'
    }

    def __init__(self, id=None, deployment=None, version=None, status=None, time_created=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """DeploymentRequestBatchCreateResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._deployment = None
        self._version = None
        self._status = None
        self._time_created = None
        self.discriminator = None

        self.id = id
        self.deployment = deployment
        self.version = version
        self.status = status
        self.time_created = time_created

    @property
    def id(self):
        """Gets the id of this DeploymentRequestBatchCreateResponse.  # noqa: E501


        :return: The id of this DeploymentRequestBatchCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeploymentRequestBatchCreateResponse.


        :param id: The id of this DeploymentRequestBatchCreateResponse.  # noqa: E501
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
        """Gets the deployment of this DeploymentRequestBatchCreateResponse.  # noqa: E501


        :return: The deployment of this DeploymentRequestBatchCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """Sets the deployment of this DeploymentRequestBatchCreateResponse.


        :param deployment: The deployment of this DeploymentRequestBatchCreateResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and (
            deployment is not None and not isinstance(deployment, str)
        ):
            raise ValueError("Parameter `deployment` must be a string")  # noqa: E501

        self._deployment = deployment

    @property
    def version(self):
        """Gets the version of this DeploymentRequestBatchCreateResponse.  # noqa: E501


        :return: The version of this DeploymentRequestBatchCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DeploymentRequestBatchCreateResponse.


        :param version: The version of this DeploymentRequestBatchCreateResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and (
            version is not None and not isinstance(version, str)
        ):
            raise ValueError("Parameter `version` must be a string")  # noqa: E501

        if self.local_vars_configuration.client_side_validation and (
            version is not None and len(version) < 1
        ):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501

        self._version = version

    @property
    def status(self):
        """Gets the status of this DeploymentRequestBatchCreateResponse.  # noqa: E501


        :return: The status of this DeploymentRequestBatchCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeploymentRequestBatchCreateResponse.


        :param status: The status of this DeploymentRequestBatchCreateResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if self.local_vars_configuration.client_side_validation and (
            status is not None and not isinstance(status, str)
        ):
            raise ValueError("Parameter `status` must be a string")  # noqa: E501
        allowed_values = ["pending", "processing", "completed", "failed", "cancelled_pending", "cancelled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def time_created(self):
        """Gets the time_created of this DeploymentRequestBatchCreateResponse.  # noqa: E501


        :return: The time_created of this DeploymentRequestBatchCreateResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this DeploymentRequestBatchCreateResponse.


        :param time_created: The time_created of this DeploymentRequestBatchCreateResponse.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and time_created is None:  # noqa: E501
            raise ValueError("Invalid value for `time_created`, must not be `None`")  # noqa: E501

        self._time_created = time_created

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
        if not isinstance(other, DeploymentRequestBatchCreateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeploymentRequestBatchCreateResponse):
            return True

        return self.to_dict() != other.to_dict()

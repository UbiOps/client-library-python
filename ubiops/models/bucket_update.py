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


class BucketUpdate(object):
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
        'credentials': 'dict(str, str)',
        'configuration': 'dict(str, str)',
        'ttl': 'int',
        'description': 'str',
        'labels': 'dict(str, str)'
    }

    attribute_map = {
        'credentials': 'credentials',
        'configuration': 'configuration',
        'ttl': 'ttl',
        'description': 'description',
        'labels': 'labels'
    }

    def __init__(self, credentials=None, configuration=None, ttl=None, description=None, labels=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """BucketUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._credentials = None
        self._configuration = None
        self._ttl = None
        self._description = None
        self._labels = None
        self.discriminator = None

        self.credentials = credentials
        self.configuration = configuration
        self.ttl = ttl
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels

    @property
    def credentials(self):
        """Gets the credentials of this BucketUpdate.  # noqa: E501


        :return: The credentials of this BucketUpdate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this BucketUpdate.


        :param credentials: The credentials of this BucketUpdate.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and (
            credentials is not None and not isinstance(credentials, dict)
        ):
            raise ValueError("Parameter `credentials` must be a dictionary")  # noqa: E501

        self._credentials = credentials

    @property
    def configuration(self):
        """Gets the configuration of this BucketUpdate.  # noqa: E501


        :return: The configuration of this BucketUpdate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this BucketUpdate.


        :param configuration: The configuration of this BucketUpdate.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and (
            configuration is not None and not isinstance(configuration, dict)
        ):
            raise ValueError("Parameter `configuration` must be a dictionary")  # noqa: E501

        self._configuration = configuration

    @property
    def ttl(self):
        """Gets the ttl of this BucketUpdate.  # noqa: E501


        :return: The ttl of this BucketUpdate.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this BucketUpdate.


        :param ttl: The ttl of this BucketUpdate.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and (
            ttl is not None and not isinstance(ttl, int)
        ):
            raise ValueError("Parameter `ttl` must be an integer")  # noqa: E501

        self._ttl = ttl

    @property
    def description(self):
        """Gets the description of this BucketUpdate.  # noqa: E501


        :return: The description of this BucketUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BucketUpdate.


        :param description: The description of this BucketUpdate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and (
            description is not None and not isinstance(description, str)
        ):
            raise ValueError("Parameter `description` must be a string")  # noqa: E501

        self._description = description

    @property
    def labels(self):
        """Gets the labels of this BucketUpdate.  # noqa: E501


        :return: The labels of this BucketUpdate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this BucketUpdate.


        :param labels: The labels of this BucketUpdate.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and (
            labels is not None and not isinstance(labels, dict)
        ):
            raise ValueError("Parameter `labels` must be a dictionary")  # noqa: E501

        self._labels = labels

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
        if not isinstance(other, BucketUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BucketUpdate):
            return True

        return self.to_dict() != other.to_dict()

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


class BucketList(object):
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
        'name': 'str',
        'provider': 'str',
        'project': 'str',
        'creation_date': 'datetime',
        'configuration': 'object',
        'ttl': 'int',
        'description': 'str',
        'labels': 'dict(str, str)',
        'last_updated': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'provider': 'provider',
        'project': 'project',
        'creation_date': 'creation_date',
        'configuration': 'configuration',
        'ttl': 'ttl',
        'description': 'description',
        'labels': 'labels',
        'last_updated': 'last_updated'
    }

    def __init__(self, id=None, name=None, provider=None, project=None, creation_date=None, configuration=None, ttl=None, description=None, labels=None, last_updated=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """BucketList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._provider = None
        self._project = None
        self._creation_date = None
        self._configuration = None
        self._ttl = None
        self._description = None
        self._labels = None
        self._last_updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if provider is not None:
            self.provider = provider
        self.project = project
        if creation_date is not None:
            self.creation_date = creation_date
        self.configuration = configuration
        self.ttl = ttl
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        if last_updated is not None:
            self.last_updated = last_updated

    @property
    def id(self):
        """Gets the id of this BucketList.  # noqa: E501


        :return: The id of this BucketList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BucketList.


        :param id: The id of this BucketList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and (
            id is not None and not isinstance(id, str)
        ):
            raise ValueError("Parameter `id` must be a string")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this BucketList.  # noqa: E501


        :return: The name of this BucketList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BucketList.


        :param name: The name of this BucketList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if self.local_vars_configuration.client_side_validation and (
            name is not None and not isinstance(name, str)
        ):
            raise ValueError("Parameter `name` must be a string")  # noqa: E501

        if self.local_vars_configuration.client_side_validation and (
            name is not None and len(name) > 64
        ):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if self.local_vars_configuration.client_side_validation and (
            name is not None and len(name) < 1
        ):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this BucketList.  # noqa: E501


        :return: The provider of this BucketList.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this BucketList.


        :param provider: The provider of this BucketList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and (
            provider is not None and not isinstance(provider, str)
        ):
            raise ValueError("Parameter `provider` must be a string")  # noqa: E501
        allowed_values = ["ubiops", "google_cloud_storage", "amazon_s3", "azure_blob_storage"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and provider not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def project(self):
        """Gets the project of this BucketList.  # noqa: E501


        :return: The project of this BucketList.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this BucketList.


        :param project: The project of this BucketList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and project is None:  # noqa: E501
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501
        if self.local_vars_configuration.client_side_validation and (
            project is not None and not isinstance(project, str)
        ):
            raise ValueError("Parameter `project` must be a string")  # noqa: E501

        if self.local_vars_configuration.client_side_validation and (
            project is not None and len(project) < 1
        ):
            raise ValueError("Invalid value for `project`, length must be greater than or equal to `1`")  # noqa: E501

        self._project = project

    @property
    def creation_date(self):
        """Gets the creation_date of this BucketList.  # noqa: E501


        :return: The creation_date of this BucketList.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this BucketList.


        :param creation_date: The creation_date of this BucketList.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def configuration(self):
        """Gets the configuration of this BucketList.  # noqa: E501


        :return: The configuration of this BucketList.  # noqa: E501
        :rtype: object
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this BucketList.


        :param configuration: The configuration of this BucketList.  # noqa: E501
        :type: object
        """

        self._configuration = configuration

    @property
    def ttl(self):
        """Gets the ttl of this BucketList.  # noqa: E501


        :return: The ttl of this BucketList.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this BucketList.


        :param ttl: The ttl of this BucketList.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and (
            ttl is not None and not isinstance(ttl, int)
        ):
            raise ValueError("Parameter `ttl` must be an integer")  # noqa: E501

        self._ttl = ttl

    @property
    def description(self):
        """Gets the description of this BucketList.  # noqa: E501


        :return: The description of this BucketList.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BucketList.


        :param description: The description of this BucketList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and (
            description is not None and not isinstance(description, str)
        ):
            raise ValueError("Parameter `description` must be a string")  # noqa: E501

        if self.local_vars_configuration.client_side_validation and (
            description is not None and len(description) > 400
        ):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `400`")  # noqa: E501

        self._description = description

    @property
    def labels(self):
        """Gets the labels of this BucketList.  # noqa: E501


        :return: The labels of this BucketList.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this BucketList.


        :param labels: The labels of this BucketList.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and (
            labels is not None and not isinstance(labels, dict)
        ):
            raise ValueError("Parameter `labels` must be a dictionary")  # noqa: E501

        self._labels = labels

    @property
    def last_updated(self):
        """Gets the last_updated of this BucketList.  # noqa: E501


        :return: The last_updated of this BucketList.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this BucketList.


        :param last_updated: The last_updated of this BucketList.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

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
        if not isinstance(other, BucketList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BucketList):
            return True

        return self.to_dict() != other.to_dict()

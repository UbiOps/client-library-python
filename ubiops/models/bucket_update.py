# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class BucketUpdate(object):
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
        "credentials": "dict(str, str)",
        "configuration": "dict(str, str)",
        "ttl": "int",
        "description": "str",
        "labels": "dict(str, str)",
    }

    attribute_map = {
        "credentials": "credentials",
        "configuration": "configuration",
        "ttl": "ttl",
        "description": "description",
        "labels": "labels",
    }

    def __init__(self, credentials=None, configuration=None, ttl=None, description=None, labels=None, **kwargs):
        """
        BucketUpdate - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

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
        """
        Gets the credentials of this BucketUpdate

        :return: the credentials of this BucketUpdate
        :rtype: dict(str, str)
        """

        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this BucketUpdate

        :param credentials: the credentials of this BucketUpdate
        :type: dict(str, str)
        """

        if self.client_side_validation and (credentials is not None and not isinstance(credentials, dict)):
            raise ValueError("Parameter `credentials` must be a dictionary")

        self._credentials = credentials

    @property
    def configuration(self):
        """
        Gets the configuration of this BucketUpdate

        :return: the configuration of this BucketUpdate
        :rtype: dict(str, str)
        """

        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this BucketUpdate

        :param configuration: the configuration of this BucketUpdate
        :type: dict(str, str)
        """

        if self.client_side_validation and (configuration is not None and not isinstance(configuration, dict)):
            raise ValueError("Parameter `configuration` must be a dictionary")

        self._configuration = configuration

    @property
    def ttl(self):
        """
        Gets the ttl of this BucketUpdate

        :return: the ttl of this BucketUpdate
        :rtype: int
        """

        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """
        Sets the ttl of this BucketUpdate

        :param ttl: the ttl of this BucketUpdate
        :type: int
        """

        if self.client_side_validation and (ttl is not None and not isinstance(ttl, int)):
            raise ValueError("Parameter `ttl` must be an integer")

        self._ttl = ttl

    @property
    def description(self):
        """
        Gets the description of this BucketUpdate

        :return: the description of this BucketUpdate
        :rtype: str
        """

        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BucketUpdate

        :param description: the description of this BucketUpdate
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
        Gets the labels of this BucketUpdate

        :return: the labels of this BucketUpdate
        :rtype: dict(str, str)
        """

        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this BucketUpdate

        :param labels: the labels of this BucketUpdate
        :type: dict(str, str)
        """

        if self.client_side_validation and (labels is not None and not isinstance(labels, dict)):
            raise ValueError("Parameter `labels` must be a dictionary")

        self._labels = labels

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

        if not isinstance(other, BucketUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, BucketUpdate):
            return True

        return self.to_dict() != other.to_dict()

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


class RevisionList(object):
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
        'creation_date': 'datetime',
        'created_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'creation_date': 'creation_date',
        'created_by': 'created_by'
    }

    def __init__(self, id=None, version=None, creation_date=None, created_by=None, local_vars_configuration=None):  # noqa: E501
        """RevisionList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._version = None
        self._creation_date = None
        self._created_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.version = version
        if creation_date is not None:
            self.creation_date = creation_date
        if created_by is not None:
            self.created_by = created_by

    @property
    def id(self):
        """Gets the id of this RevisionList.  # noqa: E501


        :return: The id of this RevisionList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RevisionList.


        :param id: The id of this RevisionList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")  # noqa: E501

        self._id = id

    @property
    def version(self):
        """Gets the version of this RevisionList.  # noqa: E501


        :return: The version of this RevisionList.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RevisionList.


        :param version: The version of this RevisionList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and not isinstance(version, str)):
            raise ValueError("Parameter `version` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) < 1):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501

        self._version = version

    @property
    def creation_date(self):
        """Gets the creation_date of this RevisionList.  # noqa: E501


        :return: The creation_date of this RevisionList.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this RevisionList.


        :param creation_date: The creation_date of this RevisionList.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def created_by(self):
        """Gets the created_by of this RevisionList.  # noqa: E501


        :return: The created_by of this RevisionList.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this RevisionList.


        :param created_by: The created_by of this RevisionList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                created_by is not None and not isinstance(created_by, str)):
            raise ValueError("Parameter `created_by` must be a string")  # noqa: E501

        self._created_by = created_by

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
        if not isinstance(other, RevisionList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RevisionList):
            return True

        return self.to_dict() != other.to_dict()
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


class RoleAssignmentList(object):
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
        'user_id': 'str',
        'role': 'str',
        'object_name': 'str',
        'object_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'user_id',
        'role': 'role',
        'object_name': 'object_name',
        'object_type': 'object_type'
    }

    def __init__(self, id=None, user_id=None, role=None, object_name=None, object_type=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """RoleAssignmentList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._user_id = None
        self._role = None
        self._object_name = None
        self._object_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.user_id = user_id
        self.role = role
        if object_name is not None:
            self.object_name = object_name
        if object_type is not None:
            self.object_type = object_type

    @property
    def id(self):
        """Gets the id of this RoleAssignmentList.  # noqa: E501


        :return: The id of this RoleAssignmentList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RoleAssignmentList.


        :param id: The id of this RoleAssignmentList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")  # noqa: E501

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this RoleAssignmentList.  # noqa: E501


        :return: The user_id of this RoleAssignmentList.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this RoleAssignmentList.


        :param user_id: The user_id of this RoleAssignmentList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_id is not None and not isinstance(user_id, str)):
            raise ValueError("Parameter `user_id` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                user_id is not None and len(user_id) < 1):
            raise ValueError("Invalid value for `user_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._user_id = user_id

    @property
    def role(self):
        """Gets the role of this RoleAssignmentList.  # noqa: E501


        :return: The role of this RoleAssignmentList.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this RoleAssignmentList.


        :param role: The role of this RoleAssignmentList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and role is None:  # noqa: E501
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                role is not None and not isinstance(role, str)):
            raise ValueError("Parameter `role` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                role is not None and len(role) < 1):
            raise ValueError("Invalid value for `role`, length must be greater than or equal to `1`")  # noqa: E501

        self._role = role

    @property
    def object_name(self):
        """Gets the object_name of this RoleAssignmentList.  # noqa: E501


        :return: The object_name of this RoleAssignmentList.  # noqa: E501
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """Sets the object_name of this RoleAssignmentList.


        :param object_name: The object_name of this RoleAssignmentList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                object_name is not None and not isinstance(object_name, str)):
            raise ValueError("Parameter `object_name` must be a string")  # noqa: E501

        self._object_name = object_name

    @property
    def object_type(self):
        """Gets the object_type of this RoleAssignmentList.  # noqa: E501


        :return: The object_type of this RoleAssignmentList.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this RoleAssignmentList.


        :param object_type: The object_type of this RoleAssignmentList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                object_type is not None and not isinstance(object_type, str)):
            raise ValueError("Parameter `object_type` must be a string")  # noqa: E501

        self._object_type = object_type

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
        if not isinstance(other, RoleAssignmentList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoleAssignmentList):
            return True

        return self.to_dict() != other.to_dict()

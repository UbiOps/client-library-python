# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class RoleAssignmentCreate(object):
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
        "role": "str",
        "assignee": "str",
        "assignee_type": "str",
        "resource": "str",
        "resource_type": "str",
    }

    attribute_map = {
        "role": "role",
        "assignee": "assignee",
        "assignee_type": "assignee_type",
        "resource": "resource",
        "resource_type": "resource_type",
    }

    def __init__(self, role=None, assignee=None, assignee_type=None, resource=None, resource_type=None, **kwargs):
        """
        RoleAssignmentCreate - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._role = None
        self._assignee = None
        self._assignee_type = None
        self._resource = None
        self._resource_type = None
        self.discriminator = None

        self.role = role
        if assignee is not None:
            self.assignee = assignee
        if assignee_type is not None:
            self.assignee_type = assignee_type
        if resource is not None:
            self.resource = resource
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def role(self):
        """
        Gets the role of this RoleAssignmentCreate

        :return: the role of this RoleAssignmentCreate
        :rtype: str
        """

        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this RoleAssignmentCreate

        :param role: the role of this RoleAssignmentCreate
        :type: str
        """

        if self.client_side_validation and role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")
        if self.client_side_validation and (role is not None and not isinstance(role, str)):
            raise ValueError("Parameter `role` must be a string")

        if self.client_side_validation and (role is not None and len(role) < 1):
            raise ValueError("Invalid value for `role`, length must be greater than or equal to `1`")

        self._role = role

    @property
    def assignee(self):
        """
        Gets the assignee of this RoleAssignmentCreate

        :return: the assignee of this RoleAssignmentCreate
        :rtype: str
        """

        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """
        Sets the assignee of this RoleAssignmentCreate

        :param assignee: the assignee of this RoleAssignmentCreate
        :type: str
        """

        if self.client_side_validation and (assignee is not None and not isinstance(assignee, str)):
            raise ValueError("Parameter `assignee` must be a string")

        if self.client_side_validation and (assignee is not None and len(assignee) < 1):
            raise ValueError("Invalid value for `assignee`, length must be greater than or equal to `1`")

        self._assignee = assignee

    @property
    def assignee_type(self):
        """
        Gets the assignee_type of this RoleAssignmentCreate

        :return: the assignee_type of this RoleAssignmentCreate
        :rtype: str
        """

        return self._assignee_type

    @assignee_type.setter
    def assignee_type(self, assignee_type):
        """
        Sets the assignee_type of this RoleAssignmentCreate

        :param assignee_type: the assignee_type of this RoleAssignmentCreate
        :type: str
        """

        if self.client_side_validation and (assignee_type is not None and not isinstance(assignee_type, str)):
            raise ValueError("Parameter `assignee_type` must be a string")

        if self.client_side_validation and (assignee_type is not None and len(assignee_type) < 1):
            raise ValueError("Invalid value for `assignee_type`, length must be greater than or equal to `1`")

        self._assignee_type = assignee_type

    @property
    def resource(self):
        """
        Gets the resource of this RoleAssignmentCreate

        :return: the resource of this RoleAssignmentCreate
        :rtype: str
        """

        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this RoleAssignmentCreate

        :param resource: the resource of this RoleAssignmentCreate
        :type: str
        """

        if self.client_side_validation and (resource is not None and not isinstance(resource, str)):
            raise ValueError("Parameter `resource` must be a string")

        if self.client_side_validation and (resource is not None and len(resource) < 1):
            raise ValueError("Invalid value for `resource`, length must be greater than or equal to `1`")

        self._resource = resource

    @property
    def resource_type(self):
        """
        Gets the resource_type of this RoleAssignmentCreate

        :return: the resource_type of this RoleAssignmentCreate
        :rtype: str
        """

        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this RoleAssignmentCreate

        :param resource_type: the resource_type of this RoleAssignmentCreate
        :type: str
        """

        if self.client_side_validation and (resource_type is not None and not isinstance(resource_type, str)):
            raise ValueError("Parameter `resource_type` must be a string")

        if self.client_side_validation and (resource_type is not None and len(resource_type) < 1):
            raise ValueError("Invalid value for `resource_type`, length must be greater than or equal to `1`")

        self._resource_type = resource_type

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

        if not isinstance(other, RoleAssignmentCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, RoleAssignmentCreate):
            return True

        return self.to_dict() != other.to_dict()

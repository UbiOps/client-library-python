# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class InstanceTypeGroupUsage(object):
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
        "version": "str",
        "instance_type_group_id": "str",
        "instance_type_group_name": "str",
    }

    attribute_map = {
        "id": "id",
        "deployment": "deployment",
        "version": "version",
        "instance_type_group_id": "instance_type_group_id",
        "instance_type_group_name": "instance_type_group_name",
    }

    def __init__(
        self,
        id=None,
        deployment=None,
        version=None,
        instance_type_group_id=None,
        instance_type_group_name=None,
        **kwargs,
    ):
        """
        InstanceTypeGroupUsage - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._id = None
        self._deployment = None
        self._version = None
        self._instance_type_group_id = None
        self._instance_type_group_name = None
        self.discriminator = None

        self.id = id
        self.deployment = deployment
        self.version = version
        if instance_type_group_id is not None:
            self.instance_type_group_id = instance_type_group_id
        self.instance_type_group_name = instance_type_group_name

    @property
    def id(self):
        """
        Gets the id of this InstanceTypeGroupUsage

        :return: the id of this InstanceTypeGroupUsage
        :rtype: str
        """

        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InstanceTypeGroupUsage

        :param id: the id of this InstanceTypeGroupUsage
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
        Gets the deployment of this InstanceTypeGroupUsage

        :return: the deployment of this InstanceTypeGroupUsage
        :rtype: str
        """

        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """
        Sets the deployment of this InstanceTypeGroupUsage

        :param deployment: the deployment of this InstanceTypeGroupUsage
        :type: str
        """

        if self.client_side_validation and (deployment is not None and not isinstance(deployment, str)):
            raise ValueError("Parameter `deployment` must be a string")

        self._deployment = deployment

    @property
    def version(self):
        """
        Gets the version of this InstanceTypeGroupUsage

        :return: the version of this InstanceTypeGroupUsage
        :rtype: str
        """

        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this InstanceTypeGroupUsage

        :param version: the version of this InstanceTypeGroupUsage
        :type: str
        """

        if self.client_side_validation and (version is not None and not isinstance(version, str)):
            raise ValueError("Parameter `version` must be a string")

        self._version = version

    @property
    def instance_type_group_id(self):
        """
        Gets the instance_type_group_id of this InstanceTypeGroupUsage

        :return: the instance_type_group_id of this InstanceTypeGroupUsage
        :rtype: str
        """

        return self._instance_type_group_id

    @instance_type_group_id.setter
    def instance_type_group_id(self, instance_type_group_id):
        """
        Sets the instance_type_group_id of this InstanceTypeGroupUsage

        :param instance_type_group_id: the instance_type_group_id of this InstanceTypeGroupUsage
        :type: str
        """

        if self.client_side_validation and (
            instance_type_group_id is not None and not isinstance(instance_type_group_id, str)
        ):
            raise ValueError("Parameter `instance_type_group_id` must be a string")

        if self.client_side_validation and (instance_type_group_id is not None and len(instance_type_group_id) < 1):
            raise ValueError("Invalid value for `instance_type_group_id`, length must be greater than or equal to `1`")

        self._instance_type_group_id = instance_type_group_id

    @property
    def instance_type_group_name(self):
        """
        Gets the instance_type_group_name of this InstanceTypeGroupUsage

        :return: the instance_type_group_name of this InstanceTypeGroupUsage
        :rtype: str
        """

        return self._instance_type_group_name

    @instance_type_group_name.setter
    def instance_type_group_name(self, instance_type_group_name):
        """
        Sets the instance_type_group_name of this InstanceTypeGroupUsage

        :param instance_type_group_name: the instance_type_group_name of this InstanceTypeGroupUsage
        :type: str
        """

        if self.client_side_validation and (
            instance_type_group_name is not None and not isinstance(instance_type_group_name, str)
        ):
            raise ValueError("Parameter `instance_type_group_name` must be a string")

        self._instance_type_group_name = instance_type_group_name

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

        if not isinstance(other, InstanceTypeGroupUsage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, InstanceTypeGroupUsage):
            return True

        return self.to_dict() != other.to_dict()

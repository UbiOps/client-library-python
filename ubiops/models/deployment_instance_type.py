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


class DeploymentInstanceType(object):
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
        'display_name': 'str',
        'memory_allocation': 'int',
        'cpu_allocation': 'int',
        'gpu_allocation': 'int',
        'gpu_enabled': 'str',
        'gpu_memory_allocation': 'int',
        'gpu_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'display_name': 'display_name',
        'memory_allocation': 'memory_allocation',
        'cpu_allocation': 'cpu_allocation',
        'gpu_allocation': 'gpu_allocation',
        'gpu_enabled': 'gpu_enabled',
        'gpu_memory_allocation': 'gpu_memory_allocation',
        'gpu_type': 'gpu_type'
    }

    def __init__(self, id=None, name=None, display_name=None, memory_allocation=None, cpu_allocation=None, gpu_allocation=None, gpu_enabled=None, gpu_memory_allocation=None, gpu_type=None, local_vars_configuration=None, **kwargs):  # noqa: E501
        """DeploymentInstanceType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._display_name = None
        self._memory_allocation = None
        self._cpu_allocation = None
        self._gpu_allocation = None
        self._gpu_enabled = None
        self._gpu_memory_allocation = None
        self._gpu_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.display_name = display_name
        if memory_allocation is not None:
            self.memory_allocation = memory_allocation
        if cpu_allocation is not None:
            self.cpu_allocation = cpu_allocation
        if gpu_allocation is not None:
            self.gpu_allocation = gpu_allocation
        if gpu_enabled is not None:
            self.gpu_enabled = gpu_enabled
        if gpu_memory_allocation is not None:
            self.gpu_memory_allocation = gpu_memory_allocation
        self.gpu_type = gpu_type

    @property
    def id(self):
        """Gets the id of this DeploymentInstanceType.  # noqa: E501


        :return: The id of this DeploymentInstanceType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeploymentInstanceType.


        :param id: The id of this DeploymentInstanceType.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this DeploymentInstanceType.  # noqa: E501


        :return: The name of this DeploymentInstanceType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeploymentInstanceType.


        :param name: The name of this DeploymentInstanceType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 256):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this DeploymentInstanceType.  # noqa: E501


        :return: The display_name of this DeploymentInstanceType.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DeploymentInstanceType.


        :param display_name: The display_name of this DeploymentInstanceType.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and not isinstance(display_name, str)):
            raise ValueError("Parameter `display_name` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 256):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `256`")  # noqa: E501

        self._display_name = display_name

    @property
    def memory_allocation(self):
        """Gets the memory_allocation of this DeploymentInstanceType.  # noqa: E501


        :return: The memory_allocation of this DeploymentInstanceType.  # noqa: E501
        :rtype: int
        """
        return self._memory_allocation

    @memory_allocation.setter
    def memory_allocation(self, memory_allocation):
        """Sets the memory_allocation of this DeploymentInstanceType.


        :param memory_allocation: The memory_allocation of this DeploymentInstanceType.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                memory_allocation is not None and not isinstance(memory_allocation, int)):
            raise ValueError("Parameter `memory_allocation` must be an integer")  # noqa: E501

        self._memory_allocation = memory_allocation

    @property
    def cpu_allocation(self):
        """Gets the cpu_allocation of this DeploymentInstanceType.  # noqa: E501


        :return: The cpu_allocation of this DeploymentInstanceType.  # noqa: E501
        :rtype: int
        """
        return self._cpu_allocation

    @cpu_allocation.setter
    def cpu_allocation(self, cpu_allocation):
        """Sets the cpu_allocation of this DeploymentInstanceType.


        :param cpu_allocation: The cpu_allocation of this DeploymentInstanceType.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                cpu_allocation is not None and not isinstance(cpu_allocation, int)):
            raise ValueError("Parameter `cpu_allocation` must be an integer")  # noqa: E501

        self._cpu_allocation = cpu_allocation

    @property
    def gpu_allocation(self):
        """Gets the gpu_allocation of this DeploymentInstanceType.  # noqa: E501


        :return: The gpu_allocation of this DeploymentInstanceType.  # noqa: E501
        :rtype: int
        """
        return self._gpu_allocation

    @gpu_allocation.setter
    def gpu_allocation(self, gpu_allocation):
        """Sets the gpu_allocation of this DeploymentInstanceType.


        :param gpu_allocation: The gpu_allocation of this DeploymentInstanceType.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                gpu_allocation is not None and not isinstance(gpu_allocation, int)):
            raise ValueError("Parameter `gpu_allocation` must be an integer")  # noqa: E501

        self._gpu_allocation = gpu_allocation

    @property
    def gpu_enabled(self):
        """Gets the gpu_enabled of this DeploymentInstanceType.  # noqa: E501


        :return: The gpu_enabled of this DeploymentInstanceType.  # noqa: E501
        :rtype: str
        """
        return self._gpu_enabled

    @gpu_enabled.setter
    def gpu_enabled(self, gpu_enabled):
        """Sets the gpu_enabled of this DeploymentInstanceType.


        :param gpu_enabled: The gpu_enabled of this DeploymentInstanceType.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                gpu_enabled is not None and not isinstance(gpu_enabled, str)):
            raise ValueError("Parameter `gpu_enabled` must be a string")  # noqa: E501

        self._gpu_enabled = gpu_enabled

    @property
    def gpu_memory_allocation(self):
        """Gets the gpu_memory_allocation of this DeploymentInstanceType.  # noqa: E501


        :return: The gpu_memory_allocation of this DeploymentInstanceType.  # noqa: E501
        :rtype: int
        """
        return self._gpu_memory_allocation

    @gpu_memory_allocation.setter
    def gpu_memory_allocation(self, gpu_memory_allocation):
        """Sets the gpu_memory_allocation of this DeploymentInstanceType.


        :param gpu_memory_allocation: The gpu_memory_allocation of this DeploymentInstanceType.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                gpu_memory_allocation is not None and not isinstance(gpu_memory_allocation, int)):
            raise ValueError("Parameter `gpu_memory_allocation` must be an integer")  # noqa: E501

        self._gpu_memory_allocation = gpu_memory_allocation

    @property
    def gpu_type(self):
        """Gets the gpu_type of this DeploymentInstanceType.  # noqa: E501


        :return: The gpu_type of this DeploymentInstanceType.  # noqa: E501
        :rtype: str
        """
        return self._gpu_type

    @gpu_type.setter
    def gpu_type(self, gpu_type):
        """Sets the gpu_type of this DeploymentInstanceType.


        :param gpu_type: The gpu_type of this DeploymentInstanceType.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                gpu_type is not None and not isinstance(gpu_type, str)):
            raise ValueError("Parameter `gpu_type` must be a string")  # noqa: E501

        if (self.local_vars_configuration.client_side_validation and
                gpu_type is not None and len(gpu_type) > 64):
            raise ValueError("Invalid value for `gpu_type`, length must be less than or equal to `64`")  # noqa: E501

        self._gpu_type = gpu_type

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
        if not isinstance(other, DeploymentInstanceType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeploymentInstanceType):
            return True

        return self.to_dict() != other.to_dict()

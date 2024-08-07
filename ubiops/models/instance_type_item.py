# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class InstanceTypeItem(object):
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
        "time_created": "datetime",
        "name": "str",
        "display_name": "str",
        "cpu": "float",
        "memory": "float",
        "storage": "float",
        "accelerator": "float",
        "credit_rate": "float",
        "dedicated_node": "bool",
        "node_pool": "NodePool",
        "priority": "int",
        "schedule_timeout": "int",
    }

    attribute_map = {
        "id": "id",
        "time_created": "time_created",
        "name": "name",
        "display_name": "display_name",
        "cpu": "cpu",
        "memory": "memory",
        "storage": "storage",
        "accelerator": "accelerator",
        "credit_rate": "credit_rate",
        "dedicated_node": "dedicated_node",
        "node_pool": "node_pool",
        "priority": "priority",
        "schedule_timeout": "schedule_timeout",
    }

    def __init__(
        self,
        id=None,
        time_created=None,
        name=None,
        display_name=None,
        cpu=None,
        memory=None,
        storage=None,
        accelerator=None,
        credit_rate=None,
        dedicated_node=None,
        node_pool=None,
        priority=None,
        schedule_timeout=None,
        **kwargs,
    ):
        """
        InstanceTypeItem - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._id = None
        self._time_created = None
        self._name = None
        self._display_name = None
        self._cpu = None
        self._memory = None
        self._storage = None
        self._accelerator = None
        self._credit_rate = None
        self._dedicated_node = None
        self._node_pool = None
        self._priority = None
        self._schedule_timeout = None
        self.discriminator = None

        self.id = id
        self.time_created = time_created
        self.name = name
        self.display_name = display_name
        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if storage is not None:
            self.storage = storage
        if accelerator is not None:
            self.accelerator = accelerator
        if credit_rate is not None:
            self.credit_rate = credit_rate
        if dedicated_node is not None:
            self.dedicated_node = dedicated_node
        self.node_pool = node_pool
        if priority is not None:
            self.priority = priority
        if schedule_timeout is not None:
            self.schedule_timeout = schedule_timeout

    @property
    def id(self):
        """
        Gets the id of this InstanceTypeItem

        :return: the id of this InstanceTypeItem
        :rtype: str
        """

        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InstanceTypeItem

        :param id: the id of this InstanceTypeItem
        :type: str
        """

        if self.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        if self.client_side_validation and (id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")

        self._id = id

    @property
    def time_created(self):
        """
        Gets the time_created of this InstanceTypeItem

        :return: the time_created of this InstanceTypeItem
        :rtype: datetime
        """

        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this InstanceTypeItem

        :param time_created: the time_created of this InstanceTypeItem
        :type: datetime
        """

        self._time_created = time_created

    @property
    def name(self):
        """
        Gets the name of this InstanceTypeItem

        :return: the name of this InstanceTypeItem
        :rtype: str
        """

        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InstanceTypeItem

        :param name: the name of this InstanceTypeItem
        :type: str
        """

        if self.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if self.client_side_validation and (name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")

        if self.client_side_validation and (name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this InstanceTypeItem

        :return: the display_name of this InstanceTypeItem
        :rtype: str
        """

        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstanceTypeItem

        :param display_name: the display_name of this InstanceTypeItem
        :type: str
        """

        if self.client_side_validation and (display_name is not None and not isinstance(display_name, str)):
            raise ValueError("Parameter `display_name` must be a string")

        self._display_name = display_name

    @property
    def cpu(self):
        """
        Gets the cpu of this InstanceTypeItem

        :return: the cpu of this InstanceTypeItem
        :rtype: float
        """

        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """
        Sets the cpu of this InstanceTypeItem

        :param cpu: the cpu of this InstanceTypeItem
        :type: float
        """

        if self.client_side_validation and (cpu is not None and not isinstance(cpu, (int, float))):
            raise ValueError("Parameter `cpu` must be a float")

        self._cpu = cpu

    @property
    def memory(self):
        """
        Gets the memory of this InstanceTypeItem

        :return: the memory of this InstanceTypeItem
        :rtype: float
        """

        return self._memory

    @memory.setter
    def memory(self, memory):
        """
        Sets the memory of this InstanceTypeItem

        :param memory: the memory of this InstanceTypeItem
        :type: float
        """

        if self.client_side_validation and (memory is not None and not isinstance(memory, (int, float))):
            raise ValueError("Parameter `memory` must be a float")

        self._memory = memory

    @property
    def storage(self):
        """
        Gets the storage of this InstanceTypeItem

        :return: the storage of this InstanceTypeItem
        :rtype: float
        """

        return self._storage

    @storage.setter
    def storage(self, storage):
        """
        Sets the storage of this InstanceTypeItem

        :param storage: the storage of this InstanceTypeItem
        :type: float
        """

        if self.client_side_validation and (storage is not None and not isinstance(storage, (int, float))):
            raise ValueError("Parameter `storage` must be a float")

        self._storage = storage

    @property
    def accelerator(self):
        """
        Gets the accelerator of this InstanceTypeItem

        :return: the accelerator of this InstanceTypeItem
        :rtype: float
        """

        return self._accelerator

    @accelerator.setter
    def accelerator(self, accelerator):
        """
        Sets the accelerator of this InstanceTypeItem

        :param accelerator: the accelerator of this InstanceTypeItem
        :type: float
        """

        if self.client_side_validation and (accelerator is not None and not isinstance(accelerator, (int, float))):
            raise ValueError("Parameter `accelerator` must be a float")

        self._accelerator = accelerator

    @property
    def credit_rate(self):
        """
        Gets the credit_rate of this InstanceTypeItem

        :return: the credit_rate of this InstanceTypeItem
        :rtype: float
        """

        return self._credit_rate

    @credit_rate.setter
    def credit_rate(self, credit_rate):
        """
        Sets the credit_rate of this InstanceTypeItem

        :param credit_rate: the credit_rate of this InstanceTypeItem
        :type: float
        """

        if self.client_side_validation and (credit_rate is not None and not isinstance(credit_rate, (int, float))):
            raise ValueError("Parameter `credit_rate` must be a float")

        self._credit_rate = credit_rate

    @property
    def dedicated_node(self):
        """
        Gets the dedicated_node of this InstanceTypeItem

        :return: the dedicated_node of this InstanceTypeItem
        :rtype: bool
        """

        return self._dedicated_node

    @dedicated_node.setter
    def dedicated_node(self, dedicated_node):
        """
        Sets the dedicated_node of this InstanceTypeItem

        :param dedicated_node: the dedicated_node of this InstanceTypeItem
        :type: bool
        """

        if self.client_side_validation and (dedicated_node is not None and not isinstance(dedicated_node, bool)):
            raise ValueError("Parameter `dedicated_node` must be a boolean")

        self._dedicated_node = dedicated_node

    @property
    def node_pool(self):
        """
        Gets the node_pool of this InstanceTypeItem

        :return: the node_pool of this InstanceTypeItem
        :rtype: NodePool
        """

        return self._node_pool

    @node_pool.setter
    def node_pool(self, node_pool):
        """
        Sets the node_pool of this InstanceTypeItem

        :param node_pool: the node_pool of this InstanceTypeItem
        :type: NodePool
        """

        if self.client_side_validation and node_pool is not None:
            if isinstance(node_pool, dict):
                from ubiops.models.node_pool import NodePool

                node_pool = NodePool(**node_pool)

        self._node_pool = node_pool

    @property
    def priority(self):
        """
        Gets the priority of this InstanceTypeItem

        :return: the priority of this InstanceTypeItem
        :rtype: int
        """

        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this InstanceTypeItem

        :param priority: the priority of this InstanceTypeItem
        :type: int
        """

        if self.client_side_validation and (priority is not None and not isinstance(priority, int)):
            raise ValueError("Parameter `priority` must be an integer")

        self._priority = priority

    @property
    def schedule_timeout(self):
        """
        Gets the schedule_timeout of this InstanceTypeItem

        :return: the schedule_timeout of this InstanceTypeItem
        :rtype: int
        """

        return self._schedule_timeout

    @schedule_timeout.setter
    def schedule_timeout(self, schedule_timeout):
        """
        Sets the schedule_timeout of this InstanceTypeItem

        :param schedule_timeout: the schedule_timeout of this InstanceTypeItem
        :type: int
        """

        if self.client_side_validation and (schedule_timeout is not None and not isinstance(schedule_timeout, int)):
            raise ValueError("Parameter `schedule_timeout` must be an integer")

        self._schedule_timeout = schedule_timeout

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

        if not isinstance(other, InstanceTypeItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, InstanceTypeItem):
            return True

        return self.to_dict() != other.to_dict()

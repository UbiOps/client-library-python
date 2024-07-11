# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class InstanceList(object):
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
        "status": "str",
        "time_created": "datetime",
        "time_updated": "datetime",
        "instance_type": "InstanceType",
    }

    attribute_map = {
        "id": "id",
        "status": "status",
        "time_created": "time_created",
        "time_updated": "time_updated",
        "instance_type": "instance_type",
    }

    def __init__(self, id=None, status=None, time_created=None, time_updated=None, instance_type=None, **kwargs):
        """
        InstanceList - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._id = None
        self._status = None
        self._time_created = None
        self._time_updated = None
        self._instance_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if time_created is not None:
            self.time_created = time_created
        self.time_updated = time_updated
        self.instance_type = instance_type

    @property
    def id(self):
        """
        Gets the id of this InstanceList

        :return: the id of this InstanceList
        :rtype: str
        """

        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InstanceList

        :param id: the id of this InstanceList
        :type: str
        """

        if self.client_side_validation and (id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")

        self._id = id

    @property
    def status(self):
        """
        Gets the status of this InstanceList

        :return: the status of this InstanceList
        :rtype: str
        """

        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InstanceList

        :param status: the status of this InstanceList
        :type: str
        """

        if self.client_side_validation and (status is not None and not isinstance(status, str)):
            raise ValueError("Parameter `status` must be a string")

        self._status = status

    @property
    def time_created(self):
        """
        Gets the time_created of this InstanceList

        :return: the time_created of this InstanceList
        :rtype: datetime
        """

        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this InstanceList

        :param time_created: the time_created of this InstanceList
        :type: datetime
        """

        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this InstanceList

        :return: the time_updated of this InstanceList
        :rtype: datetime
        """

        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this InstanceList

        :param time_updated: the time_updated of this InstanceList
        :type: datetime
        """

        self._time_updated = time_updated

    @property
    def instance_type(self):
        """
        Gets the instance_type of this InstanceList

        :return: the instance_type of this InstanceList
        :rtype: InstanceType
        """

        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """
        Sets the instance_type of this InstanceList

        :param instance_type: the instance_type of this InstanceList
        :type: InstanceType
        """

        if self.client_side_validation and instance_type is not None:
            if isinstance(instance_type, dict):
                from ubiops.models.instance_type import InstanceType

                instance_type = InstanceType(**instance_type)

        self._instance_type = instance_type

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

        if not isinstance(other, InstanceList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, InstanceList):
            return True

        return self.to_dict() != other.to_dict()

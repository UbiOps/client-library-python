# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class ScheduleUpdate(object):
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
        "name": "str",
        "schedule": "str",
        "request_data": "object",
        "timeout": "int",
        "enabled": "bool",
        "description": "str",
        "labels": "dict(str, str)",
    }

    attribute_map = {
        "name": "name",
        "schedule": "schedule",
        "request_data": "request_data",
        "timeout": "timeout",
        "enabled": "enabled",
        "description": "description",
        "labels": "labels",
    }

    def __init__(
        self,
        name=None,
        schedule=None,
        request_data=None,
        timeout=None,
        enabled=None,
        description=None,
        labels=None,
        **kwargs,
    ):
        """
        ScheduleUpdate - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._name = None
        self._schedule = None
        self._request_data = None
        self._timeout = None
        self._enabled = None
        self._description = None
        self._labels = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if schedule is not None:
            self.schedule = schedule
        self.request_data = request_data
        if timeout is not None:
            self.timeout = timeout
        if enabled is not None:
            self.enabled = enabled
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels

    @property
    def name(self):
        """
        Gets the name of this ScheduleUpdate

        :return: the name of this ScheduleUpdate
        :rtype: str
        """

        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ScheduleUpdate

        :param name: the name of this ScheduleUpdate
        :type: str
        """

        if self.client_side_validation and (name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")

        if self.client_side_validation and (name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def schedule(self):
        """
        Gets the schedule of this ScheduleUpdate

        :return: the schedule of this ScheduleUpdate
        :rtype: str
        """

        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this ScheduleUpdate

        :param schedule: the schedule of this ScheduleUpdate
        :type: str
        """

        if self.client_side_validation and (schedule is not None and not isinstance(schedule, str)):
            raise ValueError("Parameter `schedule` must be a string")

        if self.client_side_validation and (schedule is not None and len(schedule) < 1):
            raise ValueError("Invalid value for `schedule`, length must be greater than or equal to `1`")

        self._schedule = schedule

    @property
    def request_data(self):
        """
        Gets the request_data of this ScheduleUpdate

        :return: the request_data of this ScheduleUpdate
        :rtype: object
        """

        return self._request_data

    @request_data.setter
    def request_data(self, request_data):
        """
        Sets the request_data of this ScheduleUpdate

        :param request_data: the request_data of this ScheduleUpdate
        :type: object
        """

        self._request_data = request_data

    @property
    def timeout(self):
        """
        Gets the timeout of this ScheduleUpdate

        :return: the timeout of this ScheduleUpdate
        :rtype: int
        """

        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """
        Sets the timeout of this ScheduleUpdate

        :param timeout: the timeout of this ScheduleUpdate
        :type: int
        """

        if self.client_side_validation and (timeout is not None and not isinstance(timeout, int)):
            raise ValueError("Parameter `timeout` must be an integer")

        self._timeout = timeout

    @property
    def enabled(self):
        """
        Gets the enabled of this ScheduleUpdate

        :return: the enabled of this ScheduleUpdate
        :rtype: bool
        """

        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this ScheduleUpdate

        :param enabled: the enabled of this ScheduleUpdate
        :type: bool
        """

        if self.client_side_validation and (enabled is not None and not isinstance(enabled, bool)):
            raise ValueError("Parameter `enabled` must be a boolean")

        self._enabled = enabled

    @property
    def description(self):
        """
        Gets the description of this ScheduleUpdate

        :return: the description of this ScheduleUpdate
        :rtype: str
        """

        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ScheduleUpdate

        :param description: the description of this ScheduleUpdate
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
        Gets the labels of this ScheduleUpdate

        :return: the labels of this ScheduleUpdate
        :rtype: dict(str, str)
        """

        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this ScheduleUpdate

        :param labels: the labels of this ScheduleUpdate
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

        if not isinstance(other, ScheduleUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, ScheduleUpdate):
            return True

        return self.to_dict() != other.to_dict()

# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class BuildList(object):
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
        "revision": "str",
        "creation_date": "datetime",
        "status": "str",
        "error_message": "str",
        "trigger": "str",
        "has_request_method": "bool",
        "has_requests_method": "bool",
    }

    attribute_map = {
        "id": "id",
        "revision": "revision",
        "creation_date": "creation_date",
        "status": "status",
        "error_message": "error_message",
        "trigger": "trigger",
        "has_request_method": "has_request_method",
        "has_requests_method": "has_requests_method",
    }

    def __init__(
        self,
        id=None,
        revision=None,
        creation_date=None,
        status=None,
        error_message=None,
        trigger=None,
        has_request_method=None,
        has_requests_method=None,
        **kwargs,
    ):
        """
        BuildList - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._id = None
        self._revision = None
        self._creation_date = None
        self._status = None
        self._error_message = None
        self._trigger = None
        self._has_request_method = None
        self._has_requests_method = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if revision is not None:
            self.revision = revision
        if creation_date is not None:
            self.creation_date = creation_date
        if status is not None:
            self.status = status
        if error_message is not None:
            self.error_message = error_message
        self.trigger = trigger
        self.has_request_method = has_request_method
        self.has_requests_method = has_requests_method

    @property
    def id(self):
        """
        Gets the id of this BuildList

        :return: the id of this BuildList
        :rtype: str
        """

        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildList

        :param id: the id of this BuildList
        :type: str
        """

        if self.client_side_validation and (id is not None and not isinstance(id, str)):
            raise ValueError("Parameter `id` must be a string")

        self._id = id

    @property
    def revision(self):
        """
        Gets the revision of this BuildList

        :return: the revision of this BuildList
        :rtype: str
        """

        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this BuildList

        :param revision: the revision of this BuildList
        :type: str
        """

        if self.client_side_validation and (revision is not None and not isinstance(revision, str)):
            raise ValueError("Parameter `revision` must be a string")

        self._revision = revision

    @property
    def creation_date(self):
        """
        Gets the creation_date of this BuildList

        :return: the creation_date of this BuildList
        :rtype: datetime
        """

        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this BuildList

        :param creation_date: the creation_date of this BuildList
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def status(self):
        """
        Gets the status of this BuildList

        :return: the status of this BuildList
        :rtype: str
        """

        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BuildList

        :param status: the status of this BuildList
        :type: str
        """

        if self.client_side_validation and (status is not None and not isinstance(status, str)):
            raise ValueError("Parameter `status` must be a string")

        self._status = status

    @property
    def error_message(self):
        """
        Gets the error_message of this BuildList

        :return: the error_message of this BuildList
        :rtype: str
        """

        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this BuildList

        :param error_message: the error_message of this BuildList
        :type: str
        """

        if self.client_side_validation and (error_message is not None and not isinstance(error_message, str)):
            raise ValueError("Parameter `error_message` must be a string")

        self._error_message = error_message

    @property
    def trigger(self):
        """
        Gets the trigger of this BuildList

        :return: the trigger of this BuildList
        :rtype: str
        """

        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """
        Sets the trigger of this BuildList

        :param trigger: the trigger of this BuildList
        :type: str
        """

        if self.client_side_validation and (trigger is not None and not isinstance(trigger, str)):
            raise ValueError("Parameter `trigger` must be a string")

        self._trigger = trigger

    @property
    def has_request_method(self):
        """
        Gets the has_request_method of this BuildList

        :return: the has_request_method of this BuildList
        :rtype: bool
        """

        return self._has_request_method

    @has_request_method.setter
    def has_request_method(self, has_request_method):
        """
        Sets the has_request_method of this BuildList

        :param has_request_method: the has_request_method of this BuildList
        :type: bool
        """

        if self.client_side_validation and (
            has_request_method is not None and not isinstance(has_request_method, bool)
        ):
            raise ValueError("Parameter `has_request_method` must be a boolean")

        self._has_request_method = has_request_method

    @property
    def has_requests_method(self):
        """
        Gets the has_requests_method of this BuildList

        :return: the has_requests_method of this BuildList
        :rtype: bool
        """

        return self._has_requests_method

    @has_requests_method.setter
    def has_requests_method(self, has_requests_method):
        """
        Sets the has_requests_method of this BuildList

        :param has_requests_method: the has_requests_method of this BuildList
        :type: bool
        """

        if self.client_side_validation and (
            has_requests_method is not None and not isinstance(has_requests_method, bool)
        ):
            raise ValueError("Parameter `has_requests_method` must be a boolean")

        self._has_requests_method = has_requests_method

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

        if not isinstance(other, BuildList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, BuildList):
            return True

        return self.to_dict() != other.to_dict()

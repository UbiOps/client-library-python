# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class WebhookTestCreate(object):
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
        "object_type": "str",
        "object_name": "str",
        "version": "str",
        "url": "str",
        "headers": "list[WebhookHeader]",
        "event": "str",
        "timeout": "int",
        "retry": "bool",
        "include_result": "bool",
    }

    attribute_map = {
        "object_type": "object_type",
        "object_name": "object_name",
        "version": "version",
        "url": "url",
        "headers": "headers",
        "event": "event",
        "timeout": "timeout",
        "retry": "retry",
        "include_result": "include_result",
    }

    def __init__(
        self,
        object_type=None,
        object_name=None,
        version=None,
        url=None,
        headers=None,
        event=None,
        timeout=None,
        retry=None,
        include_result=None,
        **kwargs,
    ):
        """
        WebhookTestCreate - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._object_type = None
        self._object_name = None
        self._version = None
        self._url = None
        self._headers = None
        self._event = None
        self._timeout = None
        self._retry = None
        self._include_result = None
        self.discriminator = None

        self.object_type = object_type
        self.object_name = object_name
        self.version = version
        self.url = url
        if headers is not None:
            self.headers = headers
        self.event = event
        if timeout is not None:
            self.timeout = timeout
        if retry is not None:
            self.retry = retry
        if include_result is not None:
            self.include_result = include_result

    @property
    def object_type(self):
        """
        Gets the object_type of this WebhookTestCreate

        :return: the object_type of this WebhookTestCreate
        :rtype: str
        """

        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this WebhookTestCreate

        :param object_type: the object_type of this WebhookTestCreate
        :type: str
        """

        if self.client_side_validation and object_type is None:
            raise ValueError("Invalid value for `object_type`, must not be `None`")
        if self.client_side_validation and (object_type is not None and not isinstance(object_type, str)):
            raise ValueError("Parameter `object_type` must be a string")

        if self.client_side_validation and (object_type is not None and len(object_type) < 1):
            raise ValueError("Invalid value for `object_type`, length must be greater than or equal to `1`")

        self._object_type = object_type

    @property
    def object_name(self):
        """
        Gets the object_name of this WebhookTestCreate

        :return: the object_name of this WebhookTestCreate
        :rtype: str
        """

        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this WebhookTestCreate

        :param object_name: the object_name of this WebhookTestCreate
        :type: str
        """

        if self.client_side_validation and object_name is None:
            raise ValueError("Invalid value for `object_name`, must not be `None`")
        if self.client_side_validation and (object_name is not None and not isinstance(object_name, str)):
            raise ValueError("Parameter `object_name` must be a string")

        if self.client_side_validation and (object_name is not None and len(object_name) < 1):
            raise ValueError("Invalid value for `object_name`, length must be greater than or equal to `1`")

        self._object_name = object_name

    @property
    def version(self):
        """
        Gets the version of this WebhookTestCreate

        :return: the version of this WebhookTestCreate
        :rtype: str
        """

        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this WebhookTestCreate

        :param version: the version of this WebhookTestCreate
        :type: str
        """

        if self.client_side_validation and (version is not None and not isinstance(version, str)):
            raise ValueError("Parameter `version` must be a string")

        if self.client_side_validation and (version is not None and len(version) < 1):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")

        self._version = version

    @property
    def url(self):
        """
        Gets the url of this WebhookTestCreate

        :return: the url of this WebhookTestCreate
        :rtype: str
        """

        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this WebhookTestCreate

        :param url: the url of this WebhookTestCreate
        :type: str
        """

        if self.client_side_validation and url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")
        if self.client_side_validation and (url is not None and not isinstance(url, str)):
            raise ValueError("Parameter `url` must be a string")

        self._url = url

    @property
    def headers(self):
        """
        Gets the headers of this WebhookTestCreate

        :return: the headers of this WebhookTestCreate
        :rtype: list[WebhookHeader]
        """

        return self._headers

    @headers.setter
    def headers(self, headers):
        """
        Sets the headers of this WebhookTestCreate

        :param headers: the headers of this WebhookTestCreate
        :type: list[WebhookHeader]
        """

        if self.client_side_validation and (headers is not None and not isinstance(headers, list)):
            raise ValueError("Parameter `headers` must be a list")
        if self.client_side_validation and headers is not None:
            from ubiops.models.webhook_header import WebhookHeader

            headers = [WebhookHeader(**item) if isinstance(item, dict) else item for item in headers]

        self._headers = headers

    @property
    def event(self):
        """
        Gets the event of this WebhookTestCreate

        :return: the event of this WebhookTestCreate
        :rtype: str
        """

        return self._event

    @event.setter
    def event(self, event):
        """
        Sets the event of this WebhookTestCreate

        :param event: the event of this WebhookTestCreate
        :type: str
        """

        if self.client_side_validation and event is None:
            raise ValueError("Invalid value for `event`, must not be `None`")
        if self.client_side_validation and (event is not None and not isinstance(event, str)):
            raise ValueError("Parameter `event` must be a string")

        self._event = event

    @property
    def timeout(self):
        """
        Gets the timeout of this WebhookTestCreate

        :return: the timeout of this WebhookTestCreate
        :rtype: int
        """

        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """
        Sets the timeout of this WebhookTestCreate

        :param timeout: the timeout of this WebhookTestCreate
        :type: int
        """

        if self.client_side_validation and (timeout is not None and not isinstance(timeout, int)):
            raise ValueError("Parameter `timeout` must be an integer")

        self._timeout = timeout

    @property
    def retry(self):
        """
        Gets the retry of this WebhookTestCreate

        :return: the retry of this WebhookTestCreate
        :rtype: bool
        """

        return self._retry

    @retry.setter
    def retry(self, retry):
        """
        Sets the retry of this WebhookTestCreate

        :param retry: the retry of this WebhookTestCreate
        :type: bool
        """

        if self.client_side_validation and (retry is not None and not isinstance(retry, bool)):
            raise ValueError("Parameter `retry` must be a boolean")

        self._retry = retry

    @property
    def include_result(self):
        """
        Gets the include_result of this WebhookTestCreate

        :return: the include_result of this WebhookTestCreate
        :rtype: bool
        """

        return self._include_result

    @include_result.setter
    def include_result(self, include_result):
        """
        Sets the include_result of this WebhookTestCreate

        :param include_result: the include_result of this WebhookTestCreate
        :type: bool
        """

        if self.client_side_validation and (include_result is not None and not isinstance(include_result, bool)):
            raise ValueError("Parameter `include_result` must be a boolean")

        self._include_result = include_result

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

        if not isinstance(other, WebhookTestCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, WebhookTestCreate):
            return True

        return self.to_dict() != other.to_dict()
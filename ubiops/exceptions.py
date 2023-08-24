# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import json

from xml.etree import cElementTree


class UbiOpsException(Exception):
    """
    The base exception class
    """

    pass


class OpenApiException(UbiOpsException):
    """
    The base exception class for all OpenAPIExceptions
    """

    pass


class ApiTypeError(OpenApiException, TypeError):
    """
    OpenApi exception for TypeErrors
    """

    def __init__(self, msg, path_to_item=None, valid_classes=None, key_type=None):
        """
        :param str msg: the exception message
        :param list|None path_to_item: a list of keys an indices to get to the current_item None if unset
        :param tuple|None valid_classes: the primitive classes that current item should be an instance of None if unset
        :param bool|None key_type: False if our value is a value in a dict, True if it is a key in a dict, False if our
            item is an item in a list, None if unset
        """
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = f"{msg} at {render_path(path_to_item)}"
        super(ApiTypeError, self).__init__(full_msg)


class ApiValueError(OpenApiException, ValueError):
    """
    OpenApi exception for ValueErrors
    """

    def __init__(self, msg, path_to_item=None):
        """
        :param str msg: the exception message
        :param list|None path_to_item: the path to the exception in the received_data dict, None if unset
        """

        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = f"{msg} at {render_path(path_to_item)}"
        super(ApiValueError, self).__init__(full_msg)


class ApiKeyError(OpenApiException, KeyError):
    """
    OpenApi exception for KeyErrors
    """

    def __init__(self, msg, path_to_item=None):
        """
        :param str msg: the exception message
        :param list|None path_to_item: the path to the exception in the received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = f"{msg} at {render_path(path_to_item)}"
        super(ApiKeyError, self).__init__(full_msg)


class ApiException(OpenApiException):
    """
    OpenApi exception for exceptions from the Api
    """

    def __init__(self, status=None, reason=None, body=None, http_resp=None, requests_resp=None):
        if http_resp is not None:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.headers
        elif requests_resp is not None:
            self.status = requests_resp.status_code
            self.reason = requests_resp.reason
            self.body = requests_resp.text
            self.headers = requests_resp.headers
        else:
            self.status = status
            self.reason = reason
            self.body = body
            self.headers = None

    def get_body_message(self):
        """
        Retrieve the error from the HTTP response body
        """

        # Parse body as JSON
        try:
            body_content = json.loads(self.body)

            if isinstance(body_content, dict) and "error" in body_content:
                return body_content["error"]

            elif isinstance(body_content, dict) and "error_message" in body_content:
                return body_content["error_message"]

        except (ValueError, TypeError, KeyError):
            pass

        # Parse body as XML
        try:
            content = cElementTree.fromstring(self.body)
            if content.find("Details") is not None:
                return content.find("Details").text
            if content.find("Message") is not None:
                return content.find("Message").text

        except (cElementTree.ParseError, ValueError, TypeError, AttributeError):
            pass

        return self.body

    def __str__(self):
        """
        Custom error messages for exception
        """

        error_message = f"{self.reason} ({self.status})"

        if self.body:
            body_message = self.get_body_message()

            if body_message:
                error_message += f"\nError: {body_message}"
            else:
                if self.headers:
                    error_message += f"\nHTTP response headers: {self.headers}"
                error_message += f"\nHTTP response body: {self.body}"

        elif self.headers:
            error_message += f"\nHTTP response headers: {self.headers}"

        return error_message


class ApiConnectionError(ApiException):
    """
    Api exception for ConnectionErrors
    """

    pass


class ApiTimeoutError(ApiException):
    """
    Api exception for Timeouts
    """

    pass


class ApiRequestError(ApiException):
    """
    Api exception for RequestExceptions
    """

    pass


def render_path(path_to_item):
    """
    Returns a string representation of a path
    """

    result = ""
    for pth in path_to_item:
        if isinstance(pth, int):
            result += f"[{pth}]"
        else:
            result += f"['{pth}']"
    return result

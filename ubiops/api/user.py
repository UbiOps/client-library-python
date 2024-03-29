# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


from ubiops.api_client import ApiClient
from ubiops.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class User(object):
    """
    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def user_create_with_http_info(self, data, **kwargs):
        """
        Create a new user

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = User.user_create_with_http_info(
                data, async_req=True
            )
        >>> result = thread.get()

        :param UserPendingCreate data: (required)
        :param kwargs:
            - bool _return_http_data_only: response data without head status code and headers
            - bool _preload_content: if False, the requests.Response object will be returned without reading/decoding
                response data. Default is True.
            - int|tuple _request_timeout: timeout setting for this request. If one number provided, it will be total
                request timeout. It can also be a pair (tuple) of (connection, read) timeouts.
            - bool async_req: execute request asynchronously
        :return: tuple(UserPendingDetail, status_code(int), headers(HTTPHeaderDict))
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "user_create"
        optional_params = []
        additional_params = [
            "async_req",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
            "_request_stream",
            "_progress_bar",
        ]

        for key, val in kwargs.items():
            if key not in optional_params + additional_params:
                raise ApiTypeError(f"Got an unexpected keyword argument '{key}' to method `{method_name}`")

        if self.api_client.client_side_validation and data is None:
            raise ApiValueError(f"Missing the required parameter `data` when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if isinstance(data, dict):
                from ubiops.models.user_pending_create import UserPendingCreate

                data = UserPendingCreate(**data)

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        body_params = data

        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])

        url = "/user"  # noqa: E501
        return self.api_client.call_api(
            url,
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type="UserPendingDetail",
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", True),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", False),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", False),
        )

    def user_delete_with_http_info(self, **kwargs):
        """
        Delete user

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = User.user_delete_with_http_info(
                async_req=True
            )
        >>> result = thread.get()

        :param kwargs:
            - bool _return_http_data_only: response data without head status code and headers
            - bool _preload_content: if False, the requests.Response object will be returned without reading/decoding
                response data. Default is True.
            - int|tuple _request_timeout: timeout setting for this request. If one number provided, it will be total
                request timeout. It can also be a pair (tuple) of (connection, read) timeouts.
            - bool async_req: execute request asynchronously
        :return: None
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "user_delete"
        optional_params = []
        additional_params = [
            "async_req",
            "_return_http_data_only",
            "_preload_content",
            "_request_timeout",
            "_request_stream",
            "_progress_bar",
        ]

        for key, val in kwargs.items():
            if key not in optional_params + additional_params:
                raise ApiTypeError(f"Got an unexpected keyword argument '{key}' to method `{method_name}`")

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        url = "/user"  # noqa: E501
        return self.api_client.call_api(
            url,
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type=None,
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", True),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", False),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", False),
        )

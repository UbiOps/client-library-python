# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


from ubiops.api_client import ApiClient
from ubiops.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class Monitoring(object):
    """
    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def notification_groups_create_with_http_info(self, project_name, data, **kwargs):
        """
        Create notification groups

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Monitoring.notification_groups_create_with_http_info(
                project_name, data, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param NotificationGroupCreate data: (required)
        :param kwargs:
            - bool _return_http_data_only: response data without head status code and headers
            - bool _preload_content: if False, the requests.Response object will be returned without reading/decoding
                response data. Default is True.
            - int|tuple _request_timeout: timeout setting for this request. If one number provided, it will be total
                request timeout. It can also be a pair (tuple) of (connection, read) timeouts.
            - bool async_req: execute request asynchronously
        :return: tuple(NotificationGroupList, status_code(int), headers(HTTPHeaderDict))
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "notification_groups_create"
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

        if self.api_client.client_side_validation and project_name is None:
            raise ApiValueError(f"Missing the required parameter `project_name` when calling `{method_name}`")
        if self.api_client.client_side_validation and data is None:
            raise ApiValueError(f"Missing the required parameter `data` when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(project_name, str):
                raise ApiValueError(f"Parameter `project_name` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if isinstance(data, dict):
                from ubiops.models.notification_group_create import NotificationGroupCreate

                data = NotificationGroupCreate(**data)

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        path_params["project_name"] = project_name

        body_params = data

        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])

        url = "/projects/{project_name}/monitoring/notification-groups"  # noqa: E501
        return self.api_client.call_api(
            url,
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type="NotificationGroupList",
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", True),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", False),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", False),
        )

    def notification_groups_delete_with_http_info(self, project_name, notification_group_name, **kwargs):
        """
        Delete notification group

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Monitoring.notification_groups_delete_with_http_info(
                project_name, notification_group_name, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param str notification_group_name: (required)
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

        method_name = "notification_groups_delete"
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

        if self.api_client.client_side_validation and project_name is None:
            raise ApiValueError(f"Missing the required parameter `project_name` when calling `{method_name}`")
        if self.api_client.client_side_validation and notification_group_name is None:
            raise ApiValueError(
                f"Missing the required parameter `notification_group_name` when calling `{method_name}`"
            )
        if self.api_client.client_side_validation:
            if not isinstance(project_name, str):
                raise ApiValueError(f"Parameter `project_name` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(notification_group_name, str):
                raise ApiValueError(
                    f"Parameter `notification_group_name` must be a string when calling `{method_name}`"
                )

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        path_params["project_name"] = project_name
        path_params["notification_group_name"] = notification_group_name

        url = "/projects/{project_name}/monitoring/notification-groups/{notification_group_name}"  # noqa: E501
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

    def notification_groups_get_with_http_info(self, project_name, notification_group_name, **kwargs):
        """
        Get notification group

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Monitoring.notification_groups_get_with_http_info(
                project_name, notification_group_name, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param str notification_group_name: (required)
        :param kwargs:
            - bool _return_http_data_only: response data without head status code and headers
            - bool _preload_content: if False, the requests.Response object will be returned without reading/decoding
                response data. Default is True.
            - int|tuple _request_timeout: timeout setting for this request. If one number provided, it will be total
                request timeout. It can also be a pair (tuple) of (connection, read) timeouts.
            - bool async_req: execute request asynchronously
        :return: tuple(NotificationGroupList, status_code(int), headers(HTTPHeaderDict))
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "notification_groups_get"
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

        if self.api_client.client_side_validation and project_name is None:
            raise ApiValueError(f"Missing the required parameter `project_name` when calling `{method_name}`")
        if self.api_client.client_side_validation and notification_group_name is None:
            raise ApiValueError(
                f"Missing the required parameter `notification_group_name` when calling `{method_name}`"
            )
        if self.api_client.client_side_validation:
            if not isinstance(project_name, str):
                raise ApiValueError(f"Parameter `project_name` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(notification_group_name, str):
                raise ApiValueError(
                    f"Parameter `notification_group_name` must be a string when calling `{method_name}`"
                )

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        path_params["project_name"] = project_name
        path_params["notification_group_name"] = notification_group_name

        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        url = "/projects/{project_name}/monitoring/notification-groups/{notification_group_name}"  # noqa: E501
        return self.api_client.call_api(
            url,
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type="NotificationGroupList",
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", True),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", False),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", False),
        )

    def notification_groups_list_with_http_info(self, project_name, **kwargs):
        """
        List notification groups

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Monitoring.notification_groups_list_with_http_info(
                project_name, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param kwargs:
            - bool _return_http_data_only: response data without head status code and headers
            - bool _preload_content: if False, the requests.Response object will be returned without reading/decoding
                response data. Default is True.
            - int|tuple _request_timeout: timeout setting for this request. If one number provided, it will be total
                request timeout. It can also be a pair (tuple) of (connection, read) timeouts.
            - bool async_req: execute request asynchronously
        :return: tuple(list[NotificationGroupList], status_code(int), headers(HTTPHeaderDict))
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "notification_groups_list"
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

        if self.api_client.client_side_validation and project_name is None:
            raise ApiValueError(f"Missing the required parameter `project_name` when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(project_name, str):
                raise ApiValueError(f"Parameter `project_name` must be a string when calling `{method_name}`")

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        path_params["project_name"] = project_name

        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        url = "/projects/{project_name}/monitoring/notification-groups"  # noqa: E501
        return self.api_client.call_api(
            url,
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type="list[NotificationGroupList]",
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", True),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", False),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", False),
        )

    def notification_groups_update_with_http_info(self, project_name, notification_group_name, data, **kwargs):
        """
        Update notification group

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Monitoring.notification_groups_update_with_http_info(
                project_name, notification_group_name, data, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param str notification_group_name: (required)
        :param NotificationGroupUpdate data: (required)
        :param kwargs:
            - bool _return_http_data_only: response data without head status code and headers
            - bool _preload_content: if False, the requests.Response object will be returned without reading/decoding
                response data. Default is True.
            - int|tuple _request_timeout: timeout setting for this request. If one number provided, it will be total
                request timeout. It can also be a pair (tuple) of (connection, read) timeouts.
            - bool async_req: execute request asynchronously
        :return: tuple(NotificationGroupList, status_code(int), headers(HTTPHeaderDict))
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "notification_groups_update"
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

        if self.api_client.client_side_validation and project_name is None:
            raise ApiValueError(f"Missing the required parameter `project_name` when calling `{method_name}`")
        if self.api_client.client_side_validation and notification_group_name is None:
            raise ApiValueError(
                f"Missing the required parameter `notification_group_name` when calling `{method_name}`"
            )
        if self.api_client.client_side_validation and data is None:
            raise ApiValueError(f"Missing the required parameter `data` when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(project_name, str):
                raise ApiValueError(f"Parameter `project_name` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(notification_group_name, str):
                raise ApiValueError(
                    f"Parameter `notification_group_name` must be a string when calling `{method_name}`"
                )
        if self.api_client.client_side_validation:
            if isinstance(data, dict):
                from ubiops.models.notification_group_update import NotificationGroupUpdate

                data = NotificationGroupUpdate(**data)

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        path_params["project_name"] = project_name
        path_params["notification_group_name"] = notification_group_name

        body_params = data

        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])

        url = "/projects/{project_name}/monitoring/notification-groups/{notification_group_name}"  # noqa: E501
        return self.api_client.call_api(
            url,
            "PATCH",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type="NotificationGroupList",
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", True),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", False),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", False),
        )

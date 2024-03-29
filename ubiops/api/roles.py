# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


from ubiops.api_client import ApiClient
from ubiops.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class Roles(object):
    """
    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def permissions_list_with_http_info(self, **kwargs):
        """
        List the available permissions

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Roles.permissions_list_with_http_info(
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
        :return: tuple(list[PermissionList], status_code(int), headers(HTTPHeaderDict))
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "permissions_list"
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

        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        url = "/permissions"  # noqa: E501
        return self.api_client.call_api(
            url,
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type="list[PermissionList]",
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", True),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", False),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", False),
        )

    def role_assignments_create_with_http_info(self, project_name, data, **kwargs):
        """
        Assign role to user/object

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Roles.role_assignments_create_with_http_info(
                project_name, data, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param RoleAssignmentCreate data: (required)
        :param kwargs:
            - bool _return_http_data_only: response data without head status code and headers
            - bool _preload_content: if False, the requests.Response object will be returned without reading/decoding
                response data. Default is True.
            - int|tuple _request_timeout: timeout setting for this request. If one number provided, it will be total
                request timeout. It can also be a pair (tuple) of (connection, read) timeouts.
            - bool async_req: execute request asynchronously
        :return: tuple(RoleAssignmentList, status_code(int), headers(HTTPHeaderDict))
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "role_assignments_create"
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
                from ubiops.models.role_assignment_create import RoleAssignmentCreate

                data = RoleAssignmentCreate(**data)

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

        url = "/projects/{project_name}/role-assignments"  # noqa: E501
        return self.api_client.call_api(
            url,
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type="RoleAssignmentList",
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", True),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", False),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", False),
        )

    def role_assignments_delete_with_http_info(self, project_name, id, **kwargs):
        """
        Delete role of user

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Roles.role_assignments_delete_with_http_info(
                project_name, id, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param str id: (required)
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

        method_name = "role_assignments_delete"
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
        if self.api_client.client_side_validation and id is None:
            raise ApiValueError(f"Missing the required parameter `id` when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(project_name, str):
                raise ApiValueError(f"Parameter `project_name` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(id, str):
                raise ApiValueError(f"Parameter `id` must be a string when calling `{method_name}`")

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        path_params["project_name"] = project_name
        path_params["id"] = id

        url = "/projects/{project_name}/role-assignments/{id}"  # noqa: E501
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

    def role_assignments_get_with_http_info(self, project_name, id, **kwargs):
        """
        Get role assignment

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Roles.role_assignments_get_with_http_info(
                project_name, id, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param str id: (required)
        :param kwargs:
            - bool _return_http_data_only: response data without head status code and headers
            - bool _preload_content: if False, the requests.Response object will be returned without reading/decoding
                response data. Default is True.
            - int|tuple _request_timeout: timeout setting for this request. If one number provided, it will be total
                request timeout. It can also be a pair (tuple) of (connection, read) timeouts.
            - bool async_req: execute request asynchronously
        :return: tuple(RoleAssignmentList, status_code(int), headers(HTTPHeaderDict))
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "role_assignments_get"
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
        if self.api_client.client_side_validation and id is None:
            raise ApiValueError(f"Missing the required parameter `id` when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(project_name, str):
                raise ApiValueError(f"Parameter `project_name` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(id, str):
                raise ApiValueError(f"Parameter `id` must be a string when calling `{method_name}`")

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        path_params["project_name"] = project_name
        path_params["id"] = id

        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        url = "/projects/{project_name}/role-assignments/{id}"  # noqa: E501
        return self.api_client.call_api(
            url,
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type="RoleAssignmentList",
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", True),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", False),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", False),
        )

    def role_assignments_per_object_list_with_http_info(self, project_name, **kwargs):
        """
        List roles on object/user

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Roles.role_assignments_per_object_list_with_http_info(
                project_name, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param kwargs:
            - str resource:
            - str resource_type:
            - str assignee:
            - str assignee_type:
            - bool _return_http_data_only: response data without head status code and headers
            - bool _preload_content: if False, the requests.Response object will be returned without reading/decoding
                response data. Default is True.
            - int|tuple _request_timeout: timeout setting for this request. If one number provided, it will be total
                request timeout. It can also be a pair (tuple) of (connection, read) timeouts.
            - bool async_req: execute request asynchronously
        :return: tuple(list[RoleAssignmentList], status_code(int), headers(HTTPHeaderDict))
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "role_assignments_per_object_list"
        optional_params = ["resource", "resource_type", "assignee", "assignee_type"]
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
        if self.api_client.client_side_validation and "resource" in kwargs and kwargs["resource"] is not None:
            if not isinstance(kwargs["resource"], str):
                raise ApiValueError(f"Parameter `resource` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation and "resource_type" in kwargs and kwargs["resource_type"] is not None:
            if not isinstance(kwargs["resource_type"], str):
                raise ApiValueError(f"Parameter `resource_type` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation and "assignee" in kwargs and kwargs["assignee"] is not None:
            if not isinstance(kwargs["assignee"], str):
                raise ApiValueError(f"Parameter `assignee` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation and "assignee_type" in kwargs and kwargs["assignee_type"] is not None:
            if not isinstance(kwargs["assignee_type"], str):
                raise ApiValueError(f"Parameter `assignee_type` must be a string when calling `{method_name}`")

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        path_params["project_name"] = project_name

        if "resource" in kwargs and kwargs["resource"] is not None:
            query_params.append(("resource", kwargs["resource"]))
        if "resource_type" in kwargs and kwargs["resource_type"] is not None:
            query_params.append(("resource_type", kwargs["resource_type"]))
        if "assignee" in kwargs and kwargs["assignee"] is not None:
            query_params.append(("assignee", kwargs["assignee"]))
        if "assignee_type" in kwargs and kwargs["assignee_type"] is not None:
            query_params.append(("assignee_type", kwargs["assignee_type"]))

        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        url = "/projects/{project_name}/role-assignments"  # noqa: E501
        return self.api_client.call_api(
            url,
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type="list[RoleAssignmentList]",
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", True),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", False),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", False),
        )

    def roles_create_with_http_info(self, project_name, data, **kwargs):
        """
        Create a custom role scoped in a project

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Roles.roles_create_with_http_info(
                project_name, data, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param RoleCreate data: (required)
        :param kwargs:
            - bool _return_http_data_only: response data without head status code and headers
            - bool _preload_content: if False, the requests.Response object will be returned without reading/decoding
                response data. Default is True.
            - int|tuple _request_timeout: timeout setting for this request. If one number provided, it will be total
                request timeout. It can also be a pair (tuple) of (connection, read) timeouts.
            - bool async_req: execute request asynchronously
        :return: tuple(RoleDetailList, status_code(int), headers(HTTPHeaderDict))
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "roles_create"
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
                from ubiops.models.role_create import RoleCreate

                data = RoleCreate(**data)

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

        url = "/projects/{project_name}/roles"  # noqa: E501
        return self.api_client.call_api(
            url,
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type="RoleDetailList",
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", True),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", False),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", False),
        )

    def roles_delete_with_http_info(self, project_name, role_name, **kwargs):
        """
        Delete a role from a project

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Roles.roles_delete_with_http_info(
                project_name, role_name, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param str role_name: (required)
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

        method_name = "roles_delete"
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
        if self.api_client.client_side_validation and role_name is None:
            raise ApiValueError(f"Missing the required parameter `role_name` when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(project_name, str):
                raise ApiValueError(f"Parameter `project_name` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(role_name, str):
                raise ApiValueError(f"Parameter `role_name` must be a string when calling `{method_name}`")

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        path_params["project_name"] = project_name
        path_params["role_name"] = role_name

        url = "/projects/{project_name}/roles/{role_name}"  # noqa: E501
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

    def roles_get_with_http_info(self, project_name, role_name, **kwargs):
        """
        Get details of a role

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Roles.roles_get_with_http_info(
                project_name, role_name, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param str role_name: (required)
        :param kwargs:
            - bool _return_http_data_only: response data without head status code and headers
            - bool _preload_content: if False, the requests.Response object will be returned without reading/decoding
                response data. Default is True.
            - int|tuple _request_timeout: timeout setting for this request. If one number provided, it will be total
                request timeout. It can also be a pair (tuple) of (connection, read) timeouts.
            - bool async_req: execute request asynchronously
        :return: tuple(RoleDetailList, status_code(int), headers(HTTPHeaderDict))
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "roles_get"
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
        if self.api_client.client_side_validation and role_name is None:
            raise ApiValueError(f"Missing the required parameter `role_name` when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(project_name, str):
                raise ApiValueError(f"Parameter `project_name` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(role_name, str):
                raise ApiValueError(f"Parameter `role_name` must be a string when calling `{method_name}`")

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        path_params["project_name"] = project_name
        path_params["role_name"] = role_name

        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        url = "/projects/{project_name}/roles/{role_name}"  # noqa: E501
        return self.api_client.call_api(
            url,
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type="RoleDetailList",
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", True),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", False),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", False),
        )

    def roles_list_with_http_info(self, project_name, **kwargs):
        """
        List the available roles in a project

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Roles.roles_list_with_http_info(
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
        :return: tuple(list[RoleList], status_code(int), headers(HTTPHeaderDict))
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "roles_list"
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

        url = "/projects/{project_name}/roles"  # noqa: E501
        return self.api_client.call_api(
            url,
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type="list[RoleList]",
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", True),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", False),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", False),
        )

    def roles_update_with_http_info(self, project_name, role_name, data, **kwargs):
        """
        Update a role in a project

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Roles.roles_update_with_http_info(
                project_name, role_name, data, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param str role_name: (required)
        :param RoleUpdate data: (required)
        :param kwargs:
            - bool _return_http_data_only: response data without head status code and headers
            - bool _preload_content: if False, the requests.Response object will be returned without reading/decoding
                response data. Default is True.
            - int|tuple _request_timeout: timeout setting for this request. If one number provided, it will be total
                request timeout. It can also be a pair (tuple) of (connection, read) timeouts.
            - bool async_req: execute request asynchronously
        :return: tuple(RoleDetailList, status_code(int), headers(HTTPHeaderDict))
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "roles_update"
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
        if self.api_client.client_side_validation and role_name is None:
            raise ApiValueError(f"Missing the required parameter `role_name` when calling `{method_name}`")
        if self.api_client.client_side_validation and data is None:
            raise ApiValueError(f"Missing the required parameter `data` when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(project_name, str):
                raise ApiValueError(f"Parameter `project_name` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(role_name, str):
                raise ApiValueError(f"Parameter `role_name` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if isinstance(data, dict):
                from ubiops.models.role_update import RoleUpdate

                data = RoleUpdate(**data)

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        path_params["project_name"] = project_name
        path_params["role_name"] = role_name

        body_params = data

        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])

        url = "/projects/{project_name}/roles/{role_name}"  # noqa: E501
        return self.api_client.call_api(
            url,
            "PATCH",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type="RoleDetailList",
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", True),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", False),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", False),
        )

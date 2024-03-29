# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


from ubiops.api_client import ApiClient
from ubiops.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class Blobs(object):
    """
    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def blobs_create_with_http_info(self, project_name, file, **kwargs):
        """
        Upload a blob

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Blobs.blobs_create_with_http_info(
                project_name, file, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param file file: (required)
        :param kwargs:
            - int blob_ttl:
            - bool _return_http_data_only: response data without head status code and headers
            - bool _preload_content: if False, the requests.Response object will be returned without reading/decoding
                response data. Default is True.
            - int|tuple _request_timeout: timeout setting for this request. If one number provided, it will be total
                request timeout. It can also be a pair (tuple) of (connection, read) timeouts.
            - bool async_req: execute request asynchronously
        :return: tuple(BlobList, status_code(int), headers(HTTPHeaderDict))
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "blobs_create"
        optional_params = ["blob_ttl"]
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
        if self.api_client.client_side_validation and file is None:
            raise ApiValueError(f"Missing the required parameter `file` when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(project_name, str):
                raise ApiValueError(f"Parameter `project_name` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation and "blob_ttl" in kwargs:
            if not isinstance(kwargs["blob_ttl"], int):
                raise ApiValueError(f"Parameter `blob_ttl` must be an integer when calling `{method_name}`")

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        path_params["project_name"] = project_name

        if "blob_ttl" in kwargs:
            header_params["blob-ttl"] = kwargs["blob_ttl"]

        files["file"] = file

        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["multipart/form-data"])

        url = "/projects/{project_name}/blobs"  # noqa: E501
        return self.api_client.call_api(
            url,
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type="BlobList",
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", True),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", False),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", True),
        )

    def blobs_delete_with_http_info(self, project_name, blob_id, **kwargs):
        """
        Delete a blob

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Blobs.blobs_delete_with_http_info(
                project_name, blob_id, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param str blob_id: (required)
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

        method_name = "blobs_delete"
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
        if self.api_client.client_side_validation and blob_id is None:
            raise ApiValueError(f"Missing the required parameter `blob_id` when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(project_name, str):
                raise ApiValueError(f"Parameter `project_name` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(blob_id, str):
                raise ApiValueError(f"Parameter `blob_id` must be a string when calling `{method_name}`")

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        path_params["project_name"] = project_name
        path_params["blob_id"] = blob_id

        url = "/projects/{project_name}/blobs/{blob_id}"  # noqa: E501
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

    def blobs_get_with_http_info(self, project_name, blob_id, **kwargs):
        """
        Get a blob

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Blobs.blobs_get_with_http_info(
                project_name, blob_id, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param str blob_id: (required)
        :param kwargs:
            - bool _return_http_data_only: response data without head status code and headers
            - bool _preload_content: if True, the file will be downloaded in a folder, which can be defined by
                api_client.configuration.temp_folder_path. Default is False.
            - int|tuple _request_timeout: timeout setting for this request. If one number provided, it will be total
                request timeout. It can also be a pair (tuple) of (connection, read) timeouts.
            - bool async_req: execute request asynchronously
        :return: tuple(file, status_code(int), headers(HTTPHeaderDict))
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "blobs_get"
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
        if self.api_client.client_side_validation and blob_id is None:
            raise ApiValueError(f"Missing the required parameter `blob_id` when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(project_name, str):
                raise ApiValueError(f"Parameter `project_name` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(blob_id, str):
                raise ApiValueError(f"Parameter `blob_id` must be a string when calling `{method_name}`")

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        path_params["project_name"] = project_name
        path_params["blob_id"] = blob_id

        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        url = "/projects/{project_name}/blobs/{blob_id}"  # noqa: E501
        return self.api_client.call_api(
            url,
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type="file",
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", False),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", True),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", True),
        )

    def blobs_list_with_http_info(self, project_name, **kwargs):
        """
        List blobs

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Blobs.blobs_list_with_http_info(
                project_name, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param kwargs:
            - int range:
            - str creation_date:
            - bool _return_http_data_only: response data without head status code and headers
            - bool _preload_content: if False, the requests.Response object will be returned without reading/decoding
                response data. Default is True.
            - int|tuple _request_timeout: timeout setting for this request. If one number provided, it will be total
                request timeout. It can also be a pair (tuple) of (connection, read) timeouts.
            - bool async_req: execute request asynchronously
        :return: tuple(list[BlobList], status_code(int), headers(HTTPHeaderDict))
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "blobs_list"
        optional_params = ["range", "creation_date"]
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
        if self.api_client.client_side_validation and "range" in kwargs and kwargs["range"] is not None:
            if not isinstance(kwargs["range"], int):
                raise ApiValueError(f"Parameter `range` must be an integer when calling `{method_name}`")
        if self.api_client.client_side_validation and "creation_date" in kwargs and kwargs["creation_date"] is not None:
            if not isinstance(kwargs["creation_date"], str):
                raise ApiValueError(f"Parameter `creation_date` must be a string when calling `{method_name}`")

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        path_params["project_name"] = project_name

        if "range" in kwargs and kwargs["range"] is not None:
            query_params.append(("range", kwargs["range"]))
        if "creation_date" in kwargs and kwargs["creation_date"] is not None:
            query_params.append(("creation_date", kwargs["creation_date"]))

        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        url = "/projects/{project_name}/blobs"  # noqa: E501
        return self.api_client.call_api(
            url,
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type="list[BlobList]",
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", True),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", False),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", False),
        )

    def blobs_update_with_http_info(self, project_name, blob_id, file, **kwargs):
        """
        Update a blob

        This method makes a synchronous HTTP request by default. To make an asynchronous HTTP request, please
        pass async_req=True.

        >>> thread = Blobs.blobs_update_with_http_info(
                project_name, blob_id, file, async_req=True
            )
        >>> result = thread.get()

        :param str project_name: (required)
        :param str blob_id: (required)
        :param file file: (required)
        :param kwargs:
            - int blob_ttl:
            - bool _return_http_data_only: response data without head status code and headers
            - bool _preload_content: if False, the requests.Response object will be returned without reading/decoding
                response data. Default is True.
            - int|tuple _request_timeout: timeout setting for this request. If one number provided, it will be total
                request timeout. It can also be a pair (tuple) of (connection, read) timeouts.
            - bool async_req: execute request asynchronously
        :return: tuple(BlobList, status_code(int), headers(HTTPHeaderDict))
             If the method is called asynchronously, returns the request thread.
        """

        method_name = "blobs_update"
        optional_params = ["blob_ttl"]
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
        if self.api_client.client_side_validation and blob_id is None:
            raise ApiValueError(f"Missing the required parameter `blob_id` when calling `{method_name}`")
        if self.api_client.client_side_validation and file is None:
            raise ApiValueError(f"Missing the required parameter `file` when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(project_name, str):
                raise ApiValueError(f"Parameter `project_name` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation:
            if not isinstance(blob_id, str):
                raise ApiValueError(f"Parameter `blob_id` must be a string when calling `{method_name}`")
        if self.api_client.client_side_validation and "blob_ttl" in kwargs:
            if not isinstance(kwargs["blob_ttl"], int):
                raise ApiValueError(f"Parameter `blob_ttl` must be an integer when calling `{method_name}`")

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        files = {}
        body_params = None

        path_params["project_name"] = project_name
        path_params["blob_id"] = blob_id

        if "blob_ttl" in kwargs:
            header_params["blob-ttl"] = kwargs["blob_ttl"]

        files["file"] = file

        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["multipart/form-data"])

        url = "/projects/{project_name}/blobs/{blob_id}"  # noqa: E501
        return self.api_client.call_api(
            url,
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=files,
            response_type="BlobList",
            auth_settings=["api_key"],
            async_req=kwargs.get("async_req", False),
            _return_http_data_only=kwargs.get("_return_http_data_only", True),
            _preload_content=kwargs.get("_preload_content", True),
            _request_timeout=kwargs.get("_request_timeout", None),
            stream=kwargs.get("_request_stream", False),
            collection_formats=collection_formats,
            progress_bar=kwargs.get("_progress_bar", True),
        )

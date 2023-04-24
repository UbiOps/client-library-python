# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.  # noqa: E501

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ubiops.api_client import ApiClient
from ubiops.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ServiceUsers(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def service_users_create_with_http_info(self, project_name, data, **kwargs):  # noqa: E501
        """Create a new service user  # noqa: E501

         ### Description  Create a new service user. A unique email is generated for the service user. Additionally, a token for this service user is generated. This token can be used to authorize requests sent to our API. It is possible to set an expiry date for this token. In addition, allowed cors origins can be configured for the service user. The service user will be allowed to make a deployment or pipeline request from these origins.   The token is **ONLY** returned on creation and will not be accessible afterwards.  ### Optional Parameters - `name`: Name of the service user   - `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from   - `expiry_date`: Date when the service user account expires (UTC). If null is passed, the account will never expire.    #### Request Examples  ``` {   \"name\": \"service-user-1\" } ```  ``` {   \"name\": \"service-user-1\",   \"allowed_cors_origins\": [     \"https://test.com\"   ] } ```  ``` {   \"name\": \"service-user-1\",   \"expiry_date\": \"2020-01-01T00:00:00.000Z\" } ```  ### Response Structure  Details of the created service user - `id`: Unique identifier for the service user (UUID)   - `email`: Email of the service user    - `token`: The API token for the created service user    - `name`: Name of the service user   - `creation_date`: Date when the service user was created   - `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from   - `expiry_date`: Date when the service user account will expire (UTC)    #### Response Examples  ``` {   \"id\": \"13a9ba27-6888-4528-826e-8e1002eab13d\",   \"email\": \"13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com\",   \"token\": \"e962d9190348af7fa8d233d75cff7385b4335f81\",   \"name\": \"service-user-1\",   \"creation_date\": \"2020-03-24T09:16:27.504+00:00\",   \"allowed_cors_origins\": [     \"https://test.com\"   ],   \"expiry_date\": \"2021-03-24T00:00:00.000+00:00\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_users_create_with_http_info(project_name, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_name: (required)
        :param ServiceUserCreate data: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ServiceUserTokenDetail, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['project_name', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_users_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_name' is set
        if self.api_client.client_side_validation and (
            'project_name' not in local_var_params or local_var_params['project_name'] is None  # noqa: E501
        ):
            raise ApiValueError("Missing the required parameter `project_name` when calling `service_users_create`")  # noqa: E501
        # verify the required parameter 'data' is set
        if self.api_client.client_side_validation and (
            'data' not in local_var_params or local_var_params['data'] is None  # noqa: E501
        ):
            raise ApiValueError("Missing the required parameter `data` when calling `service_users_create`")  # noqa: E501
        if self.api_client.client_side_validation and (
            'project_name' in local_var_params and local_var_params['project_name'] is not None  # noqa: E501
        ):
            if not isinstance(local_var_params['project_name'], str):  # noqa: E501
                raise ApiValueError("Parameter `project_name` must be a string when calling `service_users_create`")  # noqa: E501
        if self.api_client.client_side_validation and (
            'data' in local_var_params and local_var_params['data'] is not None  # noqa: E501
        ):
            if isinstance(local_var_params['data'], dict):  # noqa: E501
                from ubiops.models.service_user_create import ServiceUserCreate

                local_var_params['data'] = ServiceUserCreate(**local_var_params['data'])  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_name' in local_var_params:
            path_params['project_name'] = local_var_params['project_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in local_var_params:
            body_params = local_var_params['data']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_name}/service-users', 'POST',  # noqa: E501
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServiceUserTokenDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_users_delete_with_http_info(self, project_name, service_user_id, **kwargs):  # noqa: E501
        """Delete service user  # noqa: E501

         ### Description  Delete a service user from a project   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_users_delete_with_http_info(project_name, service_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_name: (required)
        :param str service_user_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['project_name', 'service_user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_users_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_name' is set
        if self.api_client.client_side_validation and (
            'project_name' not in local_var_params or local_var_params['project_name'] is None  # noqa: E501
        ):
            raise ApiValueError("Missing the required parameter `project_name` when calling `service_users_delete`")  # noqa: E501
        # verify the required parameter 'service_user_id' is set
        if self.api_client.client_side_validation and (
            'service_user_id' not in local_var_params or local_var_params['service_user_id'] is None  # noqa: E501
        ):
            raise ApiValueError("Missing the required parameter `service_user_id` when calling `service_users_delete`")  # noqa: E501
        if self.api_client.client_side_validation and (
            'project_name' in local_var_params and local_var_params['project_name'] is not None  # noqa: E501
        ):
            if not isinstance(local_var_params['project_name'], str):  # noqa: E501
                raise ApiValueError("Parameter `project_name` must be a string when calling `service_users_delete`")  # noqa: E501
        if self.api_client.client_side_validation and (
            'service_user_id' in local_var_params and local_var_params['service_user_id'] is not None  # noqa: E501
        ):
            if not isinstance(local_var_params['service_user_id'], str):  # noqa: E501
                raise ApiValueError("Parameter `service_user_id` must be a string when calling `service_users_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_name' in local_var_params:
            path_params['project_name'] = local_var_params['project_name']  # noqa: E501
        if 'service_user_id' in local_var_params:
            path_params['service_user_id'] = local_var_params['service_user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_name}/service-users/{service_user_id}', 'DELETE',  # noqa: E501
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_users_get_with_http_info(self, project_name, service_user_id, **kwargs):  # noqa: E501
        """Retrieve details of a service user  # noqa: E501

         ### Description  Retrieve details of a service user  ### Response Structure  Details of the service user - `id`: Unique identifier for the service user (UUID)   - `email`: Email of the service user    - `name`: Name of the service user   - `creation_date`: Date when the service user was created   - `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from   - `expiry_date`: Date when the service user account will expire (UTC)    #### Response Examples  ``` {   \"id\": \"13a9ba27-6888-4528-826e-8e1002eab13d\",   \"email\": \"13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com\",   \"name\": \"new-service-user-name\",   \"creation_date\": \"2020-03-26T12:18:43.123+00:00\",   \"allowed_cors_origins\": [     \"https://test.com\"   ],   \"expiry_date\": null } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_users_get_with_http_info(project_name, service_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_name: (required)
        :param str service_user_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ServiceUserList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['project_name', 'service_user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_users_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_name' is set
        if self.api_client.client_side_validation and (
            'project_name' not in local_var_params or local_var_params['project_name'] is None  # noqa: E501
        ):
            raise ApiValueError("Missing the required parameter `project_name` when calling `service_users_get`")  # noqa: E501
        # verify the required parameter 'service_user_id' is set
        if self.api_client.client_side_validation and (
            'service_user_id' not in local_var_params or local_var_params['service_user_id'] is None  # noqa: E501
        ):
            raise ApiValueError("Missing the required parameter `service_user_id` when calling `service_users_get`")  # noqa: E501
        if self.api_client.client_side_validation and (
            'project_name' in local_var_params and local_var_params['project_name'] is not None  # noqa: E501
        ):
            if not isinstance(local_var_params['project_name'], str):  # noqa: E501
                raise ApiValueError("Parameter `project_name` must be a string when calling `service_users_get`")  # noqa: E501
        if self.api_client.client_side_validation and (
            'service_user_id' in local_var_params and local_var_params['service_user_id'] is not None  # noqa: E501
        ):
            if not isinstance(local_var_params['service_user_id'], str):  # noqa: E501
                raise ApiValueError("Parameter `service_user_id` must be a string when calling `service_users_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_name' in local_var_params:
            path_params['project_name'] = local_var_params['project_name']  # noqa: E501
        if 'service_user_id' in local_var_params:
            path_params['service_user_id'] = local_var_params['service_user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_name}/service-users/{service_user_id}', 'GET',  # noqa: E501
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServiceUserList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_users_list_with_http_info(self, project_name, **kwargs):  # noqa: E501
        """List service users  # noqa: E501

         ### Description  List service users defined in a project  ### Response Structure  List of details of the service users: - `id`: Unique identifier for the service user (UUID)   - `email`: Email of the service user   - `name`: Name of the service user   - `creation_date`: Date when the service user was created   - `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from   - `expiry_date`: Date when the service user account will expire (UTC)    #### Response Examples  ``` [   {     \"id\": \"537bca64-5ab6-43eb-a7ef-1638bc30b6ed\",     \"email\": \"537bca64-5ab6-43eb-a7ef-1638bc30b6ed.project1@serviceuser.ubiops.com\",     \"name\": \"service-user-1\",     \"creation_date\": \"2020-03-24T09:16:27.504+00:00\",     \"allowed_cors_origins\": [       \"https://test.com\"     ],     \"expiry_date\": \"2021-03-24T00:00:00.000+00:00\"   },   {     \"id\": \"13a9ba27-6888-4528-826e-8e1002eab13d\",     \"email\": \"13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com\",     \"name\": \"service-user-2\",     \"creation_date\": \"2020-03-26T12:18:43.123+00:00\",     \"allowed_cors_origins\": [       \"https://test.com\"     ],     \"expiry_date\": null   } ] ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_users_list_with_http_info(project_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_name: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ServiceUserList], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['project_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_users_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_name' is set
        if self.api_client.client_side_validation and (
            'project_name' not in local_var_params or local_var_params['project_name'] is None  # noqa: E501
        ):
            raise ApiValueError("Missing the required parameter `project_name` when calling `service_users_list`")  # noqa: E501
        if self.api_client.client_side_validation and (
            'project_name' in local_var_params and local_var_params['project_name'] is not None  # noqa: E501
        ):
            if not isinstance(local_var_params['project_name'], str):  # noqa: E501
                raise ApiValueError("Parameter `project_name` must be a string when calling `service_users_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_name' in local_var_params:
            path_params['project_name'] = local_var_params['project_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_name}/service-users', 'GET',  # noqa: E501
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ServiceUserList]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_users_token_with_http_info(self, project_name, service_user_id, **kwargs):  # noqa: E501
        """Reset the token of a service user  # noqa: E501

         ### Description  Reset the token of a service user. The old token will be deleted and a new one will be created for the service user. No data should be sent in the body of the request.  It is not possible to reset the token of a service user whose expiry date has been reached.  ### Response Structure  Details of the new token for the service user - `token`: The new API token for the service user  #### Response Examples ``` {   \"token\": \"e962d9190348af7fa8d233d75cff7385b4335f81\" } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_users_token_with_http_info(project_name, service_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_name: (required)
        :param str service_user_id: (required)
        :param object data:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ServiceUserTokenList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['project_name', 'service_user_id', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_users_token" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_name' is set
        if self.api_client.client_side_validation and (
            'project_name' not in local_var_params or local_var_params['project_name'] is None  # noqa: E501
        ):
            raise ApiValueError("Missing the required parameter `project_name` when calling `service_users_token`")  # noqa: E501
        # verify the required parameter 'service_user_id' is set
        if self.api_client.client_side_validation and (
            'service_user_id' not in local_var_params or local_var_params['service_user_id'] is None  # noqa: E501
        ):
            raise ApiValueError("Missing the required parameter `service_user_id` when calling `service_users_token`")  # noqa: E501
        if self.api_client.client_side_validation and (
            'project_name' in local_var_params and local_var_params['project_name'] is not None  # noqa: E501
        ):
            if not isinstance(local_var_params['project_name'], str):  # noqa: E501
                raise ApiValueError("Parameter `project_name` must be a string when calling `service_users_token`")  # noqa: E501
        if self.api_client.client_side_validation and (
            'service_user_id' in local_var_params and local_var_params['service_user_id'] is not None  # noqa: E501
        ):
            if not isinstance(local_var_params['service_user_id'], str):  # noqa: E501
                raise ApiValueError("Parameter `service_user_id` must be a string when calling `service_users_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_name' in local_var_params:
            path_params['project_name'] = local_var_params['project_name']  # noqa: E501
        if 'service_user_id' in local_var_params:
            path_params['service_user_id'] = local_var_params['service_user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in local_var_params:
            body_params = local_var_params['data']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_name}/service-users/{service_user_id}/token', 'PUT',  # noqa: E501
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServiceUserTokenList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_users_update_with_http_info(self, project_name, service_user_id, data, **kwargs):  # noqa: E501
        """Update service user details  # noqa: E501

         ### Description Update the name, expiry date and cors allowed origins of a service user. The new value for the cors_allowed_origin will replace the old value. Leave as an empty list to remove the previous list of allowed origins.  It is not possible to update a service user whose expiry date has been reached.  ### Optional Parameters - `name`: Name of the service user   - `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from   - `expiry_date`: Date when the service user account will expire (UTC). If null is passed, the account will never expire.    #### Request Examples   ``` {   \"name\": \"new-service-user-name\", } ```  ``` {   \"name\": \"service-user-1\",   \"allowed_cors_origins\": [     \"https://test.com\"   ] } ```  ``` {   \"expiry_date\": \"2020-01-01T00:00:00.000Z\" } ```  ### Response Structure  Details of the updated service user - `id`: Unique identifier for the service user (UUID)   - `email`: Email of the service user    - `name`: Name of the service user   - `creation_date`: Date when the service user was created   - `allowed_cors_origins`: List of origin url's of which the service user is allowed to make a request from   - `expiry_date`: Date when the service user account will expire (UTC)    #### Response Examples  ``` {   \"id\": \"13a9ba27-6888-4528-826e-8e1002eab13d\",   \"email\": \"13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.ubiops.com\",   \"name\": \"new-service-user-name\",   \"creation_date\": \"2020-03-26T12:18:43.123+00:00\",   \"allowed_cors_origins\": [     \"https://test.com\"   ],   \"expiry_date\": null } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_users_update_with_http_info(project_name, service_user_id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_name: (required)
        :param str service_user_id: (required)
        :param ServiceUserCreate data: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ServiceUserList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['project_name', 'service_user_id', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_users_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_name' is set
        if self.api_client.client_side_validation and (
            'project_name' not in local_var_params or local_var_params['project_name'] is None  # noqa: E501
        ):
            raise ApiValueError("Missing the required parameter `project_name` when calling `service_users_update`")  # noqa: E501
        # verify the required parameter 'service_user_id' is set
        if self.api_client.client_side_validation and (
            'service_user_id' not in local_var_params or local_var_params['service_user_id'] is None  # noqa: E501
        ):
            raise ApiValueError("Missing the required parameter `service_user_id` when calling `service_users_update`")  # noqa: E501
        # verify the required parameter 'data' is set
        if self.api_client.client_side_validation and (
            'data' not in local_var_params or local_var_params['data'] is None  # noqa: E501
        ):
            raise ApiValueError("Missing the required parameter `data` when calling `service_users_update`")  # noqa: E501
        if self.api_client.client_side_validation and (
            'project_name' in local_var_params and local_var_params['project_name'] is not None  # noqa: E501
        ):
            if not isinstance(local_var_params['project_name'], str):  # noqa: E501
                raise ApiValueError("Parameter `project_name` must be a string when calling `service_users_update`")  # noqa: E501
        if self.api_client.client_side_validation and (
            'service_user_id' in local_var_params and local_var_params['service_user_id'] is not None  # noqa: E501
        ):
            if not isinstance(local_var_params['service_user_id'], str):  # noqa: E501
                raise ApiValueError("Parameter `service_user_id` must be a string when calling `service_users_update`")  # noqa: E501
        if self.api_client.client_side_validation and (
            'data' in local_var_params and local_var_params['data'] is not None  # noqa: E501
        ):
            if isinstance(local_var_params['data'], dict):  # noqa: E501
                from ubiops.models.service_user_create import ServiceUserCreate

                local_var_params['data'] = ServiceUserCreate(**local_var_params['data'])  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_name' in local_var_params:
            path_params['project_name'] = local_var_params['project_name']  # noqa: E501
        if 'service_user_id' in local_var_params:
            path_params['service_user_id'] = local_var_params['service_user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in local_var_params:
            body_params = local_var_params['data']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_name}/service-users/{service_user_id}', 'PATCH',  # noqa: E501
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServiceUserList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
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
from ubiops.exceptions import (
    ApiTypeError,
    ApiValueError
)


class RequestSchedules(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def request_schedules_create_with_http_info(self, project_name, data, **kwargs):  # noqa: E501
        """Create request schedules  # noqa: E501

         ### Description Create a new request schedule with the provided name  ### Required Parameters - `name`: Name of the request. The name is unique per project. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. - `object_type`: Type of object for which the request is made. Can be either 'deployment' or 'pipeline'. - `object_name`: Name of deployment or pipeline for which the request is made - `schedule`: Schedule in crontab format  ### Optional Parameters - `version`: Name of version for which the request schedule is made. If not provided, default version of the deployment/pipeline will be used. - `request_data`: Input data for the request schedule. For structured deployments/pipelines, it must be a dictionary. - `timeout`: Timeout of the request in seconds - `enabled`: Boolean value indicating whether the request schedule is enabled or disabled. Default is 'True'. - `description`: Description of the request schedule - `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label  #### Request Examples  ``` {   \"name\": \"test-request\",   \"object_type\": \"deployment\",   \"object_name\": \"test-deployment\",   \"version\": \"v1\",   \"schedule\": \"0 * 3 * *\",   \"request_data\": {     \"input_field_1\": 2345,     \"input_field_2\": 8765   },   \"timeout\": 300,   \"enabled\": true,   \"description\": \"Daily request schedule\",   \"labels\": {     \"type\": \"daily\"   } } ```  ### Response Structure Details of the created request schedule - `name`: Name of the request - `object_type`: Type of object for which the request is made - `object_name`: Name of deployment/pipeline for which the request schedule is made - `schedule`: Schedule in crontab format - `version`: Name of version for which the request schedule is made - `request_data`: Input data for the request schedule - `timeout`: Timeout of the request in seconds - `enabled`: Boolean value indicating whether the request schedule is enabled or disabled - `creation_date`: The date when the request schedule was created - `description`: Description of the request schedule - `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label  #### Response Examples ``` {   \"id\": \"b4a06aed-f7ab-48b3-b579-b12b62db8058\",   \"name\": \"test-request\",   \"object_type\": \"deployment\",   \"object_name\": \"test-deployment\",   \"version\": \"v1\",   \"schedule\": \"0 * 3 * *\",   \"request_data\": {     \"input_field_1\": 2345,     \"input_field_2\": 8765   },   \"timeout\": 300,   \"enabled\": true,   \"creation_date\": \"2020-09-16T08:06:34.457679Z\",   \"description\": \"Daily request schedule\",   \"labels\": {     \"type\": \"daily\"   } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_schedules_create_with_http_info(project_name, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_name: (required)
        :param ScheduleCreate data: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ScheduleList, status_code(int), headers(HTTPHeaderDict))
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
                    " to method request_schedules_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_name' is set
        if self.api_client.client_side_validation and ('project_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_name` when calling `request_schedules_create`")  # noqa: E501
        # verify the required parameter 'data' is set
        if self.api_client.client_side_validation and ('data' not in local_var_params or  # noqa: E501
                                                        local_var_params['data'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data` when calling `request_schedules_create`")  # noqa: E501
        if (self.api_client.client_side_validation and 'project_name' in local_var_params
            and local_var_params['project_name'] is not None):  # noqa: E501
            if not isinstance(local_var_params['project_name'], str):  # noqa: E501
                raise ApiValueError("Parameter `project_name` must be a string when calling `request_schedules_create`")  # noqa: E501
        if (self.api_client.client_side_validation and 'data' in local_var_params
            and local_var_params['data'] is not None):  # noqa: E501
            if isinstance(local_var_params['data'], dict):  # noqa: E501
                from ubiops.models.schedule_create import ScheduleCreate

                local_var_params['data'] = ScheduleCreate(**local_var_params['data'])  # noqa: E501

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
            '/projects/{project_name}/schedules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ScheduleList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def request_schedules_delete_with_http_info(self, project_name, schedule_name, **kwargs):  # noqa: E501
        """Delete a request schedule  # noqa: E501

         ### Description Delete the request schedule from the project.  If you want to temporarily disable a request schedule, update the request with `enabled` set to False.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_schedules_delete_with_http_info(project_name, schedule_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_name: (required)
        :param str schedule_name: (required)
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

        all_params = ['project_name', 'schedule_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_schedules_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_name' is set
        if self.api_client.client_side_validation and ('project_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_name` when calling `request_schedules_delete`")  # noqa: E501
        # verify the required parameter 'schedule_name' is set
        if self.api_client.client_side_validation and ('schedule_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['schedule_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `schedule_name` when calling `request_schedules_delete`")  # noqa: E501
        if (self.api_client.client_side_validation and 'project_name' in local_var_params
            and local_var_params['project_name'] is not None):  # noqa: E501
            if not isinstance(local_var_params['project_name'], str):  # noqa: E501
                raise ApiValueError("Parameter `project_name` must be a string when calling `request_schedules_delete`")  # noqa: E501
        if (self.api_client.client_side_validation and 'schedule_name' in local_var_params
            and local_var_params['schedule_name'] is not None):  # noqa: E501
            if not isinstance(local_var_params['schedule_name'], str):  # noqa: E501
                raise ApiValueError("Parameter `schedule_name` must be a string when calling `request_schedules_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_name' in local_var_params:
            path_params['project_name'] = local_var_params['project_name']  # noqa: E501
        if 'schedule_name' in local_var_params:
            path_params['schedule_name'] = local_var_params['schedule_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_name}/schedules/{schedule_name}', 'DELETE',
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

    def request_schedules_get_with_http_info(self, project_name, schedule_name, **kwargs):  # noqa: E501
        """Get details of a request schedule  # noqa: E501

         ### Description Retrieve details of a single request schedule  ### Response Structure Details of a request schedule - `name`: Name of the request - `object_type`: Type of object for which the request is made - `object_name`: Name of deployment/pipeline for which the request is made - `schedule`: Schedule in crontab format - `version`: Name of version for which the request schedule is made - `request_data`: Input data for the request schedule - `timeout`: Timeout of the request in seconds - `enabled`: Boolean value indicating whether the request schedule is enabled or disabled - `creation_date`: The date when the request schedule was created - `description`: Description of the request schedule - `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label  #### Response Examples ``` {   \"id\": \"b4a06aed-f7ab-48b3-b579-b12b62db8058\",   \"name\": \"test-request\",   \"object_type\": \"deployment\",   \"object_name\": \"test-deployment\",   \"version\": \"v1\",   \"schedule\": \"0 * 3 * *\",   \"request_data\": {     \"input_field_1\": 2345,     \"input_field_2\": 8765   },   \"timeout\": 200,   \"enabled\": true,   \"creation_date\": \"2020-09-16T08:06:34.457679Z\",   \"description\": \"Daily request schedule\",   \"labels\": {     \"type\": \"daily\"   } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_schedules_get_with_http_info(project_name, schedule_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_name: (required)
        :param str schedule_name: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ScheduleList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['project_name', 'schedule_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_schedules_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_name' is set
        if self.api_client.client_side_validation and ('project_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_name` when calling `request_schedules_get`")  # noqa: E501
        # verify the required parameter 'schedule_name' is set
        if self.api_client.client_side_validation and ('schedule_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['schedule_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `schedule_name` when calling `request_schedules_get`")  # noqa: E501
        if (self.api_client.client_side_validation and 'project_name' in local_var_params
            and local_var_params['project_name'] is not None):  # noqa: E501
            if not isinstance(local_var_params['project_name'], str):  # noqa: E501
                raise ApiValueError("Parameter `project_name` must be a string when calling `request_schedules_get`")  # noqa: E501
        if (self.api_client.client_side_validation and 'schedule_name' in local_var_params
            and local_var_params['schedule_name'] is not None):  # noqa: E501
            if not isinstance(local_var_params['schedule_name'], str):  # noqa: E501
                raise ApiValueError("Parameter `schedule_name` must be a string when calling `request_schedules_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_name' in local_var_params:
            path_params['project_name'] = local_var_params['project_name']  # noqa: E501
        if 'schedule_name' in local_var_params:
            path_params['schedule_name'] = local_var_params['schedule_name']  # noqa: E501

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
            '/projects/{project_name}/schedules/{schedule_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ScheduleList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def request_schedules_list_with_http_info(self, project_name, **kwargs):  # noqa: E501
        """List request schedules  # noqa: E501

         ### Description List the request schedules in a project. The user has to have 'requests.list' permission on either 'deployments.versions' or 'pipelines.versions' to list the request schedules.  ### Optional Parameters - `labels`: Filter on labels of the request schedules. Should be given in the format 'label:label_value'. Separate multiple label-pairs with a comma (,). This parameter should be given as query parameter.  ### Response Structure A list of details of all request schedules in a project - `name`: Name of the request - `object_type`: Type of object for which the request is made - `object_name`: Name of deployment/pipeline for which the request is made - `schedule`: Schedule in crontab format - `version`: Name of version for which the request schedule is made - `request_data`: Input data for the request schedule - `timeout`: Timeout of the request in seconds - `enabled`: Boolean value indicating whether the request schedule is enabled or disabled - `creation_date`: The date when the request schedule was created - `description`: Description of the request schedule - `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label  #### Response Examples ``` [   {     \"id\": \"b4a06aed-f7ab-48b3-b579-b12b62db8058\",     \"name\": \"test-request\",     \"object_type\": \"deployment\",     \"object_name\": \"test-deployment\",     \"version\": \"v1\",     \"schedule\": \"0 * 3 * *\",     \"request_data\": {       \"input_field_1\": 2345,       \"input_field_2\": 8765     },     \"timeout\": 200,     \"enabled\": true,     \"creation_date\": \"2020-09-16T08:06:34.457679Z\",     \"description\": \"Daily request schedule\",     \"labels\": {       \"type\": \"daily\"     }   } ] ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_schedules_list_with_http_info(project_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_name: (required)
        :param str labels:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ScheduleList], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['project_name', 'labels']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_schedules_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_name' is set
        if self.api_client.client_side_validation and ('project_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_name` when calling `request_schedules_list`")  # noqa: E501
        if (self.api_client.client_side_validation and 'project_name' in local_var_params
            and local_var_params['project_name'] is not None):  # noqa: E501
            if not isinstance(local_var_params['project_name'], str):  # noqa: E501
                raise ApiValueError("Parameter `project_name` must be a string when calling `request_schedules_list`")  # noqa: E501
        if (self.api_client.client_side_validation and 'labels' in local_var_params
            and local_var_params['labels'] is not None):  # noqa: E501
            if not isinstance(local_var_params['labels'], str):  # noqa: E501
                raise ApiValueError("Parameter `labels` must be a string when calling `request_schedules_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_name' in local_var_params:
            path_params['project_name'] = local_var_params['project_name']  # noqa: E501

        query_params = []
        if 'labels' in local_var_params and local_var_params['labels'] is not None:  # noqa: E501
            query_params.append(('labels', local_var_params['labels']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_name}/schedules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ScheduleList]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def request_schedules_update_with_http_info(self, project_name, schedule_name, data, **kwargs):  # noqa: E501
        """Update a request schedule  # noqa: E501

         ### Description Update a request schedule in a project  ### Optional Parameters - `name`: Name of the request. The name is unique per project. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. - `schedule`: Schedule in crontab format - `request_data`: Input data for the request schedule. For structured deployments/pipelines, it must be a dictionary. - `timeout`: Timeout of the request in seconds - `enabled`: Boolean value indicating whether the request schedule is enabled or disabled. Default is 'True'. - `description`: Description of the request schedule - `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label  #### Request Examples ``` {   \"name\": \"test-request\",   \"schedule\": \"0 * 3 * *\",   \"request_data\": {     \"input_field_1\": 2345,     \"input_field_2\": 8765   },   \"timeout\": 360,   \"enabled\": false } ```  ### Response Structure Details of the updated request schedule - `name`: Name of the request - `object_type`: Type of object for which the request is made - `object_name`: Name of deployment/pipeline for which the request is made - `schedule`: Schedule in crontab format - `version`: Name of version for which the request schedule is made - `request_data`: Input data for the request schedule - `timeout`: Timeout of the request in seconds - `enabled`: Boolean value indicating whether the request schedule is enabled or disabled - `creation_date`: The date when the request schedule was created - `description`: Description of the request schedule - `labels`: Dictionary containing key/value pairs where key indicates the label and value is the corresponding value of that label  #### Response Examples ``` {   \"id\": \"b4a06aed-f7ab-48b3-b579-b12b62db8058\",   \"name\": \"test-request\",   \"object_type\": \"deployment\",   \"object_name\": \"test-deployment\",   \"version\": \"v1\",   \"schedule\": \"0 * 3 * *\",   \"request_data\": {     \"input_field_1\": 2345,     \"input_field_2\": 8765   },   \"timeout\": 360,   \"enabled\": true,   \"creation_date\": \"2020-09-16T08:06:34.457679Z\",   \"description\": \"Daily request schedule\",   \"labels\": {     \"type\": \"daily\"   } } ```   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_schedules_update_with_http_info(project_name, schedule_name, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_name: (required)
        :param str schedule_name: (required)
        :param ScheduleUpdate data: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ScheduleList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['project_name', 'schedule_name', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_schedules_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_name' is set
        if self.api_client.client_side_validation and ('project_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['project_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project_name` when calling `request_schedules_update`")  # noqa: E501
        # verify the required parameter 'schedule_name' is set
        if self.api_client.client_side_validation and ('schedule_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['schedule_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `schedule_name` when calling `request_schedules_update`")  # noqa: E501
        # verify the required parameter 'data' is set
        if self.api_client.client_side_validation and ('data' not in local_var_params or  # noqa: E501
                                                        local_var_params['data'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data` when calling `request_schedules_update`")  # noqa: E501
        if (self.api_client.client_side_validation and 'project_name' in local_var_params
            and local_var_params['project_name'] is not None):  # noqa: E501
            if not isinstance(local_var_params['project_name'], str):  # noqa: E501
                raise ApiValueError("Parameter `project_name` must be a string when calling `request_schedules_update`")  # noqa: E501
        if (self.api_client.client_side_validation and 'schedule_name' in local_var_params
            and local_var_params['schedule_name'] is not None):  # noqa: E501
            if not isinstance(local_var_params['schedule_name'], str):  # noqa: E501
                raise ApiValueError("Parameter `schedule_name` must be a string when calling `request_schedules_update`")  # noqa: E501
        if (self.api_client.client_side_validation and 'data' in local_var_params
            and local_var_params['data'] is not None):  # noqa: E501
            if isinstance(local_var_params['data'], dict):  # noqa: E501
                from ubiops.models.schedule_update import ScheduleUpdate

                local_var_params['data'] = ScheduleUpdate(**local_var_params['data'])  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_name' in local_var_params:
            path_params['project_name'] = local_var_params['project_name']  # noqa: E501
        if 'schedule_name' in local_var_params:
            path_params['schedule_name'] = local_var_params['schedule_name']  # noqa: E501

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
            '/projects/{project_name}/schedules/{schedule_name}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ScheduleList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

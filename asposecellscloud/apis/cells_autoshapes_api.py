# coding: utf-8

"""
    Web API Swagger specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CellsAutoshapesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def cells_autoshapes_get_worksheet_autoshape(self, name, sheet_name, autoshape_number, **kwargs):
        """
        Get autoshape info.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_autoshapes_get_worksheet_autoshape(name, sheet_name, autoshape_number, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Document name. (required)
        :param str sheet_name: Worksheet name. (required)
        :param int autoshape_number: The autoshape number. (required)
        :param str folder: The document folder.
        :param str storage: storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cells_autoshapes_get_worksheet_autoshape_with_http_info(name, sheet_name, autoshape_number, **kwargs)
        else:
            (data) = self.cells_autoshapes_get_worksheet_autoshape_with_http_info(name, sheet_name, autoshape_number, **kwargs)
            return data

    def cells_autoshapes_get_worksheet_autoshape_with_http_info(self, name, sheet_name, autoshape_number, **kwargs):
        """
        Get autoshape info.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_autoshapes_get_worksheet_autoshape_with_http_info(name, sheet_name, autoshape_number, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Document name. (required)
        :param str sheet_name: Worksheet name. (required)
        :param int autoshape_number: The autoshape number. (required)
        :param str folder: The document folder.
        :param str storage: storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'sheet_name', 'autoshape_number', 'folder', 'storage']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cells_autoshapes_get_worksheet_autoshape" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `cells_autoshapes_get_worksheet_autoshape`")
        # verify the required parameter 'sheet_name' is set
        if ('sheet_name' not in params) or (params['sheet_name'] is None):
            raise ValueError("Missing the required parameter `sheet_name` when calling `cells_autoshapes_get_worksheet_autoshape`")
        # verify the required parameter 'autoshape_number' is set
        if ('autoshape_number' not in params) or (params['autoshape_number'] is None):
            raise ValueError("Missing the required parameter `autoshape_number` when calling `cells_autoshapes_get_worksheet_autoshape`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']
        if 'sheet_name' in params:
            path_params['sheetName'] = params['sheet_name']
        if 'autoshape_number' in params:
            path_params['autoshapeNumber'] = params['autoshape_number']

        query_params = []
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/{name}/worksheets/{sheetName}/autoshapes/{autoshapeNumber}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='file',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def cells_autoshapes_get_worksheet_autoshapes(self, name, sheet_name, **kwargs):
        """
        Get worksheet autoshapes info.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_autoshapes_get_worksheet_autoshapes(name, sheet_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Document name. (required)
        :param str sheet_name: The worksheet name. (required)
        :param str folder: Document's folder.
        :param str storage: storage name.
        :return: AutoShapesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cells_autoshapes_get_worksheet_autoshapes_with_http_info(name, sheet_name, **kwargs)
        else:
            (data) = self.cells_autoshapes_get_worksheet_autoshapes_with_http_info(name, sheet_name, **kwargs)
            return data

    def cells_autoshapes_get_worksheet_autoshapes_with_http_info(self, name, sheet_name, **kwargs):
        """
        Get worksheet autoshapes info.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_autoshapes_get_worksheet_autoshapes_with_http_info(name, sheet_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Document name. (required)
        :param str sheet_name: The worksheet name. (required)
        :param str folder: Document's folder.
        :param str storage: storage name.
        :return: AutoShapesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'sheet_name', 'folder', 'storage']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cells_autoshapes_get_worksheet_autoshapes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `cells_autoshapes_get_worksheet_autoshapes`")
        # verify the required parameter 'sheet_name' is set
        if ('sheet_name' not in params) or (params['sheet_name'] is None):
            raise ValueError("Missing the required parameter `sheet_name` when calling `cells_autoshapes_get_worksheet_autoshapes`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']
        if 'sheet_name' in params:
            path_params['sheetName'] = params['sheet_name']

        query_params = []
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/{name}/worksheets/{sheetName}/autoshapes', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AutoShapesResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

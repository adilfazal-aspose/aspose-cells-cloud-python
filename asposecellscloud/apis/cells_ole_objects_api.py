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


class CellsOleObjectsApi(object):
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

    def cells_ole_objects_delete_worksheet_ole_object(self, name, sheet_name, ole_object_index, **kwargs):
        """
        Delete OLE object.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_ole_objects_delete_worksheet_ole_object(name, sheet_name, ole_object_index, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The workbook name. (required)
        :param str sheet_name: The worsheet name. (required)
        :param int ole_object_index: Ole object index (required)
        :param str folder: The workbook folder.
        :param str storage: storage name.
        :return: SaaSposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cells_ole_objects_delete_worksheet_ole_object_with_http_info(name, sheet_name, ole_object_index, **kwargs)
        else:
            (data) = self.cells_ole_objects_delete_worksheet_ole_object_with_http_info(name, sheet_name, ole_object_index, **kwargs)
            return data

    def cells_ole_objects_delete_worksheet_ole_object_with_http_info(self, name, sheet_name, ole_object_index, **kwargs):
        """
        Delete OLE object.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_ole_objects_delete_worksheet_ole_object_with_http_info(name, sheet_name, ole_object_index, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The workbook name. (required)
        :param str sheet_name: The worsheet name. (required)
        :param int ole_object_index: Ole object index (required)
        :param str folder: The workbook folder.
        :param str storage: storage name.
        :return: SaaSposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'sheet_name', 'ole_object_index', 'folder', 'storage']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cells_ole_objects_delete_worksheet_ole_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `cells_ole_objects_delete_worksheet_ole_object`")
        # verify the required parameter 'sheet_name' is set
        if ('sheet_name' not in params) or (params['sheet_name'] is None):
            raise ValueError("Missing the required parameter `sheet_name` when calling `cells_ole_objects_delete_worksheet_ole_object`")
        # verify the required parameter 'ole_object_index' is set
        if ('ole_object_index' not in params) or (params['ole_object_index'] is None):
            raise ValueError("Missing the required parameter `ole_object_index` when calling `cells_ole_objects_delete_worksheet_ole_object`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']
        if 'sheet_name' in params:
            path_params['sheetName'] = params['sheet_name']
        if 'ole_object_index' in params:
            path_params['oleObjectIndex'] = params['ole_object_index']

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

        return self.api_client.call_api('/cells/{name}/worksheets/{sheetName}/oleobjects/{oleObjectIndex}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SaaSposeResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def cells_ole_objects_delete_worksheet_ole_objects(self, name, sheet_name, **kwargs):
        """
        Delete all OLE objects.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_ole_objects_delete_worksheet_ole_objects(name, sheet_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The workbook name. (required)
        :param str sheet_name: The worsheet name. (required)
        :param str folder: The workbook folder.
        :param str storage: storage name.
        :return: SaaSposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cells_ole_objects_delete_worksheet_ole_objects_with_http_info(name, sheet_name, **kwargs)
        else:
            (data) = self.cells_ole_objects_delete_worksheet_ole_objects_with_http_info(name, sheet_name, **kwargs)
            return data

    def cells_ole_objects_delete_worksheet_ole_objects_with_http_info(self, name, sheet_name, **kwargs):
        """
        Delete all OLE objects.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_ole_objects_delete_worksheet_ole_objects_with_http_info(name, sheet_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The workbook name. (required)
        :param str sheet_name: The worsheet name. (required)
        :param str folder: The workbook folder.
        :param str storage: storage name.
        :return: SaaSposeResponse
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
                    " to method cells_ole_objects_delete_worksheet_ole_objects" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `cells_ole_objects_delete_worksheet_ole_objects`")
        # verify the required parameter 'sheet_name' is set
        if ('sheet_name' not in params) or (params['sheet_name'] is None):
            raise ValueError("Missing the required parameter `sheet_name` when calling `cells_ole_objects_delete_worksheet_ole_objects`")


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

        return self.api_client.call_api('/cells/{name}/worksheets/{sheetName}/oleobjects', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SaaSposeResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def cells_ole_objects_get_worksheet_ole_object(self, name, sheet_name, object_number, **kwargs):
        """
        Get OLE object info.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_ole_objects_get_worksheet_ole_object(name, sheet_name, object_number, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Document name. (required)
        :param str sheet_name: Worksheet name. (required)
        :param int object_number: The object number. (required)
        :param str folder: The document folder.
        :param str storage: storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cells_ole_objects_get_worksheet_ole_object_with_http_info(name, sheet_name, object_number, **kwargs)
        else:
            (data) = self.cells_ole_objects_get_worksheet_ole_object_with_http_info(name, sheet_name, object_number, **kwargs)
            return data

    def cells_ole_objects_get_worksheet_ole_object_with_http_info(self, name, sheet_name, object_number, **kwargs):
        """
        Get OLE object info.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_ole_objects_get_worksheet_ole_object_with_http_info(name, sheet_name, object_number, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Document name. (required)
        :param str sheet_name: Worksheet name. (required)
        :param int object_number: The object number. (required)
        :param str folder: The document folder.
        :param str storage: storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'sheet_name', 'object_number', 'folder', 'storage']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cells_ole_objects_get_worksheet_ole_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `cells_ole_objects_get_worksheet_ole_object`")
        # verify the required parameter 'sheet_name' is set
        if ('sheet_name' not in params) or (params['sheet_name'] is None):
            raise ValueError("Missing the required parameter `sheet_name` when calling `cells_ole_objects_get_worksheet_ole_object`")
        # verify the required parameter 'object_number' is set
        if ('object_number' not in params) or (params['object_number'] is None):
            raise ValueError("Missing the required parameter `object_number` when calling `cells_ole_objects_get_worksheet_ole_object`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']
        if 'sheet_name' in params:
            path_params['sheetName'] = params['sheet_name']
        if 'object_number' in params:
            path_params['objectNumber'] = params['object_number']

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

        return self.api_client.call_api('/cells/{name}/worksheets/{sheetName}/oleobjects/{objectNumber}', 'GET',
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

    def cells_ole_objects_get_worksheet_ole_objects(self, name, sheet_name, **kwargs):
        """
        Get worksheet OLE objects info.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_ole_objects_get_worksheet_ole_objects(name, sheet_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Document name. (required)
        :param str sheet_name: The worksheet name. (required)
        :param str folder: Document's folder.
        :param str storage: storage name.
        :return: OleObjectsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cells_ole_objects_get_worksheet_ole_objects_with_http_info(name, sheet_name, **kwargs)
        else:
            (data) = self.cells_ole_objects_get_worksheet_ole_objects_with_http_info(name, sheet_name, **kwargs)
            return data

    def cells_ole_objects_get_worksheet_ole_objects_with_http_info(self, name, sheet_name, **kwargs):
        """
        Get worksheet OLE objects info.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_ole_objects_get_worksheet_ole_objects_with_http_info(name, sheet_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Document name. (required)
        :param str sheet_name: The worksheet name. (required)
        :param str folder: Document's folder.
        :param str storage: storage name.
        :return: OleObjectsResponse
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
                    " to method cells_ole_objects_get_worksheet_ole_objects" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `cells_ole_objects_get_worksheet_ole_objects`")
        # verify the required parameter 'sheet_name' is set
        if ('sheet_name' not in params) or (params['sheet_name'] is None):
            raise ValueError("Missing the required parameter `sheet_name` when calling `cells_ole_objects_get_worksheet_ole_objects`")


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

        return self.api_client.call_api('/cells/{name}/worksheets/{sheetName}/oleobjects', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='OleObjectsResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def cells_ole_objects_post_update_worksheet_ole_object(self, name, sheet_name, ole_object_index, **kwargs):
        """
        Update OLE object.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_ole_objects_post_update_worksheet_ole_object(name, sheet_name, ole_object_index, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The workbook name. (required)
        :param str sheet_name: The worsheet name. (required)
        :param int ole_object_index: Ole object index (required)
        :param OleObject ole: Ole Object
        :param str folder: The workbook folder.
        :param str storage: storage name.
        :return: SaaSposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cells_ole_objects_post_update_worksheet_ole_object_with_http_info(name, sheet_name, ole_object_index, **kwargs)
        else:
            (data) = self.cells_ole_objects_post_update_worksheet_ole_object_with_http_info(name, sheet_name, ole_object_index, **kwargs)
            return data

    def cells_ole_objects_post_update_worksheet_ole_object_with_http_info(self, name, sheet_name, ole_object_index, **kwargs):
        """
        Update OLE object.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_ole_objects_post_update_worksheet_ole_object_with_http_info(name, sheet_name, ole_object_index, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The workbook name. (required)
        :param str sheet_name: The worsheet name. (required)
        :param int ole_object_index: Ole object index (required)
        :param OleObject ole: Ole Object
        :param str folder: The workbook folder.
        :param str storage: storage name.
        :return: SaaSposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'sheet_name', 'ole_object_index', 'ole', 'folder', 'storage']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cells_ole_objects_post_update_worksheet_ole_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `cells_ole_objects_post_update_worksheet_ole_object`")
        # verify the required parameter 'sheet_name' is set
        if ('sheet_name' not in params) or (params['sheet_name'] is None):
            raise ValueError("Missing the required parameter `sheet_name` when calling `cells_ole_objects_post_update_worksheet_ole_object`")
        # verify the required parameter 'ole_object_index' is set
        if ('ole_object_index' not in params) or (params['ole_object_index'] is None):
            raise ValueError("Missing the required parameter `ole_object_index` when calling `cells_ole_objects_post_update_worksheet_ole_object`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']
        if 'sheet_name' in params:
            path_params['sheetName'] = params['sheet_name']
        if 'ole_object_index' in params:
            path_params['oleObjectIndex'] = params['ole_object_index']

        query_params = []
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ole' in params:
            body_params = params['ole']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/{name}/worksheets/{sheetName}/oleobjects/{oleObjectIndex}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SaaSposeResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def cells_ole_objects_put_worksheet_ole_object(self, name, sheet_name, **kwargs):
        """
        Add OLE object
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_ole_objects_put_worksheet_ole_object(name, sheet_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The workbook name. (required)
        :param str sheet_name: The worsheet name. (required)
        :param OleObject ole_object: Ole Object
        :param int upper_left_row: Upper left row index
        :param int upper_left_column: Upper left column index
        :param int height: Height of oleObject, in unit of pixel
        :param int width: Width of oleObject, in unit of pixel
        :param str ole_file: OLE filename
        :param str image_file: Image filename
        :param str folder: The workbook folder.
        :param str storage: storage name.
        :return: OleObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cells_ole_objects_put_worksheet_ole_object_with_http_info(name, sheet_name, **kwargs)
        else:
            (data) = self.cells_ole_objects_put_worksheet_ole_object_with_http_info(name, sheet_name, **kwargs)
            return data

    def cells_ole_objects_put_worksheet_ole_object_with_http_info(self, name, sheet_name, **kwargs):
        """
        Add OLE object
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_ole_objects_put_worksheet_ole_object_with_http_info(name, sheet_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: The workbook name. (required)
        :param str sheet_name: The worsheet name. (required)
        :param OleObject ole_object: Ole Object
        :param int upper_left_row: Upper left row index
        :param int upper_left_column: Upper left column index
        :param int height: Height of oleObject, in unit of pixel
        :param int width: Width of oleObject, in unit of pixel
        :param str ole_file: OLE filename
        :param str image_file: Image filename
        :param str folder: The workbook folder.
        :param str storage: storage name.
        :return: OleObjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'sheet_name', 'ole_object', 'upper_left_row', 'upper_left_column', 'height', 'width', 'ole_file', 'image_file', 'folder', 'storage']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cells_ole_objects_put_worksheet_ole_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `cells_ole_objects_put_worksheet_ole_object`")
        # verify the required parameter 'sheet_name' is set
        if ('sheet_name' not in params) or (params['sheet_name'] is None):
            raise ValueError("Missing the required parameter `sheet_name` when calling `cells_ole_objects_put_worksheet_ole_object`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']
        if 'sheet_name' in params:
            path_params['sheetName'] = params['sheet_name']

        query_params = []
        if 'upper_left_row' in params:
            query_params.append(('upperLeftRow', params['upper_left_row']))
        if 'upper_left_column' in params:
            query_params.append(('upperLeftColumn', params['upper_left_column']))
        if 'height' in params:
            query_params.append(('height', params['height']))
        if 'width' in params:
            query_params.append(('width', params['width']))
        if 'ole_file' in params:
            query_params.append(('oleFile', params['ole_file']))
        if 'image_file' in params:
            query_params.append(('imageFile', params['image_file']))
        if 'folder' in params:
            query_params.append(('folder', params['folder']))
        if 'storage' in params:
            query_params.append(('storage', params['storage']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ole_object' in params:
            body_params = params['ole_object']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/{name}/worksheets/{sheetName}/oleobjects', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='OleObjectResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

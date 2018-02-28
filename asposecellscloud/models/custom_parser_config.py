# coding: utf-8

"""
    Web API Swagger specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CustomParserConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'column_index': 'int',
        'parse_method': 'str',
        'custom_style': 'str'
    }

    attribute_map = {
        'column_index': 'ColumnIndex',
        'parse_method': 'ParseMethod',
        'custom_style': 'CustomStyle'
    }
    
    def get_swagger_types(self):
        return CustomParserConfig.swagger_types
        
    def get_attribute_map(self):
        return CustomParserConfig.attribute_map
    
    """
        Associative dict for storing property values
    """
    container = {}
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, column_index=None, parse_method=None, custom_style=None):
        """
        CustomParserConfig - a model defined in Swagger
        """

        self.container['column_index'] = None
        self.container['parse_method'] = None
        self.container['custom_style'] = None

        if column_index is not None:
          self.column_index = column_index
        if parse_method is not None:
          self.parse_method = parse_method
        if custom_style is not None:
          self.custom_style = custom_style

    @property
    def column_index(self):
        """
        Gets the column_index of this CustomParserConfig.

        :return: The column_index of this CustomParserConfig.
        :rtype: int
        """
        return self.container['column_index']

    @column_index.setter
    def column_index(self, column_index):
        """
        Sets the column_index of this CustomParserConfig.

        :param column_index: The column_index of this CustomParserConfig.
        :type: int
        """

        self.container['column_index'] = column_index

    @property
    def parse_method(self):
        """
        Gets the parse_method of this CustomParserConfig.

        :return: The parse_method of this CustomParserConfig.
        :rtype: str
        """
        return self.container['parse_method']

    @parse_method.setter
    def parse_method(self, parse_method):
        """
        Sets the parse_method of this CustomParserConfig.

        :param parse_method: The parse_method of this CustomParserConfig.
        :type: str
        """

        self.container['parse_method'] = parse_method

    @property
    def custom_style(self):
        """
        Gets the custom_style of this CustomParserConfig.

        :return: The custom_style of this CustomParserConfig.
        :rtype: str
        """
        return self.container['custom_style']

    @custom_style.setter
    def custom_style(self, custom_style):
        """
        Sets the custom_style of this CustomParserConfig.

        :param custom_style: The custom_style of this CustomParserConfig.
        :type: str
        """

        self.container['custom_style'] = custom_style

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.get_swagger_types()):
            value = self.get_from_container(attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CustomParserConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
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
from . import SaaSposeResponse

class RowsResponse(SaaSposeResponse):
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
        'rows': 'Rows'
    }

    attribute_map = {
        'rows': 'Rows'
    }
    
    def get_swagger_types(self):
        return dict(RowsResponse.swagger_types, **SaaSposeResponse.get_swagger_types(self))
        
    def get_attribute_map(self):
        return dict(RowsResponse.attribute_map, **SaaSposeResponse.get_attribute_map(self))
    
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, rows=None):
        """
        RowsResponse - a model defined in Swagger
        """

        self.container['rows'] = None

        if rows is not None:
          self.rows = rows

    @property
    def rows(self):
        """
        Gets the rows of this RowsResponse.

        :return: The rows of this RowsResponse.
        :rtype: Rows
        """
        return self.container['rows']

    @rows.setter
    def rows(self, rows):
        """
        Sets the rows of this RowsResponse.

        :param rows: The rows of this RowsResponse.
        :type: Rows
        """

        self.container['rows'] = rows

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
        if not isinstance(other, RowsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
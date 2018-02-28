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


class Area(object):
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
        'background_color': 'Color',
        'fill_format': 'FillFormat',
        'foreground_color': 'Color',
        'format': 'str',
        'invert_if_negative': 'bool',
        'transparency': 'float'
    }

    attribute_map = {
        'background_color': 'BackgroundColor',
        'fill_format': 'FillFormat',
        'foreground_color': 'ForegroundColor',
        'format': 'Format',
        'invert_if_negative': 'InvertIfNegative',
        'transparency': 'Transparency'
    }
    
    def get_swagger_types(self):
        return Area.swagger_types
        
    def get_attribute_map(self):
        return Area.attribute_map
    
    """
        Associative dict for storing property values
    """
    container = {}
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, background_color=None, fill_format=None, foreground_color=None, format=None, invert_if_negative=None, transparency=None):
        """
        Area - a model defined in Swagger
        """

        self.container['background_color'] = None
        self.container['fill_format'] = None
        self.container['foreground_color'] = None
        self.container['format'] = None
        self.container['invert_if_negative'] = None
        self.container['transparency'] = None

        if background_color is not None:
          self.background_color = background_color
        if fill_format is not None:
          self.fill_format = fill_format
        if foreground_color is not None:
          self.foreground_color = foreground_color
        if format is not None:
          self.format = format
        if invert_if_negative is not None:
          self.invert_if_negative = invert_if_negative
        if transparency is not None:
          self.transparency = transparency

    @property
    def background_color(self):
        """
        Gets the background_color of this Area.

        :return: The background_color of this Area.
        :rtype: Color
        """
        return self.container['background_color']

    @background_color.setter
    def background_color(self, background_color):
        """
        Sets the background_color of this Area.

        :param background_color: The background_color of this Area.
        :type: Color
        """

        self.container['background_color'] = background_color

    @property
    def fill_format(self):
        """
        Gets the fill_format of this Area.

        :return: The fill_format of this Area.
        :rtype: FillFormat
        """
        return self.container['fill_format']

    @fill_format.setter
    def fill_format(self, fill_format):
        """
        Sets the fill_format of this Area.

        :param fill_format: The fill_format of this Area.
        :type: FillFormat
        """

        self.container['fill_format'] = fill_format

    @property
    def foreground_color(self):
        """
        Gets the foreground_color of this Area.

        :return: The foreground_color of this Area.
        :rtype: Color
        """
        return self.container['foreground_color']

    @foreground_color.setter
    def foreground_color(self, foreground_color):
        """
        Sets the foreground_color of this Area.

        :param foreground_color: The foreground_color of this Area.
        :type: Color
        """

        self.container['foreground_color'] = foreground_color

    @property
    def format(self):
        """
        Gets the format of this Area.

        :return: The format of this Area.
        :rtype: str
        """
        return self.container['format']

    @format.setter
    def format(self, format):
        """
        Sets the format of this Area.

        :param format: The format of this Area.
        :type: str
        """

        self.container['format'] = format

    @property
    def invert_if_negative(self):
        """
        Gets the invert_if_negative of this Area.

        :return: The invert_if_negative of this Area.
        :rtype: bool
        """
        return self.container['invert_if_negative']

    @invert_if_negative.setter
    def invert_if_negative(self, invert_if_negative):
        """
        Sets the invert_if_negative of this Area.

        :param invert_if_negative: The invert_if_negative of this Area.
        :type: bool
        """

        self.container['invert_if_negative'] = invert_if_negative

    @property
    def transparency(self):
        """
        Gets the transparency of this Area.

        :return: The transparency of this Area.
        :rtype: float
        """
        return self.container['transparency']

    @transparency.setter
    def transparency(self, transparency):
        """
        Sets the transparency of this Area.

        :param transparency: The transparency of this Area.
        :type: float
        """

        self.container['transparency'] = transparency

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
        if not isinstance(other, Area):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
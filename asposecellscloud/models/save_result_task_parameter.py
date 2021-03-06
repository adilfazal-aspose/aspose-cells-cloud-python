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
from . import TaskParameter

class SaveResultTaskParameter(TaskParameter):
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
        'result_source': 'str',
        'result_destination': 'ResultDestination'
    }

    attribute_map = {
        'result_source': 'ResultSource',
        'result_destination': 'ResultDestination'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(SaveResultTaskParameter.swagger_types, **TaskParameter.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(SaveResultTaskParameter.attribute_map, **TaskParameter.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, result_source=None, result_destination=None, **kw):
        super(SaveResultTaskParameter, self).__init__(**kw)
		    
        """
        SaveResultTaskParameter - a model defined in Swagger
        """

        self.container['result_source'] = None
        self.container['result_destination'] = None

        if result_source is not None:
          self.result_source = result_source
        if result_destination is not None:
          self.result_destination = result_destination

    @property
    def result_source(self):
        """
        Gets the result_source of this SaveResultTaskParameter.

        :return: The result_source of this SaveResultTaskParameter.
        :rtype: str
        """
        return self.container['result_source']

    @result_source.setter
    def result_source(self, result_source):
        """
        Sets the result_source of this SaveResultTaskParameter.

        :param result_source: The result_source of this SaveResultTaskParameter.
        :type: str
        """

        self.container['result_source'] = result_source

    @property
    def result_destination(self):
        """
        Gets the result_destination of this SaveResultTaskParameter.

        :return: The result_destination of this SaveResultTaskParameter.
        :rtype: ResultDestination
        """
        return self.container['result_destination']

    @result_destination.setter
    def result_destination(self, result_destination):
        """
        Sets the result_destination of this SaveResultTaskParameter.

        :param result_destination: The result_destination of this SaveResultTaskParameter.
        :type: ResultDestination
        """

        self.container['result_destination'] = result_destination

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
        if not isinstance(other, SaveResultTaskParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

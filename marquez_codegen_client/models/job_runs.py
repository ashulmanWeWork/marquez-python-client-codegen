# coding: utf-8

"""
    Marquez

    Marquez is an open source **metadata service** for the **collection**, **aggregation**, and **visualization** of a data ecosystem's metadata.  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class JobRuns(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'runs': 'list[JobRun]'
    }

    attribute_map = {
        'runs': 'runs'
    }

    def __init__(self, runs=None):  # noqa: E501
        """JobRuns - a model defined in OpenAPI"""  # noqa: E501

        self._runs = None
        self.discriminator = None

        if runs is not None:
            self.runs = runs

    @property
    def runs(self):
        """Gets the runs of this JobRuns.  # noqa: E501


        :return: The runs of this JobRuns.  # noqa: E501
        :rtype: list[JobRun]
        """
        return self._runs

    @runs.setter
    def runs(self, runs):
        """Sets the runs of this JobRuns.


        :param runs: The runs of this JobRuns.  # noqa: E501
        :type: list[JobRun]
        """

        self._runs = runs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobRuns):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

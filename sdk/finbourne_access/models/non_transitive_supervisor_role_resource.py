# coding: utf-8

"""
    FINBOURNE Access Management API

    ### Introduction    This page documents the LUSID Access Management APIs from FINBOURNE Technology, which allow authorised users to query and update their access control policies and roles within the LUSID platform's Identity and Access Management system.      # noqa: E501

    The version of the OpenAPI document: 0.0.616
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class NonTransitiveSupervisorRoleResource(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'roles': 'list[dict(str, str)]'
    }

    attribute_map = {
        'roles': 'roles'
    }

    required_map = {
        'roles': 'optional'
    }

    def __init__(self, roles=None):  # noqa: E501
        """
        NonTransitiveSupervisorRoleResource - a model defined in OpenAPI

        :param roles: 
        :type roles: list[dict(str, str)]

        """  # noqa: E501

        self._roles = None
        self.discriminator = None

        self.roles = roles

    @property
    def roles(self):
        """Gets the roles of this NonTransitiveSupervisorRoleResource.  # noqa: E501


        :return: The roles of this NonTransitiveSupervisorRoleResource.  # noqa: E501
        :rtype: list[dict(str, str)]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this NonTransitiveSupervisorRoleResource.


        :param roles: The roles of this NonTransitiveSupervisorRoleResource.  # noqa: E501
        :type: list[dict(str, str)]
        """

        self._roles = roles

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
        if not isinstance(other, NonTransitiveSupervisorRoleResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.815
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ResourceDetails(object):
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
        'id': 'dict(str, str)',
        'metadata': 'dict(str, list[EntitlementMetadata])'
    }

    attribute_map = {
        'id': 'id',
        'metadata': 'metadata'
    }

    required_map = {
        'id': 'required',
        'metadata': 'optional'
    }

    def __init__(self, id=None, metadata=None):  # noqa: E501
        """
        ResourceDetails - a model defined in OpenAPI

        :param id:  The identifier of the resource being evaluated (required)
        :type id: dict(str, str)
        :param metadata:  Any metadata associated with the resource being requested
        :type metadata: dict(str, list[EntitlementMetadata])

        """  # noqa: E501

        self._id = None
        self._metadata = None
        self.discriminator = None

        self.id = id
        self.metadata = metadata

    @property
    def id(self):
        """Gets the id of this ResourceDetails.  # noqa: E501

        The identifier of the resource being evaluated  # noqa: E501

        :return: The id of this ResourceDetails.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceDetails.

        The identifier of the resource being evaluated  # noqa: E501

        :param id: The id of this ResourceDetails.  # noqa: E501
        :type: dict(str, str)
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this ResourceDetails.  # noqa: E501

        Any metadata associated with the resource being requested  # noqa: E501

        :return: The metadata of this ResourceDetails.  # noqa: E501
        :rtype: dict(str, list[EntitlementMetadata])
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ResourceDetails.

        Any metadata associated with the resource being requested  # noqa: E501

        :param metadata: The metadata of this ResourceDetails.  # noqa: E501
        :type: dict(str, list[EntitlementMetadata])
        """

        self._metadata = metadata

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
        if not isinstance(other, ResourceDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

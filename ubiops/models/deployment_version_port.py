# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class DeploymentVersionPort(object):
    """
    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name and the value is attribute type
      attribute_map (dict): The key is attribute name and the value is json key in definition
    """

    openapi_types = {"public_port": "int", "deployment_port": "int", "protocol": "str"}

    attribute_map = {"public_port": "public_port", "deployment_port": "deployment_port", "protocol": "protocol"}

    def __init__(self, public_port=None, deployment_port=None, protocol=None, **kwargs):
        """
        DeploymentVersionPort - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._public_port = None
        self._deployment_port = None
        self._protocol = None
        self.discriminator = None

        self.public_port = public_port
        self.deployment_port = deployment_port
        self.protocol = protocol

    @property
    def public_port(self):
        """
        Gets the public_port of this DeploymentVersionPort

        :return: the public_port of this DeploymentVersionPort
        :rtype: int
        """

        return self._public_port

    @public_port.setter
    def public_port(self, public_port):
        """
        Sets the public_port of this DeploymentVersionPort

        :param public_port: the public_port of this DeploymentVersionPort
        :type: int
        """

        if self.client_side_validation and public_port is None:
            raise ValueError("Invalid value for `public_port`, must not be `None`")
        if self.client_side_validation and (public_port is not None and not isinstance(public_port, int)):
            raise ValueError("Parameter `public_port` must be an integer")

        self._public_port = public_port

    @property
    def deployment_port(self):
        """
        Gets the deployment_port of this DeploymentVersionPort

        :return: the deployment_port of this DeploymentVersionPort
        :rtype: int
        """

        return self._deployment_port

    @deployment_port.setter
    def deployment_port(self, deployment_port):
        """
        Sets the deployment_port of this DeploymentVersionPort

        :param deployment_port: the deployment_port of this DeploymentVersionPort
        :type: int
        """

        if self.client_side_validation and deployment_port is None:
            raise ValueError("Invalid value for `deployment_port`, must not be `None`")
        if self.client_side_validation and (deployment_port is not None and not isinstance(deployment_port, int)):
            raise ValueError("Parameter `deployment_port` must be an integer")

        self._deployment_port = deployment_port

    @property
    def protocol(self):
        """
        Gets the protocol of this DeploymentVersionPort

        :return: the protocol of this DeploymentVersionPort
        :rtype: str
        """

        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this DeploymentVersionPort

        :param protocol: the protocol of this DeploymentVersionPort
        :type: str
        """

        if self.client_side_validation and protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")
        if self.client_side_validation and (protocol is not None and not isinstance(protocol, str)):
            raise ValueError("Parameter `protocol` must be a string")

        if self.client_side_validation and (protocol is not None and len(protocol) > 16):
            raise ValueError("Invalid value for `protocol`, length must be less than or equal to `16`")
        if self.client_side_validation and (protocol is not None and len(protocol) < 1):
            raise ValueError("Invalid value for `protocol`, length must be greater than or equal to `1`")

        self._protocol = protocol

    def to_dict(self):
        """
        Returns the model properties as a dict
        """

        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """

        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """

        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """

        if not isinstance(other, DeploymentVersionPort):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, DeploymentVersionPort):
            return True

        return self.to_dict() != other.to_dict()
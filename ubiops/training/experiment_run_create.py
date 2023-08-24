# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.
"""


import pprint


class ExperimentRunCreate(object):
    openapi_types = {
        "name": "str",
        "description": "str",
        "training_code": "str",
        "training_data": "str",
        "parameters": "dict(str, json)",
    }

    attribute_map = {
        "name": "name",
        "description": "description",
        "training_code": "training_code",
        "training_data": "training_data",
        "parameters": "parameters",
    }

    def __init__(
        self,
        name=None,
        description=None,
        training_code=None,
        training_data=None,
        parameters=None,
        **kwargs,
    ):
        """
        ExperimentRunCreate
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._name = None
        self._description = None
        self._training_code = None
        self._training_data = None
        self._parameters = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.training_code = training_code
        if training_data is not None:
            self.training_data = training_data
        if parameters is not None:
            self.parameters = parameters

    @property
    def name(self):
        """
        Gets the name of this ExperimentRunCreate

        :return: The name of this ExperimentRunCreate
        :rtype: str
        """

        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExperimentRunCreate

        :param name: The name of this ExperimentRunCreate
        :type: str
        """

        if self.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if self.client_side_validation and (name is not None and not isinstance(name, str)):
            raise ValueError("Parameter `name` must be a string")

        if self.client_side_validation and (name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ExperimentRunCreate

        :return: the description of this ExperimentRunCreate
        :rtype: str
        """

        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ExperimentRunCreate

        :param description: the description of this ExperimentRunCreate
        :type: str
        """

        if self.client_side_validation and (description is not None and not isinstance(description, str)):
            raise ValueError("Parameter `description` must be a string")

        self._description = description

    @property
    def training_code(self):
        """
        Gets the training_code of this ExperimentRunCreate

        :return: The training_code of this ExperimentRunCreate
        :rtype: str
        """

        return self._training_code

    @training_code.setter
    def training_code(self, training_code):
        """
        Sets the training_code of this ExperimentRunCreate

        :param training_code: The training_code of this ExperimentRunCreate
        :type: str
        """

        if self.client_side_validation and training_code is None:
            raise ValueError("Invalid value for `training_code`, must not be `None`")
        if self.client_side_validation and (training_code is not None and not isinstance(training_code, str)):
            raise ValueError("Parameter `training_code` must be a string")

        if self.client_side_validation and (training_code is not None and len(training_code) < 1):
            raise ValueError("Invalid value for `training_code`, length must be greater than or equal to `1`")

        self._training_code = training_code

    @property
    def training_data(self):
        """
        Gets the training_data of this ExperimentRunCreate

        :return: The training_data of this ExperimentRunCreate
        :rtype: str
        """

        return self._training_data

    @training_data.setter
    def training_data(self, training_data):
        """
        Sets the training_data of this ExperimentRunCreate

        :param training_data: The training_data of this ExperimentRunCreate
        :type: str
        """

        if self.client_side_validation and (training_data is not None and not isinstance(training_data, str)):
            raise ValueError("Parameter `training_data` must be a string")

        if self.client_side_validation and (training_data is not None and len(training_data) < 1):
            raise ValueError("Invalid value for `training_data`, length must be greater than or equal to `1`")

        self._training_data = training_data

    @property
    def parameters(self):
        """
        Gets the parameters of this ExperimentRunCreate

        :return: The parameters of this ExperimentRunCreate
        :rtype: dict
        """

        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this ExperimentRunCreate

        :param parameters: The parameters of this ExperimentRunCreate
        :type: dict
        """

        if self.client_side_validation and (parameters is not None and not isinstance(parameters, dict)):
            raise ValueError("Parameter `parameters` must be a dict")

        self._parameters = parameters

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

        if not isinstance(other, ExperimentRunCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, ExperimentRunCreate):
            return True

        return self.to_dict() != other.to_dict()

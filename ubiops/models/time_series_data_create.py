# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class TimeSeriesDataCreate(object):
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

    openapi_types = {"metric": "str", "labels": "dict(str, str)", "data": "list[TimeSeriesDataPointCreate]"}

    attribute_map = {"metric": "metric", "labels": "labels", "data": "data"}

    def __init__(self, metric=None, labels=None, data=None, **kwargs):
        """
        TimeSeriesDataCreate - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._metric = None
        self._labels = None
        self._data = None
        self.discriminator = None

        self.metric = metric
        if labels is not None:
            self.labels = labels
        self.data = data

    @property
    def metric(self):
        """
        Gets the metric of this TimeSeriesDataCreate

        :return: the metric of this TimeSeriesDataCreate
        :rtype: str
        """

        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this TimeSeriesDataCreate

        :param metric: the metric of this TimeSeriesDataCreate
        :type: str
        """

        if self.client_side_validation and metric is None:
            raise ValueError("Invalid value for `metric`, must not be `None`")
        if self.client_side_validation and (metric is not None and not isinstance(metric, str)):
            raise ValueError("Parameter `metric` must be a string")

        if self.client_side_validation and (metric is not None and len(metric) < 1):
            raise ValueError("Invalid value for `metric`, length must be greater than or equal to `1`")

        self._metric = metric

    @property
    def labels(self):
        """
        Gets the labels of this TimeSeriesDataCreate

        :return: the labels of this TimeSeriesDataCreate
        :rtype: dict(str, str)
        """

        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this TimeSeriesDataCreate

        :param labels: the labels of this TimeSeriesDataCreate
        :type: dict(str, str)
        """

        if self.client_side_validation and (labels is not None and not isinstance(labels, dict)):
            raise ValueError("Parameter `labels` must be a dictionary")

        self._labels = labels

    @property
    def data(self):
        """
        Gets the data of this TimeSeriesDataCreate

        :return: the data of this TimeSeriesDataCreate
        :rtype: list[TimeSeriesDataPointCreate]
        """

        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this TimeSeriesDataCreate

        :param data: the data of this TimeSeriesDataCreate
        :type: list[TimeSeriesDataPointCreate]
        """

        if self.client_side_validation and data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")
        if self.client_side_validation and (data is not None and not isinstance(data, list)):
            raise ValueError("Parameter `data` must be a list")
        if self.client_side_validation and data is not None:
            from ubiops.models.time_series_data_point_create import TimeSeriesDataPointCreate

            data = [TimeSeriesDataPointCreate(**item) if isinstance(item, dict) else item for item in data]

        self._data = data

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

        if not isinstance(other, TimeSeriesDataCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, TimeSeriesDataCreate):
            return True

        return self.to_dict() != other.to_dict()

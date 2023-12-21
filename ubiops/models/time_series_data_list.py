# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint


class TimeSeriesDataList(object):
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

    openapi_types = {
        "metric": "str",
        "metric_type": "str",
        "unit": "str",
        "start_date": "datetime",
        "end_date": "datetime",
        "aggregation_period": "int",
        "labels": "dict(str, str)",
        "data_points": "list[TimeSeriesDataPointList]",
    }

    attribute_map = {
        "metric": "metric",
        "metric_type": "metric_type",
        "unit": "unit",
        "start_date": "start_date",
        "end_date": "end_date",
        "aggregation_period": "aggregation_period",
        "labels": "labels",
        "data_points": "data_points",
    }

    def __init__(
        self,
        metric=None,
        metric_type=None,
        unit=None,
        start_date=None,
        end_date=None,
        aggregation_period=None,
        labels=None,
        data_points=None,
        **kwargs,
    ):
        """
        TimeSeriesDataList - a model defined in OpenAPI
        """

        self.client_side_validation = True
        if "local_vars_configuration" in kwargs and kwargs["local_vars_configuration"] is not None:
            self.client_side_validation = kwargs["local_vars_configuration"].client_side_validation

        self._metric = None
        self._metric_type = None
        self._unit = None
        self._start_date = None
        self._end_date = None
        self._aggregation_period = None
        self._labels = None
        self._data_points = None
        self.discriminator = None

        self.metric = metric
        self.metric_type = metric_type
        self.unit = unit
        self.start_date = start_date
        self.end_date = end_date
        self.aggregation_period = aggregation_period
        self.labels = labels
        self.data_points = data_points

    @property
    def metric(self):
        """
        Gets the metric of this TimeSeriesDataList

        :return: the metric of this TimeSeriesDataList
        :rtype: str
        """

        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this TimeSeriesDataList

        :param metric: the metric of this TimeSeriesDataList
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
    def metric_type(self):
        """
        Gets the metric_type of this TimeSeriesDataList

        :return: the metric_type of this TimeSeriesDataList
        :rtype: str
        """

        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        """
        Sets the metric_type of this TimeSeriesDataList

        :param metric_type: the metric_type of this TimeSeriesDataList
        :type: str
        """

        if self.client_side_validation and metric_type is None:
            raise ValueError("Invalid value for `metric_type`, must not be `None`")
        if self.client_side_validation and (metric_type is not None and not isinstance(metric_type, str)):
            raise ValueError("Parameter `metric_type` must be a string")

        if self.client_side_validation and (metric_type is not None and len(metric_type) < 1):
            raise ValueError("Invalid value for `metric_type`, length must be greater than or equal to `1`")

        self._metric_type = metric_type

    @property
    def unit(self):
        """
        Gets the unit of this TimeSeriesDataList

        :return: the unit of this TimeSeriesDataList
        :rtype: str
        """

        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this TimeSeriesDataList

        :param unit: the unit of this TimeSeriesDataList
        :type: str
        """

        if self.client_side_validation and (unit is not None and not isinstance(unit, str)):
            raise ValueError("Parameter `unit` must be a string")

        self._unit = unit

    @property
    def start_date(self):
        """
        Gets the start_date of this TimeSeriesDataList

        :return: the start_date of this TimeSeriesDataList
        :rtype: datetime
        """

        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this TimeSeriesDataList

        :param start_date: the start_date of this TimeSeriesDataList
        :type: datetime
        """

        if self.client_side_validation and start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this TimeSeriesDataList

        :return: the end_date of this TimeSeriesDataList
        :rtype: datetime
        """

        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this TimeSeriesDataList

        :param end_date: the end_date of this TimeSeriesDataList
        :type: datetime
        """

        if self.client_side_validation and end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")

        self._end_date = end_date

    @property
    def aggregation_period(self):
        """
        Gets the aggregation_period of this TimeSeriesDataList

        :return: the aggregation_period of this TimeSeriesDataList
        :rtype: int
        """

        return self._aggregation_period

    @aggregation_period.setter
    def aggregation_period(self, aggregation_period):
        """
        Sets the aggregation_period of this TimeSeriesDataList

        :param aggregation_period: the aggregation_period of this TimeSeriesDataList
        :type: int
        """

        if self.client_side_validation and aggregation_period is None:
            raise ValueError("Invalid value for `aggregation_period`, must not be `None`")
        if self.client_side_validation and (aggregation_period is not None and not isinstance(aggregation_period, int)):
            raise ValueError("Parameter `aggregation_period` must be an integer")

        self._aggregation_period = aggregation_period

    @property
    def labels(self):
        """
        Gets the labels of this TimeSeriesDataList

        :return: the labels of this TimeSeriesDataList
        :rtype: dict(str, str)
        """

        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this TimeSeriesDataList

        :param labels: the labels of this TimeSeriesDataList
        :type: dict(str, str)
        """

        if self.client_side_validation and labels is None:
            raise ValueError("Invalid value for `labels`, must not be `None`")
        if self.client_side_validation and (labels is not None and not isinstance(labels, dict)):
            raise ValueError("Parameter `labels` must be a dictionary")

        self._labels = labels

    @property
    def data_points(self):
        """
        Gets the data_points of this TimeSeriesDataList

        :return: the data_points of this TimeSeriesDataList
        :rtype: list[TimeSeriesDataPointList]
        """

        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """
        Sets the data_points of this TimeSeriesDataList

        :param data_points: the data_points of this TimeSeriesDataList
        :type: list[TimeSeriesDataPointList]
        """

        if self.client_side_validation and data_points is None:
            raise ValueError("Invalid value for `data_points`, must not be `None`")
        if self.client_side_validation and (data_points is not None and not isinstance(data_points, list)):
            raise ValueError("Parameter `data_points` must be a list")
        if self.client_side_validation and data_points is not None:
            from ubiops.models.time_series_data_point_list import TimeSeriesDataPointList

            data_points = [TimeSeriesDataPointList(**item) if isinstance(item, dict) else item for item in data_points]

        self._data_points = data_points

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

        if not isinstance(other, TimeSeriesDataList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """

        if not isinstance(other, TimeSeriesDataList):
            return True

        return self.to_dict() != other.to_dict()

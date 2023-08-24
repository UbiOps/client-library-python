# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API
"""


from ubiops.training.constants import DEFAULT_TRAINING_DEPLOYMENT_NAME
from ubiops.models.deployment_request_batch_create_response import DeploymentRequestBatchCreateResponse


class ExperimentRunCreateResponse(DeploymentRequestBatchCreateResponse):
    openapi_types = {"id": "str", "experiment": "str", "status": "str", "time_created": "datetime"}
    attribute_map = {"id": "id", "experiment": "experiment", "status": "status", "time_created": "time_created"}

    def __init__(self, id=None, experiment=None, status=None, time_created=None, **kwargs):
        """
        ExperimentRunCreateResponse
        """

        kwargs.pop("version", None)  # To make sure we don't pass the version twice

        super().__init__(
            id=id,
            deployment=kwargs.pop("deployment", DEFAULT_TRAINING_DEPLOYMENT_NAME),
            version=experiment,  # Convert experiment to version
            status=status,
            time_created=time_created,
            **kwargs,
        )

        self._experiment = None

        self.experiment = experiment

    @property
    def experiment(self):
        """
        Gets the experiment of this ExperimentRunCreateResponse

        :return: the experiment of this ExperimentRunCreateResponse
        :rtype: str
        """

        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """
        Sets the experiment of this ExperimentRunCreateResponse

        :param experiment: the experiment of this ExperimentRunCreateResponse
        :type: str
        """

        if self.client_side_validation and (experiment is not None and not isinstance(experiment, str)):
            raise ValueError("Parameter `experiment` must be a string")

        if self.client_side_validation and (experiment is not None and len(experiment) < 1):
            raise ValueError("Invalid value for `experiment`, length must be greater than or equal to `1`")

        self._experiment = experiment

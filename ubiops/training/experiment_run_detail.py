# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.
"""


from ubiops.training.constants import DEFAULT_TRAINING_DEPLOYMENT_NAME
from ubiops.models.deployment_request_batch_detail import DeploymentRequestBatchDetail


class ExperimentRunDetail(DeploymentRequestBatchDetail):
    openapi_types = {
        "id": "str",
        "experiment": "str",
        "status": "str",
        "success": "bool",
        "time_created": "datetime",
        "time_started": "datetime",
        "time_completed": "datetime",
        "error_message": "str",
        "retries": "int",
        "request_data": "object",
        "result": "object",
        "notification_group": "str",
        "origin": "dict(str, str)",
    }

    attribute_map = {
        "id": "id",
        "experiment": "experiment",
        "status": "status",
        "success": "success",
        "time_created": "time_created",
        "time_started": "time_started",
        "time_completed": "time_completed",
        "error_message": "error_message",
        "retries": "retries",
        "request_data": "request_data",
        "result": "result",
        "notification_group": "notification_group",
        "origin": "origin",
    }

    def __init__(
        self,
        id=None,
        experiment=None,
        status=None,
        success=None,
        time_created=None,
        time_started=None,
        time_completed=None,
        error_message=None,
        retries=None,
        request_data=None,
        result=None,
        notification_group=None,
        origin=None,
        **kwargs,
    ):
        """
        ExperimentRunDetail
        """

        kwargs.pop("version", None)  # To make sure we don't pass the version twice

        super().__init__(
            id=id,
            deployment=kwargs.pop("deployment", DEFAULT_TRAINING_DEPLOYMENT_NAME),
            version=experiment,  # Convert experiment to version
            status=status,
            success=success,
            time_created=time_created,
            time_started=time_started,
            time_completed=time_completed,
            error_message=error_message,
            retries=retries,
            request_data=request_data,
            result=result,
            notification_group=notification_group,
            origin=origin,
            **kwargs,
        )

        self._experiment = None

        self.experiment = experiment

    @property
    def experiment(self):
        """
        Gets the experiment of this ExperimentRunDetail

        :return: The experiment of this ExperimentRunDetail
        :rtype: str
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """
        Sets the experiment of this ExperimentRunDetail

        :param experiment: The experiment of this ExperimentRunDetail
        :type: str
        """
        if self.client_side_validation and (experiment is not None and not isinstance(experiment, str)):
            raise ValueError("Parameter `experiment` must be a string")

        self._experiment = experiment

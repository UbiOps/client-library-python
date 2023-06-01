import logging
import random
import string

import re  # noqa: F401

import ubiops.exceptions
from ubiops import CoreApi
from ubiops.api_client import ApiClient
from ubiops.exceptions import ApiException, ApiValueError
from ubiops.utils import handle_file_input, wait_for_experiment


DEFAULT_TRAINING_DEPLOYMENT_NAME = 'training-base-deployment'
DEFAULT_TRAINING_BUCKET_NAME = 'SYS_DEFAULT_BUCKET'
TEMPLATE_DEPLOYMENT_NAME = 'training-base-deployment'


logger = logging.getLogger("Training")


class Training(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self.core_api = CoreApi(self.api_client)

        # These class variables could be overridden in the future if desired
        self.training_deployment_name = DEFAULT_TRAINING_DEPLOYMENT_NAME

    @staticmethod
    def wrap_exception(exception):
        """
        Wrap exception handling into better readable exceptions for training

        :param ApiException exception: the exception to wrap
        """

        replace = {
            'Deployment version': 'Experiment',
            'deployment version': 'experiment',
            'Version': 'Experiment',
            'version': 'experiment',
            'Request': 'Run',
            'request': 'run',
            'Requests': 'Runs',
            'requests': 'runs',
            'deployment': 'training deployment',
            'Deployment': 'Training deployment'
        }

        for i, j in replace.items():
            if isinstance(exception.reason, str):
                exception.reason = exception.reason.replace(i, j)
            if isinstance(exception.body, str):
                exception.body = exception.body.replace(i, j)
        return exception

    def initialize(self, project_name):
        """
        Initialize the training feature for the given project

        :param str project_name: the name of the project
        """

        _, template_deployment = self._get_template_deployment()

        try:
            self.core_api.deployments_create(
                project_name=project_name,
                data=template_deployment
            )
        except ApiException as e:
            raise self.wrap_exception(e)

    def _verify_deployment_exists(self, project_name):
        """
        Check if the training deployment exists

        :param str project_name: the name of the project
        """

        # Get the 'training-base-deployment'. If not existing it will throw an exception.
        try:
            self.core_api.deployments_get(project_name=project_name, deployment_name=self.training_deployment_name)
        except ApiException as e:
            if e.status == 404:
                raise ApiException(
                    status=400,
                    reason="Training disabled",
                    body="Training feature has not been initialized yet. Please run the initialize() function"
                )
            else:
                raise

    def _verify_environment_exists(self, project_name, environment_name):
        """
        Check if the environment exists

        :param str project_name: the name of the project
        :param str environment_name: the name of the environment of which to check the existence
        """

        # Get the environment. If not existing it will throw an exception.
        try:
            self.core_api.environments_get(project_name=project_name, environment_name=environment_name)
        except ApiException as e:
            if e.status == 404:
                raise ApiException(
                    status=e.status,
                    reason="Not Found",
                    body="Environment %s not found" % environment_name
                )
            else:
                raise

    def _verify_bucket_exists(self, project_name, bucket):
        """
        Check if the bucket exists

        :param str project_name: the name of the project
        :param str bucket: the name of the bucket of which to check the existence
        """

        # Get the bucket for training artifacts. If not existing it will throw an exception.
        try:
            self.core_api.buckets_get(project_name=project_name, bucket_name=bucket)
        except ApiException as e:
            if e.status == 404:
                raise ApiException(
                    status=e.status,
                    reason="Not Found",
                    body="Bucket %s not found" % bucket
                )
            else:
                raise

    def _get_template_deployment(self):
        """
        Get the training template deployment

        :return dict training_template_deployment: the training template deployment details
        """

        template_deployments = self.core_api.template_deployments_list()

        try:
            training_template_deployment_id = None
            training_template_deployment = None
            for template_deployment in template_deployments:
                if template_deployment.details['name'] == TEMPLATE_DEPLOYMENT_NAME:
                    training_template_deployment_id = template_deployment.id
                    training_template_deployment = template_deployment.details

            if training_template_deployment is None:
                raise ApiException(
                    status=500, reason="Internal Error", body="Could not obtain a template training deployment"
                )

            return training_template_deployment_id, training_template_deployment
        except (AttributeError, KeyError):
            raise ApiException(
                status=500, reason="Internal Error", body="Could not obtain a template training deployment"
            )

    def _get_default_bucket(self, project_name, experiment_name):
        """
        Get the default bucket for the experiment

        :param str project_name: the name of the project
        :param str experiment_name: the name of the experiment
        """

        try:
            env_vars = self.core_api.deployment_version_environment_variables_list(
                project_name=project_name,
                deployment_name=self.training_deployment_name,
                version=experiment_name
            )
            for env_var in env_vars:
                if env_var.name == DEFAULT_TRAINING_BUCKET_NAME:
                    return env_var.value

        except ApiException as e:
            raise self.wrap_exception(e)

        return "default"

    def _update_default_bucket(self, project_name, experiment_name, bucket_name):
        """
        Update the default bucket for the experiment

        :param str project_name: the name of the project
        :param str experiment_name: the name of the experiment
        :param str bucket_name: the new bucket to use for the training experiment
        """

        try:
            env_vars = self.core_api.deployment_version_environment_variables_list(
                project_name=project_name,
                deployment_name=self.training_deployment_name,
                version=experiment_name
            )
            for env_var in env_vars:
                if env_var.name == DEFAULT_TRAINING_BUCKET_NAME:
                    self.core_api.deployment_version_environment_variables_update(
                        project_name=project_name,
                        deployment_name=self.training_deployment_name,
                        version=experiment_name,
                        id=env_var.id,
                        data=ubiops.EnvironmentVariableCreate(
                            name=DEFAULT_TRAINING_BUCKET_NAME,
                            value=bucket_name,
                            secret=False
                        )
                    )
                    return

            # Environment variable DEFAULT_TRAINING_BUCKET_NAME does not exist yet
            self.core_api.deployment_version_environment_variables_create(
                project_name=project_name,
                deployment_name=self.training_deployment_name,
                version=experiment_name,
                data=ubiops.EnvironmentVariableCreate(
                    name=DEFAULT_TRAINING_BUCKET_NAME,
                    value=bucket_name,
                    secret=False
                )
            )
        except ApiException as e:
            raise self.wrap_exception(e)

    @staticmethod
    def _random_string(str_length):
        """
        Create a random string of the given length

        :param int str_length: the length of the string
        """

        return ''.join(random.choice(string.ascii_letters.lower()) for _ in range(str_length))

    def experiments_create(self, project_name, data, **kwargs):
        """
        Create a new experiment

        :param str project_name: the name of the project (required)
        :param ExperimentCreate data: the details of the experiment (required)

        :return: ExperimentList
        """

        if project_name is None:
            raise ApiValueError("Missing the required parameter `project_name`")
        if data is None:
            raise ApiValueError("Missing the required parameter `data`")
        if project_name is not None and not isinstance(project_name, str):
            raise ApiValueError("Parameter `project_name` must be a string")
        if data is not None:
            from ubiops.training.experiment_create import ExperimentCreate

            if isinstance(data, dict):
                data = ExperimentCreate(**data)

            elif not isinstance(data, ExperimentCreate):
                raise ApiValueError("Parameter `data` must be an instance of ExperimentCreate")

        # Check preconditions
        self._verify_deployment_exists(project_name=project_name)
        self._verify_environment_exists(project_name=project_name, environment_name=data.environment)
        if data.default_bucket:
            self._verify_bucket_exists(project_name=project_name, bucket=data.default_bucket)

        template_deployment_id, _ = self._get_template_deployment()

        # Create a deployment version from the specified environment
        version_template = ubiops.DeploymentVersionCreate(
            version=data.name,
            environment=data.environment,
            instance_type=data.instance_type,
            maximum_instances=10,
            minimum_instances=0,
            description=data.description,
            labels=data.labels,
            request_retention_mode='full',
            request_retention_time=31536000  # 1 normal year
        )

        try:
            # Create a deployment version under the default training deployment
            self.core_api.deployment_versions_create(
                project_name=project_name,
                deployment_name=self.training_deployment_name,
                data=version_template,
                **kwargs
            )
        except ApiException as e:
            raise self.wrap_exception(e)

        # Set the default bucket name
        if data.default_bucket:
            try:
                self.core_api.deployment_version_environment_variables_create(
                    project_name=project_name,
                    deployment_name=self.training_deployment_name,
                    version=data.name,
                    data=ubiops.EnvironmentVariableCreate(
                        name=DEFAULT_TRAINING_BUCKET_NAME,
                        value=data.default_bucket,
                        secret=False
                    ),
                    **kwargs
                )
            except ApiException as e:
                raise self.wrap_exception(e)

        # Upload a default training zip file package
        try:
            response = self.core_api.revisions_file_upload(
                project_name=project_name,
                deployment_name=self.training_deployment_name,
                version=data.name,
                template_deployment_id=template_deployment_id,
                **kwargs
            )
        except ApiException as e:
            raise self.wrap_exception(e)

        wait_for_experiment(
            client=self.api_client,
            project_name=project_name,
            deployment_name=self.training_deployment_name,
            version=data.name,
            revision_id=response.revision
        )

        try:
            deployment_version = self.core_api.deployment_versions_get(
                project_name=project_name,
                deployment_name=self.training_deployment_name,
                version=data.name,
                **kwargs
            )
        except ApiException as e:
            raise self.wrap_exception(e)

        from ubiops.training.experiment_list import ExperimentList
        return ExperimentList(name=deployment_version.version, **deployment_version.to_dict())

    def experiments_list(self, project_name, **kwargs):
        """
        List experiments

        :param str project_name: the name of the project (required)

        :return: list[ExperimentList]
        """

        if project_name is None:
            raise ApiValueError("Missing the required parameter `project_name`")
        if project_name is not None and not isinstance(project_name, str):
            raise ApiValueError("Parameter `project_name` must be a string")

        self._verify_deployment_exists(project_name=project_name)

        try:
            deployment_versions = self.core_api.deployment_versions_list(
                project_name=project_name,
                deployment_name=self.training_deployment_name,
                **kwargs
            )
        except ApiException as e:
            raise self.wrap_exception(e)

        from ubiops.training.experiment_list import ExperimentList
        return [ExperimentList(name=version.version, **version.to_dict()) for version in deployment_versions]

    def experiments_get(self, project_name, experiment_name, **kwargs):
        """
        Get experiment

        :param str project_name: the name of the project (required)
        :param str experiment_name: the name of the experiment (required)

        :return: ExperimentDetail
        """

        if project_name is None:
            raise ApiValueError("Missing the required parameter `project_name`")
        if experiment_name is None:
            raise ApiValueError("Missing the required parameter `experiment_name`")
        if project_name is not None and not isinstance(project_name, str):
            raise ApiValueError("Parameter `project_name` must be a string")
        if experiment_name is not None and not isinstance(experiment_name, str):
            raise ApiValueError("Parameter `experiment_name` must be a string")

        try:
            deployment_version = self.core_api.deployment_versions_get(
                project_name=project_name,
                deployment_name=self.training_deployment_name,
                version=experiment_name,
                **kwargs
            )
        except ApiException as e:
            raise self.wrap_exception(e)

        # Get the default bucket
        default_bucket = self._get_default_bucket(project_name=project_name, experiment_name=experiment_name)

        from ubiops.training.experiment_detail import ExperimentDetail
        return ExperimentDetail(
            name=deployment_version.version,
            default_bucket=default_bucket,
            **deployment_version.to_dict()
        )

    def experiments_update(self, project_name, experiment_name, data, **kwargs):
        """
        Update an experiment

        :param str project_name: the name of the project (required)
        :param str experiment_name: the name of the experiment (required)
        :param ExperimentUpdate data: the details of the experiment (required)

        :return: ExperimentUpdate
        """

        if project_name is None:
            raise ApiValueError("Missing the required parameter `project_name`")
        if experiment_name is None:
            raise ApiValueError("Missing the required parameter `experiment_name`")
        if data is None:
            raise ApiValueError("Missing the required parameter `data`")
        if project_name is not None and not isinstance(project_name, str):
            raise ApiValueError("Parameter `project_name` must be a string")
        if experiment_name is not None and not isinstance(experiment_name, str):
            raise ApiValueError("Parameter `experiment_name` must be a string")
        if data is not None:
            from ubiops.training.experiment_update import ExperimentUpdate

            if isinstance(data, dict):
                data = ExperimentUpdate(**data)

            elif not isinstance(data, ExperimentUpdate):
                raise ApiValueError("Parameter `data` must be an instance of ExperimentUpdate")

        if data.environment:
            self._verify_environment_exists(project_name=project_name, environment_name=data.environment)
        if data.default_bucket:
            self._verify_bucket_exists(project_name=project_name, bucket=data.default_bucket)
            self._update_default_bucket(
                project_name=project_name, experiment_name=experiment_name, bucket_name=data.default_bucket
            )

        version_template = ubiops.DeploymentVersionUpdate(
            version=data.name,
            **data.to_dict()
        )

        try:
            deployment_version = self.core_api.deployment_versions_update(
                project_name=project_name,
                deployment_name=self.training_deployment_name,
                version=experiment_name,
                data=version_template,
                **kwargs
            )
        except ApiException as e:
            raise self.wrap_exception(e)

        from ubiops.training.experiment_detail import ExperimentDetail
        return ExperimentDetail(
            name=deployment_version.version,
            default_bucket=data.default_bucket,
            **deployment_version.to_dict()
        )

    def experiments_delete(self, project_name, experiment_name, **kwargs):
        """
        Delete experiment

        :param str project_name: the name of the project (required)
        :param str experiment_name: the name of the experiment to delete (required)

        :return: None
        """

        if project_name is None:
            raise ApiValueError("Missing the required parameter `project_name`")
        if experiment_name is None:
            raise ApiValueError("Missing the required parameter `experiment_name`")
        if project_name is not None and not isinstance(project_name, str):
            raise ApiValueError("Parameter `project_name` must be a string")
        if experiment_name is not None and not isinstance(experiment_name, str):
            raise ApiValueError("Parameter `experiment_name` must be a string")

        try:
            return self.core_api.deployment_versions_delete(
                project_name=project_name,
                deployment_name=self.training_deployment_name,
                version=experiment_name,
                **kwargs
            )
        except ApiException as e:
            raise self.wrap_exception(e)

    def experiment_runs_create(self, project_name, experiment_name, data, **kwargs):
        """
        Create experiment run

        :param str project_name: the name of the project (required)
        :param str experiment_name: the name of the experiment (required)
        :param ExperimentRunCreate data: the details of the experiment run (required)

        :return: ExperimentRunCreateResponse
        """

        if project_name is None:
            raise ApiValueError("Missing the required parameter `project_name`")
        if experiment_name is None:
            raise ApiValueError("Missing the required parameter `experiment_name`")
        if data is None:
            raise ApiValueError("Missing the required parameter `data`")
        if project_name is not None and not isinstance(project_name, str):
            raise ApiValueError("Parameter `project_name` must be a string")
        if experiment_name is not None and not isinstance(experiment_name, str):
            raise ApiValueError("Parameter `experiment_name` must be a string")
        if data is not None:
            from ubiops.training.experiment_run_create import ExperimentRunCreate

            if isinstance(data, dict):
                data = ExperimentRunCreate(**data)

            elif not isinstance(data, ExperimentRunCreate):
                raise ApiValueError("Parameter `data` must be an instance of ExperimentRunCreate")
        if 'timeout' in kwargs and kwargs['timeout'] is not None:
            if not isinstance(kwargs['timeout'], int):
                raise ApiValueError("Parameter `timeout` must be an integer")

        # Check if experiment is ready for a run
        experiment = self.experiments_get(project_name=project_name, experiment_name=experiment_name)

        if experiment.status != "available":
            raise ApiException(
                status=500,
                reason="Creation Error",
                body="Experiment not available for run, status %s" % experiment.status
            )

        # Check which bucket to use
        default_bucket = self._get_default_bucket(project_name=project_name, experiment_name=experiment_name)
        random_run_id = self._random_string(8)

        # Upload training code
        data.training_code = handle_file_input(
            client=self.api_client, project_name=project_name, file=data.training_code, bucket_name=default_bucket,
            file_prefix="experiments/%s/runs/%s/code/" % (experiment_name, random_run_id)
        )

        # Upload training data
        if data.training_data is not None:
            data.training_data = handle_file_input(
                client=self.api_client, project_name=project_name, file=data.training_data, bucket_name=default_bucket,
                file_prefix="experiments/%s/runs/%s/data/" % (experiment_name, random_run_id)
            )

        try:
            deployment_version_request = self.core_api.batch_deployment_version_requests_create(
                project_name=project_name,
                deployment_name=self.training_deployment_name,
                version=experiment_name,
                data=[{
                    "name": data.name,
                    "description": data.description,
                    "training_code": data.training_code,
                    "training_data": data.training_data,
                    "parameters": data.parameters if data.parameters is not None else {}
                }],
                **kwargs
            )[0]
        except ApiException as e:
            raise self.wrap_exception(e)

        from ubiops.training.experiment_run_create_response import ExperimentRunCreateResponse
        return ExperimentRunCreateResponse(
            experiment=deployment_version_request.version, **deployment_version_request.to_dict()
        )

    def experiment_runs_list(self, project_name, experiment_name, **kwargs):
        """
        List runs

        :param str project_name: the name of the project (required)
        :param str experiment_name: the name of the experiment (required)

        :return: list[EnvironmentRunList]
        """

        if project_name is None:
            raise ApiValueError("Missing the required parameter `project_name`")
        if experiment_name is None:
            raise ApiValueError("Missing the required parameter `experiment_name`")
        if project_name is not None and not isinstance(project_name, str):
            raise ApiValueError("Parameter `project_name` must be a string")
        if experiment_name is not None and not isinstance(experiment_name, str):
            raise ApiValueError("Parameter `experiment_name` must be a string")

        try:
            deployment_version_requests = self.core_api.deployment_version_requests_list(
                project_name=project_name,
                deployment_name=self.training_deployment_name,
                version=experiment_name,
                **kwargs
            )
        except ApiException as e:
            raise self.wrap_exception(e)

        from ubiops.training.experiment_run_list import ExperimentRunList
        return [
            ExperimentRunList(experiment=request.version, **request.to_dict())
            for request in deployment_version_requests
        ]

    def experiment_runs_get(self, project_name, experiment_name, run_id, **kwargs):
        """
        Get run

        :param str project_name: the name of the project (required)
        :param str experiment_name: the name of the experiment (required)
        :param str run_id: the uid of the run (required)

        :return: ExperimentRunDetail
        """

        if project_name is None:
            raise ApiValueError("Missing the required parameter `project_name`")
        if experiment_name is None:
            raise ApiValueError("Missing the required parameter `experiment_name`")
        if run_id is None:
            raise ApiValueError("Missing the required parameter `run_id`")
        if project_name is not None and not isinstance(project_name, str):
            raise ApiValueError("Parameter `project_name` must be a string")
        if experiment_name is not None and not isinstance(experiment_name, str):
            raise ApiValueError("Parameter `experiment_name` must be a string")
        if run_id is not None and not isinstance(run_id, str):
            raise ApiValueError("Parameter `run_id` must be a string")

        try:
            request = self.core_api.deployment_version_requests_get(
                project_name=project_name,
                deployment_name=self.training_deployment_name,
                version=experiment_name,
                request_id=run_id,
                **kwargs
            )
        except ApiException as e:
            raise self.wrap_exception(e)

        # Only keep the 'created_by' field in the origin of the request
        if hasattr(request, 'origin') and type(request.origin) == dict and 'created_by' in request.origin:
            request.origin = {'created_by': request.origin['created_by']}

        from ubiops.training.experiment_run_detail import ExperimentRunDetail
        return ExperimentRunDetail(experiment=request.version, **request.to_dict())

    def experiment_runs_update(self, project_name, experiment_name, run_id, data, **kwargs):
        """
        Cancel a run

        :param str project_name: the name of the project (required)
        :param str experiment_name: the name of the experiment (required)
        :param str run_id: the uid of the run (required)
        :param ExperimentRunUpdate data: the details of the experiment run (required)

        :return: ExperimentRunUpdateResponse
        """

        if project_name is None:
            raise ApiValueError("Missing the required parameter `project_name`")
        if experiment_name is None:
            raise ApiValueError("Missing the required parameter `experiment_name`")
        if run_id is None:
            raise ApiValueError("Missing the required parameter `run_id`")
        if data is None:
            raise ApiValueError("Missing the required parameter `data`")
        if project_name is not None and not isinstance(project_name, str):
            raise ApiValueError("Parameter `project_name` must be a string")
        if experiment_name is not None and not isinstance(experiment_name, str):
            raise ApiValueError("Parameter `experiment_name` must be a string")
        if run_id is not None and not isinstance(run_id, str):
            raise ApiValueError("Parameter `run_id` must be a string")
        if data is not None:
            from ubiops.training.experiment_run_update import ExperimentRunUpdate

            if isinstance(data, dict):
                data = ExperimentRunUpdate(**data)

            elif not isinstance(data, ExperimentRunUpdate):
                raise ApiValueError("Parameter `data` must be an instance of ExperimentRunUpdate")

        try:
            request = self.core_api.deployment_version_requests_update(
                project_name=project_name,
                deployment_name=self.training_deployment_name,
                version=experiment_name,
                request_id=run_id,
                data=data,
                **kwargs
            )
        except ApiException as e:
            raise self.wrap_exception(e)

        from ubiops.training.experiment_run_update_response import ExperimentRunUpdateResponse
        return ExperimentRunUpdateResponse(experiment=request.version, **request.to_dict())

    def experiment_runs_delete(self, project_name, experiment_name, run_id, **kwargs):
        """
        Delete run

        :param str project_name: the name of the project (required)
        :param str experiment_name: the name of the experiment (required)
        :param str run_id: the uid of the run (required)

        :return: None
        """

        if project_name is None:
            raise ApiValueError("Missing the required parameter `project_name`")
        if experiment_name is None:
            raise ApiValueError("Missing the required parameter `experiment_name`")
        if run_id is None:
            raise ApiValueError("Missing the required parameter `run_id`")
        if project_name is not None and not isinstance(project_name, str):
            raise ApiValueError("Parameter `project_name` must be a string")
        if experiment_name is not None and not isinstance(experiment_name, str):
            raise ApiValueError("Parameter `experiment_name` must be a string")
        if run_id is not None and not isinstance(run_id, str):
            raise ApiValueError("Parameter `run_id` must be a string")

        return self.core_api.deployment_version_requests_delete(
            project_name=project_name,
            deployment_name=self.training_deployment_name,
            version=experiment_name,
            request_id=run_id,
            **kwargs
        )

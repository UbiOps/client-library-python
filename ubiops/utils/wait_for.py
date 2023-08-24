import datetime
from time import sleep, time

from ubiops import CoreApi
from ubiops.api_client import ApiClient
from ubiops.exceptions import ApiException
from ubiops.utils.exceptions import StatusError
from ubiops.training.constants import DEFAULT_TRAINING_DEPLOYMENT_NAME


LOGS_COMPLETION_SECONDS = 20
NO_LOGS_MESSAGE_SECONDS = 20
PENDING_REQUEST_STATUS = "pending"
SUCCESS_STATUSES = ["available", "completed", "confirmation", "success"]
FAILED_STATUSES = ["failed", "cancelled"]


def _wait_for(client, retrieve_method, retrieve_kwargs, object_name="Deployment version", timeout=1800, quiet=False):
    """
    Wait for base method. Prints status updates with dots if quiet=False.

    :param str retrieve_method: retrieve method to get status updates
    :param dict retrieve_kwargs: the data to pass to the retrieve method
    :param str object_name: reference name for the object to wait for, used to print messages
    :param float timeout: the maximum time to wait
    :param bool quiet: whether to suppress informational messages
    """

    first_iteration = True
    start_time = time()
    printed_len = 0

    while True:
        obj = getattr(CoreApi(client), retrieve_method)(**retrieve_kwargs)

        # Print status
        if not quiet:
            # Do at beginning to prevent not showing any output when the request is slow
            if not first_iteration:
                print("\r" + " " * printed_len, end="\r", flush=True)

            print_str = f"{object_name}: {obj.status}"
            printed_len = len(print_str) + 4
            print(print_str, end="", flush=True)

        # Done
        if obj.status in SUCCESS_STATUSES:
            if not quiet:
                print(flush=True)  # Close last \r
            return
        if obj.status in FAILED_STATUSES:
            if not quiet:
                print(flush=True)  # Close last \r
            raise StatusError(f"{object_name}: {obj.status}")

        # Handle timeout
        if time() - start_time > timeout:
            raise ApiException(status=504, reason=f"{object_name} Timeout", body="Timeout was reached")

        # Wait and print dots
        for _ in range(3):
            sleep(1)
            if not quiet:
                print(".", end="", flush=True)

        sleep(1)
        first_iteration = False


def _wait_for_logs(
    client,
    project_name,
    filters,
    retrieve_method,
    retrieve_kwargs,
    object_name="Deployment version",
    start_date=None,
    timeout=1800,
):
    """
    Stream logs with the given filters and start date

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param dict filters: the log filters to apply
    :param retrieve_method: retrieve method to get status updates
    :param dict retrieve_kwargs: the data to pass to the retrieve method
    :param str object_name: reference name for the object to wait for, used to print messages
    :param str start_date: Start date for streaming logs in iso format milliseconds. If None, utcnow will be used.
    :param float|None timeout: the maximum time to wait
    """

    initial_date = datetime.datetime.utcnow().isoformat(timespec="milliseconds") if start_date is None else start_date
    date = initial_date
    last_retrieve_time = time()
    log_id = None

    start_time = time()
    completion_time = None

    has_request_filter = "deployment_request_id" in filters

    while True:
        obj = getattr(CoreApi(client), retrieve_method)(**retrieve_kwargs)

        # When done, wait a bit longer for logs that arrive later
        if completion_time:
            if time() - completion_time > LOGS_COMPLETION_SECONDS:
                if obj.status in SUCCESS_STATUSES:
                    print(f"{object_name}: {obj.status}", flush=True)
                    return
                if obj.status in FAILED_STATUSES:
                    raise StatusError(f"{object_name}: {obj.status}")

        elif obj.status in SUCCESS_STATUSES + FAILED_STATUSES:
            completion_time = time()

        # Filter on request_id=null while request is not picked up yet; so we will show the logs of spinning up
        # the instance
        if has_request_filter and obj.status == PENDING_REQUEST_STATUS:
            data_filters = {**filters, "deployment_request_id": None}

        elif has_request_filter:
            # Set has_request_filter to False the first time the request is not in pending status anymore, so we will
            # not change the date/log again
            has_request_filter = False

            # Ignore the previous log_id that was found with deployment_request_id=None
            if log_id:
                date = initial_date
                log_id = None

            # Unset the deployment_request_id=None filter
            data_filters = filters

        else:
            data_filters = filters

        while True:
            data = {"filters": data_filters, "date_range": 86400, "limit": 500}
            if date is not None:
                data["date"] = date
            if log_id is not None:
                data["id"] = log_id
            logs = CoreApi(api_client=client).projects_log_list(project_name=project_name, data=data)

            has_logs = False
            for log in logs:
                if log.id == log_id or not log.log:
                    continue

                has_logs = True
                print(log.log.strip("\n"), flush=True)  # Remove additional blank lines

            if has_logs:
                date = None
                log_id = logs[-1].id
                last_retrieve_time = time()

            if time() - last_retrieve_time > NO_LOGS_MESSAGE_SECONDS:
                print(
                    "No logs have been received for the last %.0f seconds" % (time() - last_retrieve_time), flush=True
                )

            # Handle timeout
            if time() - start_time > timeout:
                raise ApiException(status=504, reason=f"{object_name} Timeout", body="Timeout was reached")

            sleep(3)

            if not has_logs:
                sleep(3)
                break


def _wait_for_deployment_version(
    client,
    project_name,
    deployment_name,
    version,
    revision_id=None,
    timeout=1800,
    quiet=False,
    stream_logs=False,
    object_name="Deployment version",
):
    """
    Wait for a deployment version to be ready: wait for the environment build and deployment revision to complete. This
    function is used for both deployment versions and experiments.

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str deployment_name: the name of the deployment
    :param str version: the version of the deployment
    :param str revision_id: the build id of the revision - if not provided, the latest revision will be used
    :param float timeout: the maximum time to wait
    :param bool quiet: whether to suppress informational messages
    :param bool stream_logs: Whether to stream logs while waiting, only used when quiet=False. When set to True, we will
        wait 20 seconds longer than the environment and deployment revision were first seen as completed to make sure
        all logs are retrieved. Logs will be shown starting from environment last update time and deployment revision
        creation time.
    :param str object_name: reference name for the version object, used to print success message
    """

    if not isinstance(client, ApiClient):
        raise AssertionError("Provided client is not of type ubiops.ApiClient")

    start_time = time()
    version_data = CoreApi(client).deployment_versions_get(
        project_name=project_name, deployment_name=deployment_name, version=version
    )

    if not revision_id:
        revision_id = version_data.latest_revision

    wait_for_environment(
        client=client,
        project_name=project_name,
        environment_name=version_data.environment,
        timeout=timeout,
        quiet=quiet,
        stream_logs=stream_logs,
    )

    elapsed_time = time() - start_time

    wait_for_revision(
        client=client,
        project_name=project_name,
        deployment_name=deployment_name,
        version=version,
        revision_id=revision_id,
        timeout=timeout - elapsed_time,
        quiet=quiet,
        stream_logs=stream_logs,
    )

    if not quiet:
        version_data = CoreApi(client).deployment_versions_get(
            project_name=project_name, deployment_name=deployment_name, version=version
        )
        print(f"{object_name}: {version_data.status}", flush=True)


def _wait_for_logs_deployment_request(
    client,
    project_name,
    deployment_name,
    request_id,
    retrieve_method,
    retrieve_kwargs,
    timeout=1800,
    object_name="Deployment request",
):
    """
    Wait for a deployment request to be completed and stream logs while waiting. This function is used for deployment
    (version) requests, experiment runs and deployment requests that are part of a pipeline request.

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str deployment_name: the name of the deployment
    :param str request_id: the id of the request
    :param retrieve_method: retrieve method to get status updates
    :param dict retrieve_kwargs: the data to pass to the retrieve method
    :param float timeout: the maximum time to wait
    :param str object_name: reference name for the request object, used to print success message
    """

    request_details = getattr(CoreApi(client), retrieve_method)(**retrieve_kwargs)
    _wait_for_logs(
        client=client,
        project_name=project_name,
        filters={
            "deployment_name": deployment_name,
            "deployment_version": request_details.version,
            "deployment_request_id": request_id,
        },
        retrieve_method=retrieve_method,
        retrieve_kwargs=retrieve_kwargs,
        object_name=object_name,
        start_date=request_details.time_created.isoformat(timespec="milliseconds"),
        timeout=timeout,
    )


def _wait_for_logs_pipeline_request(
    client, project_name, retrieve_method, retrieve_kwargs, object_name="Pipeline request", timeout=1800
):
    """
    Wait for a pipeline request to be completed and stream logs while waiting

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param retrieve_method: retrieve method to get status updates
    :param dict retrieve_kwargs: the data to pass to the retrieve method
    :param str object_name: reference name for the request object, used to print success message
    :param float timeout: the maximum time to wait
    """

    sequence_id = None

    while True:
        request_details = getattr(CoreApi(client), retrieve_method)(**retrieve_kwargs)

        # Combine deployment and sub-pipeline requests to one list
        object_requests = [(request, "deployment") for request in request_details.deployment_requests]
        object_requests.extend([(request, "pipeline") for request in request_details.pipeline_requests])

        # Sort on sequence_id
        object_requests = sorted(object_requests, key=lambda k: k[0].sequence_id)

        # Wait for all objects in the pipeline to finish
        waiting_for_requests = False
        for request, object_type in object_requests:
            # Wait only for the objects we didn't wait for yet
            if sequence_id and request.sequence_id <= sequence_id:
                continue

            waiting_for_requests = True
            sequence_id = request.sequence_id
            object_request_name = f"Request to '{request.pipeline_object}'"
            object_retrieve_kwargs = {
                "project_name": project_name,
                "version": request.version,
                "request_id": request.id,
                "metadata_only": True,
            }

            print(f"Start retrieving logs for '{request.pipeline_object}'")

            # Deployments
            if object_type == "deployment":
                _wait_for_logs_deployment_request(
                    client=client,
                    project_name=project_name,
                    deployment_name=request.deployment,
                    request_id=request.id,
                    retrieve_method="deployment_version_requests_get",
                    retrieve_kwargs={**object_retrieve_kwargs, "deployment_name": request.deployment},
                    object_name=object_request_name,
                    timeout=timeout,
                )

            # Sub-pipelines
            elif object_type == "pipeline":
                _wait_for_logs_pipeline_request(
                    client=client,
                    project_name=project_name,
                    retrieve_method="pipeline_version_requests_get",
                    retrieve_kwargs={**object_retrieve_kwargs, "pipeline_name": request.pipeline},
                    object_name=object_request_name,
                    timeout=timeout,
                )

        if request_details.status in SUCCESS_STATUSES:
            print(f"{object_name}: {request_details.status}", flush=True)
            return
        if request_details.status in FAILED_STATUSES:
            raise StatusError(f"{object_name}: {request_details.status}")

        # We are not waiting for any deployment request in this iteration, just waiting for the pipeline request status
        if not waiting_for_requests:
            sleep(2)


def wait_for_deployment_version(
    client, project_name, deployment_name, version, revision_id=None, timeout=1800, quiet=False, stream_logs=False
):
    """
    Wait for a deployment version to be ready: wait for the environment build and deployment revision to complete

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str deployment_name: the name of the deployment
    :param str version: the version of the deployment
    :param str revision_id: the build id of the revision - if not provided, the latest revision will be used
    :param float timeout: the maximum time to wait
    :param bool quiet: whether to suppress informational messages
    :param bool stream_logs: Whether to stream logs while waiting, only used when quiet=False. When set to True, we will
        wait 20 seconds longer than the environment and deployment revision were first seen as completed to make sure
        all logs are retrieved. Logs will be shown starting from environment last update time and deployment revision
        creation time.
    """

    try:
        _wait_for_deployment_version(
            client=client,
            project_name=project_name,
            deployment_name=deployment_name,
            version=version,
            revision_id=revision_id,
            timeout=timeout,
            quiet=quiet,
            stream_logs=stream_logs,
            object_name="Deployment version",
        )
    except KeyboardInterrupt:
        pass


def wait_for_experiment(
    client, project_name, experiment_name, revision_id=None, timeout=1800, quiet=False, stream_logs=False
):
    """
    Wait for an experiment to be ready

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str experiment_name: the name of the experiment
    :param str revision_id: the id of the revision - if not provided, the latest revision will be used
    :param float timeout: the maximum time to wait
    :param bool quiet: whether to suppress informational messages
    :param bool stream_logs: Whether to stream logs while waiting, only used when quiet=False. When set to True, we will
        wait 20 seconds longer than the environment and deployment revision were first seen as completed to make sure
        all logs are retrieved. Logs will be shown starting from environment last update time and deployment revision
        creation time.
    """

    try:
        _wait_for_deployment_version(
            client=client,
            project_name=project_name,
            deployment_name=DEFAULT_TRAINING_DEPLOYMENT_NAME,
            version=experiment_name,
            revision_id=revision_id,
            timeout=timeout,
            quiet=quiet,
            stream_logs=stream_logs,
            object_name="Experiment",
        )
    except KeyboardInterrupt:
        pass


def wait_for_environment(client, project_name, environment_name, timeout=1800, quiet=False, stream_logs=False):
    """
    Wait for an environment to be ready

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str environment_name: the name of the environment
    :param float timeout: the maximum time to wait
    :param bool quiet: whether to suppress informational messages
    :param bool stream_logs: Whether to stream logs while waiting, only used when quiet=False. When set to True, we will
        wait 20 seconds longer than the environment was first seen as completed to make sure all logs are retrieved.
        Logs will be shown from environment last_updated time onwards.
    """

    if not isinstance(client, ApiClient):
        raise AssertionError("Provided client is not of type ubiops.ApiClient")

    # Get the environment details
    environment = CoreApi(client).environments_get(project_name=project_name, environment_name=environment_name)

    if environment.base_environment is None:
        # Environment is a base environment, it doesn't need to build
        if not quiet:
            print("Environment: success", flush=True)
        return

    if not environment.latest_build or not environment.latest_revision:
        raise ApiException(status=404, reason="Not Found", body=f"No build found for environment {environment_name}")

    retrieve_method = "environment_builds_get"
    retrieve_kwargs = {
        "project_name": project_name,
        "environment_name": environment_name,
        "revision_id": environment.latest_revision,
        "build_id": environment.latest_build,
    }

    try:
        if stream_logs and not quiet:
            _wait_for_logs(
                client=client,
                project_name=project_name,
                filters={"environment_name": environment_name, "environment_build_id": environment.latest_build},
                retrieve_method=retrieve_method,
                retrieve_kwargs=retrieve_kwargs,
                object_name="Environment",
                start_date=environment.last_updated.isoformat(timespec="milliseconds"),
                timeout=timeout,
            )
        else:
            _wait_for(
                client=client,
                retrieve_method=retrieve_method,
                retrieve_kwargs=retrieve_kwargs,
                object_name="Environment",
                timeout=timeout,
                quiet=quiet,
            )
    except KeyboardInterrupt:
        pass


def wait_for_revision(
    client, project_name, deployment_name, version, revision_id, timeout=1800, quiet=False, stream_logs=False
):
    """
    Wait for a deployment revision to be ready

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str deployment_name: the name of the deployment
    :param str version: the version of the deployment
    :param str revision_id: the build id of the revision
    :param float timeout: the maximum time to wait
    :param bool quiet: whether to suppress informational messages
    :param bool stream_logs: Whether to stream logs while waiting, only used when quiet=False. When set to True, we will
        wait 20 seconds longer than the deployment revision was first seen as completed to make sure all logs are
        retrieved. Logs will be shown from revision creation time onwards.
    """

    if not isinstance(client, ApiClient):
        raise AssertionError("Provided client is not of type ubiops.ApiClient")

    retrieve_method = "revisions_get"
    retrieve_kwargs = {
        "project_name": project_name,
        "deployment_name": deployment_name,
        "version": version,
        "revision_id": revision_id,
    }

    try:
        if stream_logs and not quiet:
            request_details = getattr(CoreApi(client), retrieve_method)(**retrieve_kwargs)
            _wait_for_logs(
                client=client,
                project_name=project_name,
                filters={
                    "deployment_name": deployment_name,
                    "deployment_version": version,
                    "deployment_version_revision_id": revision_id,
                },
                retrieve_method=retrieve_method,
                retrieve_kwargs=retrieve_kwargs,
                object_name="Deployment revision",
                start_date=request_details.creation_date.isoformat(timespec="milliseconds"),
                timeout=timeout,
            )
        else:
            _wait_for(
                client=client,
                retrieve_method=retrieve_method,
                retrieve_kwargs=retrieve_kwargs,
                object_name="Deployment revision",
                timeout=timeout,
                quiet=quiet,
            )
    except KeyboardInterrupt:
        pass


def wait_for_deployment_request(
    client, project_name, deployment_name, request_id, timeout=1800, quiet=False, stream_logs=False
):
    """
    Wait for a deployment request to be completed

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str deployment_name: the name of the deployment
    :param str request_id: the id of the request
    :param float timeout: the maximum time to wait
    :param bool quiet: whether to suppress informational messages
    :param bool stream_logs: Whether to stream logs while waiting, only used when quiet=False. When set to True, we will
        wait 20 seconds longer than the request was first seen as completed to make sure all logs are retrieved. Logs
        will be shown from request creation time onwards.
    """

    if not isinstance(client, ApiClient):
        raise AssertionError("Provided client is not of type ubiops.ApiClient")

    retrieve_method = "deployment_requests_get"
    retrieve_kwargs = {
        "project_name": project_name,
        "deployment_name": deployment_name,
        "request_id": request_id,
        "metadata_only": True,
    }

    try:
        if stream_logs and not quiet:
            _wait_for_logs_deployment_request(
                client=client,
                project_name=project_name,
                deployment_name=deployment_name,
                request_id=request_id,
                retrieve_method=retrieve_method,
                retrieve_kwargs=retrieve_kwargs,
                object_name="Deployment request",
                timeout=timeout,
            )
        else:
            _wait_for(
                client=client,
                retrieve_method=retrieve_method,
                retrieve_kwargs=retrieve_kwargs,
                object_name="Deployment request",
                timeout=timeout,
                quiet=quiet,
            )
    except KeyboardInterrupt:
        pass


def wait_for_deployment_version_request(
    client, project_name, deployment_name, version, request_id, timeout=1800, quiet=False, stream_logs=False
):
    """
    Wait for a deployment version request to be completed

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str deployment_name: the name of the deployment
    :param str version: the version of the deployment
    :param str request_id: the id of the request
    :param float timeout: the maximum time to wait
    :param bool quiet: whether to suppress informational messages
    :param bool stream_logs: Whether to stream logs while waiting, only used when quiet=False. When set to True, we will
        wait 20 seconds longer than the request was first seen as completed to make sure all logs are retrieved. Logs
        will be shown from request creation time onwards.
    """

    if not isinstance(client, ApiClient):
        raise AssertionError("Provided client is not of type ubiops.ApiClient")

    retrieve_method = "deployment_version_requests_get"
    retrieve_kwargs = {
        "project_name": project_name,
        "deployment_name": deployment_name,
        "version": version,
        "request_id": request_id,
        "metadata_only": True,
    }

    try:
        if stream_logs and not quiet:
            _wait_for_logs_deployment_request(
                client=client,
                project_name=project_name,
                deployment_name=deployment_name,
                request_id=request_id,
                retrieve_method=retrieve_method,
                retrieve_kwargs=retrieve_kwargs,
                object_name="Deployment version request",
                timeout=timeout,
            )
        else:
            _wait_for(
                client=client,
                retrieve_method=retrieve_method,
                retrieve_kwargs=retrieve_kwargs,
                object_name="Deployment version request",
                timeout=timeout,
                quiet=quiet,
            )
    except KeyboardInterrupt:
        pass


def wait_for_experiment_run(
    client, project_name, experiment_name, run_id, timeout=1800, quiet=False, stream_logs=False
):
    """
    Wait for an experiment run to be completed

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str experiment_name: the name of the experiment
    :param str run_id: the id of the training run
    :param float timeout: the maximum time to wait
    :param bool quiet: whether to suppress informational messages
    :param bool stream_logs: Whether to stream logs while waiting, only used when quiet=False. When set to True, we will
        wait 20 seconds longer than the training run was first seen as completed to make sure all logs are retrieved.
        Logs will be shown from training run creation time onwards.
    """

    if not isinstance(client, ApiClient):
        raise AssertionError("Provided client is not of type ubiops.ApiClient")

    retrieve_method = "deployment_version_requests_get"
    retrieve_kwargs = {
        "project_name": project_name,
        "deployment_name": DEFAULT_TRAINING_DEPLOYMENT_NAME,
        "version": experiment_name,
        "request_id": run_id,
        "metadata_only": True,
    }

    try:
        if stream_logs and not quiet:
            _wait_for_logs_deployment_request(
                client=client,
                project_name=project_name,
                deployment_name=DEFAULT_TRAINING_DEPLOYMENT_NAME,
                request_id=run_id,
                retrieve_method=retrieve_method,
                retrieve_kwargs=retrieve_kwargs,
                object_name="Experiment run",
                timeout=timeout,
            )
        else:
            _wait_for(
                client=client,
                retrieve_method=retrieve_method,
                retrieve_kwargs=retrieve_kwargs,
                object_name="Experiment run",
                timeout=timeout,
                quiet=quiet,
            )
    except KeyboardInterrupt:
        pass


def wait_for_pipeline_request(
    client, project_name, pipeline_name, request_id, timeout=1800, quiet=False, stream_logs=False
):
    """
    Wait for a pipeline request to be completed

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str pipeline_name: the name of the pipeline
    :param str request_id: the id of the request
    :param float timeout: The maximum time to wait. When stream_logs=True, this it the maximum time to wait for each
        deployment request
    :param bool quiet: whether to suppress informational messages
    :param bool stream_logs: Whether to stream logs while waiting, only used when quiet=False. When set to True, we will
        wait 20 seconds longer than the request was first seen as completed to make sure all logs are retrieved. Logs
        will be shown from request creation time onwards.
    """

    if not isinstance(client, ApiClient):
        raise AssertionError("Provided client is not of type ubiops.ApiClient")

    retrieve_method = "pipeline_requests_get"
    retrieve_kwargs = {
        "project_name": project_name,
        "pipeline_name": pipeline_name,
        "request_id": request_id,
        "metadata_only": True,
    }

    try:
        if stream_logs and not quiet:
            _wait_for_logs_pipeline_request(
                client=client,
                project_name=project_name,
                retrieve_method=retrieve_method,
                retrieve_kwargs=retrieve_kwargs,
                timeout=timeout,
            )
        else:
            _wait_for(
                client=client,
                retrieve_method=retrieve_method,
                retrieve_kwargs=retrieve_kwargs,
                object_name="Pipeline request",
                timeout=timeout,
                quiet=quiet,
            )
    except KeyboardInterrupt:
        pass


def wait_for_pipeline_version_request(
    client, project_name, pipeline_name, version, request_id, timeout=1800, quiet=False, stream_logs=False
):
    """
    Wait for a pipeline version request to be completed

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str pipeline_name: the name of the pipeline
    :param str version: the version of the pipeline
    :param str request_id: the id of the request
    :param float timeout: the maximum time to wait
    :param bool quiet: whether to suppress informational messages
    :param bool stream_logs: Whether to stream logs while waiting, only used when quiet=False. When set to True, we will
        wait 20 seconds longer than the request was first seen as completed to make sure all logs are retrieved. Logs
        will be shown from request creation time onwards.
    """

    if not isinstance(client, ApiClient):
        raise AssertionError("Provided client is not of type ubiops.ApiClient")

    retrieve_method = "pipeline_version_requests_get"
    retrieve_kwargs = {
        "project_name": project_name,
        "pipeline_name": pipeline_name,
        "version": version,
        "request_id": request_id,
        "metadata_only": True,
    }

    try:
        if stream_logs and not quiet:
            _wait_for_logs_pipeline_request(
                client=client,
                project_name=project_name,
                retrieve_method=retrieve_method,
                retrieve_kwargs=retrieve_kwargs,
                timeout=timeout,
            )
        else:
            _wait_for(
                client=client,
                retrieve_method=retrieve_method,
                retrieve_kwargs=retrieve_kwargs,
                object_name="Pipeline version request",
                timeout=timeout,
                quiet=quiet,
            )
    except KeyboardInterrupt:
        pass


def wait_for_export(client, project_name, export_id, timeout=1800, quiet=False):
    """
    Wait for an export to be completed

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str export_id: the id of the export
    :param float timeout: the maximum time to wait
    :param bool quiet: whether to suppress informational messages
    """

    if not isinstance(client, ApiClient):
        raise AssertionError("Provided client is not of type ubiops.ApiClient")

    try:
        _wait_for(
            client=client,
            retrieve_method="exports_get",
            retrieve_kwargs={"project_name": project_name, "export_id": export_id},
            object_name="Export",
            timeout=timeout,
            quiet=quiet,
        )
    except KeyboardInterrupt:
        pass


def wait_for_import(client, project_name, import_id, timeout=1800, quiet=False):
    """
    Wait for an import to be completed or ready for confirmation

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str import_id: the id of the import
    :param float timeout: the maximum time to wait
    :param bool quiet: whether to suppress informational messages
    """

    if not isinstance(client, ApiClient):
        raise AssertionError("Provided client is not of type ubiops.ApiClient")

    try:
        _wait_for(
            client=client,
            retrieve_method="imports_get",
            retrieve_kwargs={"project_name": project_name, "import_id": import_id},
            object_name="Import",
            timeout=timeout,
            quiet=quiet,
        )
    except KeyboardInterrupt:
        pass

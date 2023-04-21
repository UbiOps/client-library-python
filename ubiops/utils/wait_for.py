from time import sleep, time

from ubiops import CoreApi
from ubiops.api_client import ApiClient
from ubiops.exceptions import ApiException
from ubiops.utils.exceptions import BuildStatusError

SUCCESS_STATUSES = ['success']
FAILED_STATUSES = ['failed', 'cancelled']


def wait_for_deployment_version(client, project_name, deployment_name, version, revision_id=None, timeout=1800,
                                quiet=False):
    """
    Wait for a deployment version to be ready: wait for the environment build and deployment revision to complete

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param string project_name: The name of the project
    :param string deployment_name: The name of the deployment
    :param string version: The version of the deployment
    :param string revision_id: The build id of the revision - if not provided, the latest revision will be used
    :param float timeout: The maximum time to wait for the deployment version to be ready
    :param bool quiet: Whether to suppress informational messages
    """

    if not isinstance(client, ApiClient):
        raise AssertionError("Provided client is not of type ubiops.ApiClient")

    api = CoreApi(client)
    start_time = time()
    version_data = api.deployment_versions_get(
        project_name=project_name, deployment_name=deployment_name, version=version
    )

    if not revision_id:
        revision_id = version_data.latest_revision

    wait_for_environment(
        client=client,
        project_name=project_name,
        environment_name=version_data.environment,
        timeout=timeout,
        quiet=quiet
    )

    elapsed_time = time() - start_time

    wait_for_revision(
        client=client,
        project_name=project_name,
        deployment_name=deployment_name,
        version=version,
        revision_id=revision_id,
        timeout=timeout - elapsed_time,
        quiet=quiet
    )

    if not quiet:
        version_data = api.deployment_versions_get(
            project_name=project_name, deployment_name=deployment_name, version=version
        )
        print("Deployment version:", version_data.status)


def wait_for_experiment(client, project_name, deployment_name, version, revision_id=None, timeout=1800):
    """
    Wait for a deployment version to be ready

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param string project_name: The name of the project
    :param string deployment_name: The name of the deployment
    :param string version: The version of the deployment
    :param string revision_id: The id of the revision - if not provided, the latest revision will be used
    :param float timeout: The maximum time to wait for the deployment version to be ready
    """

    api = CoreApi(client)
    start_time = time()
    deployment_version_data = api.deployment_versions_get(
        project_name=project_name,
        deployment_name=deployment_name,
        version=version
    )

    if not revision_id:
        revision_id = deployment_version_data.latest_revision

    try:
        wait_for_environment(
            client=client,
            project_name=project_name,
            environment_name=deployment_version_data.environment,
            timeout=timeout
        )
    except ApiException as e:
        # If error is 404 Not Found - environment is base environment and does not need to be built
        if (e.status, e.reason) != (404, 'Not Found'):
            raise e

    elapsed_time = time() - start_time

    wait_for_revision(
        client=client,
        project_name=project_name,
        deployment_name=deployment_name,
        version=version,
        revision_id=revision_id,
        timeout=timeout - elapsed_time
    )
    print("Experiment %s is ready" % version)


def wait_for_environment(client, project_name, environment_name, timeout=1800, quiet=False):
    """
    Wait for an environment to be ready

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param string project_name: The name of the project
    :param string environment_name: The name of the environment
    :param float timeout: The maximum time to wait for the environment to be ready
    :param bool quiet: Whether to suppress informational messages
    """

    if not isinstance(client, ApiClient):
        raise AssertionError("Provided client is not of type ubiops.ApiClient")

    api = CoreApi(client)

    # Get the environment details
    environment = api.environments_get(project_name=project_name, environment_name=environment_name)

    if environment.base_environment is None:
        # Environment is a base environment, it doesn't need to build
        if not quiet:
            print("Environment: success")
        return

    if not environment.latest_build or not environment.latest_revision:
        raise ApiException(
            status=404, reason="Not Found", body="No build found for environment %s" % environment_name
        )

    first_iteration = True
    start_time = time()
    printed_len = 0

    while True:
        build = api.environment_builds_get(
            project_name=project_name,
            environment_name=environment_name,
            revision_id=environment.latest_revision,
            build_id=environment.latest_build
        )

        # Print status
        if not quiet:
            # Do at beginning to prevent not showing any output when the request is slow
            if not first_iteration:
                print("\r" + " " * printed_len, end='\r', flush=True)

            print_str = "Environment: %s" % build.status
            printed_len = len(print_str) + 4
            print(print_str, end="", flush=True)

        # Build completed
        if build.status in SUCCESS_STATUSES:
            if not quiet:
                print()  # Close last \r
            return
        if build.status in FAILED_STATUSES:
            if not quiet:
                print()  # Close last \r
            raise BuildStatusError('Environment build %s' % build.status)

        # Handle timeout
        if time() - start_time > timeout:
            raise ApiException(
                status=504, reason="Environment Timeout", body="Failed to build environment within timeout"
            )

        # Wait and print dots
        for _ in range(3):
            sleep(1)
            if not quiet:
                print('.', end='', flush=True)

        sleep(1)
        first_iteration = False


def wait_for_revision(client, project_name, deployment_name, version, revision_id, timeout=1800, quiet=False):
    """
    Wait for a deployment revision to be ready

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param string project_name: The name of the project
    :param string deployment_name: The name of the deployment
    :param string version: The version of the deployment
    :param string revision_id: The build id of the revision
    :param float timeout: The maximum time to wait for the revision to be ready
    :param bool quiet: Whether to suppress informational messages
    """

    if not isinstance(client, ApiClient):
        raise AssertionError("Provided client is not of type ubiops.ApiClient")

    api = CoreApi(client)

    first_iteration = True
    start_time = time()
    printed_len = 0

    while True:
        revision = api.revisions_get(
            project_name=project_name, deployment_name=deployment_name, version=version, revision_id=revision_id
        )

        # Print status
        if not quiet:
            # Do at beginning to prevent not showing any output when the request is slow
            if not first_iteration:
                print("\r" + " " * printed_len, end='\r', flush=True)

            print_str = "Deployment revision: %s" % revision.status
            printed_len = len(print_str) + 4
            print(print_str, end="", flush=True)

        # Build completed
        if revision.status in SUCCESS_STATUSES:
            if not quiet:
                print()  # Close last \r
            return
        if revision.status in FAILED_STATUSES:
            if not quiet:
                print()  # Close last \r
            raise BuildStatusError('Deployment revision build %s' % revision.status)

        # Handle timeout
        if time() - start_time > timeout:
            raise ApiException(
                status=504, reason="Revision Timeout", body="Failed to build deployment revision within timeout"
            )

        # Wait and print dots
        for _ in range(3):
            sleep(1)
            if not quiet:
                print('.', end='', flush=True)

        sleep(1)
        first_iteration = False

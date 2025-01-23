import json
import requests

from ubiops.exceptions import UbiOpsException
from ubiops.models import DeploymentRequestCreateResponse, PipelineRequestCreateResponse


def stream_request(
    client, project_name, reference_type, reference_name, version=None, data=None, timeout=3600, full_response=False
):
    """
    Create a streaming request to a deployment or pipeline version

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str reference_type: type of the reference, either deployment or pipeline
    :param str reference_name: the name of the deployment or pipeline
    :param str version: the name of the version. If not provided, requests are made to the default version.
    :param str|dict|list[dict] data: request data
    :param int timeout: timeout for the request
    :param bool full_response: whether to return the full response of the request
    :return: partial results of the request and, if requested, the full response at the end of the request
    """

    headers = {"Accept": "text/event-stream", "User-Agent": client.user_agent}
    if "Authorization" in client.configuration.api_key:
        headers["Authorization"] = client.configuration.get_api_key_with_prefix("Authorization")

    if isinstance(data, str):
        headers["Content-Type"] = client.select_header_content_type(["text/plain"])
    elif isinstance(data, dict) or isinstance(data, list):
        headers["Content-Type"] = client.select_header_content_type(["application/json"])
        data = json.dumps(data)
    else:
        raise UbiOpsException(
            f"Input data must be of type dict or list for structured {reference_type}s and of type string for plain "
            f"{reference_type}s"
        )

    url = f"{client.configuration.host}/projects/{project_name}/{reference_type}s/{reference_name}"
    if version:
        url += f"/versions/{version}"

    url += f"/requests/stream?timeout={timeout}"

    stream_response = requests.post(
        url=url,
        headers=headers,
        data=data if data is not None else "",
        stream=True,
        params={"timeout": timeout},
    )

    for line in stream_response.iter_lines():
        line = line.decode("utf-8")
        if line.startswith("data:"):
            yield line[5:]
        elif not line.startswith("event:") and not line.startswith("update:") and line != "":
            try:
                line_json = json.loads(line)

                try:
                    error_message = json.loads(line)["error_message"]
                except (ValueError, KeyError):
                    error_message = None

                if error_message:
                    raise UbiOpsException(f"Request failed with error message: {error_message}")

                if full_response:
                    if reference_type == "deployment":
                        yield DeploymentRequestCreateResponse(**line_json)
                    else:
                        yield PipelineRequestCreateResponse(**line_json)

            except json.JSONDecodeError as e:
                print(f"Error decoding the the full response JSON: {e}")

                if full_response:
                    yield line


def stream_deployment_request(
    client, project_name, deployment_name, version=None, data=None, timeout=3600, full_response=False
):
    """
    Create a streaming request to a deployment version

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str deployment_name: the name of the deployment
    :param str version: the name of the deployment version. If not provided, requests are made to the default version
        of the deployment.
    :param str|dict|list[dict] data: request data
    :param int timeout: timeout for the request
    :param bool full_response: whether to return the full response of the request
    :return: partial results of the request and, if requested, the full response at the end of the request
    """

    return stream_request(
        client=client,
        project_name=project_name,
        reference_type="deployment",
        reference_name=deployment_name,
        version=version,
        data=data,
        timeout=timeout,
        full_response=full_response,
    )


def stream_pipeline_request(
    client, project_name, pipeline_name, version=None, data=None, timeout=7200, full_response=False
):
    """
    Create a streaming request to a pipeline version

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str pipeline_name: the name of the pipeline
    :param str version: the name of the pipeline version. If not provided, requests are made to the default version
        of the pipeline.
    :param str|dict|list[dict] data: request data
    :param int timeout: timeout for the request
    :param bool full_response: whether to return the full response of the request
    :return: partial results of the request and, if requested, the full response at the end of the request
    """

    return stream_request(
        client=client,
        project_name=project_name,
        reference_type="pipeline",
        reference_name=pipeline_name,
        version=version,
        data=data,
        timeout=timeout,
        full_response=full_response,
    )

import json
import requests

from ubiops.exceptions import UbiOpsException


def stream_deployment_request(
    client, project_name, deployment_name, version=None, data=None, timeout=30, full_response=False
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

    headers = {"Accept": "text/event-stream"}
    if "Authorization" in client.configuration.api_key:
        headers["Authorization"] = client.configuration.get_api_key_with_prefix("Authorization")

    if isinstance(data, str):
        headers["Content-Type"] = client.select_header_content_type(["text/plain"])
    elif isinstance(data, dict) or isinstance(data, list):
        headers["Content-Type"] = client.select_header_content_type(["application/json"])
        data = json.dumps(data)
    else:
        raise UbiOpsException(
            "Input data must be of type dict or list for structured deployments and of type string"
            "for plain deployments"
        )

    url = f"{client.configuration.host}/projects/{project_name}/deployments/{deployment_name}"
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
                    yield line_json

            except json.JSONDecodeError as e:
                print(f"Error decoding the the full response JSON: {e}")

                if full_response:
                    yield line

from os import path

import requests

from ubiops import CoreApi
from ubiops.exceptions import ApiException


def upload_file(client, project_name, file_path, bucket_name='default', file_name=None):
    """
    Upload a file to a bucket

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str file_path: the location of the file to upload
    :param str bucket_name: the name of the bucket
    :param str file_name: the name of the file in the bucket. May contain prefixes.
    :return: ubiops file uri, which you can use in your request data for file input fields
    """

    core_api = CoreApi(client)

    # Use the basename of the file_path if not a more specific name is provided for the file in the bucket.
    file_name = path.basename(file_path) if file_name is None else file_name

    response = core_api.files_upload(
        project_name=project_name,
        bucket_name=bucket_name,
        file=file_name,
    )

    # Azure requires custom headers in the request
    if response.provider == 'azure_blob_storage':
        headers = {
            'x-ms-version': '2020-04-08',
            'x-ms-blob-type': 'BlockBlob'
        }
    else:
        headers = {}

    with open(file_path, "rb") as filestream:
        try:
            response = requests.put(url=response.url, headers=headers, data=filestream)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise ApiException(
                status=e.response.status_code,
                reason=str(e)
            )

    return f"ubiops-file://{bucket_name}/{file_name}"


def download_file(client, project_name, bucket_name='default', file_name=None, file_uri=None, output_path='.',
                  stream=True, chunk_size=8192):
    """
    Download a file from a bucket by either providing a bucket_name and file_name, or
        a file_uri (e.g. 'ubiops-file://default/my-file.jpg')

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str bucket_name: the name of the bucket
    :param str file_name: the name of the file to download
    :param str file_uri: bucket name and file name formatted as ubiops uri, e.g. 'ubiops-file://default/my-file.jpg'
    :param str output_path: the file or directory location to download the file to
    :param bool stream: whether to download the file streaming or not
    :param int chunk_size: if streaming enabled, the size for each chunk
    """

    assert (bucket_name and file_name) or file_uri, "Please, use either bucket_name and file_name or file_uri"
    assert not (bucket_name and file_name and file_uri), "Please, use either bucket_name and file_name or file_uri, " \
                                                         "not both"

    core_api = CoreApi(client)

    if file_uri:
        assert str(file_uri).startswith("ubiops-file://"), "Wrong format given for file_uri"
        bucket_file_split = str(file_uri)[len("ubiops-file://"):].split('/', maxsplit=1)

        assert len(bucket_file_split) == 2, "Wrong format given for file_uri"
        bucket_name, file_name = bucket_file_split

    response = core_api.files_download(
        project_name=project_name,
        bucket_name=bucket_name,
        file=file_name
    )
    try:
        response = requests.get(url=response.url, stream=stream)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise ApiException(
            status=e.response.status_code,
            reason=str(e)
        )

    if path.isdir(output_path):
        output_path = path.join(output_path, path.basename(file_name))

    with open(output_path, "wb") as filestream:
        if not stream:
            filestream.write(response.content)
        else:
            for chunk in response.iter_content(chunk_size=chunk_size):
                filestream.write(chunk)

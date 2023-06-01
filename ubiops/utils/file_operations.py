import logging
import requests

from os import path
from shutil import make_archive

from ubiops import CoreApi
from ubiops.api_client import ApiClient
from ubiops.exceptions import ApiException


logger = logging.getLogger("FileOperations")


class UbiOpsFile:
    """
    Utility class for UbiOps files
    """

    def __init__(self, bucket, file):
        self._bucket = bucket
        self._file = file

    @classmethod
    def from_uri(cls, file_uri):
        if cls.validate_uri(file_uri=file_uri):
            bucket_file_split = str(file_uri)[len("ubiops-file://"):].split('/', maxsplit=1)
            return cls(*bucket_file_split)
        else:
            return None

    @classmethod
    def validate_uri(cls, file_uri):
        if not isinstance(file_uri, str):
            raise ValueError("Wrong type given for file_uri: %s" % type(file_uri))

        if not file_uri.startswith("ubiops-file://"):
            raise ValueError("Wrong format given for file_uri %s" % file_uri)

        bucket_file_split = str(file_uri)[len("ubiops-file://"):].split('/', maxsplit=1)

        if not len(bucket_file_split) == 2:
            raise ValueError("Wrong format given for file_uri %s" % file_uri)

        return True

    @property
    def bucket(self):
        return self._bucket

    @property
    def file(self):
        return self._file

    @property
    def file_uri(self):
        return "ubiops-file://%s/%s" % (self._bucket, self._file)


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

    if not isinstance(client, ApiClient):
        raise AssertionError("Provided client is not of type ubiops.ApiClient")

    core_api = CoreApi(client)

    # Use the basename of the file_path if not a more specific name is provided for the file in the bucket.
    file_name = path.basename(file_path) if file_name is None else file_name

    response = core_api.files_upload(project_name=project_name, bucket_name=bucket_name, file=file_name)

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

        except requests.exceptions.ConnectionError as e:
            raise ApiException(status=502, reason="Connection Error", body="Failed to connect to bucket\n%s" % e)

        except requests.exceptions.Timeout:
            raise ApiException(status=504, reason="Connection Timeout", body="Failed to upload file")

        except requests.exceptions.RequestException as e:
            raise ApiException(status=502, reason="Upload Error", body="Failed to upload file\n%s" % e)

        if response.status_code < 200 or response.status_code > 300:
            raise ApiException(requests_resp=response)

    return "ubiops-file://%s/%s" % (bucket_name, file_name)


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
        ubiops_file = UbiOpsFile.from_uri(file_uri=file_uri)
    else:
        ubiops_file = UbiOpsFile(bucket=bucket_name, file=file_name)

    response = core_api.files_download(
        project_name=project_name,
        bucket_name=ubiops_file.bucket,
        file=ubiops_file.file
    )
    try:
        response = requests.get(url=response.url, stream=stream)

    except requests.exceptions.ConnectionError as e:
        raise ApiException(status=502, reason="Connection Error", body="Failed to connect to bucket\n%s" % e)

    except requests.exceptions.Timeout:
        raise ApiException(status=504, reason="Connection Timeout", body="Failed to download file")

    except requests.exceptions.RequestException as e:
        raise ApiException(status=502, reason="Download Error", body="Failed to download file\n%s" % e)

    if response.status_code < 200 or response.status_code > 300:
        raise ApiException(requests_resp=response)

    if path.isdir(output_path):
        output_path = path.join(output_path, path.basename(ubiops_file.file))

    with open(output_path, "wb") as filestream:
        if not stream:
            filestream.write(response.content)
        else:
            for chunk in response.iter_content(chunk_size=chunk_size):
                filestream.write(chunk)


def handle_file_input(client, project_name, file, bucket_name='default', file_prefix=None, file_name=None):
    """
    Handle file input:
    - `file` can be an UbiOps file uri; validate the file exists and, if required, is a zip
    - `file` can be a directory; zip and upload it
    - `file` can be a file; zip if required, and upload it

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str file: the path to a local file or directory, or an ubiops uri, e.g. 'ubiops-file://default/my-file.jpg'
    :param str bucket_name: the name of the bucket to upload the file to in case of a local file/directory
    :param str file_prefix: optional prefix of the file in the bucket
    :param str file_name: optional name of the file in the bucket in case of a local file/directory. If None, the name
        of the local file is used. May contain prefixes.
        The file will be uploaded to "{bucket_name}/{file_prefix}{file_name}".
    """

    if not isinstance(file, str):
        raise ApiException(status=400, reason="Invalid", body="File %s is not a string" % file)

    try:
        ubiops_file = UbiOpsFile.from_uri(file)
    except ValueError:
        ubiops_file = None

    if ubiops_file:
        core_api = CoreApi(client)

        try:
            core_api.files_get(project_name=project_name, bucket_name=ubiops_file.bucket, file=ubiops_file.file)

        except ApiException as e:
            if e.status == 404:
                raise ApiException(status=404, reason="Not Found", body="File %s not found" % file)
            else:
                raise

        return file

    def _format_file_name(file_path):
        name = path.basename(file_path) if file_name is None else file_name
        if file_prefix:
            name = "%s%s" % (file_prefix, name)
        return name

    if file.endswith('.zip'):
        return upload_file(
            client=client, project_name=project_name, file_path=file,
            bucket_name=bucket_name, file_name=_format_file_name(file)
        )

    if path.isdir(file):
        zip_file = make_archive(path.basename(file), 'zip', file)
        return upload_file(
            client=client, project_name=project_name, file_path=zip_file,
            bucket_name=bucket_name, file_name=_format_file_name(zip_file)
        )

    if path.isfile(file):
        return upload_file(
            client=client, project_name=project_name, file_path=file,
            bucket_name=bucket_name, file_name=_format_file_name(file)
        )

    raise ApiException(
        status=400, reason="Invalid", body="File %s is not a ubiops-file:// or local directory or local file" % file
    )

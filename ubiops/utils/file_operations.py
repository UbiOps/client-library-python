import logging
import requests
import tqdm

from os import path, stat
from shutil import make_archive
from tqdm.utils import CallbackIOWrapper

from ubiops import CoreApi
from ubiops.api_client import ApiClient
from ubiops.exceptions import ApiConnectionError, ApiException, ApiRequestError, ApiTimeoutError


logger = logging.getLogger("FileOperations")


class UbiOpsFile:
    """
    Utility class for UbiOps files
    """

    def __init__(self, bucket, file):
        """
        Initialize UbiOps File with bucket and filename

        :param str bucket: the bucket where the file is located
        :param str file: the filename in the bucket
        """

        self._bucket = bucket
        self._file = file

    @staticmethod
    def remove_file_prefix(file_uri):
        """
        Remove 'ubiops-file://'-prefix from file uri

        :param str file_uri: the file uri to remove the prefix from
        """

        if file_uri.startswith("ubiops-file://"):
            return file_uri[14:]
        return file_uri

    @classmethod
    def from_uri(cls, file_uri):
        """
        Initialize UbiOps File from file uri

        :param str file_uri: the file uri to initialize from
        """

        if cls.validate_uri(file_uri=file_uri):
            without_prefix = cls.remove_file_prefix(file_uri=str(file_uri))
            bucket_file_split = without_prefix.split("/", maxsplit=1)
            return cls(*bucket_file_split)
        else:
            return None

    @classmethod
    def validate_uri(cls, file_uri):
        """
        Validate the format of a file uri

        :param str file_uri: the file uri to validate
        """

        if not isinstance(file_uri, str):
            raise ValueError(f"Wrong type given for file_uri: {type(file_uri)}")

        if not file_uri.startswith("ubiops-file://"):
            raise ValueError(f"Wrong format given for file_uri {file_uri}")

        without_prefix = cls.remove_file_prefix(file_uri=str(file_uri))
        bucket_file_split = without_prefix.split("/", maxsplit=1)

        if not len(bucket_file_split) == 2:
            raise ValueError(f"Wrong format given for file_uri {file_uri}")

        return True

    @property
    def bucket(self):
        """
        The bucket where the file is located
        """

        return self._bucket

    @property
    def file(self):
        """
        The filename in the bucket
        """

        return self._file

    @property
    def file_uri(self):
        """
        The bucket and filename in UbiOps file uri format
        """

        return f"ubiops-file://{self._bucket}/{self._file}"


def upload_file(client, project_name, file_path, bucket_name="default", file_name=None, _progress_bar=True):
    """
    Upload a file to a bucket

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str file_path: the location of the file to upload
    :param str bucket_name: the name of the bucket
    :param str file_name: the name of the file in the bucket. May contain prefixes.
    :param bool _progress_bar: whether to show a TQDM progress bar
    :return: ubiops file uri, which you can use in your request data for file input fields
    """

    if not isinstance(client, ApiClient):
        raise AssertionError("Provided client is not of type ubiops.ApiClient")

    core_api = CoreApi(client)

    # Use the basename of the file_path if not a more specific name is provided for the file in the bucket.
    file_name = path.basename(file_path) if file_name is None else file_name
    file_size = stat(file_path).st_size

    response = core_api.files_upload(project_name=project_name, bucket_name=bucket_name, file=file_name)

    headers = {"Content-Disposition": "multipart/form-data"}

    # Azure requires custom headers in the request
    if response.provider == "azure_blob_storage":
        headers["x-ms-version"] = "2020-04-08"
        headers["x-ms-blob-type"] = "BlockBlob"

    with open(file_path, "rb") as filestream:
        try:
            if _progress_bar:
                with tqdm.tqdm(
                    total=file_size,
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024,
                    miniters=1,
                    desc=f"Uploading {file_name}",
                ) as bar:
                    file_wrapper = CallbackIOWrapper(bar.update, filestream, "read")
                    response = requests.put(url=response.url, headers=headers, data=file_wrapper)
            else:
                response = requests.put(url=response.url, headers=headers, data=filestream)

        except requests.exceptions.ConnectionError as e:
            raise ApiConnectionError(status=502, reason="Connection Error", body=f"Failed to connect to bucket\n{e}")

        except requests.exceptions.Timeout:
            raise ApiTimeoutError(status=504, reason="Connection Timeout", body="Failed to upload file")

        except requests.exceptions.RequestException as e:
            raise ApiRequestError(status=502, reason="Upload Error", body=f"Failed to upload file\n{e}")

        if not 200 <= response.status_code <= 299:
            raise ApiRequestError(requests_resp=response)

    return f"ubiops-file://{bucket_name}/{file_name}"


def download_file(
    client,
    project_name,
    bucket_name="default",
    file_name=None,
    file_uri=None,
    output_path=".",
    stream=True,
    chunk_size=8192,
    _progress_bar=True,
):
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
    :param bool _progress_bar: whether to show a TQDM progress bar
    """

    assert (bucket_name and file_name) or file_uri, "Please, use either bucket_name and file_name or file_uri"
    assert not (bucket_name and file_name and file_uri), (
        "Please, use either bucket_name and file_name or file_uri, " "not both"
    )

    core_api = CoreApi(client)

    if file_uri:
        ubiops_file = UbiOpsFile.from_uri(file_uri=file_uri)
    else:
        ubiops_file = UbiOpsFile(bucket=bucket_name, file=file_name)

    response = core_api.files_download(project_name=project_name, bucket_name=ubiops_file.bucket, file=ubiops_file.file)
    try:
        response = requests.get(url=response.url, stream=stream)

    except requests.exceptions.ConnectionError as e:
        raise ApiConnectionError(status=502, reason="Connection Error", body=f"Failed to connect to bucket\n{e}")

    except requests.exceptions.Timeout:
        raise ApiTimeoutError(status=504, reason="Connection Timeout", body="Failed to download file")

    except requests.exceptions.RequestException as e:
        raise ApiRequestError(status=502, reason="Download Error", body=f"Failed to download file\n{e}")

    if not 200 <= response.status_code <= 299:
        raise ApiRequestError(requests_resp=response)

    if path.isdir(output_path):
        output_path = path.join(output_path, path.basename(ubiops_file.file))

    with open(output_path, "wb") as filestream:
        if not stream:
            filestream.write(response.content)

        elif _progress_bar:
            with tqdm.tqdm(
                unit="B",
                unit_scale=True,
                unit_divisor=1024,
                miniters=1,
                desc=f"Downloading {ubiops_file.file}",
                total=int(response.headers.get("Content-Length", 0)),
            ) as bar:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    filestream.write(chunk)
                    bar.update(len(chunk))

        else:
            for chunk in response.iter_content(chunk_size=chunk_size):
                filestream.write(chunk)


def handle_file_input(
    client, project_name, file, bucket_name="default", file_prefix=None, file_name=None, _progress_bar=True
):
    """
    Handle file input:
    - `file` can be an UbiOps file uri; validate the file exists
    - `file` can be a directory; zip and upload it
    - `file` can be a file; upload it

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param str file: the path to a local file or directory, or an ubiops uri, e.g. 'ubiops-file://default/my-file.jpg'
    :param str bucket_name: the name of the bucket to upload the file to in case of a local file/directory
    :param str file_prefix: optional prefix of the file in the bucket
    :param str file_name: optional name of the file in the bucket in case of a local file/directory. If None, the name
        of the local file is used. May contain prefixes.
        The file will be uploaded to "{bucket_name}/{file_prefix}{file_name}".
    :param bool _progress_bar: whether to show a TQDM progress bar
    """

    if not isinstance(file, str):
        raise ApiException(status=400, reason="Invalid", body=f"File {file} is not a string")

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
                raise ApiException(status=404, reason="Not Found", body=f"File {file} not found")
            else:
                raise

        return file

    def _format_file_name(file_path):
        name = path.basename(file_path) if file_name is None else file_name
        if file_prefix:
            name = f"{file_prefix}{name}"
        return name

    if path.isdir(file):
        zip_file = make_archive(path.basename(file), "zip", file)
        return upload_file(
            client=client,
            project_name=project_name,
            file_path=zip_file,
            bucket_name=bucket_name,
            file_name=_format_file_name(zip_file),
            _progress_bar=_progress_bar,
        )

    if path.isfile(file):
        return upload_file(
            client=client,
            project_name=project_name,
            file_path=file,
            bucket_name=bucket_name,
            file_name=_format_file_name(file),
            _progress_bar=_progress_bar,
        )

    raise ApiException(
        status=400, reason="Invalid", body=f"File {file} is not a ubiops-file:// or local directory or local file"
    )

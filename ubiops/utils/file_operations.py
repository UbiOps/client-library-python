import base64
import logging
import math
import os
import requests
import tqdm

from contextlib import nullcontext
from multiprocessing.pool import ThreadPool
from os import path, stat, makedirs
from shutil import make_archive
from tqdm.utils import CallbackIOWrapper

from ubiops import CoreApi
from ubiops.api_client import ApiClient
from ubiops.exceptions import (
    ApiConnectionError,
    ApiException,
    ApiRequestError,
    ApiTimeoutError,
    ApiValueError,
    ApiTypeError,
)
from ubiops.models import FileCompleteMultipartUpload


logger = logging.getLogger("FileOperations")

MULTIPART_CHUNK_SIZE = 1024 * 1024 * 1024 * 1  # 1 GB
MULTIPART_MIN_SIZE = 1024 * 1024 * 1024 * 4  # 4 GB


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


def upload_file(
    client,
    project_name,
    file_path,
    bucket_name="default",
    file_name=None,
    _progress_bar=True,
):
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
        raise ApiTypeError("Provided client is not of type ubiops.ApiClient")

    if not (isinstance(project_name, str) and project_name):
        raise ApiValueError("project_name must be a non-empty string")

    if not (isinstance(file_path, str) and path.isfile(file_path)):
        raise ApiValueError("file_path must be a valid file")

    if not (isinstance(bucket_name, str) and bucket_name):
        raise ApiValueError("bucket_name must be a non-empty string")

    if file_name is not None and not isinstance(file_name, str):
        raise ApiValueError("file_name must be a string")

    core_api = CoreApi(client)

    # Use the basename of the file_path if not a more specific name is provided for the file in the bucket.
    file_name = path.basename(file_path) if file_name is None else file_name
    file_size = stat(file_path).st_size

    general_headers = {"Content-Disposition": "multipart/form-data"}

    # Azure requires custom headers in the request
    azure_headers = {
        "Content-Disposition": "multipart/form-data",
        "x-ms-version": "2020-04-08",
        "x-ms-blob-type": "BlockBlob",
    }

    def _read_chunk(file_object, chunk_size=MULTIPART_CHUNK_SIZE):
        """
        Lazy function (generator) to read a file piece by piece
        """

        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data

    def _upload_chunk(url, upload_headers, data):
        """
        Upload a chunk of data via a PUT request to a signed url
        """

        try:
            put_response = requests.put(url=url, headers=upload_headers, data=data)

        except requests.exceptions.ConnectionError as e:
            raise ApiConnectionError(
                status=502,
                reason="Connection Error",
                body=f"Failed to connect to bucket\n{e}",
            )

        except requests.exceptions.Timeout:
            raise ApiTimeoutError(status=504, reason="Connection Timeout", body="Failed to upload file")

        except requests.exceptions.RequestException as e:
            raise ApiRequestError(status=502, reason="Upload Error", body=f"Failed to upload file\n{e}")

        if not 200 <= put_response.status_code <= 299:
            raise ApiRequestError(requests_resp=put_response)

        return put_response

    # Initiate context manager without progress bar
    cm = nullcontext()

    # Small file < 4 GB
    if file_size < MULTIPART_MIN_SIZE:
        if _progress_bar:
            cm = tqdm.tqdm(
                total=file_size,
                unit="B",
                unit_scale=True,
                unit_divisor=1024,
                miniters=1,
                desc=f"Uploading {file_name}",
            )

        response = core_api.files_upload(project_name=project_name, bucket_name=bucket_name, file=file_name)
        headers = azure_headers if response.provider == "azure_blob_storage" else general_headers

        with cm as bar:
            with open(file_path, "rb") as filestream:
                if bar:
                    file_wrapper = CallbackIOWrapper(bar.update, filestream, "read")
                    _upload_chunk(url=response.url, upload_headers=headers, data=file_wrapper)
                else:
                    _upload_chunk(url=response.url, upload_headers=headers, data=filestream)

    # Big file: use multipart file upload
    else:
        if _progress_bar:
            cm = tqdm.tqdm(
                total=math.ceil(file_size / MULTIPART_CHUNK_SIZE),
                desc=f"Uploading {file_name}",
            )

        start_response = core_api.files_start_multipart_upload(
            project_name=project_name, bucket_name=bucket_name, file=file_name
        )
        is_azure = start_response.provider == "azure_blob_storage"

        parts = []
        with cm as bar:
            with open(file_path, "rb") as filestream:
                part_number = 1
                for chunk in _read_chunk(file_object=filestream):
                    if is_azure:
                        block_id = base64.b64encode(f"{file_name}_{part_number}".encode()).decode()
                        signed_url = core_api.files_upload(
                            project_name=project_name, bucket_name=bucket_name, file=file_name, upload_id=block_id
                        )
                        _upload_chunk(url=signed_url.url, upload_headers=azure_headers, data=chunk)
                        parts.append({"BlockId": block_id})
                    else:
                        signed_url = core_api.files_upload(
                            project_name=project_name,
                            bucket_name=bucket_name,
                            file=file_name,
                            upload_id=start_response.upload_id,
                            part_number=str(part_number),
                        )
                        upload_response = _upload_chunk(url=signed_url.url, upload_headers=general_headers, data=chunk)
                        parts.append({"ETag": upload_response.headers["ETag"], "PartNumber": part_number})

                    part_number += 1

                    if bar:
                        bar.update()

        core_api.files_complete_multipart_upload(
            project_name=project_name,
            bucket_name=bucket_name,
            file=file_name,
            data=FileCompleteMultipartUpload(upload_id=start_response.upload_id, parts=parts),
        )

    return f"ubiops-file://{bucket_name}/{file_name}"


def upload_files(
    client,
    project_name,
    file_paths,
    bucket_name="default",
    file_prefix=None,
    parallel_uploads=5,
    _progress_bar=True,
):
    """
    Upload multiple files or directories to a bucket.
    If a directory path is provided, all files in the directory and its subdirectories will be uploaded preserving the
    directory structure.

    :param ubiops.ApiClient client: a preconfigured UbiOps client
    :param str project_name: the name of the project
    :param list[str] file_paths: list of file or directory paths to upload
    :param str bucket_name: the name of the bucket to upload the files to
    :param str|None file_prefix: optional prefix to add to all uploaded files in the bucket
    :param int parallel_uploads: the number of parallel uploads
    :param bool _progress_bar: whether to show a TQDM progress bar
    :return: list of uploaded file URIs
    """

    if not isinstance(client, ApiClient):
        raise ApiTypeError("Provided client is not of type ubiops.ApiClient")

    if not (isinstance(project_name, str) and project_name):
        raise ApiValueError("project_name must be a non-empty string")

    if not isinstance(file_paths, list):
        raise ApiValueError("file_paths must be a list of strings")

    if not (isinstance(bucket_name, str) and bucket_name):
        raise ApiValueError("bucket_name must be a non-empty string")

    if not isinstance(parallel_uploads, int) or parallel_uploads <= 0:
        raise ApiValueError("parallel_uploads must be a positive integer")

    if len(file_paths) == 0:
        return

    # Validate all paths are files
    invalid_files = [f for f in file_paths if not path.isfile(f) and not path.isdir(f)]
    if invalid_files:
        raise ValueError(f"The following paths are not valid files or directories: {invalid_files}")

    # Prepare upload tasks
    upload_tasks = []

    for item_to_upload in file_paths:
        if path.isfile(item_to_upload):
            bucket_file_name = path.basename(item_to_upload)
            if file_prefix:
                bucket_file_name = f"{file_prefix}{bucket_file_name}"

            upload_tasks.append((item_to_upload, bucket_file_name))

        if path.isdir(item_to_upload):
            for root, _, files in os.walk(item_to_upload):
                for file in files:
                    file_path = path.join(root, file)
                    bucket_file_name = path.relpath(file_path, item_to_upload)

                    # Add the file with its relative path as prefix
                    if file_prefix:
                        bucket_file_name = f"{file_prefix}{bucket_file_name}"

                    upload_tasks.append((file_path, bucket_file_name))

    def upload_single_file(file_tuple):
        """
        Upload a single file to the bucket
        It's a separate function to be used in ThreadPool

        :param tuple file_tuple: tuple of (file_path, bucket_file_name)
        """

        return upload_file(
            client=client,
            project_name=project_name,
            file_path=file_tuple[0],
            bucket_name=bucket_name,
            file_name=file_tuple[1],
            _progress_bar=_progress_bar,
        )

    # Use ThreadPool for parallel uploads
    with ThreadPool(parallel_uploads) as pool:
        results = pool.map(upload_single_file, upload_tasks)

    return results


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

    if not isinstance(client, ApiClient):
        raise ApiTypeError("Provided client is not of type ubiops.ApiClient")

    if not (isinstance(project_name, str) and project_name):
        raise ApiValueError("project_name must be a non-empty string")

    if not (bucket_name and file_name) and not file_uri:
        raise ApiValueError("Please, use either bucket_name and file_name or file_uri")

    if bucket_name and file_name and file_uri:
        raise ApiValueError("Please, use either bucket_name and file_name or file_uri, not both")

    if not isinstance(chunk_size, int) or chunk_size <= 0:
        raise ApiValueError("chunk_size must be a positive integer")

    core_api = CoreApi(client)

    if file_uri:
        ubiops_file = UbiOpsFile.from_uri(file_uri=file_uri)
    else:
        ubiops_file = UbiOpsFile(bucket=bucket_name, file=file_name)

    response = core_api.files_download(project_name=project_name, bucket_name=ubiops_file.bucket, file=ubiops_file.file)
    try:
        response = requests.get(url=response.url, stream=stream)

    except requests.exceptions.ConnectionError as e:
        raise ApiConnectionError(
            status=502,
            reason="Connection Error",
            body=f"Failed to connect to bucket\n{e}",
        )

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


def download_files(
    client,
    project_name,
    bucket_name="default",
    prefix=None,
    output_path=".",
    stream=True,
    chunk_size=8192,
    parallel_downloads=5,
    _progress_bar=True,
):
    """
    Download all files from a bucket or files with a given prefix into given directory.

    :param ubiops.ApiClient client: a preconfigured Ubiops client
    :param str project_name: the name of the project
    :param str bucket_name: the name of the bucket
    :param str|None prefix: the prefix to filter files in the bucket
    :param str output_path: the directory location to download the files to
    :param bool stream: whether to download the files streaming or not
    :param int chunk_size: if streaming enabled, the size for each chunk
    :param int parallel_downloads: the number of parallel downloads
    :param bool _progress_bar: whether to show a TQDM progress bar
    """

    if not isinstance(client, ApiClient):
        raise ApiTypeError("Provided client is not of type ubiops.ApiClient")

    if not (isinstance(project_name, str) and project_name):
        raise ApiValueError("project_name must be a non-empty string")

    if not (isinstance(bucket_name, str) and bucket_name):
        raise ApiValueError("bucket_name must be a non-empty string")

    if not path.isdir(output_path):
        raise ApiValueError("Output path must be a directory")

    if not isinstance(chunk_size, int) or chunk_size <= 0:
        raise ApiValueError("chunk_size must be a positive integer")

    if not isinstance(parallel_downloads, int) or parallel_downloads <= 0:
        raise ApiValueError("parallel_downloads must be a positive integer")

    core_api = CoreApi(client)

    continuation_token = None
    files = []

    while True:
        file_list = core_api.files_list(
            project_name=project_name,
            bucket_name=bucket_name,
            prefix=prefix,
            continuation_token=continuation_token,
        )
        files.extend(file_list.files)

        continuation_token = file_list.continuation_token
        if not continuation_token:
            break

    def download_file_wrapper(file_item):
        """
        Download a single file
        It's a separate function to be used in ThreadPool

        :param ubiops.models.FileItem file_item: the file item to download
        """
        file_dir = path.dirname(file_item.file)
        makedirs(path.join(output_path, file_dir), exist_ok=True)

        file_output_path = path.join(output_path, file_item.file)

        download_file(
            client=client,
            project_name=project_name,
            bucket_name=bucket_name,
            file_name=file_item.file,
            output_path=file_output_path,
            stream=stream,
            chunk_size=chunk_size,
            _progress_bar=_progress_bar,
        )

    with ThreadPool(parallel_downloads) as pool:
        pool.map(download_file_wrapper, files)


def handle_file_input(
    client,
    project_name,
    file,
    bucket_name="default",
    file_prefix=None,
    file_name=None,
    _progress_bar=True,
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

    if not isinstance(client, ApiClient):
        raise ApiTypeError("Provided client is not of type ubiops.ApiClient")

    if not (isinstance(project_name, str) and project_name):
        raise ApiValueError("project_name must be a non-empty string")

    if not isinstance(file, str):
        raise ApiValueError(f"File {file} is not a string")

    if not (isinstance(bucket_name, str) and bucket_name):
        raise ApiValueError("bucket_name must be a non-empty string")

    if file_prefix is not None and not isinstance(file_prefix, str):
        raise ApiValueError("file_prefix must be a string")

    if file_name is not None and not isinstance(file_name, str):
        raise ApiValueError("file_name must be a string")

    try:
        ubiops_file = UbiOpsFile.from_uri(file)
    except ValueError:
        ubiops_file = None

    if ubiops_file:
        core_api = CoreApi(client)

        try:
            core_api.files_get(
                project_name=project_name,
                bucket_name=ubiops_file.bucket,
                file=ubiops_file.file,
            )

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
        status=400,
        reason="Invalid",
        body=f"File {file} is not a ubiops-file:// or local directory or local file",
    )

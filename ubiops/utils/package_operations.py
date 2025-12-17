import datetime
import os
import zipfile

from .gitignorefile.gitignorefile import parse as parse_ignore


def abs_path(path_param):
    """
    Get the absolute path if the path is a relative path

    :param str path_param: either a relative or absolute path
    """

    if not os.path.isabs(path_param):
        path_param = os.path.join(os.getcwd(), path_param)
    return path_param


def default_zip_name(prefix):
    """
    Obtain the default name for a package zip file based on given prefix and the current datetime

    :param str|None prefix: prefix used for the zip
    """

    datetime_str = str(datetime.datetime.now()).replace(" ", "_").replace(".", "_").replace(":", "-")
    if prefix:
        return f"{prefix}_{datetime_str}.zip"
    return f"{datetime_str}.zip"


def zip_dir(  # noqa: PLR0913, PLR0917
    directory,
    output_path,
    ignore_filename=".ubiops-ignore",
    prefix=None,
    force=False,
    package_directory="deployment_package",
):
    """
    Zip a directory while omitting files specified in the ubiops ignore file. The absolute path of the created zip file
    will be returned.

    :param str directory: the directory that should be zipped
    :param str output_path: the output location of the zip, either a file or directory
    :param str ignore_filename: the name of the ignore file
    :param str|None prefix: the prefix of the default filename, only used when output_path is a directory
    :param bool force: whether to overwrite when the file already exists
    :param str package_directory: the root directory of the zip
    """

    if not directory:
        raise NotADirectoryError("Directory is required.")

    path_dir = abs_path(directory)
    if not os.path.isdir(path_dir):
        raise NotADirectoryError(f"Given path {path_dir} is not a directory.")

    has_ignore_file = os.path.isfile(os.path.join(path_dir, ignore_filename)) if ignore_filename else False

    output_path = abs_path(output_path)
    if os.path.isdir(output_path):
        output_path = os.path.join(output_path, default_zip_name(prefix=prefix))

    # Normalize the output path to remove intermediate directories like '.' - this is necessary to prevent zip-inception
    output_path = os.path.normpath(output_path)
    path_dir = os.path.normpath(path_dir)

    if not force and os.path.isfile(output_path):
        raise FileExistsError(f"File {output_path} already exists")

    # Initialize 'is_ignored' function. It will be overwritten if a .ubiops-ignore file is present.
    def is_ignored(_):  # noqa: F811
        """
        If no ignore file is present, nothing will be ignored
        """
        return False

    if has_ignore_file:
        # Ignore what we found in the .ubiops-ignore file
        is_ignored = parse_ignore(os.path.join(path_dir, ignore_filename), path_dir)  # noqa: F811

    package_path = str(os.path.join(path_dir, ""))
    with zipfile.ZipFile(output_path, "w") as f:
        for root, _, files in os.walk(path_dir):
            root_subdir = os.path.join("", *root.split(package_path)[1:])
            package_subdir = os.path.join(package_directory, root_subdir)
            for filename in files:
                source_file = os.path.join(root, filename)
                if source_file != output_path and not is_ignored(source_file):
                    f.write(source_file, os.path.join(package_subdir, filename))

    return output_path


def files_present_in_dir(files, directory, ignore_filename=".ubiops-ignore"):
    """
    Check whether at least one of the provided files is present in the directory, excluding files that are in the ignore
    file.

    :param list[str] files: list of filenames to check for
    :param str directory: the directory to check in
    :param str ignore_filename: the name of the ignore file in the directory
    """

    if not directory:
        raise NotADirectoryError("Directory is required.")

    path_dir = os.path.abspath(directory)

    if not os.path.isdir(path_dir):
        raise NotADirectoryError(f"Given path {path_dir} is not a directory.")

    has_ignore_file = os.path.isfile(os.path.join(path_dir, ignore_filename)) if ignore_filename else False

    # Initialize 'is_ignored' function. It will be overwritten if a .ubiops-ignore file is present.
    def is_ignored(_):  # noqa: F811
        """
        If no ignore file is present, nothing will be ignored
        """
        return False

    if has_ignore_file:
        # Ignore what we found in the .ubiops-ignore file
        is_ignored = parse_ignore(os.path.join(path_dir, ignore_filename), path_dir)  # noqa: F811

    # Whether at least one of the files is present in the directory and not ignored
    files_present = False

    package_path = str(os.path.join(path_dir, ""))
    for root, _, filenames in os.walk(path_dir):
        root_subdir = os.path.join("", *root.split(package_path)[1:])
        for filename in filenames:
            source_file = os.path.join(root, filename)
            if not is_ignored(source_file):
                if len(root_subdir.split()) == 0 and filename in files:
                    files_present = True

    return files_present

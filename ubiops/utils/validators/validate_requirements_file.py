import logging
import re

import requests

from ..exceptions import ValidateError, ValidateSkip, ValidateWarning


def validate_requirement_line(index, line):
    """
    Validates a single line of the requirements.txt file with data from PyPi.
    Raises exceptions to be handled by the caller if the line isn't perfectly valid.

    :param int index: the index of the line in the requirements.txt file
    :param str line: the line to validate
    """

    line = get_formatted_line(line, index)

    # Find name and dependencies
    search_name = re.compile(r"(([a-zA-Z0-9_.\-]+)(\[([a-zA-Z,]+)])?)").search(line)
    package_name = search_name.group(2)
    # dependencies = search_name.group(4)

    if not package_name:
        raise ValidateError("No package name specified")

    # Check if package starts with a number or letter
    if not package_name[0].isalnum() or not package_name[-1].isalnum():
        raise ValidateError("Invalid package name: %s" % line)

    # Check if package exists on pypi and return json if so - package-json used later on
    package_json = get_package_json_from_pypi(package_name)

    # Stop checking if only a package name (with dependencies) is specified
    if search_name.group(1) == line:
        return

    regex_version_and_specifier = re.compile(r"\s*([<>=!~]+)\s*([0-9_.\-*]+)")
    version_details = regex_version_and_specifier.findall(line)
    if not version_details:
        raise ValidateError("No version details found: %s" % line)

    # Check all specifiers for validity
    validate_version_details(version_details, index)

    # Check if version can be found on PyPi for the specifications given
    possible_package_versions = get_possible_versions_from_pypi(version_details, package_json, index)

    if not possible_package_versions:
        raise ValidateError("No valid version found for %s" % package_name)

    # Check correct structure
    regex_total = re.compile(r"[a-zA-Z0-9_.\-]+(\[(.*)])?(\s*([<>=!~]+)\s*([0-9a-zA-Z+_.\-*]+),?)+")
    total_find = regex_total.match(line)
    if not total_find or total_find.group(0) != line:
        raise ValidateError(
            "Invalid line '%s'. Expected: '[Package name] [[specifiers] [version], ...]'" % line
        )


def get_formatted_line(line, index):
    """
    Returns formatted line without comments and conditional statements or raises exception

    :param str line: line to be formatted
    :param int index: index of the line in the requirements.txt file
    """

    # Remove comments
    line = line.split("#")[0].strip()
    # Ignore blank lines and comments
    if not line:
        raise ValidateSkip("Empty line found in requirements.txt")
    # Check if the line is a valid package specification
    if line.startswith("-") or line.startswith("http://") or line.startswith("https://") or line.startswith("git+"):
        if line.startswith("git+"):
            logging.warning("Line %s: Git must be installed on the deployment environment" % (index + 1))

        raise ValidateWarning("Line will not be checked")

    if ";" in line:
        logging.warning("Line %s: Conditional statement encountered, the condition will not be checked." % (index + 1))
        line = line.split(";")[0].strip()

    return line


def get_package_json_from_pypi(package_name):
    """
    Returns the json of the package from pypi or raises exception

    :param str package_name: name of the package
    """

    url = "https://pypi.org/pypi/%s/json" % package_name
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        raise ValidateError("Package %s not found on pypi.org" % package_name)


def validate_version_details(version_details, line_index):
    """
    Checks if version details are valid and logs warnings/errors - raises exception if invalid

    :param list version_details: list of tuples containing the specifier and version
    :param int line_index: index of the line in the requirements.txt file
    """

    raise_error = False
    for specifier, version in version_details:
        # Check if specifiers are valid
        if specifier not in ["==", ">=", "<=", ">", "<", "~=", "!="]:
            if specifier == "===":
                logging.warning("Line %s, Are you sure you want to use '===' ?" % (line_index + 1))
            else:
                logging.error("Line %s, Invalid specifiers: %s" % (line_index + 1, specifier))
                raise_error = True

        # Check if version is valid
        if not (version[-1] == "*" or version[-1].isdigit() or version[-1].isalpha()):
            logging.error("Line %s, Invalid version: %s" % (line_index + 1, version))
            raise_error = True

    if raise_error:
        raise ValidateError("Found invalid version details")


def get_possible_versions_from_pypi(version_details, package_json, line_index):
    """
    Returns a list of possible versions for the requirements package specifications and the versions available
        on pypi

    :param list version_details: list of tuples containing the specifier and version
    :param dict package_json: json of the package from pypi
    :param int line_index: index of the line in the requirements.txt file
    """

    package_versions = list(package_json["releases"].keys())

    # Create a list of possible versions
    for specifier, version in version_details:
        # Check if version is in list and remove the versions that are not valid
        if specifier == "==":
            if version[-1] == "*":
                package_versions = [v for v in package_versions if v.startswith(version[:-2])]
            elif version in package_versions:
                package_versions = [version]
            else:
                package_versions = []

        elif specifier == "!=":
            if version[-1] == "*":
                package_versions = [v for v in package_versions if not v.startswith(version[:-2])]
            else:
                package_versions = [v for v in package_versions if v != version]

        elif specifier == "~=":
            version_details.extend([(">=", version), ("==", ".".join(version.split(".")[:-1] + ["*"]))])

        else:
            if version[-1] == "*":
                logging.warning(
                    "Line %s: Bigger/smaller (or equal) than a version with an asterisk"
                    " is not recommended, validate the version manually or change the version details"
                    % (line_index + 1)
                )
                version = version[:-2]

            if specifier == ">=":
                for version_check in package_versions:
                    # Split version at first occurrence of a letter keeping the letter
                    version_check_split = re.split(r"([^\d.])", version_check, 1)

                    # Remove trailing . if present
                    if version_check_split[0][-1] == ".":
                        version_check_split[0] = version_check_split[0][:-1]

                    if version_tuple(version_check_split[0]) < version_tuple(version):
                        package_versions.remove(version_check)

            elif specifier == "<=":
                for version_check in package_versions:
                    # Split version at first occurrence of a letter keeping the letter
                    version_check_split = re.split(r"([^\d.])", version_check, 1)
                    if version_tuple(version_check_split[0]) > version_tuple(version):
                        package_versions.remove(version_check)
            elif specifier == ">":
                for version_check in package_versions:
                    # Split version at first occurrence of a letter keeping the letter
                    version_check_split = re.split(r"([^\d.])", version_check, 1)
                    if version_tuple(version_check_split[0]) <= version_tuple(version):
                        package_versions.remove(version_check)

            elif specifier == "<":
                for version_check in package_versions:
                    # Split version at first occurrence of a letter keeping the letter
                    version_check_split = re.split(r"([^\d.])", version_check, 1)
                    if version_tuple(version_check_split[0]) >= version_tuple(version):
                        package_versions.remove(version_check)

    return package_versions


def version_tuple(v):
    return tuple(map(int, (v.split("."))))

# PackageOperations

Helper functions for package operations.

| Method                                                                  | Description                                                                                                    |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**abs_path**](./PackageOperations.md#abs_path)                         | Get the absolute path of a given file or directory                                                             |
| [**default_zip_name**](./PackageOperations.md#default_zip_name)         | Obtain the default name for a package zip file                                                                 |
| [**list_files**](./PackageOperations.md#list_files)                     | List files in a directory while skipping files specified in the ignore file                                    |
| [**files_present_in_dir**](./PackageOperations.md#files_present_in_dir) | Checking if any of given files is present in given directory while skipping files specified in the ignore file |
| [**zip_dir**](./PackageOperations.md#zip_dir)                           | Zip a directory while omitting files specified in the ignore file                                              |

# **abs_path**
> abs_path(path_param)

Get the absolute path of a given file or directory

## Description
Helper function to get the absolute path of a given file or directory

### Example

```python
import ubiops

ubiops.utils.abs_path(path_param=".")
```

### Parameters

| Name           | Type    | Notes   |
|----------------|---------|---------|
| **path_param** | **str** |         |


[[Back to top]](#)


# **default_zip_name**
> default_zip_name(prefix)

Obtain the default name for a package zip file based on given prefix and the current datetime

## Description
Helper function to obtain the default name for a package zip file based on given prefix and the current datetime

### Example

```python
import ubiops

ubiops.utils.default_zip_name(prefix="")
```

### Parameters

| Name       | Type    | Notes  |
|------------|---------|--------|
| **prefix** | **str** |        |


[[Back to top]](#)


# **list_files**
> list_files(directory, ignore_filename=".ubiops-ignore")

List files in given directory, excluding files that are in the ignore file

## Description
Helper function to list files in given directory, excluding files that are in the ignore file

### Example

```python
import ubiops

ubiops.utils.list_files(directory=".", ignore_filename=".ubiops-ignore")
```

### Parameters

| Name                | Type    | Notes                                    |
|---------------------|---------|------------------------------------------|
| **directory**       | **str** |                                          |
| **ignore_filename** | **str** | [optional] [default to ".ubiops-ignore"] |


[[Back to top]](#)


# **files_present_in_dir**
> files_present_in_dir(files, directory, ignore_filename=".ubiops-ignore")

Check whether at least one of the provided files is present in the directory

## Description
Helper function to check whether at least one of the provided files is present in the directory, excluding files that
are in the ignore file.

### Example

```python
import ubiops

ubiops.utils.files_present_in_dir(
    files=["file.txt"],
    directory=".",
    ignore_filename=".ubiops-ignore",
)
```

### Parameters

| Name                | Type          | Notes                                    |
|---------------------|---------------|------------------------------------------|
| **files**           | **list[str]** |                                          |
| **directory**       | **str**       |                                          |
| **ignore_filename** | **str**       | [optional] [default to ".ubiops-ignore"] |


[[Back to top]](#)

# **zip_dir**
> zip_dir(
    directory,
    output_path,
    ignore_filename=".ubiops-ignore",
    prefix=None,
    force=False,
    package_directory="deployment_package",
 )

Zip a directory while omitting files specified in the ignore file

## Description
Helper function to zip a directory while omitting files specified in the ubiops ignore file. The absolute path of the
created zip file will be returned.

### Example

```python
import ubiops

ubiops.utils.zip_dir(
    directory=".",
    output_path="/tmp",
    ignore_filename=".ubiops-ignore",
    prefix=None,
    force=False,
    package_directory="deployment_package",
)
```

### Parameters

| Name                  | Type     | Notes                                        |
|-----------------------|----------|----------------------------------------------|
| **directory**         | **str**  |                                              |
| **output_path**       | **str**  | [optional]                                   |
| **ignore_filename**   | **str**  | [optional] [default to ".ubiops-ignore"]     |
| **prefix**            | **str**  | [optional]                                   |
| **force**             | **bool** | [optional] [default to False]                |
| **package_directory** | **str**  | [optional] [default to "deployment_package"] |


[[Back to top]](#)

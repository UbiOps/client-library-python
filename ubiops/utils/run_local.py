import importlib.util
import inspect
import os
import sys
import traceback

dummy_init_context = {
    'project': 'run-local',
    'project_id': '123',
    'deployment_id': '456',
    'deployment': 'My Deployment',
    'version_id': '789',
    'version': 'v1',
    'input_type': 'structured',
    'output_type': 'structured',
    'input_fields': ['input_field_1', 'input_field_2', 'input_field_3'],
    'output_fields': ['output_field_1', 'output_field_2', 'output_field_3'],
    'language': 'python',
    'environment_variables': {
        'ENV_VAR': 'abc123'
    }
}

dummy_request_context = {
    'id': "a64c1dfb-d9bb-4e23-b66f-3795e67bb6cf",
    'request_mode': 'express',
    'user_id': "d9e30331-3edc-4a88-b8c3-027412e8baeb"
}


def _append_libraries_to_sys_path(deployment_directory):
    """
    Appends the libraries directory to the system path

    :param str deployment_directory: absolute path to deployment_directory
    """
    sys.path.append(deployment_directory)
    sys.path.append(os.path.join(deployment_directory, 'libraries'))


def _create_module_from_spec(deployment_directory):
    """
    Creates a module with spec from the deployment package

    :param str deployment_directory: absolute path to deployment_directory
    """
    spec = importlib.util.spec_from_file_location("Deployment", os.path.join(deployment_directory, "deployment.py"))
    module_from_spec = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = module_from_spec

    try:
        spec.loader.exec_module(module_from_spec)
    except FileNotFoundError:
        raise FileNotFoundError(
            "Deployment package not found."
            "Expected to find a file called 'deployment.py' in the deployment directory."
        )
    except Exception as e:
        raise Exception("Failed to load deployment package: %s" % e)
    return module_from_spec


def _create_deployment_instance(module_from_spec, deployment_directory, context):
    """
    Creates an instance of the deployment class

    :param module module_from_spec: module from spec
    :param str deployment_directory: absolute path to deployment_directory
    :param dict context: context to be passed to the deployment init function
    """
    try:
        mod = module_from_spec.Deployment

        # Inspect params of the deployment
        init_params = inspect.signature(mod).parameters

        # Search for potential **kwargs parameter
        has_kwargs = any(param.kind is inspect.Parameter.VAR_KEYWORD for param in init_params.values())

        # Support importing the deployment with and without the base_directory and context parameters
        if has_kwargs or ('base_directory' in init_params and 'context' in init_params):
            deployment_instance = mod(base_directory=deployment_directory, context=context)
        elif 'base_directory' in init_params:
            deployment_instance = mod(base_directory=deployment_directory)
        elif 'context' in init_params:
            deployment_instance = mod(context=context)
        else:
            deployment_instance = mod()

    except AttributeError as e:
        raise AttributeError("Deployment package does not contain a class called 'Deployment': %s" % e)
    except Exception as e:
        raise Exception("Failed to initialize deployment: %s" % e)

    return deployment_instance


def _create_request(deployment_instance, request_function, data, context):
    """
    Calls the request(s) function of the deployment

    :param instance deployment_instance: the initialized deployment instance
    :param str request_function: the request function to use; 'request' or 'requests'
    :param str|dict|list data: the data passed to the request(s) function
    :param dict context: context to be passed to the deployment request(s) function
    """

    if not callable(getattr(deployment_instance, request_function, None)):
        raise Exception("Function '%s' is not callable" % request_function)

    request_function = getattr(deployment_instance, request_function)

    try:
        # Inspect params of the request function
        request_params = inspect.signature(request_function).parameters

        if 'context' in request_params and len(request_params) == 2:
            return request_function(data, context)
        return request_function(data)

    except Exception as e:
        # Print the exception stacktrace for debugging
        print(traceback.format_exc())

        # Raise custom user error message if present
        if getattr(e, 'public_error_message', False):
            raise Exception(str(getattr(e, 'public_error_message')))

        raise Exception("An exception occurred in the request. See the logs for details.")


def run_local(deployment_directory, data, init_context=None, request_context=None):
    """
    Run a deployment locally and call its request(s) function

    :param str deployment_directory: the name of the deployment directory, absolute or relative to the current working
        directory, e.g. 'deployment_package'
    :param dict data: the data to be passed to the deployment request(s) function
    :param dict init_context: the context to be passed to the deployment init function
    :param dict request_context: the context to be passed to the deployment request(s) function

    The following dummy contexts are automatically added unless specified otherwise:

    init_context = {
        'project': 'run-local',
        'project_id': '123',
        'deployment_id': '456',
        'deployment': 'My Deployment',
        'version_id': '789',
        'version': 'v1',
        'input_type': 'structured',
        'output_type': 'structured',
        'input_fields': ['input_field_1', 'input_field_2', 'input_field_3'],
        'output_fields': ['output_field_1', 'output_field_2', 'output_field_3'],
        'language': 'python',
        'environment_variables': {
            'ENV_VAR': 'abc123'
        }
    }

    request_context = {
        'id': "a64c1dfb-d9bb-4e23-b66f-3795e67bb6cf",
        'request_mode': 'express',
        'user_id': "d9e30331-3edc-4a88-b8c3-027412e8baeb"
    }

    See https://ubiops.com/docs/deployments/deployment-package/deployment-structure/ for more context information.
    """

    if init_context is None:
        init_context = dummy_init_context

    if request_context is None:
        request_context = dummy_request_context

    # Check if deployment_directory is absolute
    if not os.path.isabs(deployment_directory):
        deployment_directory = os.path.join(os.getcwd(), deployment_directory)

    # Check if the deployment directory exists
    if not os.path.isdir(deployment_directory):
        raise FileNotFoundError("Deployment directory not found")

    _append_libraries_to_sys_path(deployment_directory=deployment_directory)

    # Create module from spec and initialize it
    module_from_spec = _create_module_from_spec(deployment_directory=deployment_directory)
    deployment_instance = _create_deployment_instance(
        module_from_spec=module_from_spec, deployment_directory=deployment_directory, context=init_context
    )

    # Return the result
    if hasattr(deployment_instance, "request") and not isinstance(data, list):
        # 'request' function and data is a single item
        return _create_request(
            deployment_instance=deployment_instance, request_function='request', data=data, context=request_context
        )
    elif hasattr(deployment_instance, "requests") and isinstance(data, list):
        # 'requests' function and data is a list
        return _create_request(
            deployment_instance=deployment_instance, request_function='requests', data=data, context=request_context
        )
    elif hasattr(deployment_instance, "requests") and not isinstance(data, list):
        # 'requests' function and data is NOT a list -> make it a list
        return _create_request(
            deployment_instance=deployment_instance, request_function='requests', data=[data], context=request_context
        )
    elif hasattr(deployment_instance, "request") and isinstance(data, list):
        # 'request' function and data is a list -> loop over the items in the list
        result = []
        for data_item in data:
            result.append(
                _create_request(
                    deployment_instance=deployment_instance,
                    request_function='request',
                    data=data_item,
                    context=request_context
                )
            )
        return result
    else:
        raise AttributeError("Deployment has no 'request' function")

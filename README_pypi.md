# ubiops
Client Library to interact with the [UbiOps](https://ubiops.com) API (v2.1).

For more information, please visit [https://ubiops.com/docs/](https://ubiops.com/docs/)


## Requirements

Python 3.7+. Python 3.13+ is recommended.


## Installation

```sh
pip install ubiops
```


## Troubleshooting

Python 3.10/11/12 raise a `SSLError (EOF occurred in violation of protocol)` instead of
`Request Entity Too Large (413)` for too large file uploads, see https://github.com/urllib3/urllib3/issues/2733.


## Usage
To use the library, one has to authenticate to the UbiOps API with an API token.
Please, visit https://ubiops.com/docs/organizations/service-users for more information.

```python
import ubiops

configuration = ubiops.Configuration()
configuration.api_key['Authorization'] = 'Token <YOUR_API_KEY>'

client = ubiops.ApiClient(configuration)

api = ubiops.api.CoreApi(client)
print(api.service_status())
```

## Documentation
The library is fully documented at https://github.com/UbiOps/client-library-python/tree/master/docs.


## Examples
Jupyter notebook examples can be found at https://github.com/UbiOps/client-library-python/tree/master/examples.

## License
Ubiops is available under the Apache 2.0 license.

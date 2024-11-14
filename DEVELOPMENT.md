# Development Guide

## Using Docker

Setup dependencies:
```shell
docker build . -f Dockerfile.dev -t emnify/python-sdk
```

Run a command:
```shell
# docker run -t -v $(pwd):/sdk emnify/python-sdk [command] [...args]
# [command] - command to run, e.g. pytest
# [...args] - command arguments

# Run unit tests
docker run -t -v $(pwd):/sdk emnify/python-sdk pytest --cov=emnify --cov-fail-under=90
```
For end-to-end testing, make use of the other Dockerfile provided (it uses our package from [PyPI](https://pypi.org/project/emnify-sdk/)):
```shell
docker build . -f Dockerfile.e2e -t emnify/python-sdk-e2e
```

### Local debug example
To perform local debugging, we provide an example file located at `docs/examples/local_debug.py`.
To set up your sandbox, modify the code in this file as needed.
> ⚠️ **Please be careful about placing any sensitive information in the file!**

Once your sandbox is set up, you can launch the file and view the results.
```shell
docker run -t -e EMNIFY_SDK_APPLICATION_TOKEN=<your_token_here> -e EMNIFY_SDK_API_ENDPOINT_URL=<your_debug_API_endpoint> -v $(pwd):/sdk emnify/python-sdk python docs/examples/local_debug.py
```
End-to-end:
```shell
docker run -t -e EMNIFY_SDK_APPLICATION_TOKEN=<your_token_here> -e EMNIFY_SDK_API_ENDPOINT_URL=<your_debug_API_endpoint> -v $(pwd):/sdk emnify/python-sdk-e2e python docs/examples/local_debug.py
```

## Version Bump

```shell
bump2version minor
```

## Branching and PR

PR names must follow [angular convention](https://github.com/angular/angular/blob/main/CONTRIBUTING.md).

Squash changes while merging to `development` and do regular merge to `main`.

## Linting

We use `ruff` for lint and format checks. To run the lint check, execute the following command:
```shell
pipenv run ruff check
```
To fix the issues, run:
```shell
pipenv run ruff check --fix
```
To run formatting checks only, execute:
```shell
pipenv run ruff format --check
```
To fix the formatting issues, run:
```shell
pipenv run ruff format
```
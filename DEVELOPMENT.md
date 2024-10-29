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
docker run -t -v $(pwd):/sdk emnify/python-sdk pipenv run pytest -cov=emnify -cov-fail-under=90
```

### Local debug example
To perform local debugging, we provide an example file located at `docs/examples/local_debug.py`.
To set up your sandbox, modify the code in this file as needed.
> ⚠️ **Please be careful about placing any sensitive information in the file!**

Once your sandbox is set up, you can launch the file and view the results.
```shell
docker run -t -e EMNIFY_SDK_APPLICATION_TOKEN=<your_token_here> -e EMNIFY_SDK_API_ENDPOINT_URL=<your_debug_API_endpoint> -v $(pwd):/sdk emnify/python-sdk pipenv run python docs/examples/local_debug.py
```

## Version Bump

```shell
bump2version minor
```

## Branching and PR

PR names must follow [angular convention](https://github.com/angular/angular/blob/main/CONTRIBUTING.md).

Squash changes while merging to `development` and do regular merge to `main`.

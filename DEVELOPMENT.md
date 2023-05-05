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

### Local debug example
In order to perform debug locally, there is an example file provided that can serve for your sandbox experience.

```shell
docker run -t -e EMNIFY_APPLICATION_TOKEN=<your_token_here> -v $(pwd):/sdk emnify/python-sdk python docs/examples/local_debug.py
```
## Version Bump

```shell
bump2version minor
```

## Branching and PR

PR names must follow [angular convention](https://github.com/angular/angular/blob/main/CONTRIBUTING.md).

Squash changes while merging to `development` and do regular merge to `main`.

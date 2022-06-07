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

docker run -t -v $(pwd):/sdk emnify/python-sdk pytest --cov=emnify --cov-fail-under=90
```

## Version Bump

```shell
bump2version minor
```

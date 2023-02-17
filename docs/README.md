# Documentation guide

## Prerequisites

- [Docker](https://www.docker.com/)

## Running the documentation locally

If you haven't already, clone and move into this repository:

```shell
git clone https://github.com/emnify/emnify-sdk-python.git
cd emnify-sdk-python
```

From the root, build the Docker container:

```shell
docker build . -f docs/Dockerfile.dev -t emnify/python-sdk-docs
```

2. Run docgen

```shell
# macOS and Linux
docker run -t -v $(pwd):/docs emnify/python-sdk-docs
```

```shell
# Windows
docker run -t -v %cd%:/docs emnify/python-sdk-docs
```

This command sets up (or updates) the `build_sphinx` project to run from inside the `docs/` directory. 

Once complete, you can preview the documentation as HTML pages in `docs/build_sphinx`.

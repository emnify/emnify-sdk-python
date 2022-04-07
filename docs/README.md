Build a container

`docker build . -f docs/Dockerfile.dev -t emnify/python-sdk-docs`

Run docgen

`docker run -it -v $(pwd):/docs emnify/python-sdk-docs`

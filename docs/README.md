Build a container

`docker build . -f docs/Dockerfile.dev -t emnify/python-sdk-docs`

Run docgen

`docker run -it -v $(pwd):/docs emnify/python-sdk-docs`

Run docgen (for windows)
`docker run -it -v %cd%:/docs emnify/python-sdk-docs`
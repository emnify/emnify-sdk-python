Build a container

`docker build . -f docs/Dockerfile.dev -t emnify/python-sdk-docs`

Run docgen (mac/linux)

`docker run -t -v $(pwd):/docs emnify/python-sdk-docs`

Run docgen (for windows)
`docker run -t -v %cd%:/docs emnify/python-sdk-docs`

### Generate Documentation Locally

1) Build a container

`docker build . -f docs/Dockerfile.dev -t emnify/python-sdk-docs`

2) Run docgen
   1) mac/linux `docker run -t -v $(pwd):/docs emnify/python-sdk-docs`
   2) for windows `docker run -t -v %cd%:/docs emnify/python-sdk-docs`

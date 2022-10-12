#!/usr/bin/env/bash
# Display c4 project dsl following
# https://github.com/pmorch/c4viz

FILE_NAME=project.dsl
echo "We are working on ${FILE_NAME}"
echo "Server is listening on http://localhost:9000"
    # -u $(id -u):$(id -g) \
docker run \
    --rm -it \
    -v $PWD/c4:/c4\
    -p 9000:9000 \
    -e SERVER_PORT=9000 \
    -e C4VIZ_SOURCE=${FILE_NAME}\
    -e C4VIZ_SOURCE_DIR=/c4 \
    -u 1000:1000 \
    pmorch/c4viz:latest

#!/usr/bin/env bash
# Convert the dsl/workspace definition to plantuml files
# Following documentation in 
# https://github.com/structurizr/cli/blob/master/docs/export.md

DSL_FILE_NAME=project.dsl
docker pull structurizr/cli:latest
docker run -it --rm -v $PWD:/usr/local/structurizr structurizr/cli \
       export -workspace ${DSL_FILE_NAME} \
      -format plantuml/c4plantuml  -output diagrams


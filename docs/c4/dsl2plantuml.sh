#!/usr/bin/env bash
# Convert the dsl/workspace definition to plantuml files
# Following documentation in 
# https://github.com/structurizr/cli/blob/master/docs/export.md

# and copy them to $DESTINATION
 
set -eux
DSL_FILE_NAME=project.dsl
DESTINATION=../diagrams/src

docker pull structurizr/cli:latest
docker run -it --rm -v $PWD:/usr/local/structurizr structurizr/cli \
       export -workspace ${DSL_FILE_NAME} \
      -format plantuml/c4plantuml  -output diagrams

echo "copy the generated Diagramms to ${DESTINATION}"
cp diagrams/* ${DESTINATION} 
#/bin/rm -f diagrams/*

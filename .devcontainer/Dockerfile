#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------

# Update the VARIANT arg in devcontainer.json to pick a Python version: 3, 3.8, 3.7, 3.6 
# To fully customize the contents of this image, use the following Dockerfile instead:
# https://github.com/microsoft/vscode-dev-containers/tree/v0.128.0/containers/python-3/.devcontainer/base.Dockerfile
ARG VARIANT="3"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
#
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional packages.
#
RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends nodejs npm

# update nodejs   to the lastest stable version 
# https://askubuntu.com/questions/426750/how-can-i-update-my-nodejs-to-the-latest-version
RUN npm cache clean -f && npm install -g n && n stable
# Install the CDK
RUN npm install -g aws-cdk

# Install the AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install


# Install poetry
# https://gist.github.com/jthorniley/fba81c62a9d45c723777c7205ff96481
USER vscode
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH "/home/vscode/.poetry/bin:$PATH"
# doc
RUN /home/vscode/.local/bin/poetry config virtualenvs.in-project true


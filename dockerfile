# USING PYTHON 3.6
FROM ubuntu:18.04
ENV DEBIAN_FRONTEND=noninteractive 

# INSTALL DEPENDECIES
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3.6 python3-pip python3.6-dev tzdata build-essential python3-setuptools python3-wheel python3-cffi

RUN adduser --disabled-password --gecos "" docker_deploy_user

USER docker_deploy_user

RUN mkdir -p /home/docker_deploy_user
RUN mkdir -p /home/docker_deploy_user/applogs
RUN mkdir -p /home/docker_deploy_user/pids
RUN chown docker_deploy_user:docker_deploy_user /home/docker_deploy_user/applogs
RUN chown docker_deploy_user:docker_deploy_user /home/docker_deploy_user/pids

WORKDIR /home/docker_deploy_user

# Install Python Requirements
COPY --chown=docker_deploy_user:docker_deploy_user ./requirements.txt /home/docker_deploy_user/app/requirements.txt
WORKDIR /home/docker_deploy_user/app/requirements
RUN python3.6 -m pip install --user -r production.txt
ENV PATH=$PATH:/home/docker_deploy_user/.local/bin

# COPY SOURCE
COPY --chown=docker_deploy_user:docker_deploy_user . /home/docker_deploy_user/app
WORKDIR /home/docker_deploy_user/app

USER root
RUN chown docker_deploy_user:docker_deploy_user /home/docker_deploy_user/app/container-run.sh

USER docker_deploy_user
RUN chmod u+x /home/docker_deploy_user/app/container-run.sh

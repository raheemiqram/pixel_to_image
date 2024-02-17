FROM python:3.11

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE "image_processing.settings.local"

RUN apt-get update

# install psycopg2 dependencies
RUN apt-get install -y apt-utils python3-psycopg2 python3-dev

# install lxml dependencies
RUN apt-get install -y libxslt-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements/base.txt ./requirements.txt

RUN pip install -r ./requirements.txt

# Replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Install base dependencies
RUN apt-get update && apt-get install -y -q --no-install-recommends \
        apt-transport-https \
        build-essential \
        ca-certificates \
        curl \
        git \
        libssl-dev \
        wget \
    && rm -rf /var/lib/apt/lists/*

COPY . .


#docker run --rm -e NAME='ALI' alihhussain/env:test /usr/bin/python /root/test.py
FROM ubuntu:xenial

MAINTAINER alihhussain <alihhussain@live.com>

COPY test.py /root/test.py

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y supervisor software-properties-common vim jq wget git net-tools man
RUN add-apt-repository ppa:jonathonf/python-3.6 -y
RUN apt-get update
RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel

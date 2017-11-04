# This is a base image created out of ubuntu:latest
FROM resin/rpi-raspbian

MAINTAINER alihhussain <alihhussain@live.com>

RUN mkdir /root/.ssh
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY .vimrc /root/.vimrc
COPY authorized_keys /root/.ssh/authorized_keys
COPY id_rsa /root/.ssh/id_rsa
COPY install.py /root/install.py

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y wget \
    python \
    sense-hat \
    python-picamera \
    build-essential \
    libssl-dev \
    libffi-dev \
    python-dev

RUN pip install azure

# Install Redis client
RUN pip install redis


RUN /usr/bin/python /root/install.py
RUN rm -rf /tmp/*.dep
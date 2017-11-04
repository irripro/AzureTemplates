FROM resin/rpi-raspbian

MAINTAINER alihhussain <alihhussain@live.com>

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y wget \
    python \
    sense-hat \
    python-picamera \
    build-essential \
    libssl-dev \
    libffi-dev \
    python-dev

RUN wget -P / https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

RUN pip install azure

# Install Redis client
RUN pip install redis

RUN rm -rf /tmp/*.dep

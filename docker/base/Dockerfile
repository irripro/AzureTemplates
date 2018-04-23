# This is a base image created out of ubuntu:latest
FROM ubuntu:xenial

MAINTAINER alihhussain <alihhussain@live.com>

ADD ./ /root/
 
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y software-properties-common vim jq wget git net-tools man
RUN apt-get install libssl-dev libffi-dev build-essential python-pip python-dev -y
RUN pip install --upgrade pip
RUN echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ wheezy main" |  tee /etc/apt/sources.list.d/azure-cli.list
RUN apt-key adv --keyserver packages.microsoft.com --recv-keys 52E16F86FEE04B979B07E28DB02C46DF417A0893
RUN apt-get install apt-transport-https
RUN apt-get update &&  apt-get install azure-cli
RUN apt-get install python -y
RUN echo "10th Live Demo" > /tmp/livedemo.txt
ENTRYPOINT ["/bin/bash"]

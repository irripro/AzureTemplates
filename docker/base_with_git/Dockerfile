# This is a base image created out of ubuntu:latest
FROM ubuntu:xenial

MAINTAINER alihhussain <alihhussain@live.com>

ADD ./ /root/
 
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y software-properties-common vim jq wget git net-tools man
RUN add-apt-repository ppa:jonathonf/python-3.6 -y
RUN apt-get update
RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel
RUN /usr/bin/pip3 install flask flask-ask
RUN apt-get install libssl-dev libffi-dev python3-dev build-essential -y
RUN echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ wheezy main" |  tee /etc/apt/sources.list.d/azure-cli.list
RUN apt-key adv --keyserver packages.microsoft.com --recv-keys 52E16F86FEE04B979B07E28DB02C46DF417A0893
RUN apt-get install apt-transport-https
RUN apt-get update &&  apt-get install azure-cli
RUN apt-get install python git -y
RUN /usr/bin/git clone "https://github.com/alihhussain/AzureTemplates.git" /github
ENTRYPOINT ["/bin/bash"]

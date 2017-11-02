# This is a base image created out of ubuntu:latest
FROM ubuntu:xenial

MAINTAINER alihhussain <alihhussain@live.com>

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y software-properties-common vim jq wget git net-tools man && \
    add-apt-repository ppa:jonathonf/python-3.6 -y && \
    apt-get update && \
    apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv && \
    python3.6 -m pip install pip --upgrade && \
    python3.6 -m pip install wheel && \
    ln -s /usr/bin/python3.6 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip && \
    pip install flask flask-ask && \
    apt-get install libssl-dev libffi-dev python3-dev build-essential -y && \
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ wheezy main" |  tee /etc/apt/sources.list.d/azure-cli.list && \
    apt-key adv --keyserver packages.microsoft.com --recv-keys 52E16F86FEE04B979B07E28DB02C46DF417A0893 && \
    apt-get install apt-transport-https && \
    apt-get update &&  apt-get install azure-cli && \
    apt-get install -y openssh-server && \
    mkdir /var/run/sshd && \
    echo 'root:root' |chpasswd && \
    sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \
    sed -ri 's,#AuthorizedKeysFile,AuthorizedKeysFile,g' /etc/ssh/sshd_config && \
    service ssh start



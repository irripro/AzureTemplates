FROM ubuntu:xenial

MAINTAINER alihhussain <alihhussain@live.com>

ADD . /root/autocomplete

RUN apt-get update && apt-get upgrade -y && apt-get install python -y

EXPOSE 80

#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["/usr/bin/python", "/root/autocomplete/app.py"]

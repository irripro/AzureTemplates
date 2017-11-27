FROM ubuntu:xenial

MAINTAINER alihhussain <alihhussain@live.com>

ADD . /root/autocomplete

RUN apt-get update && apt-get upgrade -y && apt-get install python -y

EXPOSE 443

ENTRYPOINT ["/usr/bin/python", "/root/autocomplete/app.py"]

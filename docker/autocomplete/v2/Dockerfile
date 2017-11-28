FROM ubuntu:xenial

MAINTAINER alihhussain <alihhussain@live.com>

ADD . /root/autocomplete

RUN apt-get update && apt-get upgrade -y
RUN apt-get install python supervisor -y

EXPOSE 443 80
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/root/autocomplete/supervisord.conf"]
#ENTRYPOINT ["/usr/bin/python", "/root/autocomplete/app.py"]
#ENTRYPOINT ["/bin/bash"]

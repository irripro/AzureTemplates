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

RUN /usr/bin/python /root/install.py

RUN curl -sS https://bootstrap.pypa.io/get-pip.py | /usr/bin/python
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | /usr/bin/python3
RUN apt-get install -y supervisor jq
RUN /usr/bin/pip install flask flask-ask
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:root' |chpasswd
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN sed -ri 's,#AuthorizedKeysFile,AuthorizedKeysFile,g' /etc/ssh/sshd_config

EXPOSE 22
CMD ["/usr/bin/supervisord"]
RUN rm -rf /tmp/*.dep


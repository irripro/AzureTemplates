# This is a base image created out of ubuntu:latest
FROM centos:7

MAINTAINER alihhussain <alihhussain@live.com>

ADD ./ /root/
 
RUN yum update && yum upgrade -y
RUN cp /root/kubectl /usr/local/bin/kubectl
RUN mkdir /root/.kube && mv /root/myconfig /root/.kube/config
ENTRYPOINT ["/bin/bash"]

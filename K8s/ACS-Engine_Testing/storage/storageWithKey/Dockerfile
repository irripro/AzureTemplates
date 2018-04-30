FROM ubuntu:latest
MAINTAINER Ali Hussain "alhussai@microsoft.com"
EXPOSE 80
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip
COPY . /app
RUN pip install -r /app/requirements.txt
ENTRYPOINT ["/usr/bin/python", "/app/app.py"]
#ENTRYPOINT ["/bin/bash"]

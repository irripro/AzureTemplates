#!/bin/bash
#Update system
yum upgrade -y
yum update -y

#Install pip
yum  install python-pip python-dev build-essential -y
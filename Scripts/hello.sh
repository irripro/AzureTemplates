#!/bin/bash

yum update -y

echo 'This is great, seems like the custom script is working\n' > /tmp/testing.txt;
cat /etc/hostname > /tmp/hostname.txt

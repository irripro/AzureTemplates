#!/usr/bin/env python
import sys, json
from fabric.api import *
from pprint import pprint

numberofnodes = {nodeschosen}
if numberofnodes == 2:
    env.hosts = ['{elbpublicdns}:8022','{elbpublicdns}:8023']
elif numberofnodes == 3:
    env.hosts = ['{elbpublicdns}:8022','{elbpublicdns}:8023','{elbpublicdns}:8024']
elif numberofnodes == 4:
    env.hosts = ['{elbpublicdns}:8022','{elbpublicdns}:8023','{elbpublicdns}:8024','{elbpublicdns}:8025']
elif numberofnodes == 5:
    env.hosts = ['{elbpublicdns}:8022','{elbpublicdns}:8023','{elbpublicdns}:8024','{elbpublicdns}:8025','{elbpublicdns}:8026']
elif numberofnodes == 6:
    env.hosts = ['{elbpublicdns}:8022','{elbpublicdns}:8023','{elbpublicdns}:8024','{elbpublicdns}:8025','{elbpublicdns}:8026','{elbpublicdns}:8027']
elif numberofnodes == 7:
    env.hosts = ['{elbpublicdns}:8022','{elbpublicdns}:8023','{elbpublicdns}:8024','{elbpublicdns}:8025','{elbpublicdns}:8026','{elbpublicdns}:8027','{elbpublicdns}:8028']
else:
    sys.exit("Select the right amount of nodes")
    
    
def deploy():
    env.user = 'azureuser'
    env.key_filename = '/var/lib/jenkins/.ssh/id_rsa'
    #env.combine_stderr = False
    env.disable_known_hosts = True
    env.output_prefix = False
    env.colorize_errors = True
    env.linewise = True
#    with hide('everything'):
#        sudo("yum update -y")
    sudo("yum upgrade -y")
    sudo("yum update -y")
    sudo("yum  install python-pip python-dev build-essential -y")
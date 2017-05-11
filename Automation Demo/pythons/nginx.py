#!/usr/bin/env python
from fabric.api import *

env.hosts = open('vmname.txt', 'r').read().replace('\n', '')
env.user = 'alihhussain'

env.key_filename = '/var/lib/jenkins/.ssh/id_rsa'
#env.combine_stderr = False
env.disable_known_hosts = True
env.output_prefix = False
env.colorize_errors = True

domain=env.hosts
domain=domain.split('.',1)
domain=domain[0]

def precheck():
    with hide('everything'):
        sudo("yum update -y")

def installnginx():
    sudo("yum install epel-release -y")
    sudo("yum -y install nginx")
    sudo("service nginx start")
    sudo("systemctl enable nginx")
    sudo("useradd %s" %domain)
    sudo("echo %s | passwd %s --stdin" %(domain,domain))

if __name__ == "__main__":
    execute(precheck)
#    execute(installnginx)

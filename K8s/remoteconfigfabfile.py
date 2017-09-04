#!/usr/bin/env python
import sys, json
from fabric.api import *
from pprint import pprint

totalnodes = {nodeschosen}
if totalnodes == 2:
    env.hosts = ['{elbpublicdns}:8022','{elbpublicdns}:8023']
elif totalnodes == 3:
    env.hosts = ['{elbpublicdns}:8022','{elbpublicdns}:8023','{elbpublicdns}:8024']
elif totalnodes == 4:
    env.hosts = ['{elbpublicdns}:8022','{elbpublicdns}:8023','{elbpublicdns}:8024','{elbpublicdns}:8025']
elif totalnodes == 5:
    env.hosts = ['{elbpublicdns}:8022','{elbpublicdns}:8023','{elbpublicdns}:8024','{elbpublicdns}:8025','{elbpublicdns}:8026']
elif totalnodes == 6:
    env.hosts = ['{elbpublicdns}:8022','{elbpublicdns}:8023','{elbpublicdns}:8024','{elbpublicdns}:8025','{elbpublicdns}:8026','{elbpublicdns}:8027']
elif totalnodes == 7:
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
    with hide('everything'):
        sudo("yum upgrade -y")
        sudo("yum update -y")
    sudo("""curl 'https://bootstrap.pypa.io/get-pip.py' -o '/tmp/get-pip.py'""")
    sudo("/usr/bin/python /tmp/get-pip.py")
    sudo("yum install -y ntp")
    sudo("systemctl enable ntpd && systemctl start ntpd")
    sudo("systemctl status ntpd")
    sudo("""curl 'https://raw.githubusercontent.com/alihhussain/AzureTemplates/master/K8s/hosts' -o /etc/hosts""")
    sudo("""curl 'https://raw.githubusercontent.com/alihhussain/AzureTemplates/master/K8s/virt7-docker-common-release.repo' -o /etc/yum.repos.d/virt7-docker-common-release.repo""")
    sudo("yum update -y")
    sudo("groupadd docker")
    sudo("yum -y install --enablerepo=virt7-docker-common-release docker kubernetes etcd flannel")
    sudo("systemctl start docker")
    sudo("systemctl enable docker")
    sudo("usermod -aG docker %s" %env.user)
    sudo("init 6")
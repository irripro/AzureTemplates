#!/usr/bin/env python
import sys, json
from fabric.api import *
from pprint import pprint

vm0 = "{elbpublicdns}:8022"
vm1 = "{elbpublicdns}:8023"
vm2 = "{elbpublicdns}:8024"
vm3 = "{elbpublicdns}:8025"
vm4 = "{elbpublicdns}:8026"
vm5 = "{elbpublicdns}:8027"
vm6 = "{elbpublicdns}:8028"

totalnodes = {nodeschosen}   
if totalnodes == 2:
    env.hosts = [vm0,vm1]
elif totalnodes == 3:
    env.hosts = [vm0,vm1,vm2]
elif totalnodes == 4:
    env.hosts = [vm0,vm1,vm2,vm3]
elif totalnodes == 5:
    env.hosts = [vm0,vm1,vm2,vm3,vm4]
elif totalnodes == 6:
    env.hosts = [vm0,vm1,vm2,vm3,vm4,vm5]
elif totalnodes == 7:
    env.hosts = [vm0,vm1,vm2,vm3,vm4,vm5,vm6]
else:
    sys.exit("Select the right amount of nodes")    
        
def deployall():
    env.user = 'azureuser'
    env.key_filename = '/var/lib/jenkins/.ssh/id_rsa'
    #env.combine_stderr = False
    env.disable_known_hosts = True
    env.output_prefix = False
    env.colorize_errors = True
    env.linewise = True
    with hide('everything'):
        sudo("apt-get update -y && apt-get upgrade -y")
    sudo("apt-get install ntp jq apt-transport-https ca-certificates -y")
    sudo("systemctl enable ntp && systemctl start ntp")
    sudo("apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D")
    sudo("""bash -c "echo 'deb https://apt.dockerproject.org/repo ubuntu-xenial main' > /etc/apt/sources.list.d/docker.list"""")
    sudo("apt-get update -y")
    sudo("apt-get install docker-engine=1.12.6-0~ubuntu-xenial -y")
    sudo("systemctl enable docker && systemctl start docker")
    sudo("usermod -aG docker %s" %env.user)
    run("curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.6.6/bin/linux/amd64/kubectl")
    run("chmod +x /home/azureuser/kubectl")
    sudo("mv /home/azureuser/kubectl /usr/local/bin/kubectl")
    run("""echo "source <(kubectl completion bash)" >> ~/.bashrc""")
    sudo("apt-get update && apt-get install -y apt-transport-https")
    sudo("curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -")
    sudo("""bash -c "echo 'deb http://apt.kubernetes.io/ kubernetes-xenial main' > /etc/apt/sources.list.d/kubernetes.list"""")
    sudo("apt-get update -y")
    sudo("apt-get install -y kubelet kubeadm=1.6.6-00")
    try:
        sudo("init 6")
    except:
        print("This was fine just restarted the system.")
        
def deployallpart2():
    env.user = 'azureuser'
    env.key_filename = '/var/lib/jenkins/.ssh/id_rsa'
    #env.combine_stderr = False
    env.disable_known_hosts = True
    env.output_prefix = False
    env.colorize_errors = True
    env.linewise = True
    sudo("systemctl enable kubelet && systemctl start kubelet")
    run("hostname")

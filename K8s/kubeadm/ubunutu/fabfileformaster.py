#!/usr/bin/env python
import sys, json
from fabric.api import *
from fabric.api import local
from pprint import pprint

vm0 = "{elbpublicdns}:8022"
vm0PiP = "VM0"
env.hosts = [vm0]
        
def deployall():
    env.user = 'azureuser'
    env.key_filename = '/var/lib/jenkins/.ssh/id_rsa'
    #env.combine_stderr = False
    env.disable_known_hosts = True
    env.output_prefix = False
    env.colorize_errors = True
    env.linewise = True
    sudo("kubeadm init --pod-network-cidr=192.168.0.0/16 > /tmp/kubeadm.first.output")
    sudo("""kubeadm init > /tmp/kubeadm.first.output""")
    sudo("""bash -c "echo 'export KUBECONFIG=$HOME/admin.conf' >> /home/azureuser/.profile"""")
    sudo("cat /tmp/kubeadm.first.output")
    run("kubectl get nodes")
    output=run("cat /tmp/kubeadm.first.output")
    output_stdout = output.stdout.split("\r\n")
    outputlist=output_stdout[39].split()
    token=outputlist[3]
    local("echo '%s' > ./token.kube" %token)
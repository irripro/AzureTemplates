#!/usr/bin/env python
import sys, json
from fabric.api import *
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
    sudo("hostname")
    sudo("""kubeadm init > /tmp/kubeadm.first.output""")
    sudo("cat /tmp/kubeadm.first.output")
    output=run("cat /tmp/kubeadm.first.output")
    output_stdout = output.stdout.split("\r\n")
    outputlist=output_stdout[39].split()
    token=outputlist[3]
    local("echo '%s' > ./token.kube" %token)
#    sudo("kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml")
#    sudo("kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel-rbac.yml")
#    sudo("kubectl get pods --all-namespaces")
#    try:
#        sudo("init 6")
#    except:
#        print("This was fine just restarted the system.")
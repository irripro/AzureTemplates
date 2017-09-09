#!/usr/bin/env python
import sys, json
from fabric.api import *
from pprint import pprint

vm0 = "{elbpublicdns}:8022"
env.hosts = [vm0]
vm0PiP = "VM0"

def deployall():
    env.user = 'azureuser'
    env.key_filename = '/var/lib/jenkins/.ssh/id_rsa'
    #env.combine_stderr = False
    env.disable_known_hosts = True
    env.output_prefix = False
    env.colorize_errors = True
    env.linewise = True
    run("kubectl describe nodes")
    run("kubectl get nodes")
#    run("curl 'https://bitbucket.org/Dhyaniarun/kubernetes/raw/bcc3c46179773691ae51c11785eb70bfca58ba9e/DNS/skydns-svc.yaml' -o skydns-svc.yaml")
#    run("curl 'https://bitbucket.org/Dhyaniarun/kubernetes/raw/bcc3c46179773691ae51c11785eb70bfca58ba9e/DNS/skydns-rc.yaml' -o skydns-rc.yaml")
#    run("curl 'https://bitbucket.org/Dhyaniarun/kubernetes/raw/bcc3c46179773691ae51c11785eb70bfca58ba9e/Dashboard/dashboard-controller.yaml' -o dashboard-controller.yaml")
#    run("curl 'https://bitbucket.org/Dhyaniarun/kubernetes/raw/bcc3c46179773691ae51c11785eb70bfca58ba9e/Dashboard/dashboard-service.yaml' -o dashboard-service.yaml")
#    sudo("kubectl create -f dashboard-controller.yaml")
#    sudo("kubectl create -f dashboard-service.yaml")
#    sudo("kubectl create -f skydns-rc.yaml")
#    sudo("kubectl create -f skydns-svc.yaml")
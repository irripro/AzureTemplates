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
    sudo("hostname")
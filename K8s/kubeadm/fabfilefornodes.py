#!/usr/bin/env python
import sys, json
from fabric.api import *
from pprint import pprint

vm1 = "{elbpublicdns}:8023"
vm2 = "{elbpublicdns}:8024"
vm3 = "{elbpublicdns}:8025"
vm4 = "{elbpublicdns}:8026"
vm5 = "{elbpublicdns}:8027"
vm6 = "{elbpublicdns}:8028"

vm0PiP = "10.0.0.4"
totalnodes = {nodeschosen}   

if totalnodes == 2:
    env.hosts = [vm1]
elif totalnodes == 3:
    env.hosts = [vm1,vm2]
elif totalnodes == 4:
    env.hosts = [vm1,vm2,vm3]
elif totalnodes == 5:
    env.hosts = [vm1,vm2,vm3,vm4]
elif totalnodes == 6:
    env.hosts = [vm1,vm2,vm3,vm4,vm5]
elif totalnodes == 7:
    env.hosts = [vm1,vm2,vm3,vm4,vm5,vm6]
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
    token=local("cat ./token.kube")
    print("This is the token: %s " %token)
    sudo("kubeadm join --token %s %s:6443" %(token,vm0PiP)
#    try:
#        sudo("init 6")
#    except:
#        print("This was fine just restarted the system.")
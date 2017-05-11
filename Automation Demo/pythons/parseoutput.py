#!/usr/bin/env python
#import pdb; pdb.set_trace();

import json, sys
from pprint import pprint

filename=sys.argv[1]

with open(filename) as data_file:    
    data = json.load(data_file)

vms=data["properties"]["outputs"]["sshCommand"]["value"]
elbfile = open("elbfile.txt", "w")
elbfile.write(vms)
elbfile.close()


#vms1=vms.split('#',1)
#vm1=vms1[0]
#vm2=vms1[1]

#vm1file = open("vm1file.txt", "w")
#vm1file.write(vm1)
#vm1file.close()

#vm1file = open("vm2file.txt", "w")
#vm1file.write(vm2)
#vm1file.close()
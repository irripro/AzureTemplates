#!/usr/bin/env python
#import pdb; pdb.set_trace();
import json, sys
from pprint import pprint

filename=sys.argv[1]

with open(filename) as data_file:    
    data = json.load(data_file)

print(data["properties"]["outputs"]["sshCommand"]["value"])

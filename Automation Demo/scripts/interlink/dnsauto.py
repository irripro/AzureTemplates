from __future__ import absolute_import, division, print_function, unicode_literals, with_statement
import dns.query
import dns.tsigkeyring
import dns.update
import sys
import dns.resolver #import the module
from dns import resolver, reversename
import sys, os
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
#from haikunator import Haikunator
#haikunator = Haikunator()
# STORAGE_ACCOUNT_NAME = haikunator.haikunate(delimiter='')

class ResourceGroupDetails(object):
    def __init__(self, storage_accounts=None, storage_accounts_locations=None,
                 vms=None, public_ip_addresses=None, virtual_networks=None):
        self.storage_accounts = storage_accounts
        self.storage_accounts_locations = storage_accounts_locations
        self.vms = vms
        self.public_ip_addresses = public_ip_addresses
        self.virtual_networks = virtual_networks

global appID, tenant1, passwd, subscription_id, dnsserver, domain
#dnsserver = '10.0.0.8'
#domain = 'altst.local'
dnsserver=str("%s" %sys.argv[6])
domain=str("%s" %sys.argv[7])


#appID=str("a289cbdd-4fca-4a7d-88c4-6a02892223d4")
#tenant1=str("72f988bf-86f1-41af-91ab-2d7cd011db47")
#sub_id=str("e729c299-db43-40ce-991a-7e4572a69d50")
#passwd=str("2#Adam26185")

appID=str("%s" %sys.argv[1])
tenant1=str("%s" %sys.argv[2])
sub_id=str("%s" %sys.argv[3])
passwd=str("%s" %sys.argv[4])
res_name=str("%s" %sys.argv[5])

"""Resource Group management example."""

# Create all clients with an Application (service principal) token provider

subscription_id=sub_id

creds = ServicePrincipalCredentials(
    client_id=appID,
    secret=passwd,
    tenant=tenant1
)

def get_resource_group_details(subscription_id, creds, resource_group_name):
    compute_client = ComputeManagementClient(creds, subscription_id)
    
    model = ResourceGroupDetails()
    model.vms = list(compute_client.virtual_machines.list(resource_group_name))

    return model

def add_to_dns(fqdn,ipadd):
    update = dns.update.Update(domain)
    update.add(fqdn,300,'A', ipadd)
    response = dns.query.tcp(update, dnsserver)
    response=str(response)
    if 'noerror' in response.lower():
        return("Successful")
    else:
        return("Unsuccessful")

def main():
    template=get_resource_group_details(subscription_id,creds,res_name)
    network_client = NetworkManagementClient(creds, subscription_id)
    for vm in template.vms:
        ni_reference = vm.network_profile.network_interfaces[0]
        ni_reference = ni_reference.id.split('/')
        ni_group = ni_reference[4]
        ni_name = ni_reference[8]

        net_interface = network_client.network_interfaces.get(ni_group, ni_name)
        import pdb; pdb.set_trace()
        private_ip=net_interface.ip_configurations[0].private_ip_address
        vmname=vm.name
        #print("The name of the VM is: %s\nThe private IP is: %s" %(vmname,private_ip))
        #print("Addition to the DNS server: %s" %add_to_dns(vmname,private_ip))
if __name__ == "__main__":
    main()

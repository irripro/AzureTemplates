# Study Notes
Some notes taken as I was studying for the CKA exam.

## Create cluster
Lets create a cluster to play around with in Azure.

### 1. Create Resource Group
```bash
myRG=myK8swithKubeadm
myLocation=eastus
az group create --name myK8swithKubeadm --location eastus
```
### 2. Create VNET
```bash
myVnet=myK8sVnet
az network vnet create \
    --resource-group $myRG \
    --name $myVnet \
    --subnet-name nodes \
    --subnet-prefix 192.168.2.0/24

# Create a Second Subnet
az network vnet subnet create -g $myRG --vnet-name $myVnet -n master \
                            --address-prefix 192.168.1.0/24
```
### 3. Create private DNS Zone
```bash
az network dns zone create -g $myRG -n k8s.local --zone-type Private --resolution-vnets $myVnet
```
If you get an error ```az network dns zone create: error: unrecognized argument: --zone-type Private``` ensure you have the latest version of CLI 2.0 installed.

### 4. Create a Public IP for Master
```bash
myDNS=myk8s
az network public-ip create \
    --resource-group $myRG \
    --name myMaster \
    --dns-name $myDNS
```
If you get an error stating the ```--dns-name``` is not unique, then prefix ```myk8s``` with some other unique characters.

### 5. Create NSG
```bash
#Public NSG
myNSG=myPublicNSG
az network nsg create \
    --resource-group $myRG \
    --name $myNSG
```
### 6. Create NSG Rule
```bash
az network nsg rule create \
    --resource-group $myRG \
    --nsg-name $myNSG \
    --name $myNSGRuleSSH \
    --protocol tcp \
    --priority 1001 \
    --destination-port-range 22 \
    --access allow
```

### 7. Create a Master Node
```bash
myRG=myK8swithKubeadm
myNIC=myMasterNic
myVnet=myK8sVnet
myNSG=myPublicNSG
myLocation=eastus
mySSHKey="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCsvQoaddMbc5zdqMXnBrn53eatB1hzHwk0rlpg/SUn+B6yMJRq0fvntn1/LWkhsOv2QIOkSZhnZO5rUJuoSaBZuRkXf2wUsva2Z9iaKMozzcadUXCU0y/2ekCPY+8eUZOSvTgmn2K0xT12H+rrzGK6MBgnFgDZ2npROZa4eF4SkMxcMpFbOiOEY53/OiokbwEFUXD3omrhURqJzOOWdaCy4XPjWvjEzpNagTM/uy0habgSVVa3Uj/aF8QkgixJOlgME4jBMyM4uyd/lCsgKvrFquwVbOWZUcic+lZTDVfjIUyqTkq6+avzxtWnxMNrktW7gfOA1Des53Vs4N4QL+af jenkins@jenkins"

# Create the NIC for the VM first
az network nic create \
    --resource-group $myRG \
    --name $myNIC \
    --vnet-name $myVnet \
    --subnet master \
    --public-ip-address myMaster \
    --network-security-group $myNSG

#Creating the VM itself
az vm create \
    --resource-group $myRG \
    --name myMasterVM \
    --location $myLocation \
    --nics $myNIC \
    --image UbuntuLTS \
    --admin-username azureuser \
    --ssh-key-value "$mySSHKey"
```
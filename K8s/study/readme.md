# Study Notes
Some notes taken as I was studying for the CKA exam.

## Create cluster
Lets create a cluster to play around with in Azure.

### 1. Create Resource Group
```bash
az group create --name myK8swithKubeadm --location eastus
```
### 2. Create VNET
```bash
az network vnet create \
    --resource-group myK8swithKubeadm \
    --name myK8sVnet \
    --address-prefix 192.168.0.0/16 \
    --subnet-name master \
    --subnet-prefix 192.168.1.0/24 \
    --subnet-name nodes \
    --subnet-prefix 192.168.2.0/24
```
### 3. Create private DNS Zone
```bash
az network dns zone create -g myK8swithKubeadm -n k8s.local --zone-type Private --resolution-vnets myK8sVnet
```
If you get an error ```az network dns zone create: error: unrecognized argument: --zone-type Private``` ensure you have the latest version of CLI 2.0 installed.

### 4. Create a Public IP for Master
```bash
az network public-ip create \
    --resource-group myK8swithKubeadm \
    --name myMaster \
    --dns-name myk8s
```
If you get an error stating the ```--dns-name``` is not unique, then prefix ```myk8s``` with some other unique characters.


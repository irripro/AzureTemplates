# Study Notes
Some notes taken as I was studying for the CKA exam.

## Create cluster
Lets create a cluster to play around with in Azure.

### 1. Create Resource Group
```bash
myRG=myK8swithKubeadm
myLocation=eastus
az group create --name $myRG --location $myLocation
```
### 2. Create VNET
```bash
myVnet=myK8sVnet
az network vnet create \
    --resource-group $myRG \
    --name $myVnet \
    --address-prefix 192.168.0.0/16 \
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
## This is for SSH
az network nsg rule create \
    --resource-group $myRG \
    --nsg-name $myNSG \
    --name RuleSSH \
    --protocol tcp \
    --priority 1001 \
    --destination-port-range 22 \
    --access allow
#This is for the API Server
az network nsg rule create \
    --resource-group $myRG \
    --nsg-name $myNSG \
    --name myAPIServerRule \
    --protocol tcp \
    --priority 1002 \
    --destination-port-range 6443 \
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
    --ssh-key-value "$mySSHKey" \
    --size Standard_D2s_v3

#   kubeadm join 192.168.1.4:6443 --token l9729c.3gthcw5zs04c9za0 --discovery-token-ca-cert-hash sha256:38afd44768f609e0236e7a5eeeed56236f93947cdd0bcb690bc8e051872dab46
```
### 8. Setup Master
```bash
#Copy the id_rsa file into the master node
scp ~/.ssh/id_rsa azureuser@myk8s.eastus.cloudapp.azure.com:/home/azureuser/.ssh/id_rsa

# On the master
sudo su
# Install Docker
apt-get update
apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository \
   "deb https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
   $(lsb_release -cs) \
   stable"
apt-get update && apt-get install -y docker-ce=$(apt-cache madison docker-ce | grep 17.03 | head -1 | awk '{print $3}')
apt-get update -y && apt-get upgrade -y

#As a normal user
sudo usermod -aG docker azureuser

#List out Kubernetes Versions
curl -sL https://apt.kubernetes.io/dists/kubernetes-xenial/main/binary-amd64/Packages | grep -E 'Package|Version'

#Set up Repo
apt-get update && apt-get install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb http://apt.kubernetes.io/ kubernetes-xenial main
EOF
apt-get update
apt-get install -y kubelet=1.10.3-00 kubeadm=1.10.3-00 kubectl=1.10.3-00

kubeadm init --pod-network-cidr=10.244.0.0/16
#Copy output
#   kubeadm join 192.168.1.4:6443 --token 58gm7w.wncw5fzztmvzs892 --discovery-token-ca-cert-hash sha256:0b4092ea8ffb805f8f2597465a18485a4648d41f3331a2a6c5fb34f34566c511

#Run as a normal User
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

#Install Flannel
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/v0.10.0/Documentation/kube-flannel.yml
```

### 9. Provision Node VMs
```bash
myRG=myK8swithKubeadm
myNIC=myNodeNic
myVnet=myK8sVnet
myNSG=myPublicNSG
myLocation=eastus
myVMName=myNodeVM
mySSHKey="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCsvQoaddMbc5zdqMXnBrn53eatB1hzHwk0rlpg/SUn+B6yMJRq0fvntn1/LWkhsOv2QIOkSZhnZO5rUJuoSaBZuRkXf2wUsva2Z9iaKMozzcadUXCU0y/2ekCPY+8eUZOSvTgmn2K0xT12H+rrzGK6MBgnFgDZ2npROZa4eF4SkMxcMpFbOiOEY53/OiokbwEFUXD3omrhURqJzOOWdaCy4XPjWvjEzpNagTM/uy0habgSVVa3Uj/aF8QkgixJOlgME4jBMyM4uyd/lCsgKvrFquwVbOWZUcic+lZTDVfjIUyqTkq6+avzxtWnxMNrktW7gfOA1Des53Vs4N4QL+af jenkins@jenkins"

# Create the NIC for the VM first
az network nic create \
    --resource-group $myRG \
    --name $myNIC \
    --vnet-name $myVnet \
    --subnet nodes \
    --network-security-group $myNSG

#Creating the VM itself
az vm create \
    --resource-group $myRG \
    --name $myVMName \
    --location $myLocation \
    --nics $myNIC \
    --image UbuntuLTS \
    --admin-username azureuser \
    --ssh-key-value "$mySSHKey" \
    --size Standard_D2s_v3 \
    --no-wait
```

### 10. Configure Node
```bash
# On the Node
sudo su
# Install Docker
apt-get update
apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository \
   "deb https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
   $(lsb_release -cs) \
   stable"
apt-get update && apt-get install -y docker-ce=$(apt-cache madison docker-ce | grep 17.03 | head -1 | awk '{print $3}')
apt-get update -y && apt-get upgrade -y

#As a normal user
sudo usermod -aG docker azureuser

#Set up Repo
apt-get update && apt-get install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb http://apt.kubernetes.io/ kubernetes-xenial main
EOF
apt-get update
apt-get install -y kubelet=1.10.3-00 kubeadm=1.10.3-00 kubectl=1.10.3-00

#Join using the copied command from earlier
kubeadm join 192.168.1.4:6443 --token 58gm7w.wncw5fzztmvzs892 --discovery-token-ca-cert-hash sha256:0b4092ea8ffb805f8f2597465a18485a4648d41f3331a2a6c5fb34f34566c511
```

### Repeat Step 9 and 10 for additional Nodes

### Random Notes
```bash
Master=myk8s.eastus.cloudapp.azure.com
Node=myNodeVM
Node1=MyNodevm1
joinCmd="kubeadm join 192.168.1.4:6443 --token 58gm7w.wncw5fzztmvzs892 --discovery-token-ca-cert-hash sha256:0b4092ea8ffb805f8f2597465a18485a4648d41f3331a2a6c5fb34f34566c511"
```
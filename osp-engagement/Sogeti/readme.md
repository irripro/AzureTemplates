# Configure Kubectl

Two Options
* [Base Container](#container-kubectl)
* [Download Config file](#config-file)

## Container Kubectl
To get the container up and running:

1. [Install Docker](https://docs.docker.com/engine/installation/)
2. Pull Image
    * Run: ```docker pull alihhussain/azurepublic:301Base```
3. Run the image
    * Run: ```docker run -it alihhussain/azurepublic:301Base```
4. Check Kubernetes Status
    * Run: ```kubectl get nodes```
```bash
ali@MININT-alhussai:~$ kubectl get nodes
NAME                       STATUS    AGE       VERSION
aks-nodepool1-23314708-0   Ready     2h        v1.7.7
aks-nodepool1-23314708-1   Ready     2h        v1.7.7
aks-nodepool1-23314708-2   Ready     2h        v1.7.7
aks-nodepool1-23314708-3   Ready     2h        v1.7.7
```

## Config File

Prerequisites:
* [Install Bash on Windows](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
* [Install Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
* [Download Config File](https://functionc134d59b8177.blob.core.windows.net/config/myconfig)

1. Open Bash
2. Make directory inside of your home directory
```bash
cd ~
mkdir ~/.kube/
```
3. Download the file and Copy downloaded file inside of ```~/.kube/```
```bash
cd ~/.kube/
wget https://functionc134d59b8177.blob.core.windows.net/config/myconfig
mv myconfig config
```
4. The output of ```ls -alh ~/.kube/config``` should look like 
```bash
ali@MININT-alhussai:~$ ls -alh ~/.kube/config
-rwxrwxrwx 1 ali ali 9.4K Jan 16 00:33 /home/ali/.kube/config
```
5.  Check Kubernetes Status
    * Run: ```kubectl get nodes```

```bash
ali@MININT-alhussai:~$ kubectl get nodes
NAME                       STATUS    AGE       VERSION
aks-nodepool1-23314708-0   Ready     2h        v1.7.7
aks-nodepool1-23314708-1   Ready     2h        v1.7.7
aks-nodepool1-23314708-2   Ready     2h        v1.7.7
aks-nodepool1-23314708-3   Ready     2h        v1.7.7
```

# Live Demo
## Ch 02

### Pod
Get to the directory
```bash
cd /mnt/c/Users/alhussai/Documents/GitHub/AzureTemplates/docker/base_301_AKS/container-hackfest/challenges/SolutionHelperFiles/ch02
```

Deploy the pod
```bash
kubectl create -f pod.yaml
pod "my-pod" created
```

Describe the Pod
```bash
kubectl describe pods my-pod
```

Test the Pod
```bash
kubectl port-forward my-pod 8080:8080
Forwarding from 127.0.0.1:8080 -> 8080
Forwarding from [::1]:8080 -> 8080
```

### Deployment

Deploy the Deployment
```bash
kubectl create -f deploy.yaml
deployment "my-deploy" created
```

List the Deployment
```bash
kubectl get all

NAME                            READY     STATUS    RESTARTS   AGE
po/my-deploy-2287124240-mkt28   1/1       Running   0          28s
po/my-deploy-2287124240-s00k1   1/1       Running   0          28s
po/my-deploy-2287124240-wdjxx   1/1       Running   0          28s

NAME             CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
svc/kubernetes   10.0.0.1     <none>        443/TCP   2h

NAME               DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deploy/my-deploy   3         3         3            3           28s

NAME                      DESIRED   CURRENT   READY     AGE
rs/my-deploy-2287124240   3         3         3         28s
```

Describe the Deployment
```bash
kubectl describe deploy my-deploy
Name:                   my-deploy
Namespace:              default
CreationTimestamp:      Tue, 16 Jan 2018 01:28:46 -0800
Labels:                 version=v1
                        zone=prod
Annotations:            deployment.kubernetes.io/revision=1
Selector:               app=my-app
Replicas:               3 desired | 3 updated | 3 total | 3 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        15
RollingUpdateStrategy:  1 max unavailable, 1 max surge
Pod Template:
  Labels:       app=my-app
  Containers:
   my-ctr2:
    Image:              evillgenius/kuar:1
    Port:               8080/TCP
    Environment:        <none>
    Mounts:             <none>
  Volumes:              <none>
Conditions:
  Type          Status  Reason
  ----          ------  ------
  Available     True    MinimumReplicasAvailable
  Progressing   True    NewReplicaSetAvailable
OldReplicaSets: <none>
NewReplicaSet:  my-deploy-2287124240 (3/3 replicas created)
Events:
  FirstSeen     LastSeen        Count   From                    SubObjectPath   Type            Reason                  Message
  ---------     --------        -----   ----                    -------------   --------        ------                  -------
  7m            7m              1       deployment-controller                   Normal          ScalingReplicaSet       Scaled up replica set my-deploy-2287124240 to 3
```

Test out the deployment
```bash
kubectl port-forward <OnePodID> 8080:8080
Forwarding from 127.0.0.1:8080 -> 8080
Forwarding from [::1]:8080 -> 8080
```

Deploy a Service on Top of Deployment to make it public
```bash
kubectl create -f service.yaml
service "my-svc" created

kubectl get all
NAME                            READY     STATUS    RESTARTS   AGE
po/my-deploy-2287124240-fw2hv   1/1       Running   0          3m
po/my-deploy-2287124240-jnm4k   1/1       Running   0          3m
po/my-deploy-2287124240-mq7lj   1/1       Running   0          3m

NAME             CLUSTER-IP    EXTERNAL-IP     PORT(S)          AGE
svc/kubernetes   10.0.0.1      <none>          443/TCP          11h
svc/my-svc       10.0.166.57   13.92.224.176   8080:31786/TCP   4m

NAME               DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deploy/my-deploy   3         3         3            3           3m

NAME                      DESIRED   CURRENT   READY     AGE
rs/my-deploy-2287124240   3         3         3         3m

```

# Deploying Clusters

## ACS-Engine

### Install ACS-Engine
1. Download the ACS-Engine [Binaries](https://github.com/Azure/acs-engine/releases/tag/v0.11.0)

For Linux x64
```bash
cd ~
wget https://github.com/Azure/acs-engine/releases/download/v0.11.0/acs-engine-v0.11.0-linux-amd64.tar.gz
```

2. Untar the file

```bash
cd ~
tar -xvzf acs-engine-v0.11.0-linux-amd64.tar.gz
```

3. Move the ace-engine binary to path

```bash
cd ~/acs-engine-v0.11.0-linux-amd64
sudo mv acs-engine /usr/local/bin
```
4. Test ACS-Engine

```bash
acs-engine

ACS-Engine deploys and manages Kubernetes, Swarm Mode, and DC/OS clusters in Azure

Usage:
  acs-engine [command]

Available Commands:
  deploy        deploy an Azure Resource Manager template
  generate      Generate an Azure Resource Manager template
  help          Help about any command
  orchestrators provide info about supported orchestrators
  scale         scale a deployed cluster
  upgrade       upgrades an existing Kubernetes cluster
  version       Print the version of ACS-Engine

Flags:
      --debug   enable verbose debug logs
  -h, --help    help for acs-engine

Use "acs-engine [command] --help" for more information about a command.
```

### Use ACS-Engine to create a cluster

1. Get the kubernetes api model

```bash
cd ~
wget https://raw.githubusercontent.com/Azure/acs-engine/fc56e540144aad66baf769446d1d87ebc86e0911/examples/kubernetes.json
```

2. Create cluster using ACS-Engine CLI

```bash
acs-engine deploy --subscription-id e729c299-db43-40ce-991a-7e4572a69d50 \
    --dns-prefix livedemosogeti --location westus2 \
    --auto-suffix --api-model kubernetes.json
```

Output
```bash
WARN[0001] To sign in, use a web browser to open the page https://aka.ms/devicelogin and enter the code <YourCode> to authenticate.
WARN[0073] apimodel: missing masterProfile.dnsPrefix will use "livedemosogeti-5a5e50c9"
WARN[0073] --resource-group was not specified. Using the DNS prefix from the apimodel as the resource group name: livedemosogeti-5a5e50c9
WARN[0080] apimodel: ServicePrincipalProfile was missing or empty, creating application...
WARN[0081] created application with applicationID (244bc649-3e14-437a-bcff-88e056eb21c4) and servicePrincipalObjectID (0672a270-235c-4c5b-b00f-ae6a70012f11).
WARN[0081] apimodel: ServicePrincipalProfile was empty, assigning role to application...
INFO[0109] Starting ARM Deployment (livedemosogeti-5a5e50c9-276076987). This will take some time...
INFO[0468] Finished ARM Deployment (livedemosogeti-5a5e50c9-276076987).
```

Check out _output directory to get the binaries compiled

```bash
cd _output
ls -alh
total 244K
drwx------ 0 ali ali  512 Jan 16 11:34 .
drwx------ 0 ali ali  512 Jan 16 11:21 ..
-rw------- 1 ali ali  28K Jan 16 11:22 apimodel.json
-rw------- 1 ali ali 5.0K Jan 16 11:22 apiserver.crt
-rw------- 1 ali ali 3.2K Jan 16 11:22 apiserver.key
-rw------- 1 ali ali 136K Jan 16 11:22 azuredeploy.json
-rw------- 1 ali ali  39K Jan 16 11:22 azuredeploy.parameters.json
-rw------- 1 ali ali 3.2K Jan 16 11:21 azureuser_rsa
-rw------- 1 ali ali 1.7K Jan 16 11:22 ca.crt
-rw------- 1 ali ali 3.2K Jan 16 11:22 ca.key
-rw------- 1 ali ali 1.8K Jan 16 11:22 client.crt
-rw------- 1 ali ali 3.2K Jan 16 11:22 client.key
drwx------ 0 ali ali  512 Jan 16 11:22 kubeconfig
-rw------- 1 ali ali 1.8K Jan 16 11:22 kubectlClient.crt
-rw------- 1 ali ali 3.2K Jan 16 11:22 kubectlClient.key
```
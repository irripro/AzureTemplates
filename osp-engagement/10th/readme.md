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
    --dns-prefix livedemo11th --location westus2 \
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

# Live Demo Second Session

## Access the Dash Board

1. Ensure the correct ```~/.kube/config``` file is present
2. Run ```kubectl proxy```
3. Navigate to the browser and run ```http://localhost:8001/ui```

## To Install Helm locally

1. Bring up the container by running ```docker run -it alihhussain/azurepublic:301Base```
2. [Download](https://github.com/kubernetes/helm/archive/v2.8.0-rc.1.tar.gz) the helm binaries by running the following command ``` wget https://storage.googleapis.com/kubernetes-helm/helm-v2.8.0-rc.1-linux-amd64.tar.gz```
3. Untar the file by running: ```tar -zxvf helm-v2.8.0-rc.1-linux-amd64.tar.gz```
4. Move the helm binary to PATH by running: ```sudo mv ./linux-amd64/helm /usr/local/bin/helm```
5. Check to see if helm is executable by running: 
```bash
helm
The Kubernetes package manager

To begin working with Helm, run the 'helm init' command:

        $ helm init

This will install Tiller to your running Kubernetes cluster.
It will also set up any necessary local configuration.
...
```
6. Check helm install correctly by running:
```bash
helm version
Client: &version.Version{SemVer:"v2.8.0-rc.1", GitCommit:"e1027fae732034e0390f5cd231c6116e63b75aa2", GitTreeState:"clean"}
Error: cannot connect to Tiller
```
The error message comes in if the kubectl config file is not installed

## Install Helm on Cluster
1. Verify kubectl config file is correct
2. Verify tiller application is not running via: ```kubectl get pods --namespace kube-system```
3. Install Helm Tiller by running: ```helm init```
4. Verify Tiller application is running on the cluster by running: 
```bash
kubectl get pods --namespace kube-system
AME                                    READY     STATUS    RESTARTS   AGE
heapster-342135353-j69qx                2/2       Running   0          2d
kube-dns-v20-1654923623-rwq3b           3/3       Running   0          2d
kube-dns-v20-1654923623-zdwkc           3/3       Running   0          2d
kube-proxy-54vw1                        1/1       Running   0          2d
kube-proxy-6pf9m                        1/1       Running   0          2d
kube-proxy-6wq07                        1/1       Running   0          2d
kube-proxy-84xf8                        1/1       Running   0          2d
kube-svc-redirect-71qjl                 1/1       Running   0          2d
kube-svc-redirect-g9vqk                 1/1       Running   0          2d
kube-svc-redirect-h3nt7                 1/1       Running   0          2d
kube-svc-redirect-tsrrr                 1/1       Running   0          2d
kubernetes-dashboard-1672970692-k40fl   1/1       Running   0          2d
tiller-deploy-2114845795-kss9d          1/1       Running   0          11h
tunnelfront-3436842133-2kt5c            1/1       Running   0          2d
```

# Deploy a sample elasticSearch Helm Chart

1. Add incubator repo
```bash
helm repo add incubator http://storage.googleapis.com/kubernetes-charts-incubator
```
2. Deploy helm chart by:
```bash
helm install --name my-release incubator/elasticsearch
```
3. Follow the instructions and run the following commands
```bash
export POD_NAME=$(kubectl get pods --namespace default -l "app=elasticsearch,component=client,release=my-release" -o jsonpath="{.items[0].metadata.name}")
echo "Visit http://127.0.0.1:9200 to use Elasticsearch"
```
4. Test if the Elasticsearch application is running by:
```bash
kubectl port-forward --namespace default $POD_NAME 9200:9200
```
5. Visit ```http://localhost:9200``` to insure the elasticsearch applicaiton is indeed running in the cluster.

### Check out Helm deployment binaries

Sample Chart Binaries on Git:
* [ElasticSearch](https://github.com/kubernetes/charts/tree/master/incubator/elasticsearch)
* [Nginx](https://github.com/kubernetes/helm/tree/master/docs/examples/nginx)

Binaries on the filesystem
1. Go to the folder inside of your home directory
```bash
cd ~/.helm/cache/archive/
ls -alh
total 24K
drwxr-xr-x 0 ali ali  512 Jan 17 23:33 .
drwxr-xr-x 0 ali ali  512 Jan 17 23:15 ..
-rw-r--r-- 1 ali ali 9.0K Jan 17 23:33 elasticsearch-0.4.6.tgz
-rw-r--r-- 1 ali ali  12K Jan 17 23:26 jenkins-0.12.0.tgz
```
2. untar the files
```bash
tar -zxvf elasticsearch-0.4.6.tgz
cd ./elasticsearch/
ls -alh
total 20K
drwxrwxrwx 0 ali ali  512 Jan 18 11:37 .
drwxr-xr-x 0 ali ali  512 Jan 18 11:37 ..
-rwxr-xr-x 1 ali ali  638 Dec 31  1969 Chart.yaml
-rwxr-xr-x 1 ali ali  11K Dec 31  1969 README.md
drwxrwxrwx 0 ali ali  512 Jan 18 11:37 templates
-rwxr-xr-x 1 ali ali 2.2K Dec 31  1969 values.yaml
```
# Logging and Monitoring Cluster

### Create a Log Analytics Workspace
1. Create a workspace by following directions on [this link](https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-quick-create-workspace)
2. Fetch and note down the Workspace ID and Key
```bash
Sample:
Workspace ID: 88361439-79ec-4690-be15-c9f50c294438
Workspace Key: jf5qEA6SkEMmz6tcA5rc
```

### Log Analytics Workspace Setup for K8s (Following Instructions on this [link](https://github.com/Microsoft/OMS-docker/tree/master/Kubernetes))
1. Fetch the yaml deploy file
```bash
wget https://raw.githubusercontent.com/Microsoft/OMS-docker/master/Kubernetes/omsagent.yaml
```
2. Modify the downloaded file and replace <WSID> and <KEY> values with yours
```bash
vim omsagent.yaml
apiVersion: extensions/v1beta1
kind: DaemonSet
metadata:
 name: omsagent
spec:
 template:
  metadata:
   labels:
    app: omsagent
    agentVersion: 1.4.0-12
    dockerProviderVersion: 10.0.0-25
  spec:
   containers:
     - name: omsagent
       image: "microsoft/oms"
       imagePullPolicy: Always
       env:
       - name: WSID
         value: <WSID>
       - name: KEY
         value: <KEY>
       securityContext:
```
3. Run the command to deploy the template: ```kubectl create -f omsagent.yaml```
4. Run the following command to see the status of pods:
```bash
watch kubectl get all
Every 2.0s: kubectl get all                                                                                                                                                 Thu Jan 18 11:59:49 2018

NAME                            READY     STATUS    RESTARTS   AGE
po/my-deploy-2287124240-48pdl   1/1       Running   0          19h
po/my-deploy-2287124240-9snh9   1/1       Running   0          19h
po/my-deploy-2287124240-txskz   1/1       Running   0          1d
po/omsagent-6cmjl               1/1       Running   0          1m
po/omsagent-7wl6g               1/1       Running   0          1m
po/omsagent-nl11n               1/1       Running   0          1m
po/omsagent-x7z3d               1/1       Running   0          1m

NAME             CLUSTER-IP    EXTERNAL-IP      PORT(S)          AGE
svc/kubernetes   10.0.0.1      <none>           443/TCP          2d
svc/my-svc       10.0.168.79   52.191.212.139   8080:31789/TCP   1d

NAME               DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deploy/my-deploy   3         3         3            3           1d

NAME                      DESIRED   CURRENT   READY     AGE
rs/my-deploy-2287124240   3         3         3         1d
```

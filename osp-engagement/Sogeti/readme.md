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


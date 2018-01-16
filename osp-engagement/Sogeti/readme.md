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
3. Copy downloaded file inside of ```~/.kube/```
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
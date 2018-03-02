# Random Notes and Useful Commands


Get info on Nodes Running: ```kubectl get nodes```

Get info on Pods Running: ```kubectl get pods```

Get info on Services Running: ```kubectl get services```

Get detailed info on Nodes Running: ```kubectl describe nodes```

Get detailed on Pods Running: ```kubectl describe pods```

Get detailed on Services Running: ```kubectl describe services```

Sample config file (YAML)
```YAML
apiVersion: v1
kind: Pod
metadata:
    name: nginx
spec:
    containers:
    - name: nginx
      image: nginx:1.7.9
      ports:
      - containerPort: 80
```
Start Pod with sample config file: ```kubectl create -f nginx.yaml```

Start a pod from command line:  ```kubectl run busybox --image=busybox --restart=Never --tty -i --generator=run-pod/v1 ```

To test the running box: ```wget -qO- http://10.244.0.8```

To Delete a pod: ```kubectl delete pod busybox```

To expose a port on a running pod: ```kubectl port-forward service <Hostport>:<ContainerPort>``` 
+ As an example: ```kubectl port-forward nginx 8008:80```

Sample Config file with Label (YAML)
```YAML
apiVersion: v1
kind: Pod
metadata:
    name: nginx
    labels:
        app: nginx
spec: 
    containers:
    - name: nginx
      image: nginx:1.7.9
      ports:
      - containerPort: 80
```

To get pods with a specific label: ```kubectl get pods -l app=nginx```

To describe pods with a specific label: ```kubectl describe -l app=nginx```

Sample config file for deployment (YAML)
```YAML
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-deployment-prod
spec:
  replicas: 1
  template: 
    metadata:
      labels:
        app: nginx-deployment-prod
    spec: 
      containers:
      - name: nginx-deployment-prod
        image: nginx:1.7.9
        ports:
        - containerPort: 80
```

To deploy a deployment via config file: ```kubectl create -f nginx-deployment-prod```

To get deployments: ```kubectl get deployments```

To get all deployments: ```kubectl get deployments --show-all```

To get deployments with a specific label: ```kubectl get deployments -l app=nginx-deployment-prod```

To describe a specific deployment: ```kubectl describe deployments -l app=nginx-deployment-dev```

Sample **update** config file for deployment(YAML)
```YAML
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-deployment-dev
spec:
  replicas: 1
  template: 
    metadata:
      labels:
        app: nginx-deployment-dev
    spec: 
      containers:
      - name: nginx-deployment-dev
        image: nginx:1.8
        ports:
        - containerPort: 80
```
To apply an update to an existing deployment: ```kubectl apply -f nginx-deployment-dev-update.yaml```

Sample replica-controller config file (YAML)
```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx-www
spec:
  replicas: 2
  selector: 
    app: nginx
  template:
    metadata:
      name: nginx
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
```

To deploy a replication Controller: ```kubectl create -f nginx-multi.yaml```

To get replication controller: ```kubectl get rc```

To delete a replication controller ```kubectl delete rc nginx-www```

Sample service config file (YAML)
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  ports:
  - port: 8000
    targetPort: 80
    protocol: TCP
  selector: 
    app: nginx
```

To deploy a service: ```kubectl create -f nginx-service.yaml```

To get services: ```kubectl get svc```
```shell
$ kubectl get svc
NAME            CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
kubernetes      10.0.0.1       <none>        443/TCP    3d
nginx-service   10.0.138.251   <none>        8000/TCP   3m
```

To test service: ```wget -qO- 10.0.0.138.251:8000```

To describe service deployed: ```kubectl describe svc nginx-service```

To run temp pods from command line: ```kubectl run mysample --image=latest123/apache```

To delete a running deployment: ```kubectl delete deployment mysample```

To run multiple read replicas of a pod with labels: ```kubectl run myreplicas --image=latest123/apache --replicas=2 --labels=app=myapache,version=1.0```

To run a specific command on a pod: ```kubectl exec myapache hostname```

To run a specific command on a specific pod: ```kubectl exec myapache -c <CID> hostname```

To interactively attach to a pod (without using kubectl attach): ```kubectl exec myapache -it -- /bin/bash```

To get logs from a running pod with 1 container: ```kubectl logs myapache```

To tail the logs from a container: ```kubectl logs --tail=1 myapache```

To show logs for the previous N time: ```kubectl logs --since=(1s/1m/1h/1d) myapache```

To follow the logs on a specific pod: ```kubectl logs -f myapache```

To follow logs of a spcific pod: ```kubectl -f -c CID myapache```

Run run a pod image from commandline: ```kubectl run myautoscale --image=latest123/apache --port=80 --labels=app=myautoscale```

To apply a autoscaling policy to a deployment: ```kubectl autoscale deployment myautoscale --min=2 --max=6```

To modify an existing autoscaling policy: ```kubectl scale --current-replicas=2 --replicas=4 deployment/myautoscale```

Important Note:   
*   Once a pod is instantiated on a node it will stay there until it is deleted
    * Meaning once a pod on a host goes down. it will **not** be moved over to another node.
    * **If the node goes down all the pods running on the node will be down and they will not come up on the other nodes**
    * **Once a node comes back up the deployed pods will come back up. Nothing will be redeployed**
    * **This means its important to keep track of node health so that deployments/pods can be scaled out incase of failure to nodes**
    
   
=======
# Kubernetes Needed!
These are the items you should consider before taking a cluster into production:
*   Nodes Architecture (Networking)
*   Backup etcd in Master (censo to monitor)
*   Monitoring to detect failure on Master
    *    Once detected, automation to failover master node
*    Monitoring to scale up/down cluster
    *    Automation to scale up/down cluster
    *    Manual / ACI
*    Blue/Green Deployment procedure
*    Monitoring Nodes (Patch/Performance/Security)
*    Container Log Monitoring
*   Persistent Storage layer
*   Demistfy ACS Magic
    *   What is ACS doing?
    *   What components is it configuring
    *   Limitations
*   DevOps how to deploy
*   Diaster Recovery & High Avalibility of nodes in cluster
*   Training
    *   Increase competency across customer/partner operational and development team

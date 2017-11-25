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

To interactively attach to a pod (without using kubectl attach): ```kubectle exec myapache -it -- /bin/bash```


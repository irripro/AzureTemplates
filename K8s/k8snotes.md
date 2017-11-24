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

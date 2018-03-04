from flask import Flask, request, render_template
from fabric.api import local
import os

runtime = str("None")
try:
    k8s_node_name = str(os.environ['MY_NODE_NAME'])
    k8s_pod_name = str(os.environ['MY_POD_NAME'])
    k8s_pod_namespace = str(os.environ['MY_POD_NAMESPACE'])
    k8s_pod_ip = str(os.environ['MY_POD_IP'])
    k8s_serviceaccount_name = str(os.environ['MY_POD_SERVICE_ACCOUNT'])
    runtime = str("Kubernetes")
except:
    runtime = str("Docker")
IP_output = str(local("""ip -o -4 a | awk '$2 == "eth0" { gsub(/\/.*/, "", $4); print $4 }'""", capture=True))
ID_output = str(local("""cat /proc/self/cgroup | head -n 1 | cut -d '/' -f3""", capture=True))

app = Flask(__name__)

@app.route('/')
def hello_world():
    if 'docker' in runtime.lower():
        return render_template("docker_index.html", container_IP=IP_output, container_ID=ID_output)
    else:
        return render_template("k8s_enhance_index.html", k8s_node_name=k8s_node_name, k8s_pod_name=k8s_pod_name, k8s_pod_namespace=k8s_pod_namespace, k8s_pod_ip=k8s_pod_ip, k8s_serviceaccount_name=k8s_serviceaccount_name)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)

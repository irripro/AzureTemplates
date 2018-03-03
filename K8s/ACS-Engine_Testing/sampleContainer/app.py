from flask import Flask, request, render_template
from fabric.api import local

app = Flask(__name__)

IP_output = str(local("""ip -o -4 a | awk '$2 == "eth0" { gsub(/\/.*/, "", $4); print $4 }'""", capture=True))
ID_output = str(local("""cat /proc/self/cgroup | head -n 1 | cut -d '/' -f3""", capture=True))

@app.route('/')
def hello_world():
    return render_template("docker_index.html", container_IP=IP_output, container_ID=ID_output)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)

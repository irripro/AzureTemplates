from flask import Flask, request, render_template
from fabric.api import local

app = Flask(__name__)

output = str(local("""ip -o -4 a | awk '$2 == "eth0" { gsub(/\/.*/, "", $4); print $4 }'""", capture=True))

@app.route('/')
def hello_world():
    return render_template("index.html", container_IP=output)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)

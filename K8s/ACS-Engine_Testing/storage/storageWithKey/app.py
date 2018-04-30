from flask import Flask, request, render_template
from fabric.api import local
import os

storageKey = "Some Value"

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("k8s_index.html", k8s_key=storageKey)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)

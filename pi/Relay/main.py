from flask import Flask, request, render_template
import os
import random
import socket
import sys
import pymongo

app = Flask(__name__)

# Load configurations
app.config.from_pyfile('config_file.cfg')
title =         app.config['TITLE']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html", title=title)

    elif request.method == 'POST':
        print("Button Value is %s " %request.form)
#        if request.form['red'] == "ON":
#            return render_template("index.html", title=title)
#        elif request.form['red'] == "OFF":
#            return render_template("index.html", title=title)
#        elif request.form['yellow'] == "OFF":
        return render_template("index.html", title=title)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=5000)

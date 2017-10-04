from flask import Flask, request, render_template
import os
import random
import socket
import sys
import pprint
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
        response = request.form.to_dict()
        try: 
            if response['red'] == "ON":
                print("RED ON.")
            elif response['red'] == "OFF":
                print("RED OFF.")
        except:
            pass
        try:    
            if response['yellow'] == "ON":
                print("YELLOW ON.")
            elif response['yellow'] == "OFF":
                print("YELLOW OFF.")
        except:
            pass
        return render_template("index.html", title=title)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=5000)

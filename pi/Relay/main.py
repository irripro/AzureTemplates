from flask import Flask, request, render_template
import os
import random
import socket
import sys
import pymongo

app = Flask(__name__)
global button1value, button2value

# Load configurations
app.config.from_pyfile('config_file.cfg')
button1 =       app.config['VOTE1VALUE']  
button2 =       app.config['VOTE2VALUE']
title =         app.config['TITLE']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        button1value = "OFF"
        button2value = "OFF"
        return render_template("index.html", button1=button1, button2=button2, button1value=button1value, button2value=button2value, title=title)

    elif request.method == 'POST':
        if request.form['red'] == button1:
            print(request.form['red'])
            button1value = "OFF"
            button2value = "OFF"
#            if button1value == "OFF":
#                button1value = "ON"
#            elif butt1value == "ON":
#                butt1value = "OFF"
            return render_template("index.html", button1=button1, button2=button2, button1value=button1value, button2value=button2value, title=title)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=5000)

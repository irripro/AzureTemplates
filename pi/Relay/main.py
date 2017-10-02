from flask import Flask, request, render_template
import os
import random
import socket
import sys
import pymongo

app = Flask(__name__)

# Load configurations
app.config.from_pyfile('config_file.cfg')
button1 =       app.config['VOTE1VALUE']  
button2 =       app.config['VOTE2VALUE']
title =         app.config['TITLE']
title1 =         app.config['TITLE1']
title2 =         app.config['TITLE2']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html", button1=button1, button2=button2, title=title, title1=title1,title2=title2, message="You have just started")

    elif request.method == 'POST':

        if request.form['red'] == button1:
            return render_template("index.html", button1=button1, button2=button2, title=title, title1=title1,title2=title2, message="You have chosen red ON.")
        elif request.form['red'] == button2:
            return render_template("index.html", button1=button1, button2=button2, title=title, title1=title1,title2=title2, message="You have chosen red OFF.")
            
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=5000)

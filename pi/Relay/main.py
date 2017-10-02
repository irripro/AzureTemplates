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
        # Return index 
        return render_template("index.html", button1=button1, button2=button2, button3=button3, button4=button4, title=title, title1=title1,title2=title2)

    elif request.method == 'POST':

        if request.form['vote'] == 'reset':
            return render_template("index.html", button1=button1, button2=button2, button3=button3, button4=button4, title=title, title1=title1,title2=title2)
        elif request.form['vote'] == button1:
            return render_template("index.html", button1=button1, button2=button2, button3=button3, button4=button4, title=title, title1=title1,title2=title2)
        elif request.form['vote'] == button2:
            return render_template("index.html", button1=button1, button2=button2, button3=button3, button4=button4, title=title, title1=title1,title2=title2)
            
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=5000)

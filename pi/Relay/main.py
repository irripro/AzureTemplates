from flask import Flask, request, render_template
import RPi.GPIO as GPIO
from GenericCache.GenericCache import GenericCache

GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.output(7,GPIO.HIGH)
GPIO.output(11,GPIO.HIGH)

global redvalue, yellowvalue

cache = GenericCache()
app = Flask(__name__)
cache.insert("red", "OFF")
cache.insert("yellow", "OFF")

# Load configurations
app.config.from_pyfile('config_file.cfg')
title =         app.config['TITLE']

def red(turnon):
    if turnon == True:
        GPIO.output(7,GPIO.LOW)
    elif turnon == False:
        GPIO.output(7,GPIO.HIGH)
    return

def yellow(turnon):
    if turnon == True:
        GPIO.output(11,GPIO.LOW)
    elif turnon == False:
        GPIO.output(11,GPIO.HIGH)
    return

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html", redvalue=cache.fetch('red'), yellowvalue=cache.fetch('yellow'), title=title)

    elif request.method == 'POST':
        response = request.form.to_dict()
        try: 
            if response['red'] == "ON":
                red(False)
                cache.insert("red", "OFF")
            elif response['red'] == "OFF":
                red(True)
                cache.insert("red", "ON")
        except:
            pass
        try:    
            if response['yellow'] == "ON":
                yellow(False)
                cache.insert("yellow", "OFF")
            elif response['yellow'] == "OFF":
                yellow(True)
                cache.insert("yellow", "ON")
        except:
            pass
        return render_template("index.html", redvalue=cache.fetch('red'), yellowvalue=cache.fetch('yellow'), title=title)

@app.route('/red/<action>')
def redaction(action):
    try:
        if 'on' in action.lower():
            red(True)
            cache.insert("red", "ON")
        elif 'off' in action.lower():
            red(False)
            cache.insert("red", "OFF")
    except:
        pass
    return render_template("index.html", redvalue=cache.fetch('red'), yellowvalue=cache.fetch('yellow'), title=title)

@app.route('/yellow/<action>')
def yellowaction(action):
    try:
        if 'on' in action.lower():
            yellow(True)
            cache.insert("yellow", "ON")
        elif 'off' in action.lower():
            yellow(False)
            cache.insert("yellow", "OFF")
    except:
        pass
    return render_template("index.html", redvalue=cache.fetch('red'), yellowvalue=cache.fetch('yellow'), title=title)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=80)
#    app.run(host='0.0.0.0',ssl_context='adhoc', port=443)

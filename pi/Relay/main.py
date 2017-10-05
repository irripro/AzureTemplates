from flask import Flask, request, render_template

app = Flask(__name__)

global redvalue, yellowvalue
redvalue = "OFF"
yellowvalue = "OFF"

# Load configurations
app.config.from_pyfile('config_file.cfg')
title =         app.config['TITLE']


@app.route('/', methods=['GET', 'POST'])
def index():
    global redvalue, yellowvalue 
    if request.method == 'GET':
        return render_template("index.html", redvalue=redvalue, yellowvalue=yellowvalue, title=title)

    elif request.method == 'POST':
        response = request.form.to_dict()
        try: 
            if response['red'] == "ON":
                redvalue = "OFF"                
            elif response['red'] == "OFF":
                redvalue = "ON" 
        except:
            pass
        try:    
            if response['yellow'] == "ON":
                yellowvalue = "OFF"
            elif response['yellow'] == "OFF":
                yellowvalue = "ON"
        except:
            pass
        return render_template("index.html", redvalue=redvalue, yellowvalue=yellowvalue, title=title)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=5000)

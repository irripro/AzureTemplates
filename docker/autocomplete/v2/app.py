# Reference Cities from: http://www.citymayors.com/statistics/largest-cities-population-125.html
# Code inspired by: https://github.com/salmanarshad2000/demos/blob/v1.0.0/jquery-ui-autocomplete/highlight-matched-text.html

from flask import Flask, Response, render_template, request
import json
from wtforms import TextField, Form

app = Flask(__name__)

class SearchForm(Form):
    autocomp = TextField('Guess country and find out how its ranked in the world by population', id='country_autocomplete')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    return render_template("country.html", form=form)

if __name__ == '__main__':
    app.run('0.0.0.0',ssl_context=('/root/autocomplete/cert1.pem', '/root/autocomplete/privkey1.pem'), port=443)

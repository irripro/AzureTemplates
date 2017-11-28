# Reference Cities from: http://www.citymayors.com/statistics/largest-cities-population-125.html
# Code inspired by: https://github.com/salmanarshad2000/demos/blob/v1.0.0/jquery-ui-autocomplete/highlight-matched-text.html

from flask import Flask, Response, render_template, request
import json
from wtforms import TextField, Form
import urllib2
import ssl

app = Flask(__name__)
context = ssl._create_unverified_context()
response = urllib2.urlopen('https://raw.githubusercontent.com/BestBuyAPIs/open-data-set/master/products.json', context=context)

products = response.read()
jproduct = json.loads(products)
productnames = []

for p in jproduct:
    productnames.append(p['name'])

class SearchForm(Form):
    autocomp = TextField('Product', id='product_autocomplete')

@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
    return Response(json.dumps(productnames[:5000]), mimetype='application/json')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    return render_template("products.html", form=form)

if __name__ == '__main__':
#    app.run('0.0.0.0', port=80)
    app.run('0.0.0.0',ssl_context=('/root/autocomplete/cert1.pem', '/root/autocomplete/privkey1.pem'), port=443)

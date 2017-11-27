# Reference Cities from: http://www.citymayors.com/statistics/largest-cities-population-125.html
# Code inspired by: https://github.com/salmanarshad2000/demos/blob/v1.0.0/jquery-ui-autocomplete/highlight-matched-text.html

from flask import Flask, Response, render_template, request
import json
from wtforms import TextField, Form

app = Flask(__name__)

cities = ["Tokyo,Japak (1)",
          "New York,USA (2)",
          "Sao Paulo,Brazil (3)",
          "Seoul,South Korea (4)",
          "Mexico City,Mexico (5)",
          "Osaka,Japan (6)",
          "Manila,Philippines (7)",
          "Mumbai,India (8)",
          "Delhi,India (9)",
          "Jakarta,Indonesia (10)",
          "Lagos, Nigeria (11)",
          "Kolkata,India (12)",
          "Cairo,Egypt (13)",
          "Los Angeles,USA (14)",
          "Buenos Aires,Argentina (15)",
          "Rio de Janeiro,Brazil (16)",
          "Moscow,Russia (17)",
          "Shanghai,China (18)",
          "Karachi,Pakistan (19)",
          "Paris,France (20)",
          "Istanbul,Turkey (21)",
          "Nagoya,Japan (22)",
          "Beijing,China (23)",
          "Chicago,USA (24)",
          "London, England (25)",
          "Shenzhen,China (26)",
          "Essen,Germany (27)",
          "Tehran,Iran (28)",
          "Bogota,Colombia (29)",
          "Lima,Peru (30)"
          ]


class SearchForm(Form):
    autocomp = TextField('Guess city and find out how its ranked in the world by population', id='city_autocomplete')


@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
    return Response(json.dumps(cities), mimetype='application/json')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    return render_template("city.html", form=form)

if __name__ == '__main__':
    app.run('0.0.0.0', port=80)

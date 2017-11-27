#!/usr/local/env python

from flask import Flask, redirect
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'], defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
# return 307 temp redirection to avoid POST calls to being tranformed to GET
    return redirect("https://autocomplete.cloudyprojects.com", code=307)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "THIS IS THE HOME PAGE"

@app.route('/tuna')
def tuna():
    return "<h2>Tuna is good</h2>"

@app.route('/action/<todo>')
def action(todo):
    if 'still' in todo.lower():
        return "<h2>You have asked to take a picture</h2>"
    elif 'video' in todo.lower():
        return "<h2>You have asked to take a video</h2>"
    else:
        return "<h2>Please ask either to take a picture or video</h2>"

@app.route('/post/<int:postid>')
def post(postid):
    return "<h2>The Post ID is: %s</h2>" %postid

@app.route("/bacon", methods=['GET','POST'])
def bacon():
    if request.method == 'POST':
        return "You are using the Post"
    else:
        return "You are probably using GET"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

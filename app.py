from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return " <p>Hello World</p>"

@app.route("/end")
def end(): 
    return "<h1>HELLO WORld this is THE END</h1>"

@app.route("/username/<name>")
def username(name):
    return f"<h2>{name}</h2>"
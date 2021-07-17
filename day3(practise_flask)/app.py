from flask import Flask;

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

@app.route("/<name>")
def index1(name):
    return f"Hello {name}"


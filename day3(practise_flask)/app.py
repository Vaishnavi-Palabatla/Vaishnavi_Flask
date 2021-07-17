from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    
    return "Hello world"

# @app.route("/<name>")
# def index(name):
#     return render_template("index.html",name=name)

@app.route("/<name>")
def index1(name):
    return render_template("index.html", name=name)

# @app.route("/logout1")
# def logout1():
#     return render_template("logout1.html")


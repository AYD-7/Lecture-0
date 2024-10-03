from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Hello, World!"

@app.route("/ayodeji")
def ayodeji():
    return "Welcome, Ayodeji!!!"

@app.route("/seun")
def seun():
    return "Welcome, Seun!!!"

@app.route("/<string:name>")
def welcome(name):
    name = name.capitalize()
    return f"<h1>Welcome, {name}!!!</h1>"

# Using HTML in Flask web application
@app.route("/")
def index():
    return render_template("index.html")

# Rendering a headline from Python into HTML
@app.route("/inner")
def inner():
    headline = "Welcome, User!!!"
    return render_template("index.html", headline=headline)

# Setting conditions in Flask


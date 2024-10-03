import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

# Using conditions in flask
@app.route("/birthday")
def birthday():
    now = datetime.datetime.now()
    my_birthday = now.month == 10 and now.day == 16
    return render_template("condition.html", my_birthday=my_birthday)

# Using Loop in flask
@app.route("/names")
def names():
    names = ["Ayodeji", "Babatunde", "Collins", "Daniel", "Ezekiel"]
    return render_template("loop.html", names=names)


# Using links in Flask
@app.route("/url")
def url():
    return render_template("url.html")
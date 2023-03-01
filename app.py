from flask import Flask, render_template, request
# from data import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contactus")
def contactus():
    return render_template("contactus.html")


@app.route("/top20")
def top20():
    return render_template("top20.html")

if __name__ == "__main__":
    app.run(debug=True)
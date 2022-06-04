import sqlite3
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("pages/home/home.html")


@app.route('/class/')
def classRoom():
    return render_template('pages/class/class.html')


if(__name__ == "__main__"):
    app.run(debug=True)

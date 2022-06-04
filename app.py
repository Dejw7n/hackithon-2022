import sqlite3
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("base.html", page="")


@app.route('/class/')
def classRoom():
    return render_template('base.html', page="class")


if(__name__ == "__main__"):
    app.run(debug=True)

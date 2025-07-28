#!/usr/bin/python3
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    texter = escape(text).replace("_", " ")
    return f"C {texter}"


@app.route("/python/", defaults={"text": "is cool"},
           strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_fun(text="is cool"):
    texter = escape(text).replace("_", " ")
    return f"Python {texter}"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

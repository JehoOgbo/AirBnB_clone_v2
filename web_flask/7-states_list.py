#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_app_context
def teardown():
    """call close method after every request"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ list all states"""
    list_state = storage.all('State')
    return render_template("7-states_list.html", lister=list_state)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

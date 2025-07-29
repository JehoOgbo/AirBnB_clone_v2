#!/usr/bin/python3
"""starts a web app for airbnb_clone"""

from flask import Flask
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

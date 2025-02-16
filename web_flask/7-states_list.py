#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return f'Hello HBNB!'


@app.teardown_appcontext
def close(exception):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    return render_template('7-states_list.html',
                           states=storage.all(State).values())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

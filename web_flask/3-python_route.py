#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return f'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    return f'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    return f'C {text.replace("_", " ")}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>')
def hello_python(text):
    return f'Python {text.replace("_", " ")}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

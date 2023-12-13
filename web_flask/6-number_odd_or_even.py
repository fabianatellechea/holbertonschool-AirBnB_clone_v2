#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def hello_n(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def hello_html(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    if n % 2 == 0:
        evenodd = 'even'
    else:
        evenodd = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, evenodd=evenodd)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

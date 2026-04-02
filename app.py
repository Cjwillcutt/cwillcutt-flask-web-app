# module 11 - Flask Application
# Chris Willcutt 03/31/2026

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!!"


@app.route("/chris")
def chris():
    x = 6
    y = 15
    z = x + y
    name = "chris"
    return f"Hello {name}, the sum of {x} and {y} is {z}!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)

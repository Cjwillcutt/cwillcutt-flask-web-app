# module 11 - Flask Application
# Chris Willcutt 03/31/2026

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)

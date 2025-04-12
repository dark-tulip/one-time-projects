import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    greeting = os.getenv("HELLO_MESSAGE", "Hello from Python!")
    return f"<h2>{greeting}</h2>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

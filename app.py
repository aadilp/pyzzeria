from flask import Flask


app = Flask(__name__)


@app.route("/", methods=["GET"])
def get():
    return "OK"


@app.route("/", methods=["POST"])
def post():
    return "OK"

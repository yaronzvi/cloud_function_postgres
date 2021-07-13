import flask

import main


app = flask.Flask(__name__)


@app.route("/")
def index():
    return main.insert(flask.request)
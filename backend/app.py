from flask import Flask, make_response
from bson.json_util import dumps

from db import Database

app = Flask(__name__)


@app.route("/")
def index():
    resp = make_response("This is home page.")
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


@app.route("/restaurants")
def list_restaurants():
    db = Database()
    db.insert_random_data()

    results = list()
    for result in db.text_search("higgin"):
        results.append(result)

    resp = make_response(dumps(results))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

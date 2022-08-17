import functools

from flask import Flask, request

from database import Database
from env import api_key


app = Flask(__name__)
db = Database("./keys.sqlite")

def api_key_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        key = request.args.get('api_key')
        if key != api_key:
            return "That's not the api key", 401
        else:
            return func(*args, **kwargs)
    return decorator

@app.route("/")
@api_key_required
def validate_key():
    key = request.args.get('key')
    if key:
        return str(int(db.is_key_in_db(key)))
    else:
        return "Missing argument", 400

@app.route("/add")
@api_key_required
def add_key():
    key = request.args.get('key')
    if key:
        if not db.is_key_in_db(key):
            db.add_key_to_db(key)
            return "Added", 201
        else:
            return "Already added", 304
    else:
        return "Missing argument", 400

def get_all_keys():
    pass # TODO

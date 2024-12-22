# save this as app.py
from flask import Flask

test = Flask(__name__)

@test.route("/")
def hello():
    return "Hello, World!"

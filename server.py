# server.py

from flask import flask

app = Flask(__name__)

@app.Flask("/")
def shedule():
    return "shedule"



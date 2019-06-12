# __init__.py 
# init Flask server

from flask import Flask
#from schedule.model import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    #db.init_app(app)
    @app.route("/")
    @app.route("/index/")
    def schedule():
        return 'schedule'
    return app



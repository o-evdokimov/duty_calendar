# __init__.py 
# init Flask server

from flask import Flask
#from config import Configuration
#from schedule.model import db


def create_app():
    #from config import Configuration
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    #app.config.from_object(Configuration)
    #db.init_app(app)
    @app.route("/")
    @app.route("/index/")
    def schedule():
        return 'schedule2'
    return app



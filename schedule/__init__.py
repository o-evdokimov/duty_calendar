# __init__.py 
# init Flask server

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.pyxx')
    @app.route("/")
    def schedule():
        return 'schedule'
    return app



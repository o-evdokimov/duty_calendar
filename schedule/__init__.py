from flask import Flask, render_template
from schedule.model import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/smeny")
    def smeny():
        return render_template('smeny.html')
    return app



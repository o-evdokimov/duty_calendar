from flask import Flask, render_template
from flask_migrate import Migrate
from schedule.model import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route("/")
    def index():
        title = "Рабочий календарь"
        return render_template('index.html', title = title)

    @app.route("/smeny")
    def smeny():
        title = "Смены дежурств"
        return render_template('smeny.html', title = title)
    return app



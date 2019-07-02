from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager,current_user, login_required
from flask_migrate import Migrate


from schedule.db import db
from schedule.admin.views import blueprint as admin_blueprint
from schedule.user.models import Person,Role,Roleperson
from schedule.user.views import blueprint as user_blueprint



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)


    @login_manager.user_loader
    def load_user(user_id):
        return Person.query.get(user_id)

    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/smeny")
    def smeny():
        return render_template('smeny.html')
    
    

   
    
    return app


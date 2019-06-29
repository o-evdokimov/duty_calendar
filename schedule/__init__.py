from flask import Flask, render_template, flash, redirect, url_for
from flask.views import MethodView
from flask_migrate import Migrate
from schedule.model import db
from schedule.model import Person, Role, Timeinterval

from schedule.forms import LoginForm
from flask_login import LoginManager, login_user, logout_user, current_user


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config.from_pyfile('config_local.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return Person.query.get(user_id)

    @app.shell_context_processor
    def make_shell_context():
        return {'db':db, 'Person':Person, 'Role':Role}

    @app.route('/')
    def index():
        title = "Рабочий календарь"
        return render_template('index.html', title = title)

    @app.route('/smeny')
    def smeny():
        if current_user.is_authenticated:
            title = "Смены дежурств"
            return render_template('smeny.html', title = title)
        else:
            flash('Log in for access', 'alert-info')
            return redirect(url_for('login'))

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', title = title, form=login_form)

    @app.route('/logout')
    def logout():
        if current_user.is_authenticated:
            logout_user()
            flash('You are logged out', 'alert-secondary')
        else:
            flash('You are not logged in', 'alert-secondary')
        return redirect(url_for('login'))

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()

        if form.validate_on_submit():
            user = Person.query.filter(Person.username == form.login_name.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('You are logged in', 'alert-success')
                return redirect(url_for('index'))

        flash('Username or Password are invalid', 'alert-danger')
        return redirect(url_for('login'))

    return app


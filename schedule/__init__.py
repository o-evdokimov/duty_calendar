from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, current_user
from flask.views import MethodView
from flask_migrate import Migrate
from datetime import datetime


from schedule.user.models import Person
from schedule.user.views import blueprint as user_blueprint
from schedule.calendar.models import db
from schedule.calendar.models import Role, Dutytype, Timeinterval, Roleperson
from schedule.calendar.views import blueprint as calendar_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(user_blueprint)
    app.register_blueprint(calendar_blueprint)

    @app.route('/')
    def index():
        title = "Рабочий календарь"
        current_date = datetime.today()
        year = int(current_date.strftime('%Y'))
        month = int(current_date.strftime('%m'))
        return redirect(url_for('calendar.index',year_=year,month_=month)) 

    @login_manager.user_loader
    def load_user(user_id):
        return Person.query.get(user_id)

    @app.shell_context_processor
    def make_shell_context():
        return {'db':db, 'Person':Person, 'Role':Role, 'Dutytype':Dutytype, 'Timeinterval':Timeinterval, 'Roleperson':Roleperson}


    @app.template_filter('get_duty_person')
    def get_duty_person(duty_event,n):
        duty_persons = list()
        if not duty_event: 
            duty_persons =  '_is_empty_'
            return duty_persons
        for event in range(len(duty_event.all())):
                duty_persons.append((Person.query.filter_by(id=duty_event[event].duty_person_id))[0].username)
                
        try:
            return duty_persons[n]
        except IndexError:
            return '_is_empty_'

    return app


from flask_login import login_user, logout_user, current_user
from flask import Blueprint, render_template, flash, redirect, url_for
from datetime import datetime


from schedule.user.forms import LoginForm
from schedule.user.models import Person

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('login.html', title = title, form=login_form)

@blueprint.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('You are logged out', 'alert-secondary')
    else:
        flash('You are not logged in', 'alert-secondary')
    return redirect(url_for('user.login'))

@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Person.query.filter(Person.username == form.login_name.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('You are logged in as '+user.username, 'alert-secondary')
            year = int(datetime.today().strftime('%Y'))
            month = int(datetime.today().strftime('%m'))
            return redirect(url_for('calendar.index',year=2019,month=1))

    flash('Username or Password are invalid', 'alert-danger')
    return redirect(url_for('user.login'))

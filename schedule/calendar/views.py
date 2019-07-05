from flask_login import current_user
from flask import Blueprint, render_template, flash, redirect, url_for
from datetime import datetime


from schedule.calendar.models import Dutytype

blueprint = Blueprint('calendar', __name__, url_prefix='/calendar')

@blueprint.route('/')
def index():
    title = "Рабочий календарь"
    current_date = datetime.today().strftime('%d-%m-%Y')
    return render_template('index.html', title = title, date=current_date)

@blueprint.route('/smeny')
def smeny():
    if current_user.is_authenticated:
        title = "Смены дежурств"
        dutytypes = Dutytype.query.all()
        colors = ('btn btn-primary', 'btn btn-warning', 'btn btn-success', 'btn btn-secondary')
        new_dict = dict(zip(colors, dutytypes))

        print(new_dict)

        return render_template('smeny.html', title = title, dutytypes = dutytypes, new_dict = new_dict)
    else:
        flash('Log in for access', 'alert-info')
        return redirect(url_for('user.login'))

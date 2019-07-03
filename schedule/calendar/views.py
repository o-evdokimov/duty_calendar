from flask_login import current_user
from flask import Blueprint, render_template, flash, redirect, url_for


from schedule.calendar.models import Dutytype

blueprint = Blueprint('calendar', __name__, url_prefix='/calendar')

@blueprint.route('/')
def index():
    title = "Рабочий календарь"
    print(Dutytype.query.get("evd"))
    return render_template('index.html', title = title)

@blueprint.route('/smeny')
def smeny():
    if current_user.is_authenticated:
        title = "Смены дежурств"
        return render_template('smeny.html', title = title)
    else:
        flash('Log in for access', 'alert-info')
        return redirect(url_for('user.login'))

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
        len_dt = len(dutytypes) 
        shift = []
        time_interval = []
        role = []
        n=0
        for n in range(len_dt):
            dutytype = str(dutytypes[n]).split('_')
            shift.append(dutytype[0])
            time_interval.append(int(dutytype[1]))
            role.append(dutytype[2])
        color_btn = ['btn btn-primary', 'btn btn-warning', 'btn btn-success', 'btn btn-secondary']
        color_row = ['info', 'warning', 'success', 'active']
        #new_dict = dict(zip(colors, dutytypes))

        #print(new_dict)

        return render_template('smeny.html', color_btn = color_btn, color_row = color_row, title = title, shift=shift, time_interval=time_interval, role=role)
    else:
        flash('Log in for access', 'alert-info')
        return redirect(url_for('user.login'))

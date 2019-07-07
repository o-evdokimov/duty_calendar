from flask_login import current_user
from flask import Blueprint, render_template, flash, redirect, url_for
from datetime import datetime


from schedule.calendar.models import Dutytype, Timeinterval
from schedule.user.models import Person

blueprint = Blueprint('calendar', __name__, url_prefix='/calendar')

color_btn = ['primary', 'warning', 'success', 'secondary']
color_row = ['info', 'warning', 'success', 'active']

@blueprint.route('/')
def index():
    title = "Расписание"
    mydate = datetime.today()
    persons = Person.query.all()
    itslen = len(Dutytype.query.all())
    print('len=',type(itslen))
    return render_template('index.html', title = title, persons = persons, mydate=mydate, color_btn = color_btn, color_row = color_row, itslen = itslen)

@blueprint.route('/smeny')
def smeny():
    if current_user.is_authenticated:
        title = "Смены дежурств"
        timeintervals = Timeinterval.query.all()
        itslen = len(timeintervals)
        #new_dict = dict(zip(colors, dutytypes))
        #print(new_dict)
        print('len=',type(itslen))
        return render_template('smeny.html', title = title, timeintervals = timeintervals, color_btn = color_btn, color_row = color_row, itslen = itslen)
    else:
        flash('Log in for access', 'alert-info')
        return redirect(url_for('user.login'))

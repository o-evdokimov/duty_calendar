from flask_login import current_user
from flask import Blueprint, render_template, flash, redirect, url_for
from datetime import datetime
from calendar import monthrange
import calendar


from schedule.calendar.models import Dutytype, Timeinterval
from schedule.user.models import Person

blueprint = Blueprint('calendar', __name__, url_prefix='/calendar')

color_btn = ['primary', 'warning', 'success', 'secondary']
color_row = ['info', 'warning', 'success', 'active']

@blueprint.route('/')
def index():
    title = "Расписание"
    mydate = datetime.today()
    cal = calendar.Calendar()
    persons = Person.query.all()
    itslen = len(Dutytype.query.all())
    month = int(mydate.strftime('%m'))+1
    year = int(mydate.strftime('%Y'))
    days = monthrange(year,month)[1]
    first_day = monthrange(year,month)[0]
    mcal = cal.monthdays2calendar(year,month)
    print('len=',type(itslen))
    return render_template('index.html', title = title, mcal = mcal, persons = persons, mydate=mydate, color_btn = color_btn, color_row = color_row, itslen = itslen, days = days, first_day = first_day)

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

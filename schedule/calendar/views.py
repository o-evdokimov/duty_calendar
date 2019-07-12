from flask_login import current_user
from flask import Blueprint, render_template, flash, redirect, url_for
from datetime import datetime
from calendar import monthrange
import calendar


from schedule.calendar.models import Dutytype, Dutyevent, Timeinterval
from schedule.user.models import Person

blueprint = Blueprint('calendar', __name__, url_prefix='/calendar')

def InitCalendar(mcal, persons, dutytypes):
    pass

@blueprint.route('/<int:year_>/<int:month_>')
def index(year_,month_):
    title = "Расписание"
    current_date = datetime.today()
    cal = calendar.Calendar()
    persons = Person.query.all()
    dutytypes = Dutytype.query.all()
    dutytype_number = len(Dutytype.query.all())
    #month = int(mydate.strftime('%m'))
    #year = int(mydate.strftime('%Y'))
    year = year_
    month = month_
    mydate = datetime.strptime('{},{}'.format(year,month), '%Y,%m')
    #year=2021
    first_day = monthrange(year,month)[0]
    mcal = cal.monthdays2calendar(year,month)
    InitCalendar(mcal,persons,dutytypes)
    return render_template('index.html', title = title, mcal = mcal, persons = persons, mydate=mydate, dutytype_number = dutytype_number, first_day = first_day)

@blueprint.route('/smeny')
def smeny():
    if current_user.is_authenticated:
        title = "Смены дежурств"
        timeintervals = Timeinterval.query.all()
        itslen = len(timeintervals)
        #new_dict = dict(zip(colors, dutytypes))
        #print(new_dict)
        print('len=',type(itslen))
        return render_template('smeny.html', title = title, timeintervals = timeintervals, itslen = itslen)
    else:
        flash('Log in for access', 'alert-info')
        return redirect(url_for('user.login'))

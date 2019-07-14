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

@blueprint.route('/')
def index_default():
    current_date = datetime.today()
    year = int(current_date.strftime('%Y'))
    month = int(current_date.strftime('%m'))
    return redirect(url_for('calendar.index',year_=year,month_=month))

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
    if (month < 1): 
        month=12
        year-=1
        return redirect(url_for('calendar.index',year_=year,month_=month)) 
    if (month > 12): 
        month=1
        year+=1
        return redirect(url_for('calendar.index',year_=year,month_=month)) 
    mydate = datetime.strptime('{},{}'.format(year,month), '%Y,%m')
    #year=2021
    first_day = monthrange(year,month)[0]
    mcal = cal.monthdays2calendar(year,month)
    InitCalendar(mcal,persons,dutytypes)

    duty_events_month = list()
    de_month = Dutyevent.query.filter_by(table_date = datetime.strptime('{}-{}-14'.format(year,month),'%Y-%m-%d'))
    de = de_month[0]
    de14 = Dutyevent.query.filter_by(table_date = datetime.strptime('{}-{}-14'.format(year,month),'%Y-%m-%d'))
    pe14 = Person.query.filter_by(id=de14[0].duty_person_id) 

    for day in range(31):
        print(day)
        duty_events_month.append(pe14[0].username)




    return render_template('index.html', title = title, mcal = mcal, persons = persons, duty_events_month = duty_events_month, mydate=mydate, dutytype_number = dutytype_number, first_day = first_day)

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

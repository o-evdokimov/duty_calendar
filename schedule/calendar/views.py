from flask_login import current_user
from flask import Blueprint, render_template, flash, redirect, url_for
from datetime import datetime
from calendar import monthrange
import calendar


from schedule.calendar.models import Dutytype, Dutyevent, Timeinterval, Role
from schedule.user.models import Person


blueprint = Blueprint('calendar', __name__, url_prefix='/calendar')

#def InitCalendar(mcal, persons, dutytypes):
#    pass

#def EmptyDay(day_date):
    #table_date = datetime.strptime(day_date, '%Y-%m-%d')
    #de = Dutyevent(table_date=table_date)
    #return de


@blueprint.route('/')
def index_default():
    year = int(datetime.today().strftime('%Y'))
    month = int(datetime.today().strftime('%m'))
    return redirect(url_for('calendar.index',year=year,month=month))

@blueprint.route('/<int:year>/<int:month>')
def index(year,month):
    title = "Расписание"
    dutytypes = Dutytype.query.all()
    dutytype_number = len(dutytypes)
    if (month < 1): 
        month=12
        year-=1
        return redirect(url_for('calendar.index',year=year,month=month)) 
    if (month > 12): 
        month=1
        year+=1
        return redirect(url_for('calendar.index',year=year,month=month)) 
    mydate = datetime.strptime('{},{}'.format(year,month), '%Y,%m')
    first_day = monthrange(year,month)[0]
    cal = calendar.Calendar()
    mcal = cal.monthdays2calendar(year,month)
    week_numbers = len(mcal)
    #InitCalendar(mcal,persons,dutytypes)

    # получаем словарь с dutyevents и отдаём его в calendar.index
    # ключ = день, значение = список объектов класса Dutyevent
    de_day = dict()
    for x in cal.itermonthdays2(year,month):
        if not x[0]: continue
        day = x[0]
        day_date = (datetime.strptime('{}-{}-{}'.format(year,month,str(day)),'%Y-%m-%d')).strftime('%Y-%m-%d')
        #day_date = '2019-07-14'
        de_day[day] = Dutyevent.query.filter_by(date_ymd = day_date)
        #if not de_day[day].all(): de_day[day] = EmptyDay(day_date)

    return render_template('index.html', title = title, week_numbers=week_numbers, mcal = mcal, de_day = de_day, mydate=mydate, dutytype_number = dutytype_number, first_day = first_day)

@blueprint.route('/smeny')
def smeny():
    if current_user.is_authenticated:
        title = "Смены дежурств"
        timeintervals = Timeinterval.query.all()
        itslen = len(timeintervals)
        print('len=',type(itslen))
        return render_template('smeny.html', title = title, timeintervals = timeintervals, itslen = itslen)
    else:
        flash('Log in for access', 'alert-info')
        return redirect(url_for('user.login'))


# получаем словарь (dict) с persons, номер ячейки соответствует dutytype_id
# данный template используем в calendar.index
@blueprint.app_template_filter('get_event_duty_person')
def get_event_duty_person(duty_event):
    dutytypes = Dutytype.query.all()
    dt_len = len(dutytypes)
    duty_persons_empty = dict()
    for k in range(dt_len-1):
        duty_persons_empty[k] = '.......................'  
    duty_persons = duty_persons_empty
    if not duty_event: 
        return duty_persons_empty
    for event in range(len(duty_event.all())):
            dt_id = duty_event[event].duty_type_id
            duty_persons[dt_id-1] = (Person.query.filter_by(id=duty_event[event].duty_person_id))[0].username
            
    try:
        return duty_persons
    except IndexError:
        return duty_persons_empty

@blueprint.app_template_filter('get_role_duty_person')
def get_role_duty_person(n):
    role = Dutytype.query.filter_by(id=n+1)[0].role_id
    persons = Role.query.get(role).users
    return list(set(persons))

@blueprint.app_template_filter('get_dutytype_name')
def get_dutytype_name(n):
    return Dutytype.query.filter_by(time_interval_id=n+1)[0].name


@blueprint.app_context_processor
def  write_dutyevent():
   print('yes')
   return dict(write_dutyevent=777)


@blueprint.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return "nothing"


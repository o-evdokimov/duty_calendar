from flask_sqlalchemy import SQLAlchemy
#from schedule.user.models import db
from schedule.database import db
from datetime import datetime
from schedule.user.models import Person 


#db = SQLAlchemy()
 
class Timeinterval(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    time_start = db.Column(db.Time, nullable=False) 
    time_end = db.Column(db.Time, nullable=False) 
    time_end2 = db.Column(db.Time, nullable=True)
    duty_type = db.relationship('Dutytype', backref='timeinterval', lazy=True)
    #__abstract__ = True

    def __init__(self, time_start, time_end):
        self.time_start = time_start
        self.time_end = time_end
    def __repr__(self):
        return ("{}-{} >> {}".format(datetime.strftime(self.time_start,"%H:%M"), datetime.strftime(self.time_end,"%H:%M"), self.duty_type))

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    duty_type = db.relationship('Dutytype', backref='role', lazy=True)
    users = db.relationship("Person", secondary = 'roleperson', back_populates='duty_roles')
    #__abstract__ = True

    def __repr__(self):
        return ("Role: {}".format(self.name), self.duty_type)

class Dutytype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    time_interval_id = db.Column(db.Integer, db.ForeignKey('timeinterval.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    #__abstract__ = True

    def __repr__(self):
        return ("{}".format(self.id))
    def __init__(self, name, time_interval_id, role_id):
        self.name = name
        self.time_interval_id = time_interval_id
        self.role_id = role_id
    #def __init__(self, *args, **kwargs):
    #    super(Dutytype,self).__init__(*args, **kwargs)

class Roleperson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    #__abstract__ = True
    #role_id = db.Column(db.Integer, db.ForeignKey('role.id'), primary_key = True)
    #person_id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key = True)

    def __init__(self, *args, **kwargs):
        super(Roleperson,self).__init__(*args, **kwargs)

class Dutyevent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    duty_type_id = db.Column(db.Integer, db.ForeignKey('dutytype.id'), default=0)
    duty_person_id = db.Column(db.Integer, db.ForeignKey('person.id'), default=0)
    duty_person = db.Column(db.String, nullable=True)
    date_time_start = db.Column(db.DateTime, default = datetime.now(), nullable=False) 
    date_time_stop = db.Column(db.DateTime, default = datetime.now(), nullable=False)
    date_ym = db.Column(db.String, default = datetime.today().strftime('%Y-%m'), nullable=False) 
    date_ymd = db.Column(db.String, default = datetime.today().strftime('%Y-%m-%d'), nullable=False)
    table_date = db.Column(db.DateTime, default = datetime.now(), unique=False, nullable=False)
    #__abstract__ = True

    def __repr__(self):
        return ("Duty event: {}".format(self.id))
    def create_ym(self):
        return self.table_date.strftime('%Y-%m')
    #def get_person(self):
    #    return Person.query.filter_by(id=self.duty_person_id)[0]
    def create_ymd(self):
        return self.table_date.strftime('%Y-%m-%d')
    def __init__(self, duty_type_id = duty_type_id, duty_person_id = duty_person_id, table_date=table_date):
        self.duty_type_id = duty_type_id
        self.duty_person_id = duty_person_id
        #self.duty_person = self.get_person()
        self.table_date = table_date
        self.date_ym = self.create_ym()
        self.date_ymd = self.create_ymd()

class Testdutyevent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    duty_type_id = db.Column(db.Integer, db.ForeignKey('dutytype.id'), default=0)
    duty_person_id = db.Column(db.Integer, db.ForeignKey('person.id'), default=0)
    duty_person = db.Column(db.String, nullable=True)
    date_time_start = db.Column(db.DateTime, default = datetime.now(), nullable=False) 
    date_time_stop = db.Column(db.DateTime, default = datetime.now(), nullable=False)
    date_ym = db.Column(db.String, default = datetime.today().strftime('%Y-%m'), nullable=False) 
    date_ymd = db.Column(db.String, default = datetime.today().strftime('%Y-%m-%d'), nullable=False)
    table_date = db.Column(db.DateTime, default = datetime.now(), unique=False, nullable=False)
    def __repr__(self):
        return ("Duty event: {}".format(self.id))
    # @property
    def create_ym(self):
        return self.table_date.strftime('%Y-%m')
    def get_person(self):
        return Person.query.filter_by(id=self.duty_person_id)[0]
    # @property
    def create_ymd(self):
        return self.table_date.strftime('%Y-%m-%d')
    #def __init__(self, duty_type_id = duty_type_id, duty_person_id = duty_person_id, duty_person=duty_person, date_time_start=date_time_start, date_time_stop=date_time_stop, date_ym=date_ym, date_ymd=date_ymd, table_date=table_date):
    #    self.duty_type_id = duty_type_id
    #    self.duty_person_id = duty_person_id
    #    self.duty_person = duty_person
    #    self.date_time_start = date_time_start
    #    self.date_time_stop = date_time_stop
    #    self.table_date = table_date
    #    self.date_ym = self.date_ym
    #    self.date_ymd = self.date_ymd
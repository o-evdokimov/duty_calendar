from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#from schedule.user.models import Person 


db = SQLAlchemy()
 
class Timeinterval(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    time_start = db.Column(db.DateTime, nullable=False) 
    time_end = db.Column(db.DateTime, nullable=False) 
    duty_type = db.relationship('Dutytype', backref='timeinterval', lazy=True)

    def __init__(self, time_start, time_end):
        self.time_start = time_start
        self.time_end = time_end
    def __repr__(self):
        return ("{}-{} >> {}".format(datetime.strftime(self.time_start,"%H:%M"), datetime.strftime(self.time_end,"%H:%M"), self.duty_type))

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    duty_type = db.relationship('Dutytype', backref='role', lazy=True)
    def __repr__(self):
        return ("Role: {}".format(self.name), self.duty_type)

class Dutytype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    time_interval_id = db.Column(db.Integer, db.ForeignKey('timeinterval.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    def __repr__(self):
        return ("{}".format(self.name))
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

    def __init__(self, *args, **kwargs):
        super(Roleperson,self).__init__(*args, **kwargs)

class Dutyevent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    duty_type_id = db.Column(db.Integer, db.ForeignKey('dutytype.id'), default=1000)
    duty_person_id = db.Column(db.Integer, db.ForeignKey('person.id'), default=1000)
    date_time_start = db.Column(db.DateTime, default = datetime.today().strftime('%Y-%m-%d'), nullable=False) 
    date_time_stop = db.Column(db.DateTime, default = datetime.today().strftime('%Y-%m-%d'), nullable=False)
    date_ym = db.Column(db.String, default = datetime.today().strftime('%Y-%m'), nullable=False) 
    date_ymd = db.Column(db.String, default = datetime.today().strftime('%Y-%m-%d'), nullable=False)
    table_date = db.Column(db.DateTime, default = datetime.today().strftime('%Y-%m-%d'), unique=False, nullable=False)
    def __repr__(self):
        return ("Duty event: {}".format(self.id))
    # @property
    def create_ym(self):
        return self.table_date.strftime('%Y-%m')
    # @property
    def create_ymd(self):
        return self.table_date.strftime('%Y-%m-%d')
    def __init__(self,table_date=table_date):
        self.table_date = table_date
        self.date_ym = self.create_ym()
        self.date_ymd = self.create_ymd()

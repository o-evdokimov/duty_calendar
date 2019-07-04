from flask_sqlalchemy import SQLAlchemy
#from schedule.user.models import Person 


db = SQLAlchemy()
 
class Timeinterval(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    time_start = db.Column(db.DateTime, nullable=False) 
    time_end = db.Column(db.DateTime, nullable=False) 

    def __init__(self, time_start, time_end):
        self.time_start = time_start
        self.time_end = time_end

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    def __repr__(self):
        return ("Role: {}".format(self.name))

class Dutytype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    time_interval_id = db.Column(db.Integer, db.ForeignKey('timeinterval.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    def __repr__(self):
        return ("Dutytype: {}".format(self.name))
    def __init__(self, *args, **kwargs):
        super(Dutytype,self).__init__(*args, **kwargs)

class Roleperson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    def __init__(self, *args, **kwargs):
        super(Roleperson,self).__init__(*args, **kwargs)

class Dutyevent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    duty_type_id = db.Column(db.Integer, db.ForeignKey('dutytype.id'))
    duty_person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    date_time_start = db.Column(db.DateTime, nullable=False) 
    date_time_stop = db.Column(db.DateTime, nullable=False)
    table_date = db.Column(db.DateTime, nullable=False)
    def __repr__(self):
        return ("Duty event: {}".format(self.id))

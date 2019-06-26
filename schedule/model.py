from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
 

class Timeinterval(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    time_start = db.Column(db.Time, nullable=False) 
    time_end = db.Column(db.Time, nullable=False) 

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    def __repr__(self):
        return ("Role: {}".format(self.name))

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True) 
    active = db.Column(db.Boolean,nullable=False )
    def __repr__(self):
        return ("Person: {}".format(self.name))

class Dutytype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_interval_id = db.Column(db.DateTime,db.ForeignKey('timeinterval.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    name = db.Column(db.String, nullable=False)
    def __repr__(self):
        return ("Dutytype: {}".format(self.name))

class Roleperson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

class Dutyevent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    duty_type_id = db.Column(db.Integer, db.ForeignKey('dutytype.id'))
    duty_person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    date_time_start = db.Column(db.DateTime, nullable=False) 
    date_time_stop = db.Column(db.DateTime, nullable=False)
    def __repr__(self):
        return ("Duty event: {}".format(self.id))

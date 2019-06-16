from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy

class DutyEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String, foreign_key=True, nullable=False)
    duty_person_id = db.Column(db.Integer, unique=True, nullable=False)
    datetime_start = db.Column(db.DateTime, nullable=False)
    datetime_end = db.Column(db.DateTime, nullable=False)

class DutyType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    datetime_start = db.Column(db.DateTime, nullable=False)
    datetime_end = db.Column(db.DateTime, nullable=False)

class DutyPerson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    role_id = db.Column(db.Integer, foreign_key=True, nullable=False)

class DutyRolesType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, foreign_key=True, nullable=False)

class DutyRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
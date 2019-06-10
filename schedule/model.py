from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy

class Duty_Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String, foreign_key=True, nullable=False)
    duty_person_id = db.Column(db.Integer, unique=True, nullable=False)
    datetime_start = db.Column(db.DateTime, nullable=False)
    datetime_end = db.Column(db.DateTime, nullable=False)

class Duty_Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    datetime_start = db.Column(db.DateTime, nullable=False)
    datetime_end = db.Column(db.DateTime, nullable=False)

class Duty_Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    role_id = db.Column(db.DateTime, foreign_key=True, nullable=False)

class Duty_Roles_Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.DateTime, foreign_key=True, nullable=False)

class Duty_Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
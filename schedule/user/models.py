from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


from schedule.db import db

class Person(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index = True, nullable=False, unique=True) 
    password = db.Column(db.String(128))
    active = db.Column(db.Boolean, nullable=False, default = True)
    role = db.Column(db.String(10), index=True)
    email = db.Column(db.String(50))
    
    def set_password(self, password):
        self.password =  generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin' and self.active == True
    
    def __repr__(self):
        return ("Person: {}".format(self.username))

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    def __repr__(self):
        return ("Role: {}".format(self.name))


class Roleperson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
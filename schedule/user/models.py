from schedule.model import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

#db = SQLAlchemy()

class Person(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index = True, nullable=False, unique=True) 
    password = db.Column(db.String(128))
    active = db.Column(db.Boolean, nullable=False, default=True)
    role = db.Column(db.String, nullable=False)
    def __repr__(self):
        return ("Person: {}".format(self.username))
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password) 
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)
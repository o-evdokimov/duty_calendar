from datetime import timedelta
import os


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'schedule.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'FEWEFW34MI3O4JR4O3JR4mivoer43'
REMEMBER_COOKIE_DURATION = timedelta(days=5)
SQLALCHEMY_TRACK_MODIFICATIONS = False

try:
    from config_local import *
except ImportError:
    pass
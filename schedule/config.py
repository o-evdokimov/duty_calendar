"""
    configuration file for schedule
"""

import os

DEBUG = True
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'schedule.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'JHKJhu%$&I^IO'

try:
    from config_local import *
except ImportError:
    pass
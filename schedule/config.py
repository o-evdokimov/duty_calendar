# configuration file for schedule
#
#
#
import os

class Configuration(object):
    DEBUG = True
DEBUG = True
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'schedule.db')







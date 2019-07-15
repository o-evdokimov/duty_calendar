from schedule.calendar.models import db
#from schedule import db 
from schedule.__init__ import create_app

db.create_all(app=create_app())

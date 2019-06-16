# view.py

from app import app
from flask import render_template

@app.route("/")
def index():
   return render_template('base.html')

@app.route("/calendar")
def calendar():
   return render_template('calendar.html')



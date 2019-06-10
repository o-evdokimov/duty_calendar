# __init__.py 
# init Flask server

from flask import Flask


app = Flask(__name__)
#app.config.from_pyfile('config.py')

@app.route("/")
def schedule():
   return 'schedule'
   #return app

if __name__=='__main__':
    app.run()

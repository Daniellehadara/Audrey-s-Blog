#Step 1: from the official homepage of flask copy paste the following:
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

#Step 2: open in cmd the project and write the following comments:
#set FLASK_APP = FlaskBlog.py --> set FLASK_ENV=development--> flask run --> get IP address
#--> http://127.0.0.1:5000/ --> this is a running webserver
#Problems: pip install virtualenv, couldn't find a Flask app
#solution to the problem: set FLASK_APP=FlaskBlog.py # dont use a space when setting the environment variable
#solution to the problem: set FLASK_APP=FlaskBlog.py # dont use a space when setting the environment variable


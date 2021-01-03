import os


class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'demo@gmail.com'
    MAIL_PASSWORD = 'demo123456'

#this is not done yet! --> viedeo 11, 27:00
#Environment Variables (Windows):
#https://youtu.be/IolxqkL7cD8
#sidebar at the end of the video


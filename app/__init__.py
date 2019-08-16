from flask import Flask
from flask_mail import Message, Mail
# from config import Config


app = Flask(__name__)
app.secret_key = 'textbook pro submission only HaiFar'


# app.config.from_object(Config)
# app.secret_key = 'development key'

from app import routes


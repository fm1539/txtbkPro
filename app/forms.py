from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError
recipMail = TextField("Email", [validators.Required("Please enter your email"), validators.Email()])
class ContactForm(Form):
  name = TextField("Name", [validators.Required("Please enter your name.")])
  email = recipMail
  subject = TextField("Subject", [validators.Required("Please enter a subject")])
  message = TextAreaField("Message", [validators.Required("Please enter a message.")])
  submit = SubmitField("Send")
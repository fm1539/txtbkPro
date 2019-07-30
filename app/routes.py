from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/contacts', methods = ['GET','POST'])    
def contacts():
    if request.method == "GET":
        return "Please fill out the contacts section"
    else:
        return "Thanks for filling out the form! You will be helped shortly."
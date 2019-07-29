from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
@app.route('/search', methods = ['GET','POST'])    
def search():
    if request.method == "GET":
        return "Please fill out the form in the index"
    else:
        return "Find the cheapest textbook"
    



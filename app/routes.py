from app import app
from app.models.scraper import send_mail
from flask import render_template, request
from app.models import scraper, formopener


title = ''
# converted_price = scraper.converted_price
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
# @app.route('/contacts', methods = ['GET','POST'])    
# def contacts():
#     if request.method == "GET":
#         return "Please fill out the contacts section"
#     else:
#         return "Thanks for filling out the form! You will be helped shortly."
        
    
    # print(title)
    # print(converted_price)
    # converted_price = str(converted_price)
    # return render_template("url.html", title = title, converted_price = converted_price)

email = ""
# @app.route('/email', methods = ['GET', 'POST']) 


# def userEmail():
#     if request.method == 'GET':
#         return "Sorry, please enter your e-mail adress."
#     else:
#         formData = dict(request.form)
#         global email
#         title, converted_price = scraper.checkPrice(txtbkLink)
#         email = formData["userEmail"]
#         print(converted_price)
#         if (converted_price < 4.00):
#             # print(email)
#             scraper.send_mail(email)
#             # print("email")
#             return render_template("url.html", txtbkLink = txtbkLink, title = title, converted_price = converted_price)
#         else:
#             return "Your book is over $4.00"
            # return "The textbook was more than $4.00"
        #  send_mail(email) 
        
        
@app.route('/url', methods = ['GET', 'POST'])
def txtbkLink():
    if request.method == 'GET':
        return "Sorry, please enter a valid URL on the home page."
    else:
        global title, converted_price, email
        formData = dict(request.form)
        
        txtbkLink = formData["txtbkLink"]
        email = formData["userEmail"]
        # link = formData["txtbkLink"]
        title, converted_price = scraper.checkPrice(txtbkLink, email)
        # scraper.checkPrice(txtbkLink, 'farhan.mashud.174@gmail.com')
        # print(type(converted_price))
        if (converted_price < 4.00):
            # print(email)
            scraper.send_mail(email)
            # print("email")
            # return render_template("url.html", txtbkLink = txtbkLink, title = title, converted_price = converted_price)
        #  :
            # return "The textbook was more than $4.00"
        
        return render_template("url.html", txtbkLink = txtbkLink, title = title, converted_price = converted_price)


# @app.route('/url', methods = ['GET','POST'])
# def userTxtbkLink():
#     userdata = dict(request.form)
    # user
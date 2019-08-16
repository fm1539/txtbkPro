from app import app
from app.models.scraper import send_mail
from flask import Flask, render_template, request, flash
from app.models import scraper, formopener
from app.forms import ContactForm
from flask_mail import Message, Mail
mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'textbookproapp@gmail.com'
app.config["MAIL_PASSWORD"] = 'xyrvubinkzrncnvb'
 
mail.init_app(app)

# title = ''
# converted_price = scraper.converted_price
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/contacts', methods = ['GET','POST'])    
def contacts():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('One or more fields is either blank or filled out incorrectly. Please try again')
            return render_template('contacts.html', form=form)
        else:
            msg = Message(form.subject.data, sender='textbookproapp@gmail.com', recipients=['farhan.mashud.174@gmail.com','haiyingman8@gmail.com','textbookproapp@gmail.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return 'Form posted.'
 
    elif request.method == 'GET':
        return render_template('contacts.html', form=form)
    
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
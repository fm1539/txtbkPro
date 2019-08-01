import requests
from bs4 import BeautifulSoup
import smtplib
from flask import Flask, escape, request 

# title = "" 
# price = ""
# converted_price = 0

app = Flask("Textbook Pro by HaiFar")

def send_mail(email):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('farhan.mashud.174@gmail.com', 'tcvwxvbphbqktvue')
    
    subject = "Price fell down!"
    body = "Check the ebay link  "
    
    msg = "Subject: {}\n\n{}".format(subject, body)
    
    server.sendmail(
        'farhan.mashud.174@gmail.com',
        email,
        msg
    )
    
    return "EMAIL SENT!" and server.quit()
    

def checkPrice(txtbkLink, email):
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    page = requests.get(txtbkLink, headers=headers)
    # soup = BeautifulSoup(page.content, 'html.parser')
    # title = soup.find(id="productTitle")

    soup1 = BeautifulSoup(page.content, "html.parser")
    
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    global title 
    title = soup2.find(id="itemTitle").get_text()
   

    global price 
    price = soup2.find(id="prcIsum").get_text()
    global converted_price 
    converted_price = float(price[10:14])
    # converted_price = float(converted_price)
    
    # (title.strip())
    # print(converted_price)
    # return (title.strip(), converted_price)

    return(title.strip(), converted_price)

def textbook():
    global title, price, converted_price
    price = request.args.get("price", converted_price)
    title = request.args.get("title", title )
    
    # cereturn "The price of {} is ${}".format(escape(title), escape(price))
    



# checkPrice(input("Enter URL \n"))
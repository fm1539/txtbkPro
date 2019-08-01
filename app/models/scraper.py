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
    body = "Check the ebay link https://www.ebay.com/itm/Schaums-Outline-of-College-Physics-11th-Edition-Schaums-Outlines/264299992135?epid=6012772980&_trkparms=ispr%3D1&hash=item3d8981d447:g:opUAAOSwUlRbsw8Z&enc=AQAEAAAB4BPxNw%2BVj6nta7CKEs3N0qXyMKaPqSWFYFjtddM%2FSpeQ0GWvoOsxMeQc%2BuUXNqBTv%2Bcv2JrK3HPONqpcDZH3gVf9CHPIfuiCSsoUHXd1E7LXvHS%2BHSYJHJ7t6qe%2BoULzgnuTdkcuZwajNl3Ta9IktY9u0V33FW67wrO5Lfh0MVwPDh%2Bow2pWRAqJTg5wDDPv%2BJaSH1YCZ%2BHjJMj%2Fd9Y9wbUGhrWPVKxfqZTa%2FRJsZKsnN4tAQtzMm15E3Dsykm6k7sFTwWwsKc%2FL2Fyk6qPU9l96egZFHVkyd%2F3orSlPcc2Q8r1bq4oUwDRAcj4Sopv1Uu6y%2F3fWurOMY7algGktONMru9q%2BazjXtLY4QleruDuC1AY9zQvh7As7RGbgFUaq8D23Rxyar1BiE78n9Iv29KY%2BxKG%2BXHPABNDkiooJwyHtE0yRFOi31VqSjMLsY55E%2FKMPSTKH1wDxgb24wNlDiPO5sXZ%2BtD9oqyUYjJoPv%2By1irEF4%2BJtJIwLjY%2B2NRTmeJO48QbZMpbSQxKss7VBrxSivVfVKBddWXsdtuAnSPYj63CU93e%2F5T6O1IZax6ZwKFsi5B5RAnSe%2FN%2FIPIS%2Fe9mAnUTVf%2FzKF2Cotym%2Bby1oP3%2BzH3MutILOnPqS4jxxyg%3D%3D&checksum=2642999921353054c6f79ae14a8db386b6d1bd3dafbc"
    
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
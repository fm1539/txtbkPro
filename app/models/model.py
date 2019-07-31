import requests
from bs4 import BeautifulSoup
def getText():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = 'https://www.amazon.com/s?k=ap+calculus+ab+princeton+review+2019&crid=3I9ZRNEWC41Z1&sprefix=princeton+review+ab+ca%2Caps%2C300&ref=nb_sb_ss_i_1_22'
 
    page = requests.get(url, headers = headers)
    # soup = BeautifulSoup(page.text, 'html.parser')
    return page.text






 
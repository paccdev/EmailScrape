import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from bs4 import BeautifulSoup
import time
import re

#Scrapping this example website
page = requests.get('https://www.nwahomepage.com/')
html = page.content

soup = BeautifulSoup(html, 'lxml')
Times = soup.findAll(string=re.compile("ago"))

if "seconds ago" in Times:
    email()

def email():
    sender = 'youremail@domain.com'
    receivers = 'receiveremail@domain.com'
    body_of_email = 'There are new articles posted Link: https://www.nwahomepage.com/'

    msg = MIMEText (body_of_email, 'plain', 'utf-8')
    #msg.attach(msg)
    msg ['Subject'] = 'New Articles Posted just a few seconds ago!'
    msg ['From'] = sender
    msg ['To'] = receivers

    s = smtplib.SMTP_SSL (host = 'smtp.gmail.com', port = 465)
    s.login (user = 'youremail@domain.com', password = 'email password')
    s.sendmail (sender, receivers, msg.as_string())
    print("Email has been sent!")
    s.quit()
    time.sleep(20*5)
email()








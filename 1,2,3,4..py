import re

c = input ("Escriba su correo :")
m = re.search('\w+@\w+.\w+', c)

print(m)

import smtplib


gmail_user = 'camilolopezperea.1927@gmail.com'
gmail_password = ''

sender = 'camilolopezperea.1927@gmail.com'
receivers = ['camilolopezperea_1927@hotmail.com']

message = """ From: Cristian camilo lopez <camilolopezperea.1927@gmail.com>
To: <camilolopezperea_1927@hotmail.com>
Subject: SMTP e-mail test 

This is a test e-mail message.
"""

try:
  smtpObj = smtplib.SMTP('smtp.gmail.com',587)
  #smtpObj = smtplib.SMTP_SSL('smtp.gmail.com',465)
  smtpObj.ehlo()
  smtpObj.starttls()
  smtpObj.login(gmail_user, gmail_password)
   
  smtpObj.sendmail(sender, receivers, message)
  smtpObj.quit()  
  print ("Successfully sent email")
except smtplib.SMTPException:
  print ("Error: unable to send email")

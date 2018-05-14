import smtplib
import config
import json
import rea
import checkWeather
from twisted.internet import task
from twisted.internet import reactor

timeout = 10.0 # ten seconds

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587') #need port number in order to connect
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)

        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, rea.email_list, message)
        server.quit()
        print('Success: email sent!')
    except:
        print('Email failed to send.')

subject = 'Test subject' #subject line
msg = checkWeather.returninfo() #extracts information concerning the weather
send_email(subject, msg)


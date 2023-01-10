import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import dotenv
class SendEmail:
    def __init__(self, sender:str, addressee:str, message:str, subject:str, password:str):
        self.sender   = sender
        self.adressee = addressee
        self.message  = message
        self.subject  = subject
        self.password = password
    def send(self):
        mail =  MIMEMultipart()
        mail['From']    = self.sender
        mail['To']      = self.adressee
        mail['Subject'] = self.subject
        mail.attach(MIMEText(self.subject,'plain'))
        server = smtplib.SMTP('smtp.gmail.com', port=587)
        server.starttls()
        server.login(mail['From'], self.password)
        server.sendmail(mail['From'], mail['To'], mail.as_string())
        server.quit()
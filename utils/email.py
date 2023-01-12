import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from accounts.models import Account
import smtplib
import os
import dotenv


class Email:

    def __init__(self, adressee:Account, subject:str, order_id:str):
        self.adressee = adressee
        self.subject  = subject
        self.mail     = MIMEMultipart()
        self.message  = f" Olá {adressee.username} gostariamos de informar que seu pedido de ID {order_id} acaba de ser enviado."


    def load_credentials(self):
        dotenv.load_dotenv()
        self.sender   = os.getenv("EMAIL_SENDER")
        self.password = os.getenv("APP_PASSWORD")


    def build_message(self, message:str | None = None):

        self.load_credentials()
        
        if  message:
            self.message = message
        
        self.mail['From']    = self.sender
        self.mail['To']      = self.adressee.email
        self.mail['Subject'] = self.subject
        self.mail.attach(MIMEText(self.message,'plain'))
    

    def send(self):
        
        self.build_message()

        server = smtplib.SMTP('smtp.gmail.com', port=587)
        server.starttls()
        server.login(self.mail['From'], self.password) 
        server.sendmail(self.mail['From'], self.mail['To'], self.mail.as_string())
        server.quit()  

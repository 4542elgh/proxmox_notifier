import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

class GM_SMTP:
    def __init__(self, g_app_key):
        self.g_app_key = g_app_key

    def compose(self, subject, body, sender, recipients, payload=""):
        self.sender = sender
        self.recipients = recipients

        self.msg = MIMEMultipart("mixed")
        self.msg['Subject'] = subject
        self.msg['From'] = self.sender
        self.msg['To'] = ', '.join(self.recipients)
        self.body = MIMEText(body, 'html')
        self.msg.attach(self.body)

        if payload != "":
            self.p = MIMEApplication(payload,_subtype="txt")
            self.p.add_header('Content-Disposition', "attachment; filename=payload.txt") 
            self.msg.attach(p)

    def send_email(self):
        self.smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.smtp_server.login(self.sender, self.g_app_key)
        self.smtp_server.sendmail(self.sender, self.recipients, self.msg.as_string())
        self.smtp_server.quit()

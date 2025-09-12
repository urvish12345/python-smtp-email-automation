"""
📌 Problem Statement
Create a python script that automates sending emails via SMTP - usefull for reminders, reports, or alerts
"""

import smtplib
from email.message import EmailMessage

def send_email(to, subject, body):
    email = EmailMessage()
    email['From'] = 'example@example.com'
    email['To'] = to
    email['Subject'] = subject
    email.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('email', 'password')
        smtp.send_message(email)


send_email('receiver email', 'Test Subject', 'Hello, this is a testemail!')
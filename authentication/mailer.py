import smtplib
from email.mime.text import MIMEText
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from django.contrib.auth.models import User
from django.http import response
from django.core.mail import send_mail 
from django.conf import settings
from .models import *


def send_registered_mail(sender, **kwargs):
    """For sending account activation Email to the user/customer
    who has created their account on the Ecommerce API"""
    if sender in [None,'']:
        return False

    sender_email = "saroelzamathew259@gmail.com"
    recepient_email = sender
    subject = f"Welcome {sender}, Account Activated"
    body = "Your account has been activated, Happy Shopping!"

    message = MIMEText(body)
    message["From"] = sender_email
    message["To"] = recepient_email
    message["Subject"] = subject

    smtp_server = "sandbox.smtp.mailtrap.io"
    smtp_user = "cfc0eb23136b33"
    smtp_password = "24106ca8f88a2c"
    smtp_port = "2525"

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(sender_email, recepient_email, message.as_string())
    server.quit()


def index(request,):
    if request.method=='POST':
        message = request.POST['message']
        email_id = request.POST['email_id']
        name = request.POST['name']

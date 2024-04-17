from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(email):
    subject = 'Welcome to Our Website!'
    message = 'Thank you for fill the form. We hope you enjoy your experience!'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

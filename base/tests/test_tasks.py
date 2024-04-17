from django.test import TestCase
from base.tasks import send_welcome_email
from django.core.mail import send_mail
from django.conf import settings



class SendWelcomeEmailTestCase(TestCase):
    def test_sending_welcome_email(self):
        send_welcome_email.delay('blackbutlersiham2001@gmail.com')





import os
from django.core.mail import EmailMultiAlternatives,EmailMessage
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings



def send_otp_email_verify(obj):
    NEW_INVITE_EMAIL_SUBJECT = "{0}".format(obj.otp,"One time password")
    msg_html = render_to_string("email/otp.html",{"obj":obj})
    send_mail(NEW_INVITE_EMAIL_SUBJECT,"message","Hello",[obj.email],html_message=msg_html,)
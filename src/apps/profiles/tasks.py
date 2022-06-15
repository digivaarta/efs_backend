from huey.contrib.djhuey import periodic_task, task

from .events import send_otp_email_verify

@task()
def send_otp_email(obj):
    send_otp_email_verify(obj)



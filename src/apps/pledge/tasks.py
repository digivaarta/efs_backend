from huey.contrib.djhuey import periodic_task, task

from .events import send_otp_email,addtextImage,sent_certificates

@task()
def send_otp(obj):
    send_otp_email(obj)


@task()
def generate_and_Save_cert(obj):
    addtextImage(obj)

@task()
def send_cert(obj):
    sent_certificates(obj)

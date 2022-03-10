from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from io import BytesIO
from django.core.files import File
import os
from django.core.mail import EmailMultiAlternatives,EmailMessage
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings


def draw_text():
    img = Image.open("lp.jpg")
    font = ImageFont.truetype("Aaargh.ttf", 60)
    draw.text((1500, 1300),"Draw This Text",(0,0,0),font=font)
    img.save("final_output.jpg")


def send_otp_email(obj):
    NEW_INVITE_EMAIL_SUBJECT = "{0}".format(obj.otp,"One time password")
    msg_html = render_to_string("pledge/otp.html",{"obj":obj})
    send_mail(NEW_INVITE_EMAIL_SUBJECT,"message","Hello",[obj.email],html_message=msg_html,)


def addtextImage(obj):
    W,H = (3508,2481)
    img = Image.open(obj.pledge.raw_certificate.path)
    dateFont = ImageFont.truetype("Roboto-Regular.ttf", 40)
    font = ImageFont.truetype("GreatVibes.ttf", 100)
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(obj.user.profile.full_name,font)
    print("{0}-{1}".format(w,h))
    blob = BytesIO()
    draw.text(((W-w)/2,(H-h)/2.1), obj.user.profile.full_name.title(), font=font,fill="black")
    #draw.text(((W)/5.1,(H)/1.145), obj.cert_time_stamp,font=dateFont,fill="black")
    draw.text(((W)/7.8,(H)/1.25), obj.cert_time_stamp,font=dateFont,fill="black")
    draw.text(((W)/7.8,(H)/1.22), obj.uid.upper(),font=dateFont,fill="black")
    #img.save("{0}.jpg".format(obj.uid.upper()))
    img.save(blob, 'JPEG')
    obj.certificate.save("{0}.jpg".format(obj.uid.upper()), File(blob), save=True)
    #os.remove(settings.BASE_DIR,)


def sent_certificates(obj):
    #ins = Recipient.objects.first()
    # html_content = render_to_string('email/body.html', {'obj':ins}) # render with dynamic value
    # text_content = strip_tags(html_content) #
    # print(html_content)
    # template = get_template('email/body.html')
    # context = {'obj':ins}
    # content = template.render(context)

    #html_content = format_html('<p>This is an <strong>important</strong> message.</p>')
    html_content = render_to_string('pledge/body.html', {"obj":obj})
    text_content = strip_tags(html_content)
    #print(html_content)
    #msg = EmailMessage(SUBJECT,text_content,"my-update@ibbi.gov.in",[ins.email])
    msg = EmailMultiAlternatives("{0} {1}".format("Pledge certificate of",obj.pledge.title), html_content, settings.DEFAULT_FROM_EMAIL, [obj.user.username])
    msg.attach_alternative(html_content,"text/html")
    #msg = EmailMultiAlternatives(SUBJECT, Content, "hinfodot@gmail.com", [ins.email])
    #msg.attach_alternative("This is to certify that", "text/html")
    #pdf = render_to_pdf("email/certificate.html",{"obj":ins})
    #print(pdf)
    #msg.attach("{0}.pdf".format(ins.name),pdf)
    msg.attach_file(obj.certificate.path)
    msg.send()

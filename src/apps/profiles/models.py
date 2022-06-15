from pickle import TRUE
from statistics import mode
from webbrowser import get
from django.db import models
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django_extensions.db.fields import RandomCharField

from profiles.tasks import send_otp_email

# Create your models here.


User = get_user_model()

class Profiles(models.Model):
    user = models.OneToOneField("account.User",related_name="user_profiles",on_delete=models.CASCADE,primary_key=True)
    full_name = models.CharField(max_length=150,blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    state = models.CharField(max_length=100,blank=True,null=True)
    district = models.CharField(max_length=100,blank=True,null=True)
    pincode = models.CharField(max_length=100,blank=True,null=True)
    gender = models.CharField(max_length=100,blank=True,null=True)
    mobile = models.CharField(max_length=10,blank=True,null=True)
    last_update = models.DateTimeField(auto_now=TRUE)

User.profile = property(lambda u:Profiles.objects.get(user=u))


@receiver(post_save,sender="account.User")
def create_profile_instance(sender,instance,created,**kwargs):
    if created:
        Profiles.objects.create(user=instance)


class UserOtp(models.Model):
    email = models.EmailField()
    otp = RandomCharField(length=6,include_alpha=False)

    def __str__(self) -> str:
        return self.email

@receiver(post_save,sender="profiles.UserOtp")
def create_profile_instance(sender,instance,created,**kwargs):
    send_otp_email(instance)
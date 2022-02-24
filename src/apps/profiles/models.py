from pickle import TRUE
from statistics import mode
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Profiles(models.Model):
    user = models.OneToOneField("account.User",related_name="user_profiles",on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    gender = models.CharField(max_length=100,blank=True,null=True)
    last_update = models.DateTimeField(auto_now=TRUE)



@receiver(post_save,sender="account.User")
def create_profile_instance(sender,instance,created,**kwargs):
    if created:
        Profiles.objects.create(user=instance)
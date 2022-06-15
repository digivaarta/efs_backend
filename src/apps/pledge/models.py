from distutils.command.upload import upload
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import slugify
from django_extensions.db.fields import RandomCharField
from pledge.events import addtextImage
from pledge.tasks import send_cert

# Create your models here.



class Pledge(models.Model):
    user = models.ForeignKey("account.User",related_name="user_pledge",on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=700,blank=True,null=True)
    cover_image = models.ImageField(upload_to="pledge/",blank=True,null=True)
    raw_certificate = models.ImageField(upload_to="certificate/")
    creation_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Pledge, self).save(*args, **kwargs) 
               
class PledgeData(models.Model):
    pledge = models.ForeignKey("pledge.Pledge",related_name="pledge_data",on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=700,blank=True,null=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to="pledge/",blank=True,null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(PledgeData, self).save(*args, **kwargs)     



class UserPledge(models.Model):
    user = models.OneToOneField("account.User",on_delete=models.CASCADE,related_name="user_register_pledge")
    pledge = models.ForeignKey("pledge.Pledge",related_name="user_pledge_data",on_delete=models.CASCADE)
    uid = RandomCharField(length=12, lowercase=False, include_digits=True)
    certificate = models.ImageField(upload_to="usercert/",blank=True,null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{0}".format(self.user)

    @property
    def cert_time_stamp(self):
        return self.creation_date.strftime('%d %b, %Y')     


@receiver(post_save,sender=UserPledge)
def execute_otp(sender,instance,created,**kwargs):
    if created:
        addtextImage(instance)
        #send_otp(instance)
        send_cert(instance)
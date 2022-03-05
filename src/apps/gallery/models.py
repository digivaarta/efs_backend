from django.db import models

# Create your models here.


class Gallery(models.Model):
    user = models.ForeignKey("account.User",on_delete=models.CASCADE,related_name="user_gallery")
    link = models.CharField(max_length=100,blank=True,null=True)
    title = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="banners/")
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return "{0}".format(self.image)
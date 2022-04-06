from distutils.command.upload import upload
from random import choice, choices
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class NewsChoices(models.TextChoices):

    NEWS = "news","News"
    WHATSNEW = "wn","What's New"

class News(models.Model):
    user = models.ForeignKey("account.User",on_delete=models.CASCADE,related_name="user_news")
    title = models.CharField(max_length=500)
    description = models.TextField()
    content = RichTextUploadingField()
    image = models.ImageField(upload_to="news/")
    news_type = models.CharField(max_length=100,choices=NewsChoices.choices,default=NewsChoices.NEWS)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        ordering = ["-id"]    
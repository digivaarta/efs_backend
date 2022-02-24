from statistics import mode
from django.db import models

# Create your models here.


class PostAttachChoices(models.TextChoices):

    IMAGE = "image","Image",
    TEXT = "text","Text"

class Post(models.Model):
    user = models.ForeignKey("account.User",related_name="user_social",on_delete=models.CASCADE)
    description = models.TextChoices()
    link = models.URLField(blank=True,null=True

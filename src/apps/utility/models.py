from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class MetaContent(models.Model):
    user = models.ForeignKey("account.User",related_name="user_mc",on_delete=models.CASCADE)
    title = models.CharField(max_length=400,unique=True)
    slug = models.SlugField(max_length=600,blank=True,null=True)
    content = RichTextUploadingField(blank=True,null=True)
    extra = models.JSONField(blank=True,null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(MetaContent, self).save(*args, **kwargs)


from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class MetaContentCategory(models.Model):

    user = models.ForeignKey("account.User",on_delete=models.CASCADE,related_name="mcc_user")
    title = models.CharField(max_length=400,unique=True)
    slug = models.SlugField(max_length=600,blank=True,null=True)

    def __str__(self) -> str:
        return self.title


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(MetaContentCategory, self).save(*args, **kwargs)
    

class MetaContent(models.Model):
    user = models.ForeignKey("account.User",related_name="user_mc",on_delete=models.CASCADE)
    meta_category = models.ForeignKey("utility.MetaContentCategory",related_name="user_mcc",on_delete=models.CASCADE)
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


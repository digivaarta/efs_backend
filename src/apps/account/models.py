from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin,BaseUserManager)
from django.utils import timezone
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.utils.translation import gettext as _


now = timezone.now

class AuthManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):

        if not username:
            raise ValueError("username must be set")

        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self._create_user(username, password, **extra_fields)

class MyUserManager(BaseUserManager):
    pass

class MyUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=100,unique=True)
    email = models.CharField(unique=True,blank=True,null=True,max_length=150)
    picture_url = models.URLField(blank=True,null=True)
    display_name = models.CharField(max_length=100,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=now)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    class Meta:
        abstract = True

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = AuthManager()

    def __str__(self):
        return "{0}".format(self.username)

    def get_full_name(self):
        pass

    def get_short_name(self):
        pass

class User(MyUser):
    pass

User.token = property(lambda u:Token.objects.get(user=u))

@receiver(pre_save,sender=User)
def put_email(sender,instance,*args,**kwargs):
    print(kwargs)
    instance.email = instance.username


@receiver(post_save,sender=User)
def create_token(sender,instance,created,**kwargs):
    if created:Token.objects.create(user=instance)
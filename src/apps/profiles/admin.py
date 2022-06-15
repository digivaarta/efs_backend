from django.contrib import admin
from profiles.models import Profiles,UserOtp
# Register your models here.

@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin):pass


@admin.register(UserOtp)
class UserOtpAdmin(admin.ModelAdmin):pass

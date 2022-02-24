from django.contrib import admin
from profiles.models import Profiles
# Register your models here.

@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin):pass
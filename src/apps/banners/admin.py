from django.contrib import admin
from banners.models import Banner
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    exclude = ("user",)


    def save_model(self,request,obj,form,change):
        obj.user = request.user
        obj.save()
        super(BannerAdmin,self).save_model(request,obj,form,change)
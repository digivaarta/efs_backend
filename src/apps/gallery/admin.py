from django.contrib import admin
from gallery.models import Gallery
# Register your models here.

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    exclude = ("user",)


    def save_model(self,request,obj,form,change):
        obj.user = request.user
        obj.save()
        super(GalleryAdmin,self).save_model(request,obj,form,change)
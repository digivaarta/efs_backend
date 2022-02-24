from django.contrib import admin
from news.models import News
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def save_model(self,request,obj,form,change):
        obj.user = request.user
        obj.save()
        super(NewsAdmin,self).save_model(request,obj,form,change)

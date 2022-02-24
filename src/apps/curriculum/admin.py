from django.contrib import admin
from curriculum.models import Curriculum,UserTask
# Register your models here.

@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def save_model(self,request,obj,form,change):
        obj.user = request.user
        obj.save()
        super(CurriculumAdmin,self).save_model(request,obj,form,change)


@admin.register(UserTask)
class UserTask(admin.ModelAdmin):
    list_display = ("user","curriculum","content","creation_date","is_active",)
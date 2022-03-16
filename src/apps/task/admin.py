from django.contrib import admin
from task.models import Curriculum,UserTask
# Register your models here.

@admin.register(Curriculum)
class TaskAdmin(admin.ModelAdmin):
    exclude = ("user",)
    list_display = ("id","title","task_type",)

    def save_model(self,request,obj,form,change):
        obj.user = request.user
        obj.save()
        super(TaskAdmin,self).save_model(request,obj,form,change)


@admin.register(UserTask)
class UserTask(admin.ModelAdmin):pass
    #list_display = ("user","curriculum","content","creation_date","is_active",)
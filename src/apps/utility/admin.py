from django.contrib import admin
from utility.models import MetaContent
# Register your models here.

@admin.register(MetaContent)
class MetaContentAdmin(admin.ModelAdmin):
    exclude = ("user",)
    list_display = ("title","slug","creation_date","last_update","is_active",)


    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
        return super().save_model(request, obj, form, change)

from django.contrib import admin
from pledge.models import Pledge,PledgeData,UserPledge
# Register your models here.
from modeltranslation.admin import TranslationAdmin,TranslationTabularInline,TranslationStackedInline


class PledgeDataInline(TranslationStackedInline):
    model = PledgeData

@admin.register(Pledge)
class PledgeAdmin(TranslationAdmin):
    exclude = ("user",)
    readonly_fields = ("slug",)
    list_display = ("title","slug","creation_date","is_active")
    inlines = [PledgeDataInline,]

    def save_model(self,request,obj,form,change):
        obj.user = request.user
        obj.save()
        super(PledgeAdmin,self).save_model(request,obj,form,change)


@admin.register(UserPledge)
class UserPledgeAdmin(admin.ModelAdmin):
    list_display = ("user","pledge","creation_date",)

    
from django.contrib import admin
from utility.models import MetaContent,MetaContentCategory,Suggestion
# Register your models here.
from modeltranslation.admin import TranslationAdmin

@admin.register(MetaContentCategory)
class MetaContentCategoryAdmin(admin.ModelAdmin):
    exclude = ("user",)
    readonly_fields = ("slug",)
    list_display = ("id","title","slug",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
        return super().save_model(request, obj, form, change)


@admin.register(MetaContent)
class MetaContentAdmin(TranslationAdmin):
    exclude = ("user",)
    readonly_fields = ("slug",)
    list_display = ("title","slug","creation_date","last_update","is_active",)


    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
        return super().save_model(request, obj, form, change)

@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    exclude = ("user",)

    list_display = ("title","creation_date","is_active",)


    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
        return super().save_model(request, obj, form, change)

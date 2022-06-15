from django.contrib import admin
from scholarship.models import Scholarship,ScholarshipTask,ScholarshipSubTask,UserScholarshipTask
from modeltranslation.admin import TranslationAdmin,TranslationTabularInline,TranslationStackedInline


# Register your models here.

@admin.register(Scholarship)
class ScholarshipAdmin(TranslationAdmin):pass

class ScholarshipSubTaskInline(TranslationStackedInline):
    model = ScholarshipSubTask

@admin.register(ScholarshipTask)
class ScholarshipTaskAdmin(TranslationAdmin):
    inlines = [ScholarshipSubTaskInline,]

@admin.register(UserScholarshipTask)
class UserScholarshipTaskAdmin(admin.ModelAdmin):
    pass    
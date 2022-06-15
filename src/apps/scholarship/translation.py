# -*- coding: utf-8 -*-
# Model Translation
from modeltranslation.translator import translator, TranslationOptions
from scholarship.models import Scholarship,ScholarshipTask,ScholarshipSubTask



class ScholarshipOptions(TranslationOptions):
    fields = ('title', 'content',)   # Select here the fields you want to translate  
translator.register(Scholarship, ScholarshipOptions)


class ScholarshipTaskOptions(TranslationOptions):
    fields = ('title',)   # Select here the fields you want to translate  
translator.register(ScholarshipTask, ScholarshipTaskOptions)

class ScholarshipSubTaskOptions(TranslationOptions):
    fields = ('title',)   # Select here the fields you want to translate  
translator.register(ScholarshipSubTask, ScholarshipSubTaskOptions)

# You can add as many models as you want to translate here
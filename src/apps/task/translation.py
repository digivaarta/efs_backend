# -*- coding: utf-8 -*-
# Model Translation
from modeltranslation.translator import translator, TranslationOptions
from task.models import Curriculum


class CurriculumOptions(TranslationOptions):
    fields = ('title', 'content')   # Select here the fields you want to translate  
translator.register(Curriculum, CurriculumOptions)

# You can add as many models as you want to translate here
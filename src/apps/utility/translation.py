# -*- coding: utf-8 -*-
# Model Translation
from modeltranslation.translator import translator, TranslationOptions
from utility.models import MetaContent,Suggestion


class MetaContentOptions(TranslationOptions):
    fields = ('title', 'content')   # Select here the fields you want to translate  
translator.register(MetaContent, MetaContentOptions)


# You can add as many models as you want to translate here
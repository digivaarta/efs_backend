# -*- coding: utf-8 -*-
# Model Translation
from modeltranslation.translator import translator, TranslationOptions
from news.models import News


class NewsOptions(TranslationOptions):
    fields = ('title', 'description',"content",)   # Select here the fields you want to translate  
translator.register(News, NewsOptions)

# You can add as many models as you want to translate here
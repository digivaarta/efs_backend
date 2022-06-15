# -*- coding: utf-8 -*-
# Model Translation
from modeltranslation.translator import translator, TranslationOptions
from banners.models import Banner


class BannerOptions(TranslationOptions):
    fields = ('title', 'description',"image",)   # Select here the fields you want to translate  
translator.register(Banner, BannerOptions)

# You can add as many models as you want to translate here
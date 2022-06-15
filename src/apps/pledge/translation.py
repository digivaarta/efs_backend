# -*- coding: utf-8 -*-
# Model Translation
from modeltranslation.translator import translator, TranslationOptions
from pledge.models import Pledge,PledgeData


class PledgeOptions(TranslationOptions):
    fields = ('title', 'cover_image',)   # Select here the fields you want to translate  
translator.register(Pledge, PledgeOptions)


class PledgeDataOptions(TranslationOptions):
    fields = ('title',"content" ,'cover_image',)   # Select here the fields you want to translate  
translator.register(PledgeData, PledgeDataOptions)

# You can add as many models as you want to translate here
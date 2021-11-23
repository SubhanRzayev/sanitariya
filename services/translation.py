from modeltranslation.translator import translator, TranslationOptions
from .models import Services

class ServicesTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

translator.register(Services, ServicesTranslationOptions)
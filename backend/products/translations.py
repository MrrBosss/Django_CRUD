from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import Product, ProductWeight, FAQ, Banner , Brand


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'content')



@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title','subtitle')


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')



@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ('brands', 'name')

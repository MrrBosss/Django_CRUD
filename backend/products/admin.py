from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

# Register your models here.
from .models import Product, ProductWeight, FAQ, Banner , Brand
from .models import ProductList, ProductColor
# from .models import 

# admin.site.register(ProductRetrieve)

admin.site.register(ProductList)

admin.site.register(Product)

admin.site.register(ProductWeight)    

admin.site.register(ProductColor)

admin.site.register(FAQ)

admin.site.register(Banner)

admin.site.register(Brand)


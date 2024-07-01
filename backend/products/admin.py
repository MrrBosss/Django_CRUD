from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

# Register your models here.
from .models import Product, ProductWeight, FAQ, Banner , Brand, Category, Order
from .models import  ProductColor #ProductList
# from .models import 

# admin.site.register(ProductRetrieve)

# admin.site.register(ProductList)

admin.site.register(Order)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']

admin.site.register(ProductWeight)    

admin.site.register(ProductColor)

admin.site.register(Category)

admin.site.register(FAQ)

admin.site.register(Banner)

admin.site.register(Brand)


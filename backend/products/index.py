from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from products.models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    # should_index = 'is_public'
    fields = [
        'title',
        'content',
        'price',
        'user',
        'public'
    ]   
    settings = {
        'searchableAttributes' : ['titile', 'content'],
        'attributesForFaceting' : ['user', 'public']
    }
    tags = 'get_tags_list'

    # admin.site.register(Product, ProductModelAdmin)
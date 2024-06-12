from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from products.models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    # should_index = 'is_public'
    fields = [
        'title',
        'body',
        'price',
        'user',
        'public',
        'path',
        'endpoint',
    ]   
    settings = {
        'searchableAttributes' : ['titile', 'body'],
        'attributesForFaceting' : ['user', 'public']
    }
    tags = 'get_tags_list'

    # admin.site.register(Product, ProductModelAdmin)
# filters.py
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    price__gte = django_filters.NumericRangeFilter(field_name='price', lookup_expr='gte')
    price__lte = django_filters.NumericRangeFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['price__gte', 'price__lte']

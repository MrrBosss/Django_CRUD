# filters.py
import django_filters
from .models import Product, ProductColor, ProductWeight

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    weight = django_filters.ModelMultipleChoiceFilter(
        field_name='weight', # shetda xato
        queryset=ProductWeight.objects.all(),
        label='Weight'
    )

    color = django_filters.ModelMultipleChoiceFilter(
        field_name='color',
        queryset=ProductColor.objects.all(),
        label='Color'
    )

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'weight', 'color']



# class ProductFilter(django_filters.FilterSet):
#     weight = django_filters.ModelMultipleChoiceFilter(
#         field_name='weight__id',
#         queryset=ProductWeight.objects.all(),
#         label='Weight'
#     )

#     color = django_filters.ModelMultipleChoiceFilter(
#         field_name='color__id',
#         queryset=ProductColor.objects.all(),
#         label='Color'
#     )

#     class Meta:
#         model = Product
#         fields = ['weight', 'color']
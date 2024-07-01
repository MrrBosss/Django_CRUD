# filters.py
import django_filters
from .models import Product, ProductColor, ProductWeight

class ProductFilter(django_filters.FilterSet):
    price__gte = django_filters.NumericRangeFilter(field_name='price', lookup_expr='gte')
    price__lte = django_filters.NumericRangeFilter(field_name='price', lookup_expr='lte')
    weight = django_filters.ModelMultipleChoiceFilter(
        field_name='weight__id',
        queryset=ProductWeight.objects.all(),
        label='Weight'
    )

    color = django_filters.ModelMultipleChoiceFilter(
        field_name='color__id',
        queryset=ProductColor.objects.all(),
        label='Color'
    )

    class Meta:
        model = Product
        fields = ['price__gte', 'price__lte', 'weight', 'color']



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
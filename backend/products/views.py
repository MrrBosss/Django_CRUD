from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics,mixins, viewsets
from .models import Product, FAQ, Banner, Brand, ProductWeight, ProductColor, Category, Order # ProductList
from .serializers import ProductSerializer, ProductSerializer, FAQSerializer, BannerSerializer, BrandSerializer, ProductWeightSerializer
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
from rest_framework.pagination import PageNumberPagination
from .serializers import ProductSerializer
from rest_framework import generics
from rest_framework import filters
from .serializers import  ProductColorSerializer, ProductDetailSerializer, CategorySerializer, OrderSerializer
import django_filters.rest_framework
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from decimal import Decimal




class ProductListCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)
        #send a Django signal

    # def get_queryset(self,*args,**kwargs):
    #     qs = super().get_queryset(*args,**kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     # print(request.user)
    #     return qs.filter(user=request.user)


product_list_create_view = ProductListCreateAPIView.as_view()
    


class ProductDetailAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = 'pk'

product_detail_view = ProductDetailAPIView.as_view()




class ProductUpdateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            ##
        
product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    
    def perform_destroy(self, instance):
        #instance
        super().perform_destroy(instance)
      
        
product_destroy_view = ProductDestroyAPIView.as_view()



# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     #lookup_field = 'pk'

# product_list_view = ProductListAPIView.as_view()



class ProductWeightViewSet(viewsets.ModelViewSet):
    queryset = ProductWeight.objects.all()
    serializer_class = ProductWeightSerializer
    http_method_names = ['get']
    pagination_class = None



class ProductColorViewset(viewsets.ModelViewSet):
    queryset = ProductColor.objects.all()
    serializer_class = ProductColorSerializer
    http_method_names = ['get']
    pagination_class = None



class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get']
    pagination_class = None




class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    http_method_names = ['get']
    pagination_class = None
    


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    http_method_names = ['get']
    pagination_class = None
    


class BrandViewSet(mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet
):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = None


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'
    max_page_size = 1000

# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 100
#     page_size_query_param = 'page_size'
#     max_page_size = 1000




class BannerView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    pagination_class = LargeResultsSetPagination


    
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter



class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
   



# class ProductListView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     http_method_names = ['get']
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
#     filterset_fields = ['weight', 'color', 'categories'] 



# class ProductList(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     http_method_names = ['get']
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = ProductFilter



class Orderview(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['post']



# class ProductColorView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailSerializer

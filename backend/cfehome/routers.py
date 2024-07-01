from rest_framework.routers import DefaultRouter
from django.urls import path
from products.views import FAQViewSet, BrandViewSet, BannerViewSet, ProductWeightViewSet, Orderview
from products.views import ProductDetailView, ProductColorViewset, ProductList, CategoryView  # ProductColorView



router = DefaultRouter()
# router.register('products', ProductViewSet, basename='products')
# router.register('orders', Orderview, basename='orders')
router.register('products-color', ProductColorViewset, basename='products-color')
router.register('products-weight', ProductWeightViewSet, basename='products-weight')
# router.register('products-list', ProductList.as_view(), basename='products-list')
router.register('categories', CategoryView, basename='categories')
router.register('faqs', FAQViewSet, basename='faqs')
router.register('banners', BannerViewSet, basename='banners')
router.register('brands', BrandViewSet, basename='brands')
urlpatterns = router.urls
urlpatterns += [
    path('orders/', Orderview.as_view(), name='orders'),
    path('products-list/', ProductList.as_view(), name='products-list'),
    path("products-detail/<int:pk>/", ProductDetailView.as_view(), name='product-detail'),
]


# TODO = Kairat Sūltan, [28.06.2024 12:18]
# Endi detail product serializeri uchun boshqa huddi shunaqa serializer yangidan yozasiz

# Kairat Sūltan, [28.06.2024 14:06]
# Keyin weights uchun serializer yozib nested qilasiz
from rest_framework.routers import DefaultRouter
from django.urls import path
from products.views import FAQViewSet, BrandViewSet, BannerViewSet, ProductWeightViewSet, ProductListViewSet

from products.views import ProductListDetailView


router = DefaultRouter()
router.register('product-weights', ProductWeightViewSet, basename='product-weights')
router.register('products', ProductListViewSet, basename='product lists')
router.register('faqs', FAQViewSet, basename='faqs')
router.register('banners', BannerViewSet, basename='banners')
router.register('brands', BrandViewSet, basename='brands')
urlpatterns = router.urls
urlpatterns += [
    path("products-detail/<int:pk>/", ProductListDetailView.as_view(), name='product-detail')
]


# TODO = Kairat Sūltan, [28.06.2024 12:18]
# Endi detail product serializeri uchun boshqa huddi shunaqa serializer yangidan yozasiz

# Kairat Sūltan, [28.06.2024 14:06]
# Keyin weights uchun serializer yozib nested qilasiz
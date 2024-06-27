from rest_framework.routers import DefaultRouter

from products.views import FAQViewSet, BrandViewSet, BannerViewSet, ProductViewSet, ProductWeightViewSet


router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('product weights', ProductWeightViewSet, basename='product weights')
router.register('faqs', FAQViewSet, basename='faqs')
router.register('banners', BannerViewSet, basename='banners')
router.register('brands', BrandViewSet, basename='brands')
urlpatterns = router.urls

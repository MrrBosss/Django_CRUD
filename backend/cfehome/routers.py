from rest_framework.routers import DefaultRouter

from products.views import FAQViewSet, BrandViewSet, BannerViewSet, ProductViewSet, ProductWeightViewSet, ProductListViewSet


router = DefaultRouter()
router.register('product-lists', ProductListViewSet, basename='product lists')
router.register('products', ProductViewSet, basename='products')
router.register('product-weights', ProductWeightViewSet, basename='product weights')
router.register('faqs', FAQViewSet, basename='faqs')
router.register('banners', BannerViewSet, basename='banners')
router.register('brands', BrandViewSet, basename='brands')
urlpatterns = router.urls



# TODO = Kairat Sūltan, [28.06.2024 12:18]
# Endi detail product serializeri uchun boshqa huddi shunaqa serializer yangidan yozasiz

# Kairat Sūltan, [28.06.2024 14:06]
# Keyin weights uchun serializer yozib nested qilasiz
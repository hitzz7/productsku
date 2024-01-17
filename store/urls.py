from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductImageViewSet,ProductViewSet,ItemViewSet

router = DefaultRouter()

router.register(r'product', ProductViewSet, basename='product')
router.register(r'image', ProductImageViewSet, basename='image')
router.register(r'item', ItemViewSet, basename='item')

urlpatterns = router.urls
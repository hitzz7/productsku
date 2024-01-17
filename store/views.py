from rest_framework import viewsets,status
from .models import Product,ProductImage,Items
from .serializers import ProductSerializer,ProductImageSerializer,ItemSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class =ProductSerializer
    
class ItemViewSet(viewsets.ModelViewSet):
    queryset=Items.objects.all()
    serializer_class =ItemSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset=ProductImage.objects.all()
    serializer_class =ProductImageSerializer


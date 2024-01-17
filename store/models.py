from django.db import models
from django.core.files.base import ContentFile
from mptt.models import MPTTModel, TreeForeignKey
from PIL import Image

from django.conf import settings
from datetime import datetime
import uuid
import random
import string


# Create your models here.
class Product(MPTTModel):
    name = models.CharField(max_length=255,unique=True)
    parent = TreeForeignKey("self",on_delete=models.CASCADE,null=True,blank=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Items(models.Model):
    
    
    sku = models.CharField(max_length=50, unique=True)
    PENDING='pending'
    ACTIVE='active'
    Inactive='inactive'
    status_choices=(
        (PENDING,'pending'),
        (ACTIVE,'active'),
        (Inactive,'inactive'),
        
        
    )
    
        

    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default=PENDING,
    )

    
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="items")
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=100)
    
    class Meta:
        indexes = [
            models.Index(fields=["sku","status","size","color","price"]),
            
            
        ]
    
   
    def __str__(self):
        return self.sku
    
    # def generate_random_sku(product_code, color_code, size_code):
    #     # Generate a random alphanumeric string
    #     random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    #     # Format the SKU using the provided information and the random part
    #     sku = f'{product_code}-{color_code}-{size_code}-{random_part}'

    #     return sku
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")
    image = models.ImageField(upload_to ='',blank=True, null=True)
    
    
    class Meta:
        indexes = [
            models.Index(fields=["image"]),
            
            
        ]
    def __str__(self):
        return f"Image for {self.product.name}"
from .models import  Product,ProductImage,Items
from rest_framework import serializers
import random
import string


# def generate_random_sku(product_code, color_code, size_code):
#     # Generate a random alphanumeric string
#     random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

#     # Format the SKU using the provided information and the random part
#     sku = f'{product_code}-{color_code}-{size_code}-{random_part}'

#     return sku

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Items
        fields =['id','size','color','status','sku','price','product']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Check the request method
        if self.context['request'].method == 'GET':
            # Remove the 'product' field from the serialized data for GET requests
            data.pop('product')

        return data
        
    # def create(self, validated_data):
    #     product_code = validated_data['product'].name[:3].upper()  # Using the first 3 characters of the product name
    #     color_code = validated_data['color'][:2].upper()  # Using the first 2 characters of the color
    #     size_code = validated_data['size'][:1].upper()  # Using the first character of the size

    #     # Call the generate_random_sku function to generate SKU
    #     sku = generate_random_sku(product_code, color_code, size_code)

    #     # Set the generated SKU in the validated_data before creating the instance
    #     validated_data['sku'] = sku

    #     # Call the create method of the parent class (ModelSerializer) to create the instance
    #     return super().create(validated_data)
        
    
        
class ProductImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImage
        fields = ['id','image','product']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Check the request method
        if self.context['request'].method == 'GET':
            # Remove the 'product' field from the serialized data for GET requests
            data.pop('product')

        return data
        
    
    
class ProductSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True,required=False)
    images = ProductImageSerializer(many=True,required=False)
    class Meta:
        model = Product
        fields = ['id','name','description','items','images']
        
# ['id','name','description','Images','Items']
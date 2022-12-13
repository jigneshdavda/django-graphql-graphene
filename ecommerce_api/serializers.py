from rest_framework import serializers
from .models import Shop, Products

class ShopSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.id')
    
    class Meta:
        model = Shop
        fields = "__all__"
        
class ProductsSerializer(serializers.ModelSerializer):
    # shop = serializers.ReadOnlyField(source='shop.id')
    
    class Meta:
        model = Products
        fields = "__all__"
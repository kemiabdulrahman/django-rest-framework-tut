from rest_framework import serializers
from .models import Item, Shop

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'shop']
        
class ShopSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Shop
        fields = ['id', 'name', 'owner', 'items']
    


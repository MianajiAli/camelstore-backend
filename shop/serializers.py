from rest_framework import serializers
from .models import Category, Product, Cart, CartItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'description']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'category', 'price', 'quantity_in_stock', 'description', 'image_url', 'date_added', 'last_updated', 'status']

class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'get_total_price']

    def get_total_price(self, obj):
        return obj.product.price * obj.quantity

    def create(self, validated_data):
        return CartItem.objects.create(**validated_data)
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=False)

    class Meta:
        model = Cart
        fields = ['id', 'created_at', 'updated_at', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        cart = Cart.objects.create(**validated_data)
        for item_data in items_data:
            CartItem.objects.create(cart=cart, **item_data)
        return cart

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', [])
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()

        # Handle CartItem updates
        for item_data in items_data:
            item_id = item_data.get('id')
            if item_id:
                item = CartItem.objects.get(pk=item_id, cart=instance)
                item.quantity = item_data.get('quantity', item.quantity)
                item.save()
            else:
                CartItem.objects.create(cart=instance, **item_data)

        return instance

from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('id','name', 'description', 'price', 'stock', 'image')

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price can not be less than 0')

        return value



class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(
        max_digits=10, 
        decimal_places=2,
        source='product.price')


      
    class Meta:
        model = models.OrderItem
        fields = ('product_name', 'product_price', 'quantity','item_subtotal')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='total')

    def total(self, obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)


    class Meta:
        model = models.Order
        fields = ('order_id', 'user','created_at','status','products', 'items', 'total_price')










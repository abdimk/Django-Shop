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

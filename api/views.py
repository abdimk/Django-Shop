from django.db.models import Max
from django.http import JsonResponse,HttpResponse
from django.shortcuts import get_object_or_404
from api.serializers import *
from api.models import Product,Order
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serialized_products = ProductSerializer(products, many=True)

    return Response(serialized_products.data)


@api_view(['GET'])
def product(request, id):
    single_product = get_object_or_404(Product, id=id)
    serialized_single_product = ProductSerializer(single_product)
    return Response(serialized_single_product.data)

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.prefetch_related('items__product')
    order_serializer = OrderSerializer(orders, many=True)
    return Response(order_serializer.data)

@api_view(['GET'])
def product_info(request):
    products = models.Product.objects.all()
    product_info = ProductInfoSerializer({
        'products':products,
        'count':len(products),
        'max_price':products.aggregate(max_price=Max('price'))['max_price']
    })
    return Response(product_info.data)





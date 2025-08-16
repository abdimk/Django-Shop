from django.db.models import Max
from django.http import JsonResponse,HttpResponse
from django.shortcuts import get_object_or_404
from api.serializers import *
from api.models import Product,Order
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView

# @api_view(['GET'])
# def product_list(request):
#     products = Product.objects.all()
#     serialized_products = ProductSerializer(products, many=True)

#     return Response(serialized_products.data)


class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.exclude(stock__gt=0)
    serializer_class = ProductSerializer



# @api_view(['GET'])
# def product(request, id):
#     single_product = get_object_or_404(Product, id=id)
#     serialized_single_product = ProductSerializer(single_product)
#     return Response(serialized_single_product.data)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    




# @api_view(['GET'])
# def order_list(request):
#     orders = Order.objects.prefetch_related('items__product')
#     order_serializer = OrderSerializer(orders, many=True)
#     return Response(order_serializer.data)

class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer


class UserOrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]



    """
    Dynamic filtering in get queryset method
    if you have a dynamic data such as a user account and if you want to fetch
    data assocated with it you can you this

    You can overried get queryset method like this
    """
    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
    


class ProductInfoAPIView(APIView):
    def get(self, request):
        products = models.Product.objects.all()
        product_info = ProductInfoSerializer({
            'products':products,
            'count':len(products),
            'max_price':products.aggregate(max_price=Max('price'))['max_price']
        })
        return Response(product_info.data)




# @api_view(['GET'])
# def product_info(request):
#     products = models.Product.objects.all()
#     product_info = ProductInfoSerializer({
#         'products':products,
#         'count':len(products),
#         'max_price':products.aggregate(max_price=Max('price'))['max_price']
#     })
#     return Response(product_info.data)
    

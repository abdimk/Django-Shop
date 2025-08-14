from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.ProductListAPIView.as_view(), name="products"),
    path('products/info/', views.product_info),
    path('products/<int:pk>/',views.ProductDetailAPIView.as_view(), name="singleProduct"),
    path('orders/', views.OrderListAPIView.as_view()),
]


















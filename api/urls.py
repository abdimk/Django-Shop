from django.urls import path
from . import views

urlpatterns = [
    # path('products/',views.ProductListAPIView.as_view(), name="products"),
    path('products/', views.ProductListCreateAPIView.as_view(), name="products"),

    # path('products/create', views.ProductCreateAPIView.as_view(), name="product_create"),
    path('products/info/', views.ProductInfoAPIView.as_view()),
    path('products/<int:pk>/',views.ProductDetailAPIView.as_view(), name="singleProduct"),
    path('orders/', views.OrderListAPIView.as_view()),
    path('user-orders/', views.UserOrderListAPIView.as_view(), name='user_orders')
]


















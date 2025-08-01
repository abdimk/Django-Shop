from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.product_list),
    path('products/<int:id>/',views.product),
    path('orders/', views.order_list),
]


















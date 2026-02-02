from django.urls import path
from .views import (
    ProductListAPIView,
    ProductDetailAPIView,
    CustomerListAPIView
)

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('customers/', CustomerListAPIView.as_view(), name='customer-list'),
]

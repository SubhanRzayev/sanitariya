from product.views import ProductDetailView, ProductView
from django.urls import path

app_name = 'product'

urlpatterns = [
    path('product/', ProductView.as_view(), name='products'),
    path('product-detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

]

from django.urls import path
from .views import ProductList, ProductDetails


app_name = 'playground'

urlpatterns = [
    path('product-list', ProductList.as_view(), name='all-products'),
    path('product-details/<int:pk>', ProductDetails.as_view(), name='product-detail') # noqa
]

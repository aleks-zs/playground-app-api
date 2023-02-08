from django.urls import path
from .views import ProductList, ProductDetails


app_name = 'playground'

urlpatterns = [
    path('product', ProductList.as_view(), name='product-list'),
    path('product/<int:pk>', ProductDetails.as_view(), name='product-detail') # noqa
]

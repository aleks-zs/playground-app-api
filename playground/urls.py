from django.urls import path
from .views import ProductList, ProductDetails


urlpatterns = [
    path('product-list', ProductList.as_view()),
    path('product-details/<int:pk>', ProductDetails.as_view())
]

from rest_framework import generics

from core.models import Product
from playground.serializers import ProductSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetails(generics.RetrieveAPIView,
                     generics.CreateAPIView,
                     generics.UpdateAPIView,
                     generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Product
from playground.serializers import ProductSerializer

from decimal import Decimal


ALL_PRODUCTS_URL = reverse('playground:all-products')


def detail_url(product_id):
    return reverse('product-detail', args=[product_id])


def create_product(**params):
    return Product.objects.create(**params)


class ProductApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

        create_product(
            title='FirstTitle',
            content='FirstContent',
            price=Decimal('1.00')
        )
        create_product(
            title='SecondTitle',
            content='SecondContent',
            price=Decimal('2.00')
        )

    def test_get_all_products(self):
        res = self.client.get(ALL_PRODUCTS_URL)

        products = Product.objects.all().order_by('id')
        serializer = ProductSerializer(products, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_product_by_id(self):
        pass

    def test_create_product(self):
        pass

    def test_update_whole_product(self):
        pass

    def test_partially_update_the_product(self):
        pass

    def test_delete_the_product(self):
        pass

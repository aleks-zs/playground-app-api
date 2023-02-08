from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Product
from playground.serializers import ProductSerializer

from decimal import Decimal


ALL_PRODUCTS_URL = reverse('playground:product-list')


def detail_url(product_id):
    return reverse('playground:product-detail', args=[product_id])


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
        products = Product.objects.all().order_by('id')
        serializer = ProductSerializer(products, many=True)

        res = self.client.get(ALL_PRODUCTS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_product(self):
        payload = {
            'title': 'InitialTitle',
            'content': 'InitialContent',
            'price': Decimal('0.00')
        }

        res = self.client.post(ALL_PRODUCTS_URL, payload, format='json')
        product = Product.objects.get(title=payload['title'])
        serializer = ProductSerializer(product)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data, serializer.data)

    def test_get_product_by_id(self):
        product = Product.objects.get(pk=1)
        serializer = ProductSerializer(product)

        res = self.client.get(detail_url(1))

        self.assertEqual(res.data, serializer.data)

    def test_update_whole_product(self):
        payload = {
            'title': 'WholeTitle',
            'content': 'WholeContent',
            'price': Decimal('100.00')
        }

        res = self.client.put(detail_url(1), payload, format='json')
        product = Product.objects.get(pk=1)
        serializer = ProductSerializer(product)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, res.data)
        self.assertFalse(Product.objects.filter(title='FirstTitle').exists())

    def test_partially_update_the_product(self):
        payload = {
            'content': 'PartialContent'
        }

        res = self.client.patch(detail_url(2), payload, format='json')
        product = Product.objects.get(pk=2)
        serializer = ProductSerializer(product)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, res.data)
        self.assertFalse(Product.objects.filter(content='SecndContent').exists()) # noqa

    def test_delete_the_product(self):
        res = self.client.delete(detail_url(1))

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.all().count(), 1)
        self.assertFalse(Product.objects.filter(title='FirstTitle').exists())

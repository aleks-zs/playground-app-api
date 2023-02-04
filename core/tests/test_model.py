from django.test import TestCase

from decimal import Decimal
from core.models import Product


class ModelTests(TestCase):

    def test_create_product(self):
        test_title = 'ProductTitle'
        test_content = 'ProductContent'
        test_price = Decimal('10.00')

        test_product = Product.objects.create(
            title=test_title,
            content=test_content,
            price=test_price
        )

        self.assertEqual(test_product.title, test_title)
        self.assertEqual(test_product.content, test_content)
        self.assertEqual(test_product.price, test_price)

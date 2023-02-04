from django.db import models # noqa


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    @property
    def sale_price(self):
        return '%.2f' % (float(self.price) * 0.9)

    def get_discount(self):
        return '%.2f' % (float(self.price) * 0.95)

    def __str__(self):
        return self.title

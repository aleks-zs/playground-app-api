from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('title', 'price')


admin.site.register(Product)

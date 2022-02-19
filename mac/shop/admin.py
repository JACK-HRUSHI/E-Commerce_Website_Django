from django.contrib import admin

from . models import Product, Orders

admin.site.register(Product)
admin.site.register(Orders)

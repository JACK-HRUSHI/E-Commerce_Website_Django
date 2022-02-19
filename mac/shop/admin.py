from django.contrib import admin

from . models import Product, Contact, Orders

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)

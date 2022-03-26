from django.contrib import admin

from . models import Blogpost, Suggest

admin.site.register(Blogpost)
admin.site.register(Suggest)

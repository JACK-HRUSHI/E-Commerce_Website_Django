# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='blogHome'),
    path("blogPost/<int:id>", views.blogpost, name='blogPost')
]
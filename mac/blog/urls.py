# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='blogHome'),
    path("suggest/", views.suggest, name='Suggest'),
    path("blogPost/<int:id>", views.blogpost, name='blogPost')
]
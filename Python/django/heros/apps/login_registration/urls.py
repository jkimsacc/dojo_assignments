from django.conf.urls import url, render, redirect
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index)
]

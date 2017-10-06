from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register/$', views.register),
    url(r'^process$', views.register_user),
    url(r'^logging$', views.logging),
]

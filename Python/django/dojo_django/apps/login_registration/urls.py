from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_registration),
    url(r'^register', views.register),
    url(r'^login', views.register),
    url(r'^temp_login', views.temp_login),
]

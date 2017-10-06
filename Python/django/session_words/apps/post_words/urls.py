from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process/', views.add_word),
    url(r'^reset/', views.reset)
]

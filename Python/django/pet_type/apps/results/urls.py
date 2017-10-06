from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.add),
    url(r'^process', views.process),
    url(r'^results', views.results),
]

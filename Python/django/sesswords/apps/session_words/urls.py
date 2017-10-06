from django.conf.urls import url
from . import views

print "urls.py loaded"

urlpatterns = [
    url(r'^$', views.index)
]

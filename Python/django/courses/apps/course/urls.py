from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^add', views.add),
    url(r'^(?P<course_id>\d+)/remove$', views.remove),
]

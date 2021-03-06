from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/new', views.new, name='new_user'),
    url(r'^/create', views.create),
    url(r'^/(?P<user_id>\d+)$', views.show, name='(?P<user_id>\d+) page'),
    url(r'^/(?P<user_id>\d+)/edit$', views.edit),
    url(r'^/(?P<user_id>\d+)/update$', views.update),
    url(r'^/(?P<user_id>\d+)/delete$', views.destroy),
]

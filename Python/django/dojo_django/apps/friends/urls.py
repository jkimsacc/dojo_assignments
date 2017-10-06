from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.friends),
    url(r'^add/(?P<friend_id>\d+)', views.add),
    url(r'^remove/(?P<friend_id>\d+)', views.remove),
]

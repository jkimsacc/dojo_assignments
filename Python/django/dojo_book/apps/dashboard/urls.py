from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^poke/(?P<poked_id>\d+)', views.poke),
]

from django.conf.urls import url, include
from django.contrib import admin

print "urls.py session loaded"

urlpatterns = [
    url(r'^', include('apps.session_words.urls')),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.user_page),
    url(r'^add$', views.add_book_review),
    url(r'^adding$', views.adding_book_review_author),
    url(r'^(?P<book_id>\d+)$', views.book_page),
]

from __future__ import unicode_literals

from django.db import models
from ..login.models import User

# Create your models here.

class AuthorManager(models.Manager):
    def author_validate(self, post_data):
        results = {'status': True, 'errors': []}
        if not len(self.filter(author = post_data['author'])) > 0:
            results['errors'].append('Author already registered')


class Author(models.Model):
    author_name = models.CharField(max_length=100)

class Book(models.Model):
    book_title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name = "written_by")

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    book = models.ForeignKey(Book, related_name = "review_of")
    user = models.ForeignKey(User, related_name = "review_by")

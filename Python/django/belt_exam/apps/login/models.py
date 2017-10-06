from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

class UserManager(models.Manager):
    def registration_validation(self, post_data):
        results = {'status': True, 'errors': []}
        if len(post_data['f_name']) < 2 or len(post_data['l_name']) <2:
            results['errors'].append('First name must be at least 2 letters long')
        if not re.match(NAME_REGEX, post_data['f_name']) or not re.match(NAME_REGEX, post_data['l_name']):
            results['errors'].append('Name must ber all letters')
        if not re.match(EMAIL_REGEX, post_data['email']):
            results['errors'].append('Invalid email format')
        if len(self.filter(email = post_data['email'])) > 0:
            results['errors'].append("Email already in use")
        if len(post_data['password']) < 1:
            results['errors'].append('Your password shold be at least 8 characters long')
        if post_data['password'] != post_data['confirm_pw']:
            results['errors'].append('Your password does not match')
        if len(results['errors']) > 0:
            results['status'] = False
        return results

    def creator(self, post_data):
        hashed = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())
        new_user = self.create(
        f_name = post_data['f_name'],
        l_name = post_data['l_name'],
        email = post_data['email'],
        password = hashed,
        )
        return new_user

    def login_validation(self, post_data):
        results = {'status': True, 'errors': [], 'user': None}
        if len(self.filter(email = post_data['email'])) == 0:
            results['errors'].append('Email not registered')
        else:
            results['user'] = self.filter(email = post_data['email'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), results['user'].password.encode()):
                results['errors'].append('Wrong password')

        if len(results['errors']) > 0:
            results['status'] = False
        return results


# Create your models here.
class User(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    objects = UserManager()

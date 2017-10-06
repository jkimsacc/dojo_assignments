# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
import datetime
from django.db import models

EMAIL_REGEX = re.compile(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

class UserManager(models.Manager):
    def register_val(self, post_data):
        results = {'status': True, 'errors': [], 'user': None}
        if len(self.filter(email = post_data['email'])) > 0:
            results['errors'].append('Email already in use')
        if not re.match(EMAIL_REGEX, post_data['email']):
            results['errors'].append('Invalid email format')
        if post_data['email'] != post_data['confirm_email']:
            results['errors'].append('Email does not match')
        if len(post_data['first_name']) < 2 or len(post_data['last_name']) <2:
            results['errors'].append('First name must be at least 2 letters long')
        if not re.match(NAME_REGEX, post_data['first_name']) or not re.match(NAME_REGEX, post_data['last_name']):
            results['errors'].append('Name must ber all letters')
        if datetime.date.today().year + datetime.date.today().month/100 + datetime.date.today().day/10000 - datetime.datetime.strptime(post_data['birthday'], '%Y-%m-%d').year - datetime.datetime.strptime(post_data['birthday'], '%Y-%m-%d').month/100 - datetime.datetime.strptime(post_data['birthday'], '%Y-%m-%d').day/10000 < 18:
            results['errors'].append('You must be 18 or older')
        if len(post_data['username']) < 2:
            results['errors'].append('Username need to be more than 2 characters')
        if len(self.filter(username = post_data['username'])) > 0:
            results['errors'].append('Username already taken')
        if len(post_data['password']) < 5:
            results['errors'].append('Your password should be at least 6 letters')
        if post_data['password'] != post_data['confirm_password']:
            results['errors'].append('Your password does not match')
        if len(results['errors']) > 0:
            results['status'] = False
        return results

    def create_user(self, post_data):
        hashed = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())
        user = self.create(
            email = post_data['email'],
            username = post_data['username'],
            first_name = post_data['first_name'][0].upper()+post_data['first_name'][1:].lower(),
            last_name = post_data['last_name'][0].upper()+post_data['last_name'][1:].lower(),
            birthday = post_data['birthday'],
            password = hashed,
        )
        return user

    def login_val(self, post_data):
        results = {'status': True, 'errors': [], 'user': None}
        if len(self.filter(email = post_data['email'])) == 0:
            results['errors'].append('Invalid Email or Password')
        else:
            results['user'] = self.filter(email = post_data['email'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), results['user'].password.encode()):
                results['errors'].append('Invalid Email or Password')
        if len(results['errors']) > 0:
            results['status'] = False
        return results

class User(models.Model):
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateTimeField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()


# Create your models here.

from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

class UserManager(models.Manager):
    def validate_register(self, post_Data):
        errors = []
        if len(post_Data['first_name']) < 2 or len(post_Data['last_name']) <2:
            errors.append('name must be longer than 3 letters')
        if not re.match(NAME_REGEX, post_Data['first_name']) or not re.match(NAME_REGEX, post_Data['last_name']):
            errors.append('name fields must be letter characters')
        if not re.match(EMAIL_REGEX, post_Data['email']):
            errors.append('invalid email')
        if len(User.objects.filter(email=post_Data['email'])) > 0:
            errors.append("email already in use")
        if post_Data['password'] != post_Data['confirm']:
            errors.append("passwords do not match")
        if not errors:
            hashed_password = bcrypt.hashpw(post_Data['password'].encode(), bcrypt.gensalt(5))

            new_user = self.create(
                first_name = post_Data['first_name'],
                last_name = post_Data['last_name'],
                email = post_Data['email'],
                password = hashed_password,
            )
            return new_user
        return errors

    def validate_login(self, post_Data):
        errors = []
        if len(self.filter(email=post_Data['email'])) > 0:
            user = self.filter(email=post_Data['email'])[0]
            if not bcrypt.checkpw(post_Data['password'].encode(), user.password.encode()):
                errors.append('incorrect email or password')
        else:
            errors.append('incorrect email or password')
        if errors:
            return errors
        return user

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()


# Create your models here.

from __future__ import unicode_literals
import re
from django.db import models

EMAIL_REGEX = re.compile(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')

class UserManager(models.Manager):
    def validate(self, post_Data):
        errors = {}
        for field, value in post_Data.iteritems():
            if len(field) < 1:
                errors[field] = "{} field is required".format(field.replace('_', ''))
            if field == "first_name" or field == "last_name":
                if not field in errors and len(value) < 2:
                    errors[field] = "{} field must be at least 2 characters".format(field.replace('_',''))
        if not "email" in errors and not re.match(EMAIL_REGEX, post_Data['email']):
            errors['email'] = "invalid email"

        else:
            if len(self.filter(email=post_Data['email'])) > 1:
                errors['email'] = "email already in use"
        return errors



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()
    def __str__(self):
        return self.email

# Create your models here.

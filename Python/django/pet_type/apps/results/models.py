from __future__ import unicode_literals

from django.db import models

class PettypeManager(models.Manager):
    def type_val(self, post_data):
        results = {'status': True, 'errors': []}
        if len(post_data['add_type']) < 2:
            results['errors'].append('Type must be at least 2 letters long')
        if len(self.filter(name = post_data['add_type'])) > 0:
            results['errors'].append('Type already Exists')
        if len(results['errors']) > 0:
            results['status'] = False
        return results

class Pettype(models.Model):
    name = models.CharField(max_length=100)
    objects = PettypeManager()

class User(models.Model):
    pet = models.ForeignKey(Pettype, related_name = 'pet_type')

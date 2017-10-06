from __future__ import unicode_literals
import datetime
from django.db import models
from ..login_registration.models import User

class Poke(models.Model):
    poked_from = models.ForeignKey(User, related_name = "to")
    poked_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

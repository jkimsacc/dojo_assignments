# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-14 18:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='city',
        ),
        migrations.RemoveField(
            model_name='book',
            name='state',
        ),
    ]

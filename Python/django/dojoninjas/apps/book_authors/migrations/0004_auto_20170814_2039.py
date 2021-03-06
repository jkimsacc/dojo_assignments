# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-14 20:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0003_author_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='like',
            field=models.ManyToManyField(related_name='users', to='book_authors.User'),
        ),
        migrations.AddField(
            model_name='book',
            name='uploaded',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_by', to='book_authors.User'),
            preserve_default=False,
        ),
    ]

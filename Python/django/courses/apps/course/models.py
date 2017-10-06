from __future__ import unicode_literals
import re
from django.db import models

class CourseManager(models.Manager):
    def validate(self, post_Data):
        errors = {}
        if len(self.filter(course_name=post_Data['course_name'])) >= 1:
            errors['course_name'] = "course already in use"
        return errors

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    objects = CourseManager()

from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.contrib.messages import error
from .models import Course

def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request,"course/index.html", context)

def add(request):
    errors = Course.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message)
        print "error"
        return redirect(reverse('index'))

    Course.objects.create(
        course_name = request.POST['course_name'],
        description = request.POST['description'],
    )
    return redirect('/')

def remove(request, course_id):
    course_2_remove = Course.objects.get(id = user_id)
    course_2_remove.delete()
    return redirect('/')
# Create your views here.

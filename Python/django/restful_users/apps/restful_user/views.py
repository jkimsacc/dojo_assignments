from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.contrib.messages import error
from .models import User

#have 7 routes

def index(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, "restful_user/index.html", context)

def new(request):
    return render(request, "restful_user/new_user.html")



def show(request, user_id):
    context ={
        "user": User.objects.get(id = user_id)

    }
    return render(request, "restful_user/user_page.html", context)

def edit(request, user_id):
    context ={
        "user": User.objects.get(id = user_id)
    }
    return render(request, "restful_user/edit_page.html", context)

def create(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message)
        return redirect('/users/new')

    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
    )

    return redirect(reverse("index"))

def destroy(request, user_id):
    user_2_destroy = User.objects.get(id = user_id)
    user_2_destroy.delete()
    return redirect(reverse("index"))

def update(request, user_id):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message)
        return redirect('/users/{}/edit'.format(user_id))

    user = User.objects.get(id = user_id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    #edit db
    return redirect(reverse("index"))

# Create your views here.

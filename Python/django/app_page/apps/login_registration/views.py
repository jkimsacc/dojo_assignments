from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'login_registration/index.html')

def login_registration(request):
    return render(request, 'login_registration/login_registration.html')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result.itteritems():
            messages.error(request, err)
        return redirect('/success')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully Logged in!")
    return redirect('/success')

def register(request):
    result = User.objects.validate_register(request.POST)
    if type(result) == list:
        for field, message in result.itteritems():
            messages.error(request, err)
        return redirect('/login_registraion')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect('/success')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/login_registration')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }

    return render(request, 'login_registration/success.html', context)
# Create your views here.

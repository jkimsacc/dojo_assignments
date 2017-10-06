from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from models import User

def index(request):
    return render(request, 'login/index.html')

def register(request):
    return render(request, 'login/register.html')

def register_user(request):
    results = User.objects.registration_validation(request.POST)
    if results['status'] == False:
        for err in results['errors']:
            messages.error(request, err)
        return redirect('/register')
    else:
        user = User.objects.creator(request.POST)
        messages.success(request, 'User has been registered. Login to continue')
    return redirect('/')

def login(request):
    return render(request, 'login/login.html')

def logging(request):
    results = User.objects.login_validation(request.POST)
    if results['status'] == False:
        for err in results['errors']:
            messages.error(request, err)
        return redirect('/')

    request.session['user_id'] = results['user'].id
    request.session['user_f_name'] = results['user'].f_name
    messages.success(request, "Logged in!")
    return redirect('/books')

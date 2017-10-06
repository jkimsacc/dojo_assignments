from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from models import User

def login_registration(request):
    try:
        request.session['user_id']
    except KeyError:
        return render(request, 'login_registration/login_registration.html')
    return redirect('/dashboard')

def login(request):
    results = User.objects.login_val(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request,error)
        return redirect('/login_registration')
    request.session['user_id'] = results['user'].id
    return redirect('/dashboard')

def register(request):
    results = User.objects.register_val(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/login_registration')
    else:
        user = User.objects.create_user(request.POST)
    request.session['user_id'] = user.id
    return redirect('/dashboard')

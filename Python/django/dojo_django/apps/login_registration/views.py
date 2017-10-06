from django.shortcuts import render, redirect
from django.contrib import messages
from models import User


def login_registration(request):
    try:
        request.session['user_id']
    except KeyError:
        return render(request, 'login_registration/login_registration_page.html')
    return redirect('/friends')

def register(request):
    results = User.objects.register_val(request.POST)
    if results['status'] == False:
        for err in results['errors']:
            messages.error(request, err)
        return redirect('/login_registration')
    else:
        user = User.objects.create_user(request.POST)
    request.session['user_id'] = user.id
    return redirect('/friends')

def login(request):
    results = User.objects.login_val(request.POST)
    if results['status'] == False:
        for err in results['errors']:
            messages.error(request, err)
        return redirect('/login_registration')
    else:
        request.session['user_id'] = results['user'].id
    return redirect('/friends')

def temp_login(request):
    request.session['user_id'] = User.objects.get(name = "Temp Id")
    return redirect('/friends')

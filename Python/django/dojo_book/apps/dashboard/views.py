from django.shortcuts import render, redirect
from ..login_registration.models import User
from models import Poke

# Create your views here.
def dashboard(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    users = User.objects.exclude(id = request.session['user_id'])
    user = User.objects.filter(id = request.session['user_id'])
    pokes = Poke.objects.all()
    context={
    'user' : user,
    'users' : users,
    'pokes' : pokes,
    }
    return render(request, 'dashboard/dashboard.html', context)

def poke(request, poked_id):
    poke = Poke.objects.create()
    return redirect('/dashboard')

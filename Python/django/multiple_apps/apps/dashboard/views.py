from django.shortcuts import render
from ..login_registration.models import User

# Create your views here.
def dashboard(request):
    status = True
    try:
        request.session['user_id']
    except KeyError:
        status = False
    context = {
    'users' : User.objects.all(),
    'logged_in' : status,
    }
    return render(request, 'dashboard/dashboard.html', context)

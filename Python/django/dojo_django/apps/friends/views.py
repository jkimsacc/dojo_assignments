from django.shortcuts import render, redirect
from ..login_registration.models import User

# Create your views here.
def friends(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context ={
    'user' : user,
    'my_friends' : user.friends.all(),
    'others' :  User.objects.exclude(id=user.id).exclude(friends = user),
    }
    return render(request, 'friends/friends.html', context)

def add(request, friend_id):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    friend = User.objects.get(id = friend_id)
    user = User.objects.get(id = request.session['user_id'])
    user.friends.add(friend)
    user.save()
    return redirect('/friends')

def remove(request, friend_id):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    friend = User.objects.get(id = friend_id)
    user = User.objects.get(id = request.session['user_id'])
    user.friends.remove(friend)
    user.save()
    return redirect('/friends')

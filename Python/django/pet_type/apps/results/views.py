from django.shortcuts import render, redirect
from models import Pettype, User
from django.contrib import messages
from django.db.models import Count

# Create your views here.
def add(request):
    context = {
    'options' : Pettype.objects.all(),
    }
    return render(request, 'results/index.html', context)

def process(request):
    if request.POST['add_type'] == "" and request.POST['type'] == "":
        return redirect('/')
    elif request.POST['add_type'] != "" and request.POST['type'] == "":
        results = Pettype.objects.type_val(request.POST)
        if results['errors'] == False:
            messages.error(request, error)
            return redirect('/')
        else:
            new_type = Pettype.objects.create(name = request.POST['add_type'])
            new_user = User.objects.create(pet = new_type)
            return redirect('/results')
    elif request.POST['add_type'] == "" and request.POST['type'] != "":
        User.objects.create(pet = Pettype.objects.get(name = request.POST['type']))
        return redirect('/results')
    return redirect('/')

def results(request):
    obj = Pettype.objects.values('name').annotate(count=Count('name'))
    print obj
    context = {
    'pet_types' : obj,
    'users' : User.objects.all(),
    'pets' : Pettype.objects.all(),
    }
    return render(request, 'results/results_page.html', context)

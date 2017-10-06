from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, redirect
import random

def index(request):
    try:
        request.session['gold']
    except KeyError:
        request.session['gold'] = 0
    return render(request, "ninjago/index.html")

def process(request, building_type):
    try:
        request.session['logs']
    except KeyError:
        request.session['logs'] = []

    if building_type == 'farm':
        earn = random.randrange(10,21)
    elif building_type == 'cave':
        earn = random.randrange(5,11)
    elif building_type == 'house':
        earn = random.randrange(2,6)
    elif building_type == 'casino':
        earn = random.randrange(-50, 51)

    request.session['gold'] += earn


    request.session['logs'].append(earn)

    return redirect ('/')
# Create your views here.

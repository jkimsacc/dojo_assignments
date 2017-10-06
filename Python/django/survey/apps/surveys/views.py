from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    print request.method
    return render(request, 'surveys/index.html')

# Create your views here.
def results(request):
    print request.method
    if request.method == "POST":
        print "dsf"
        try:
            request.session['counter']
        except:
            request.session['counter'] = 0
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['stack'] = request.POST['stack']
        request.session['comment'] = request.POST['comment']
        request.session['counter'] += 1
        return render(request, 'surveys/results.html')

    return render(request, 'surveys/results.html')

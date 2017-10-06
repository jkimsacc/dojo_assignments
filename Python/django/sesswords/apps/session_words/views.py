from django.shortcuts import render, HttpResponse, redirect

def index():
    print "index loaded"
    return render('session_words/index.html')
# Create your views here.

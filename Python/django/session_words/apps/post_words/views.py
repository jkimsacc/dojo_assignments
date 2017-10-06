from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, 'post_words/index.html')

def add_word(request):
    words = {}
    for key, value in request.POST.iteritems():
        if key != "csrfmiddlewaretoken" and key != "big":
            words[key] = value
        elif key == "big":
            words['big'] = "big"
        else:
            words['big'] = ""
    words['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
    try:
        request.session['word_list']
    except KeyError:
        request.session['word_list'] = []

    temp_list = request.session['word_list']
    temp_list.append(words)
    request.session['new_list'] = temp_list

    return redirect('/')

def reset(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

from __future__ import unicode_literals
from items import items
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if "last_transaction" in request.session.keys():
        del request.session['last_transaction']
    context = {
        "items":items
    }
    return render(request, "amazon/index.html", context)

def buy(request, item_id):

    for item in items:
        if item['id'] == int(item_id):
            amount_charged = item['price'] * int(request.POST['quantity'])
    try:
        request.session['total_charged']
    except KeyError:
        request.session['total_charged'] = 0

    try:
        request.session['total_items']
    except KeyError:
        request.session['total_items'] = 0

    request.session['total_charged'] += amount_charged
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['last_transaction'] = amount_charged
    return redirect('/checkout')

def checkout(request):
    return render(request, 'amazon/buy.html')
# Create your views here.

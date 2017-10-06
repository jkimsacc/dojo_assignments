from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..login.models import User
from models import *

def user_page(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect['/']
    try:
        request.session['logs']
    except KeyError:
        request.session['logs'] = []

    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'add_book/page.html', context)

def add_book_review(request):
    return render(request, 'add_book/add_book.html')

def adding_book_review_author(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect['/']
    print request.session['user_id']
    print type(request.session['user_id'])
    print request.POST['rating']
    user_id = request.session['user_id']
    if request.POST['author'] == 'select' and not request.POST['author_input']:
        message.error(request, "Put Author")
    if request.POST['author_input']:
        Author.objects.create(
            author_name = request.POST['author_input']
        )
        author = Author.objects.get(author_name = request.POST['author_input'])
    else:
        author = Author.objects.get(author_name = request.POST['author'])
    book = Book.objects.create(
        book_title = request.POST['title'],
        author = author,
    )

    Review.objects.create(
        review = request.POST['review'],
        rating = request.POST['rating'],
        book = Book.objects.get(book_title = request.POST['title']),
        user = User.objects.get(id = user_id),
    )
    return redirect('/books/{}'.format(book.id))

def book_page(request, book_id):
    context ={
    'books': Book.objects.get(id = book_id),
    'reviews' : Review.objects.filter(book = Book.objects.get(id = book_id)),
    }
    return render(request, 'add_book/book_page.html', context)

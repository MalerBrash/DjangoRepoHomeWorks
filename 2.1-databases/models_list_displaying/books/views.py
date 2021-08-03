from django.shortcuts import render, redirect
from  books.models import Book


def DatePaginator(request, value):
    resp = {}
    next_req = Book.objects.filter(pub_date__gt=value).order_by('pub_date')
    prev_req = Book.objects.filter(pub_date__lt=value).order_by('-pub_date')
    try:
        resp['next_page'] = next_req[0].pub_date
    except:
        resp['next_page'] = 0
    try:
        resp['prev_page'] = prev_req[0].pub_date
    except:
        resp['prev_page'] = 0
    return resp

def home_view(request):
    return redirect('books')

def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)

def book_view(request, value):
    template = 'books/book_list.html'

    context = {'books': Book.objects.filter(pub_date=value),
               'pagination': DatePaginator(request, value)
               }
    return render(request, template, context)

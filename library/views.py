from django.shortcuts import render, get_object_or_404
from .models import Scores, Book

def users(request):
    data = {'users': Scores.objects.all()}
    print(data)
    return render(request, './users.html', data)

def home(request):
    data = {'books': Book.objects.all()}
    return render(request, './home.html', data)

def book(request, id):
    book = get_object_or_404(Book, pk=id)
    data = {'book': book}
    return render(request, './book.html', data)

def not_found_404(request, exception):
    data = {'err': exception}
    return(request, '404.html', data)

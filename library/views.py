from django.shortcuts import render
from django.http import HttpResponse
from .models import books, Book

def home(request):
    data = {'books': Book.objects.all()}
    return render(request, './home.html', data)

def book(request, id):
    return HttpResponse("Book details")

def not_found_404(request, exception):
    pass

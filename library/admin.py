from django.contrib import admin
from .models import Book, Author, Scores

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Scores)

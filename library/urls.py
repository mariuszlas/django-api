from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='library-home'),
    path('users', views.users, name='library-users'),
    path('books/<int:id>', views.book, name='library-books')
]

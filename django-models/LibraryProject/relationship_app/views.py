from django.shortcuts import render
from .models import Book
from .models import Library
# Create your views here

def all_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def library_details(request):
    libraries = Library.objects.all()
    return render(request, 'relationship_app/library_detail.html', {'libraries': libraries})
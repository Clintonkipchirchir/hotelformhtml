from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm

# Create your views here.

@permission_required(('bookshelf.can_edit', 'bookshelf.can_create'), raise_exception=True)
def Editors(request):
    return render(request, 'bookshelf/book_list.html')

@permission_required('bookshelf.can_view', raise_exception=True)
def Viewers(request):
    return render(request, 'bookshelf/book_list.html')

@permission_required(('bookshelf.can_edit', 'bookshelf.can_create', 'bookshelf.can_delete', 'bookshelf.can_view'), raise_exception=True)
def Admins(request):
    return render(request, 'bookshelf/book_list.html')

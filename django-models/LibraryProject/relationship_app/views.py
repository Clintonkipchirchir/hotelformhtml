from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login , logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from .models import UserProfile


# Create your views here

def all_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def library_details(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# create user , login and logout
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('all_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def Login_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('all_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/login.html')

def Logout_user(request):
    logout(request)
    return redirect('all_books')

#create user access control
@user_passes_test(lambda user: user.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(lambda user: user.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda user: user.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

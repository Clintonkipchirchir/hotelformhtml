from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#create user profile model with roles assinged
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return self.user.username


#create user access control
@login_required
@user_passes_test(lambda u: u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin.html')

@login_required
@user_passes_test(lambda u: u.userprofile.role == 'librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian.html')

@login_required
@user_passes_test(lambda u: u.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member.html')

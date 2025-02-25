from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

class librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(library, on_delete=models.CASCADE)
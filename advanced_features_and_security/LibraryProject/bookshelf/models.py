from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser



#create custom user model
class CustomUser(AbstractUser):
    date_of_birth = models.DateField()	
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True)

class CustomUserManager(UserManager):
    pass


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
  
    def __str__(self):
        return self.title


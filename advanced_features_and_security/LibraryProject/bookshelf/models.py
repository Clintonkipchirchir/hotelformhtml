from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser


# Create a custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, date_of_birth, profile_photo, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email is required')
        if not username:
            raise ValueError('The username is required')
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo, 
            **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, date_of_birth, profile_photo, email, password=None, **extra_fields):
        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', True)
        user = self.create_user(
            email=email,
            username=username,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo, 
            **extra_fields)

        user.save()
        return user


#create custom user model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()	
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True)


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
  
    def __str__(self):
        return self.title

#create permission for the users
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('can_view', 'can_view'),
        ('can_create', 'can_create'),
        ('can_edit', 'can_edit'),
        ('can_delete', 'can_delete'),   
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='can_view')
    
    def __str__(self):
        return self.user.username
    


from django.urls import path
from . import views
from .views import library_details, register, Login_user, Logout_user
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('library_details/', views.library_details, name='library_details'),
    path('register/', views.register, name='register'),
    path('login/', views.Login_user, name='login'),
    path('logout/', views.Logout_user, name='logout'),
    path('admin/', views.admin_view, name='admin'),
    path('librarian/', views.librarian_view, name='librarian'),
    path('member/', views.member_view, name='member'),
]


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
    path('admin/add_book/', views.admin_view, name='admin'),
    path('admin/edit_book/', views.admin_view, name='admin'),
    path('admin/delete_book', views.admin_view, name='admin'),
    path('librarian/add_book/', views.librarian_view, name='librarian'),
    path('librarian/edit_book/', views.librarian_view, name='librarian'),
    path('member/add_book/', views.member_view, name='member'),
]


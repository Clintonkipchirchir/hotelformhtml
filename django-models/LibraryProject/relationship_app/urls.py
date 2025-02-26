from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('library_details/', library_details.as_view(), name='library_details'),
]


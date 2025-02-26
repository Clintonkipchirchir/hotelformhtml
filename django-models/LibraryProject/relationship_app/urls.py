from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('library_details/', library_details.as_view(), name='library_details'),
]


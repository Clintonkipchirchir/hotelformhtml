from django.urls import path
from . import views
from .views import library_details, register, loginView, logoutView

urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('library_details/', views.library_details, name='library_details'),
    path('register/', views.register, name='register'),
    path('login/', loginView.as_veiw(template_name="login.html"), name='login'),
    path('logout/', views.logoutView.as_view(template_name="logout.html"), name='logout'),
]


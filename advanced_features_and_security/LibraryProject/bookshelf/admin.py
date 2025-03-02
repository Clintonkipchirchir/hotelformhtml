from django.contrib import admin


# Register your models here.
from .models import Book
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_of_birth', 'profile_photo')
    list_filter = ('email', 'date_of_birth')
    search_fields = ('email', 'date_of_birth')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
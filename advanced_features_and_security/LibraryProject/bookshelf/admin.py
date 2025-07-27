from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')
    

class CustomUserAdmin(admin.ModelAdmin):
    list_filter = ('email', 'username', 'date_of_birth', 'profile_photo')
    search_fields = ('email', 'username', 'date_of_birth', 'profile_photo')

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)


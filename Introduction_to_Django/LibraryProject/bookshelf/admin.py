from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')
    



admin.site.register(Book, BookAdmin)


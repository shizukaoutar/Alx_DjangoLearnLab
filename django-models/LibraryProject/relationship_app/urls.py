from django.urls import path
from . import views

# App-specific URL patterns
urlpatterns = [
    # Books listing page
    path('', views.list_books, name='list_books'),
    path('books/', views.list_books, name='list_books'),
    
    # Library detail page
    path('library//', views.LibraryDetailView.as_view(), name='library_detail'),
]
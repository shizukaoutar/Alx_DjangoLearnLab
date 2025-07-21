from django.db.models.functions import Log
from django.urls import path, include
from . import views
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from .views import register


# App-specific URL patterns
urlpatterns = [
    # Books listing page
    path('', views.list_books, name='list_books'),
    path('books/', views.list_books, name='list_books'),
    
    # Library detail page
    #path('library//', LibraryDetailView.as_view(), name='library_detail'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),


    # Authentication URLs
    #path('registration/',include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
from django.db.models.functions import Log
from django.urls import path, include
from . import views
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, admin_view, librarian_view, member_view


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

    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),
]
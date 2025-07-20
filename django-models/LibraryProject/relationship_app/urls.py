from django.urls import path, include
from . import views
from .views import list_books, LibraryDetailView
from .views import SignUpView
from django.contrib.auth.views import LoginView, TemplateView


# App-specific URL patterns
urlpatterns = [
    # Books listing page
    path('', views.list_books, name='list_books'),
    path('books/', views.list_books, name='list_books'),
    
    # Library detail page
    #path('library//', LibraryDetailView.as_view(), name='library_detail'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),


    # Authentication URLs
    path('registration/',include('django.contrib.auth.urls')),
    path('registration/login/', LoginView.as_view(template_name='relationship_app/registration/login.html'), name='login'),
    path('registration/register/', SignUpView.as_view(template_name='relationship_app/registration/register.html'), name='register'),
    path('registration/logout/', TemplateView.as_view(template_name='relationship_app/registration/logout.html'), name='logout'),
]
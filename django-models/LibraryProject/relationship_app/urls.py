from django.urls import path
from . import views

urlpatterns = [
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('books/', views.book_list, name='book_list'),
]
from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [rest_framework.DjangoFilterBackend, rest_framework.SearchFilter, rest_framework.OrderingFilter]
    filterset_fields = ['author', 'publication_year']
    search_fields = ['title', 'author__name']

    ordering_fields = ['publication_year']
    ordering = ['publication_year'] #default

    pagination_class = PageNumberPagination
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer   
    permission_classes = [IsAuthenticated]

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]



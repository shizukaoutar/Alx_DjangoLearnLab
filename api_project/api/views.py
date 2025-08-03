from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, viewsets, permissions

# Create your views here.
class BookList(rest_framework.generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [rest_framework.permissions.IsAuthenticated, rest_framework.permissions.IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return super().get_permissions()


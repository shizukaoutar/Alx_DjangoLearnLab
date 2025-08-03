from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(rest_framework.generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
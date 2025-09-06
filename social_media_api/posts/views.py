from rest_framework import permissions, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# Create your views here.
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at']
    pagination_class = PageNumberPagination

    def create(self, serializer):   
        serializer.save(author=self.request.user)
        return super().create(serializer)
    

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = PageNumberPagination


"""     def create(self, serializer):   
        comment = serializer.save(author=self.request.user)
        post = comment.post

        if post.author != self.request.user:
            Notification.objects.create(
                to_user=post.author,
                from_user=self.request.user,
                post=post,
                verb=f"{self.request.user} commented on your post",
                notification_type='comment',
                target=post 
            ) """
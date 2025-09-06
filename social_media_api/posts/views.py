from rest_framework import permissions, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment, Like
from notifications.models import Notification
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
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


    def create(self, serializer):   
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
            )



class FeedView(ListView):
    serializer_class = PostSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')




@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])

def like_post(request, post_id):
    post = generics.get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if created:
        Notification.objects.create(
            to_user=post.author,
            from_user=request.user,
            post=post,
            verb=f"{request.user} liked your post",
            notification_type='like',
            target=post 
        )

        return Response({"message": "Post liked successfully"}, status=status.HTTP_200_OK)
    else:
        like.delete()
        return Response({"message": "Post unliked successfully"}, status=status.HTTP_200_OK)
    

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])

def unlike_post(request, post_id):
    post = generics.get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(user=request.user, post=post)
    if like.exists():
        like.delete()
        return Response({"message": "Post unliked successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Post not liked"}, status=status.HTTP_400_BAD_REQUEST)
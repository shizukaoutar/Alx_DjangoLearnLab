from rest_framework.routers import DefaultRouter
from .views import PostView, CommentView, like_post, unlike_post, FeedView
from django.urls import path, include


router = DefaultRouter()
router.register('posts', PostView)
router.register('comments', CommentView)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),

    path('posts/<int:pk>/like/', like_post, name='like-post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike-post'),
]
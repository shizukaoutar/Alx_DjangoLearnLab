from rest_framework.routers import DefaultRouter
from .views import PostView, CommentView
from django.urls import path, include


router = DefaultRouter()
router.register('posts', PostView)
router.register('comments', CommentView)

urlpatterns = [
    path('', include(router.urls)),
]
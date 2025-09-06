from django.urls import path
from .views import RegisterView, LoginView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('follow-user/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow-user/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
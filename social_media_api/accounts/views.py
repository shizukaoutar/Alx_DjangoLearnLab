from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .models import CustomUser
from .serializers import CustomUserSerializer, LoginSerializer




class RegisterView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        login(request, user)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
        
    

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, user_id):
        try:
            users = CustomUser.objects.all()
            user_to_follow = users.get(id=user_id)

            if request.user != user_to_follow:
                request.user.following.add(user_to_follow)
                return Response({"message": "User followed successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)



class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, user_id):
        try:
            users = CustomUser.objects.all()
            user_to_unfollow = users.get(id=user_id)

            if request.user != user_to_unfollow:
                request.user.following.remove(user_to_unfollow)
                return Response({"message": "User unfollowed successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "You cannot unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)




from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['author', 'post', 'content', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'created_at', 'updated_at', 'comments']  


    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


        

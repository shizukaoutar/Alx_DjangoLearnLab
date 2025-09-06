
from posts.serializers import PostSerializer
from posts.models import Post





class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    target = serializers.StringRelatedField()
    

    class Meta:
        model = Notification
        fields = '__all__'


    def get_target(self, obj):
        if isinstance(obj.target, Post):
            return PostSerializer(obj.target).data
        return None
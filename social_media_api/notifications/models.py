from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actor')
    verb = models.CharField(max_length=255)
    target = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='target', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.actor} - {self.verb} - {self.target}"
        


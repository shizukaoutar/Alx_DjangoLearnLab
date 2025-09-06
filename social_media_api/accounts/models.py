from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    followers = models.ManyToManyField('self', related_name='following', blank=True, symmetrical=False)

    def __str__(self):
        return self.username
        
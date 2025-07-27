from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

    

    def __str__(self):
        return self.username

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, date_of_birth, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')
        if not date_of_birth:
            raise ValueError('The Date of Birth field must be set')

        user = self.model(email=email, username=username, date_of_birth=date_of_birth)

        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, username, date_of_birth, password=None):
        user = self.create_user(email, username, date_of_birth, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user
        
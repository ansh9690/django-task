from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile/")
    phone_no = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    unique_id = models.CharField(max_length=8)

    def __str__(self):
        return self.user.username

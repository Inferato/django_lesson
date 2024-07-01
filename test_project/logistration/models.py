from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model

# User = get_user_model()


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)

class UserProfile(models.Model):
    bio = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class ActivityLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, blank=True, null=True)
    action = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

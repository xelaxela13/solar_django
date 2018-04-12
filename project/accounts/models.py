from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    location = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=15, blank=True)


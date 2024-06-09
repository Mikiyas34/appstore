from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class User(AbstractUser):
    ROLE_CHOICES = [
        ("Admin", "Admin"),
        ("User", "User")
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="User", blank=False, null=False) 
    
    def __str__(self) -> str:
        return self.username
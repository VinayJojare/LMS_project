from django.db import models 
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('parent', 'Parent')
    ]
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username

    # Add related_name to avoid conflicts
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_users",  # Custom related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_users_permissions",  # Custom related name
        blank=True
    )

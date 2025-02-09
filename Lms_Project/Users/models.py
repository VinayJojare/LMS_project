from django.db import models
from LMS.models import CustomUser
from django.core.exceptions import ValidationError
# Teacher


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.user.role != 'teacher':
            raise ValidationError(
                "Only users with the role 'teacher' can be assigned as a Teacher.")
        super().save(*args, **kwargs)
# ------------------------------------------------------
# Student Model:


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    grade = models.CharField(max_length=50)
    parent = models.ForeignKey(
        'Parent', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username
# -----------------------------------------------------------
# Parent Model :


class Parent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.PositiveBigIntegerField()

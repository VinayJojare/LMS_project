from django.db import models
from Users.models import Student

# Attendance Model:
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.BooleanField(default=False)
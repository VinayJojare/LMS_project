from django.db import models
from Users.models import Teacher

class Note(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='notes/')
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)


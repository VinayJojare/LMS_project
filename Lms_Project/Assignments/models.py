from django.db import models
from Users.models import Teacher, Student

# Assignment Model:
class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='assignments/')
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        # Ensure the teacher is set before saving
        if not self.teacher:
            raise ValueError("A teacher must be assigned to the assignment.")
        super().save(*args, **kwargs)



class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submission/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    graded = models.BooleanField(default=False)

    

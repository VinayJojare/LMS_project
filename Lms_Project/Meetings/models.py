from django.db import models 
from Users.models import Teacher

# LiveMeeting Model:
class LiveMeeting(models.Model):
    topic = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    meeting_link = models.URLField()
    scheduled_time = models.DateTimeField()
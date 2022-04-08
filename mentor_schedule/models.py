from django.db import models
import uuid
# Create your models here.
class MentorSchedule(models.Model):
  id = models.UUIDField(primary_key= True, default= uuid.uuid4, editable=False, max_length = 32)
  title = models.CharField(max_length=100, null=True)
  allDay = models.BooleanField()
  endDate = models.DateTimeField()
  rRule = models.CharField(max_length=100, null=True)
  startDate = models.DateTimeField()

  
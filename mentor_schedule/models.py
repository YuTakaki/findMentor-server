from django.db import models
from django.db.models.deletion import CASCADE
import uuid
from account.models import User

# Create your models here.
class MentorSchedule(models.Model):
  id = models.UUIDField(primary_key= True, default= uuid.uuid4, editable=False, max_length = 32)
  title = models.CharField(max_length=100, null=True)
  allDay = models.BooleanField()
  endDate = models.DateTimeField()
  rRule = models.CharField(max_length=100, null=True)
  startDate = models.DateTimeField()
  user = models.ForeignKey(User, related_name='mentor_schedule', on_delete=CASCADE)


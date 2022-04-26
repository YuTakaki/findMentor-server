from django.db import models
from account.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Schedule(models.Model):
  id = models.AutoField(primary_key=True)
  startDate = models.DateTimeField()
  endDate = models.DateTimeField()
  mentor = models.ForeignKey(User, related_name='mentor', on_delete=CASCADE)
  student = models.ForeignKey(User, related_name='student', on_delete=CASCADE)
  title = models.CharField(max_length=255)
  notes = models.TextField(null=True)
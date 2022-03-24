from django.db import models
from django.db.models.deletion import CASCADE

from account.models import User

# Create your models here.
class Skills(models.Model):
  user = models.ForeignKey(User, related_name='skills', on_delete=CASCADE)
  skill = models.CharField(max_length=100)
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=32)
  username = models.CharField(max_length=100, unique=True)
  email = models.CharField(max_length=100, unique=True)
  password = models.CharField(max_length=10000)
  account_type = models.CharField(max_length=20)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=200)
  date_joined = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.username
  

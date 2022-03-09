from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User():
  username = models.CharField(max_length=100)
  password = models.CharField(max_length=None)
  account_type = models.CharField(max_length=20)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=200)
  date_joined = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.username
  

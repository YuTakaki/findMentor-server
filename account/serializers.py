from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'username',
      'password',
      'first_name',
      'last_name',
      'email',
      'account_type',
    ]
    extra_kwargs = {
      "id": {
        "read_only": True
      },
      "password" : {
        "write_only" : True,
      }
    }
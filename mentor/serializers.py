from rest_framework import serializers
from account.models import User

class MentorSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    extra_kwargs = {
      'password' : {
        'write_only': True
      }
    }
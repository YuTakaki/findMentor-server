from rest_framework import serializers
from account.models import User

class MentorSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'id',
      'username',
      'first_name',
      'last_name',
      'email',
      'account_type',
      'job_position',
      'pay_rate',
      'bio',
      'profile_img'
    ]
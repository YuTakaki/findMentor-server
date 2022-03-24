from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'id',
      'username',
      'password',
      'first_name',
      'last_name',
      'email',
      'account_type',
      'job_position',
      'pay_rate',
      'bio',
      'profile_img'
    ]
    extra_kwargs = {
      "id": {
        "read_only": True
      },
      "password" : {
        "write_only" : True,
      },
      "job_position" : {
        "read_only" : True,
      },
      "pay_rate" : {
        "read_only" : True,
      },
      "bio" : {
        "read_only" : True,
      },
      "profile_img" : {
        "read_only" : True,
      }
    }
  def create(self, validated_data):
    password = validated_data.pop('password')
    instance = self.Meta.model(**validated_data)
    if password is not None:
      instance.set_password(password)
      instance.save()

    return instance


class LoginSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'email',
      'password',
    ]

class UserInformationSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'job_position',
      'profile_img',
      'bio',
    ]
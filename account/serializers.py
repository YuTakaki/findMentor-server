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
    ]
    extra_kwargs = {
      "id": {
        "read_only": True
      },
      "password" : {
        "write_only" : True,
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
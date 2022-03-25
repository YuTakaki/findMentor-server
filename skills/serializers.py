from rest_framework import serializers
from .models import Skills
class UserSkillSerializer(serializers.ModelSerializer):
  class Meta:
    model = Skills
    fields = ['skill']
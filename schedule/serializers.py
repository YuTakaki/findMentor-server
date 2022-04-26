from rest_framework import serializers
from .models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Schedule
    fields = '__all__'
    extra_kwargs = {
      'id' : {
        'read_only': True
      },
      'mentor' : {
        'read_only': True
      },
      'student' : {
        'read_only': True
      },
    }
from rest_framework import serializers
from mentor_schedule.models import MentorSchedule

class MentorScheduleSerializer(serializers.ModelSerializer):
  class Meta:
    model = MentorSchedule
    fields = '__all__'
    extra_kwargs = {
      'user' : {
        'read_only': True
      }
    }
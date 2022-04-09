from flask import request
from rest_framework import generics
from rest_framework.response import Response
from mentor_schedule.serializers import MentorScheduleSerializer
from mentor_schedule.models import MentorSchedule

# Create your views here.
class MentorScheduleView(generics.GenericAPIView):
  serializer_class = MentorScheduleSerializer

  def get(self, request):
    schedule = MentorSchedule.objects.filter(user=request.user)
    serialize = self.get_serializer(schedule, many=True)
    return Response(serialize.data)
  
  def post(self, request):
    serialize = self.get_serializer(data=request.data)
    serialize.is_valid(raise_exception=True)
    serialize.save(user=request.user)
    return Response(serialize.data)
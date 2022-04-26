from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.models import User
from .models import Schedule
from .serializers import ScheduleSerializer
from django.db.models import Q

# Create your views here.
@api_view(['GET'])
def getScheduleView(request):
  schedule = Schedule.objects.filter(Q(mentor=request.user) | Q(student=request.user))
  serialize = ScheduleSerializer(schedule, many=True)
  return Response(serialize.data)

@api_view(['POST'])
def saveScheduleView(request, id):
  mentor = User.objects.filter(id=id).first()
  student = request.user
  serialize = ScheduleSerializer(data=request.data)
  serialize.is_valid(raise_exception=True)
  serialize.save(student=student, mentor=mentor)
  return Response(serialize.data)
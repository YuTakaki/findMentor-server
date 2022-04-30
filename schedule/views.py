from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.models import User
from mentor_schedule.models import MentorSchedule
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
  mentorSched = MentorSchedule.objects.filter(id=request.data.get("id")).first()
  mentorSched.exDate = ('' if mentorSched.exDate == None else mentorSched.exDate) + ', ' + request.data.get("startDate")
  mentorSched.save()
  return Response(serialize.data)
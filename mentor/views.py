from math import inf
from django.shortcuts import render
from rest_framework import generics
from account.models import User
from .serializers import MentorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from django.db.models.functions import Concat
from django.db.models import Value
# Create your views here.
class MentorView(generics.GenericAPIView):
  serializer_class = MentorSerializer
  
  def get(self, request):
    q = request.query_params.get('q')
    if q is not None:
      q_array = q.split(' ')
      print(q_array)
      mentors = User.objects.annotate(
        search=Concat('first_name', Value(' '), 'last_name')).filter(Q(account_type= 'mentor') &
       (Q(search__icontains = q) | Q(skills__skill = q) | Q(username__icontains = q) | Q(skills__skill__in = q_array))).distinct()
    else:
      mentors = User.objects.filter(account_type='mentor')
    serialize = self.get_serializer(mentors, many=True)
    return Response({
      'mentors': serialize.data
    })

@api_view(['GET'])
def getMentorView(request, pk):
  mentor = User.objects.filter(id=pk).first()
  serialize = MentorSerializer(mentor)
  return Response(serialize.data)


@api_view(['GET'])
def filterMentorView(request):
  skills = request.query_params.get('skills').split(',')
  min = request.query_params.get('min') 
  max = request.query_params.get('max')
  if skills[0] != '':
    mentors = User.objects.filter(account_type='mentor', skills__skill__in = skills)
  else:
    mentors = User.objects.filter(account_type='mentor')
  if min != '' and max != '':
    mentors = mentors.filter(pay_rate__gte = min, pay_rate__lte= max)
  elif min == '' and max != '':
    mentors = mentors.filter(pay_rate__lte= max)
  elif min != '' and max == '':
    mentors = mentors.filter(pay_rate__gte= min)
  serialize = MentorSerializer(mentors.distinct(), many=True)
  return Response({
    'mentors': serialize.data
  })
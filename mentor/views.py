from math import inf
from django.shortcuts import render
from rest_framework import generics
from account.models import User
from .serializers import MentorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
class MentorView(generics.GenericAPIView):
  serializer_class = MentorSerializer

  def get(self, request):
    mentors = User.objects.filter(account_type='mentor')
    serialize = self.get_serializer(mentors, many=True)
    return Response({
      'mentors': serialize.data
    })
    
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
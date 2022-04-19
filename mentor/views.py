from django.shortcuts import render
from rest_framework import generics
from account.models import User
from .serializers import MentorSerializer
from rest_framework.response import Response
# Create your views here.
class MentorView(generics.GenericAPIView):
  serializer_class = MentorSerializer

  def get(self, request):
    mentors = User.objects.filter(account_type='mentor')
    serialize = self.get_serializer(mentors, many=True)
    return Response({
      'mentors': serialize.data
    })
    
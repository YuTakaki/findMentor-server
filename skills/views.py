from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSkillSerializer
from .models import Skills

# Create your views here.
class UserSkillsView(generics.GenericAPIView):

  serializer_class = UserSkillSerializer

  def get(self, request):
    user = request.user
    skills = Skills.objects.filter(user=user)
    serialize = self.serializer_class(skills, many=True)
    return Response({
      'skills': serialize.data
    })

  def post(self, request):
    user = request.user
    Skills.objects.filter(user=user).delete()
    for language in request.data:
      data = {
        'skill' : language
      }
      serializer = self.serializer_class(data=data)
      serializer.is_valid(raise_exception=True)
      serializer.save(user=user)
    return Response(True)
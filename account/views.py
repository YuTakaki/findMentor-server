from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import RegisterSerializer

# Create your views here.
class RegisterView(generics.GenericAPIView):
  serializer_class = RegisterSerializer
  queryset = User.objects.none()

  def post(self, request):
    print(request.data)
    return True
import os
from rest_framework import generics, permissions
from django.db.models import Q
from skills.models import Skills
from .models import User
from .serializers import LoginSerializer, RegisterSerializer, UserInformationSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.decorators import api_view



class RegisterView(generics.GenericAPIView):
  serializer_class = RegisterSerializer
  permission_classes = [
    permissions.AllowAny
  ]
  queryset = User.objects.none()

  def post(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = RefreshToken.for_user(user)
    res = Response({
      'user': serializer.data,
      'token': str(token.access_token),
    })

    res.set_cookie( key="token", value=str(token.access_token), httponly=True)
    return res


def check(user, token=None):
  if user.data.get('account_type') == 'mentor':
      skills = Skills.objects.filter(user=user.data.get('id'))
      error = None
      if user.data.get('job_position') is None:
        error = 0
      elif len(skills) == 0:
        error = 1
      elif user.data.get('pay_rate') is None:
        error = 2
      data = user.data
      return {
        'user': data,
        'error': error,
        'token': token
      }
  data = user.data
  return {
    'user': data,
    'token': token
  }


class LoginView(generics.GenericAPIView):
  serializer_class = LoginSerializer
  queryset = User.objects.none()
  permission_classes = [
    permissions.AllowAny
  ]

  def post(self, request):
    email = request.data.get('usernameOrEmail')
    password = request.data.get('password')
    user = User.objects.filter(Q(email = email) | Q(username = email)).first()
    if user is None:
      raise AuthenticationFailed({
        'error' : {
          'usernameOrEmail' : 'account does not exist'
        }
      })
    if not user.check_password(password):
      raise AuthenticationFailed({
        'error' : {
          'password' : 'password is incorrect'
        }
      })
    
    token = RefreshToken.for_user(user)
    serialize = RegisterSerializer(user)
    data = check(serialize)

    res = Response(data)

    res.set_cookie( key="token", value=str(token.access_token), httponly=True)
    return res



class VerifyTokenView(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def get(self, request):
    serialize_user = self.get_serializer(request.user)
    data = check(serialize_user)
    return Response(data)
    

class UserInformationView(generics.GenericAPIView):
  serializer_class = UserInformationSerializer
  def post(self, request):
    # user = request.user
    user = request.user
    pay_rate = request.data.get('pay_rate')
    if pay_rate is not None:
      user.pay_rate = pay_rate
      error = 2
    else:
      user.job_position = request.data.get('job_position')
      profile_img = request.data.get('profile_img')
      if not isinstance(profile_img, str):
        user.profile_img = profile_img
      user.bio = request.data.get('bio')
      error = None
    user.save()
    serializer = RegisterSerializer(user)

    return Response({
      'user' : serializer.data,
      'error' : error
    })


@api_view(['POST'])
def logoutView(request):
  res = Response()
  res.set_cookie( key="token", value="", httponly=True)
  return res
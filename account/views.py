from rest_framework import generics, permissions
from django.db.models import Q
from .models import User
from .serializers import LoginSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
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

    res = Response({
      'user': serialize.data,
      'token': str(token.access_token)
    })

    res.set_cookie( key="token", value=str(token.access_token), httponly=True)
    return res

class VerifyTokenView(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def get(self, request):
    print(request.user)
    return Response(True)
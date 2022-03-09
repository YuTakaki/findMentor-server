from rest_framework import generics
from .models import User
from .serializers import RegisterSerializer
from rest_framework.response import Response

# Create your views here.
class RegisterView(generics.GenericAPIView):
  serializer_class = RegisterSerializer
  queryset = User.objects.none()

  def post(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({
      'user': serializer.data
    })
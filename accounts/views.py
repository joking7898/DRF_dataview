from django.core import cache
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework import generics # generics class-based view 사용할 계획
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import permission_classes, authentication_classes

# JWT 사용을 위해 필요
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

from .serializers import *
from .models import *


@permission_classes([AllowAny]) #모든 사용자 접근가능
class Login(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        if user['id'] == "None":
            return Response({"message": "fail"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(
            {
                 "id": UserSerializer(
                     user,context=self.get_serializer_context()
                 ).data.get('id'),
                 "token": user['token']
             }
        )
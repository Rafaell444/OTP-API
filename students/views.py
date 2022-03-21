from django.shortcuts import render
from rest_framework.response import Response

from .models import Otp
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
import pyotp


class UserList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Otp.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(profiles=self.request.user)


class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Otp.objects.all()
    serializer_class = UserSerializer


class Generate(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        Parse_Uri = Otp.objects.get(profiles_id=request.user.id, pk=kwargs.get("pk"))
        z = pyotp.parse_uri(str(Parse_Uri))

        answer = z.now()
        return Response({'Your Code:  ': answer})

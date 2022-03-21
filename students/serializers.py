from rest_framework import serializers
from .models import Otp


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otp
        fields = ("pk", "Input_Uri")

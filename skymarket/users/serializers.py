from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone", "id", "email", "image"]


class CurrentUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    phone = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone", "id", "email", "image"]

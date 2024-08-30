from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from accounts.serializers import UserRegisterSerializer, UserSerializer

user_model = get_user_model()


class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = user_model.objects.create_user(username=username, email=email, password=password)
        user.save()
        data = UserSerializer(instance=user).data
        return Response({"message": "User created successfully", 'data': data}, status=status.HTTP_201_CREATED)

from django.shortcuts import render
from rest_framework import viewsets
from users.models import CustomUser
from users.serializers.user import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

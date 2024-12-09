from django.shortcuts import render
from rest_framework import viewsets, permissions
from app_api.models import UserDetail  
from app_api.serializers import UserSerializer 

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  


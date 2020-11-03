from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from profiles.models import UserProfile
from profiles.serializers import UserProfileSerializer


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = UserProfileSerializer

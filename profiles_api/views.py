from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers, models


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ProfileSerializer
    queryset = models.UserProfile.objects.all()

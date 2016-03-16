from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import viewsets

from .serializers import GroupSerializer, UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

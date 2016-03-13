from rest_framework import serializers
from .models import Mimic


class MimicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mimic

from rest_framework import serializers
from .models import Window


class WindowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Window
        fields = ('title', 'slug', 'description')

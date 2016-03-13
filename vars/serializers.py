from django.utils.text import slugify
from rest_framework import serializers
from .models import Device, Var


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        read_only_fields = ('slug',)

    def validate(self, data):
        data['slug'] = slugify(data['name'])
        return data


class VarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Var
        read_only_fields = ('slug',)

    def validate(self, data):
        data['slug'] = slugify(data['name'])
        return data

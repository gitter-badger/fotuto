from django.utils.text import slugify
from rest_framework import serializers
from rest_framework.reverse import reverse as drf_reverse
from .models import Device, Var


class DeviceSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Device
        read_only_fields = ('slug',)

    def validate(self, data):
        data['slug'] = slugify(data['name'])
        return data

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': drf_reverse('device-detail', kwargs={'pk': obj.pk}, request=request),
        }


class VarSerializer(serializers.ModelSerializer):
    var_type_display = serializers.SerializerMethodField()

    class Meta:
        model = Var
        read_only_fields = ('slug', 'var_type_display')

    def validate(self, data):
        data['slug'] = slugify(data['name'])
        return data

    def get_var_type_display(self, obj):
        return obj.get_var_type_display()

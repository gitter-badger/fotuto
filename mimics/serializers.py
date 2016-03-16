from rest_framework import serializers
from rest_framework.reverse import reverse as drf_reverse
from .models import Mimic


class MimicSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Mimic

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': drf_reverse('mimic-detail', kwargs={'pk': obj.pk}, request=request),
        }

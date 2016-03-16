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
            'window': drf_reverse('window-detail', kwargs={'pk': obj.window.pk}, request=request),
            'vars': drf_reverse('var-list', request=request) + '?mimic=%s' % format(obj.pk),
        }

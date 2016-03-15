from django.contrib.auth import get_user_model
from django.utils.text import slugify
from rest_framework import serializers
from rest_framework.reverse import reverse as drf_reverse

from .models import Window


class WindowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Window
        fields = ('title', 'slug', 'description')
        read_only_fields = ('slug',)

    def validate(self, data):
        data['slug'] = slugify(data['title'])
        return data


# TODO: Move this for an app to handle operators, supervisors, etc
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    links = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', 'links')

    def get_links(self, obj):
        request = self.context['request']
        username = obj.get_username()
        return {
            'self': drf_reverse('user-detail', kwargs={User.USERNAME_FIELD: username}, request=request),
        }

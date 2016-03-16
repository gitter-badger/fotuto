from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils.text import slugify
from rest_framework import serializers
from rest_framework.reverse import reverse as drf_reverse

from .models import Window


class WindowSerializer(serializers.ModelSerializer):
    mimics = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='mimic-detail')
    links = serializers.SerializerMethodField()

    class Meta:
        model = Window
        fields = ('id', 'title', 'slug', 'description', 'mimics', 'links')
        read_only_fields = ('slug',)

    def validate(self, data):
        data['slug'] = slugify(data['title'])
        return data

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': drf_reverse('window-detail', kwargs={'pk': obj.pk}, request=request),
        }


# TODO: Move this for an app to handle operators, supervisors, etc
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    groups = serializers.HyperlinkedRelatedField(view_name='group-detail', read_only=True, many=True)
    links = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', 'groups', 'links')

    def get_links(self, obj):
        request = self.context['request']
        username = obj.get_username()
        return {
            'self': drf_reverse('user-detail', kwargs={User.USERNAME_FIELD: username}, request=request),
        }


class GroupSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ('id', 'name', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': drf_reverse('group-detail', kwargs={'pk': obj.pk}, request=request),
        }

from django.utils.text import slugify
from rest_framework import serializers
from .models import Window


class WindowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Window
        fields = ('title', 'slug', 'description')
        read_only_fields = ('slug',)

    def validate(self, data):
        data['slug'] = slugify(data['title'])
        return data

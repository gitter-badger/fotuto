from unittest import TestCase

from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory, force_authenticate

from windows.serializers import WindowSerializer
from windows.views import api_root

User = get_user_model()


class WindowSerializerTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_validate(self):
        """
        Tests that WindowSerializer.validate() adds a slugged
        version of the title attribute to the data
        """
        serializer = WindowSerializer()
        data = serializer.validate({'title': 'A window'})
        self.assertEqual(data, {
            'title': 'A window',
            'slug': 'a-window'
        })

    def test_get_links(self):
        serializer = WindowSerializer(
            data={'title': "Alarm system", 'slug': 'alarm-system'},
            context={'request': self.factory.get('/api/windows/')}
        )
        serializer.is_valid()
        window = serializer.save()
        self.assertDictContainsSubset({'links': {
            'self': 'http://testserver/api/windows/%s/' % window.pk,
            'mimics': 'http://testserver/api/mimics/?window=%s' % window.pk,
            'vars': 'http://testserver/api/vars/?mimic__window=%s' % window.pk,
        }}, serializer.data,)


class APIRootURLTestCase(TestCase):
    def test_api_root_return_correct_urls(self):
        factory = APIRequestFactory()
        user = User.objects.create_user(username='maximo')
        request = factory.get('/api/groups/', )
        force_authenticate(request, user=user)
        response = api_root(request=request)
        expected_json = {
            'windows': 'http://testserver/api/windows/',
            'devices': 'http://testserver/api/devices/',
            'users': 'http://testserver/api/users/',
        }
        self.assertDictEqual(response.data, expected_json)

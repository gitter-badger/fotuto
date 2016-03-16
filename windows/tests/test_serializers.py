from unittest import TestCase
from rest_framework.test import APIRequestFactory

from windows.serializers import WindowSerializer, UserSerializer, GroupSerializer


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
        self.assertDictContainsSubset(
            {'links': {'self': 'http://testserver/api/windows/%s/' % window.pk}}, serializer.data
        )


# TODO: Move this for an app to handle operators, assistants, etc
class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_get_full_name(self):
        """Test if the user's full name is returned"""
        serializer = UserSerializer(
            data={'username': "marti", 'password': '123'},
            context={'request': self.factory.get('/api/users/')}
        )
        valid = serializer.is_valid()
        self.assertTrue(valid, serializer.errors)
        user = serializer.save()
        user.first_name = "Jose"
        user.last_name = "Marti"
        user.save()
        self.assertDictContainsSubset({'full_name': 'Jose Marti'}, serializer.data)

    def test_get_links(self):
        serializer = UserSerializer(
            data={'username': "ernesto", 'password': '123'},
            context={'request': self.factory.get('/api/users/')}
        )
        serializer.is_valid()
        serializer.save()
        self.assertDictContainsSubset({'links': {'self': 'http://testserver/api/users/ernesto/'}}, serializer.data)


class GroupSerializerTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_get_links(self):
        serializer = GroupSerializer(
            data={'name': "assistant"},
            context={'request': self.factory.get('/api/groups/')}
        )
        serializer.is_valid()
        serializer.save()
        self.assertDictContainsSubset({'links': {'self': 'http://testserver/api/groups/1/'}}, serializer.data)

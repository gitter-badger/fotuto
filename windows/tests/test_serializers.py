from unittest import TestCase
from windows.serializers import WindowSerializer, UserSerializer


class WindowSerializerTestCase(TestCase):
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


# TODO: Move this for an app to handle operators, supervisors, etc
class UserSerializerTestCase(TestCase):
    def test_get_full_name(self):
        """Test if the user's full name is returned"""
        serializer = UserSerializer(data={
            'username': "marti",
            'password': '123',
        })
        valid = serializer.is_valid()
        self.assertTrue(valid, serializer.errors)
        user = serializer.save()
        user.first_name = "Jose"
        user.last_name = "Marti"
        user.save()
        self.assertDictContainsSubset({'full_name': 'Jose Marti'}, serializer.data)


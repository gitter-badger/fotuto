from unittest import TestCase
from vars.serializers import DeviceSerializer


class DeviceSerializerTestCase(TestCase):
    def test_validate(self):
        """
        Tests that DeviceSerializer.validate() adds a slugged
        version of the name attribute to the data
        """
        serializer = DeviceSerializer()
        data = serializer.validate({'name': 'A Device'})
        self.assertEqual(data, {
            'name': 'A Device',
            'slug': 'a-device'
        })

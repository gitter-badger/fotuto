from unittest import TestCase
from vars.serializers import DeviceSerializer, VarSerializer


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


class VarSerializerTestCase(TestCase):
    def test_validate(self):
        """
        Tests that VarSerializer.validate() adds a slugged
        version of the name attribute to the data
        """
        serializer = VarSerializer()
        data = serializer.validate({'name': 'Alarm State'})
        self.assertEqual(data, {
            'name': 'Alarm State',
            'slug': 'alarm-state'
        })

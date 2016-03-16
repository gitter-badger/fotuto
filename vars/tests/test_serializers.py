from unittest import TestCase

from rest_framework.test import APIRequestFactory

from vars.models import Device, Var
from vars.serializers import DeviceSerializer, VarSerializer


class DeviceSerializerTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

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

    def test_get_links(self):
        serializer = DeviceSerializer(
            data={'name': "Alarm Controller", 'slug': 'alarm-controller', 'address': '0005'},
            context={'request': self.factory.get('/api/devices/')}
        )
        serializer.is_valid()
        device = serializer.save()
        self.assertDictContainsSubset(
            {'links': {'self': 'http://testserver/api/devices/%s/' % device.pk}}, serializer.data
        )


class VarSerializerTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

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

    def test_return_var_type_human_readable_field(self):
        device = Device.objects.create(name="Temperature Sensor 1", slug="sensor-1", address='0001')
        serializer = VarSerializer(
            data={
            'name': "Temperature 1",
            'var_type': Var.TYPE_ANALOG,
            'device': device.pk,
            },
            context={'request': self.factory.get('/api/vars/')}
        )
        valid = serializer.is_valid()
        self.assertTrue(valid, serializer.errors)
        serializer.save()
        self.assertDictContainsSubset({'var_type_display': 'Analog'}, serializer.data)

    def test_method_get_var_type_display(self):
        device = Device.objects.create(name="Temperature Sensor 2", slug="sensor-2", address='0002')
        serializer = VarSerializer()
        analog_var = Var.objects.create(**{
            'name': "Temperature 2",
            'slug': "t2",
            'var_type': Var.TYPE_ANALOG,
            'device': device,
        })
        self.assertEqual("Analog", serializer.get_var_type_display(analog_var))

        digital_var = Var.objects.create(**{
            'name': "Communication",
            'slug': "c1",
            'var_type': Var.TYPE_DIGITAL,
            'device': device,
        })
        self.assertEqual("Digital", serializer.get_var_type_display(digital_var))

    def test_get_links(self):
        device = Device.objects.create(name="Door 1 Sensor", slug="door-1-sensor", address='0004')
        serializer = VarSerializer(
            data={'name': "Door 1 State", 'slug': 'door-1-state', 'device': device.pk},
            context={'request': self.factory.get('/api/vars/')}
        )
        serializer.is_valid()
        self.assertDictEqual(serializer.errors, {}, serializer.errors)
        var = serializer.save()
        self.assertDictContainsSubset(
            {'links': {'self': 'http://testserver/api/vars/%s/' % var.pk}}, serializer.data
        )

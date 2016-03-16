from unittest import TestCase
from rest_framework.test import APIRequestFactory
from mimics.serializers import MimicSerializer
from windows.models import Window


class DeviceSerializerTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_get_links(self):
        # TODO: `Mimic.window` field should not be required, in fact, `mimics` can creates as a library to select from
        #     it to use in `Windows`, so there should be a m2m field `windows.mimics` instead `mimic.window`
        window = Window.objects.create(title="Security System", slug='security-system')
        serializer = MimicSerializer(
            data={'name': "Alarm Controller", 'slug': 'alarm-controller', 'window': window.pk},
            context={'request': self.factory.get('/api/mimics/')}
        )
        valid = serializer.is_valid()
        self.assertTrue(valid, serializer.errors)
        mimic = serializer.save()
        self.assertDictContainsSubset(
            {'links': {'self': 'http://testserver/api/mimics/%s/' % mimic.pk}}, serializer.data
        )

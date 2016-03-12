from unittest import TestCase
from windows.serializers import WindowSerializer


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

from django.core.urlresolvers import resolve
from rest_framework.test import APITestCase
from windows.models import Window


class WindowAPITestCase(APITestCase):
    def setUp(self):
        self.window_1 = Window.objects.create(
            title="Some Windows",
            slug="some-windows",
            description="The first window"
        )
        self.window_2 = Window.objects.create(
            title="Some Windows 2",
            slug="some-windows-2",
            description="The second window"
        )

    def test_list_windows(self):
        """Test that we can get a list of windows"""
        response = self.client.get('/api/windows/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['title'], "Some Windows")
        self.assertEqual(response.data[1]['description'], 'The second window')

    def test_windows_list_route(self):
        """Test that we've got routing set up for Windows"""
        route = resolve('/api/windows/')
        self.assertEqual(route.func.__name__, 'WindowViewSet')

    def test_create_solo(self):
        """Test that we can create a Window"""
        post_data = {
            'title': "Window 3",
            'slug': 'window-3',
            'description': "The third window",
        }
        response = self.client.post('/api/windows/', data=post_data, format='json')
        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(response.data, post_data)

from django.contrib.auth import get_user_model
from django.core.urlresolvers import resolve
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from windows.models import Window

# TODO: In production API should only available over https
# TODO: Api must require permissions for some actions like POST, PUT, DELETE?

User = get_user_model()


class APIAuthentication(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'user@mail.com', '123')
        self.token = Token.objects.get_or_create(user=self.user)[0].key

    def test_unauthorized_access(self):
        """Users should be authenticated to access to the api"""
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 403, response.data)
        unauthenticated_error = {
            u'detail': u'Authentication credentials were not provided.'
        }
        self.assertDictEqual(response.data, unauthenticated_error)

    def test_obtain_token(self):
        """Registered users can request for a token"""
        user2 = User.objects.create_user('user2', 'user2@mail.com', '123')
        response = self.client.post('/api-token-auth/', {'username': user2.username, 'password': '123'})
        self.assertEqual(response.status_code, 200, response.data)
        self.assertTrue('token' in response.data)
        # TODO: Test for not empty or null token value

    def test_authorization(self):
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        response = self.client.get('/api/', {}, **header)
        self.assertEqual(response.status_code, 200, "REST token-auth failed")


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
        self.user = User.objects.create_user('user', 'user@mail.com', '123')
        self.token = Token.objects.get_or_create(user=self.user)[0].key
        self.auth_header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}

    def test_list_windows(self):
        """Test that we can get a list of windows"""
        response = self.client.get('/api/windows/', {}, **self.auth_header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['title'], "Some Windows")
        self.assertEqual(response.data[1]['description'], 'The second window')

    def test_windows_list_route(self):
        """Test that we've got routing set up for Windows"""
        route = resolve('/api/windows/')
        self.assertEqual(route.func.__name__, 'WindowViewSet')

    def test_unauthenticated_cant_create_window(self):
        """Test that unauthenticated user can't create a Window"""
        post_data = {
            'title': "Window 3",
            'slug': 'window-3',
            'description': "The third window",
        }
        response = self.client.post('/api/windows/', data=post_data, format='json')
        self.assertEqual(response.status_code, 403, response.data)
        unauthenticated_error = {
            u'detail': u'Authentication credentials were not provided.'
        }
        self.assertDictEqual(response.data, unauthenticated_error)

    def test_create_window(self):
        """Test that we can create a Window"""
        post_data = {
            'title': "Window 3",
            'slug': 'window-3',
            'description': "The third window",
        }
        response = self.client.post('/api/windows/', data=post_data, format='json', **self.auth_header)
        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(response.data, post_data)

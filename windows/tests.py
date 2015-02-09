from django.core.urlresolvers import resolve
from django.test import TestCase
from windows.views import WindowDetailView


class HomePageTest(TestCase):
    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertTrue(found.func, WindowDetailView)
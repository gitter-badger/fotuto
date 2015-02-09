from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from windows.views import WindowDetailView


class HomePageTest(TestCase):
    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertTrue(found.func, WindowDetailView)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        request.method = 'GET'
        generic_window_view = WindowDetailView()
        generic_window_view.request = request
        response = generic_window_view.dispatch(request)
        self.assertEqual(response.status_code, 200)
        expected_html = render_to_string('windows/window_detail.html')
        self.assertEqual(response.rendered_content.decode(), expected_html)
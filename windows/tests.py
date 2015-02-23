from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.views.generic import CreateView
from windows.models import Window
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


class WindowModelTest(TestCase):

    # TODO: Inherit from ModelTestHelper

    def test_saving_and_retrieving_windows(self):
        Window.objects.create(title="First Window Title", slug="window1")
        Window.objects.create(title="Second Window Title", slug="window2")

        saved_windows = Window.objects.all()
        self.assertEqual(saved_windows.count(), 2)

        first_saved_window = saved_windows[0]
        second_saved_window = saved_windows[1]
        self.assertEqual(first_saved_window.title, "First Window Title")
        self.assertEqual(second_saved_window.title, "Second Window Title")


class WindowAddTest(TestCase):

    def test_add_url_resolves_to_create_view(self):
        found = resolve('/windows/add/')
        self.assertTrue(found.func, CreateView)
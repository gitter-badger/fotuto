from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.views.generic import CreateView
from fotutils.tests import ModelTestHelper
from windows.forms import WindowForm
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


class WindowModelTest(ModelTestHelper):

    # TODO: Inherit from ModelTestHelper

    def test_saving_and_retrieving_windows(self):
        win1 = {'title': "First Window Title", 'slug': 'win1'}
        win2 = {'title': "Second Window Title", 'slug': 'win2'}
        self.check_saving_and_retrieving_objects(model=Window, obj1_dict=win1, obj2_dict=win2)

    def test_require_slug(self):
        self.check_require_field(model=Window)

    def test_unique_slug(self):
        self.check_unique_field(model=Window)


class WindowAddTest(TestCase):

    def test_add_url_resolves_to_create_view(self):
        found = resolve('/windows/add/')
        self.assertTrue(found.func, CreateView)

    def test_add_window_returns_correct_html(self):
        request = HttpRequest()
        request.method = 'GET'
        generic_add_window_view = CreateView(model=Window)
        generic_add_window_view.request = request
        response = generic_add_window_view.dispatch(request)
        self.assertEqual(response.status_code, 200)
        expected_html = render_to_string('windows/window_form.html', {'form': WindowForm()})
        self.assertMultiLineEqual(response.rendered_content.decode(), expected_html)
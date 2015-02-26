from django.contrib import messages
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

    def test_add_window_can_save_a_post_request(self):
        self.client.post('/windows/add/', data={'title': 'Window 1 title'})
        self.assertEqual(Window.objects.count(), 1)
        new_window = Window.objects.first()
        self.assertEqual(new_window.title, 'Window 1 title')

    def test_add_window_message(self):
        response = self.client.post('/windows/add/', data={'title': 'Window 1 title'})
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].level_tag, 'success')
        self.assertIn(messages_list[0].message, 'Window was added.')

    def test_add_window_page_redirects_after_POST(self):
        response = self.client.post('/windows/add/', data={'title': 'Window 1 title'})
        self.assertRedirects(response, '/windows/')

    def test_add_window_print_message(self):
        response = self.client.post('/windows/add/', data={'title': 'Window 1 title'})
        response_redirected = self.client.get(response.url)
        self.assertIn('Window was added.', response_redirected.rendered_content)

    def test_autogenerate_slug_field(self):
        window = self.save_window_form(title="Some Window Title")
        self.assertEqual(window.slug, 'some-window-title')

    def test_autogenerate_slug_field_must_be_unique(self):
        window_title = "Unique title"

        win1 = self.save_window_form(title=window_title)
        win2 = self.save_window_form(title=window_title)
        self.assertEqual(win2.slug, '%s-%s' % (win1.slug, win2.pk - 1))

        win3 = self.save_window_form(title=window_title)
        self.assertEqual(win3.slug, '%s-%s' % (win1.slug, win3.pk - 1))

    def save_window_form(self, **window_data):
        """Fill :class:`~window.forms.WindowsForm` with data specified and return instance."""
        window_form = WindowForm(data=window_data)
        return window_form.save()


class WindowListTest(TestCase):

    def test_list_url_resolves_to_list_view(self):
        found = resolve('/windows/')
        self.assertEqual(found.func.func_name, 'ListView')

    def test_uses_template(self):
        response = self.client.get('/windows/')
        self.assertTemplateUsed(response, 'windows/window_list.html')

    def test_displays_all_windows(self):
        Window.objects.create(title="First Window Title", slug="win1")
        Window.objects.create(title="Second Window Title", slug="win2")
        response = self.client.get('/windows/')
        self.assertContains(response, "First Window Title")
        self.assertContains(response, "Second Window Title")
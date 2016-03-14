from django.contrib import messages
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template import RequestContext
from django.template.loader import render_to_string
from django.test import TestCase
from django.utils.datetime_safe import datetime
from windows.forms import WindowForm
from windows.models import Window
from windows.views import WindowDetailView


class HomePageTest(TestCase):
    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func.func_name, 'WindowDefaultView')

    def test_root_no_window_redirect_to_add_window(self):
        response = self.client.post('/')
        self.assertRedirects(response, '/windows/add/')

    def test_root_no_window_message(self):
        response = self.client.post('/')
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].level_tag, 'info')
        self.assertIn("No Windows were found", messages_list[0].message)

    def test_root_display_default_view(self):
        window = Window.objects.create(title="Some Window", slug='win1')
        response = self.client.post('/')
        self.assertRedirects(response, window.get_absolute_url())


class WindowAddTest(TestCase):
    maxDiff = None
    window_add_url = '/windows/add/'

    def test_add_url_resolves_to_create_view(self):
        found = resolve(self.window_add_url)
        self.assertEqual(found.func.func_name, 'WindowCreateView')

    def test_add_page_render_window_form_template(self):
        response = self.client.get(self.window_add_url)
        self.assertTemplateUsed(response, 'windows/window_form.html')

    def test_add_page_uses_window_form(self):
        response = self.client.get(self.window_add_url)
        self.assertIsInstance(response.context['form'], WindowForm)

    def test_add_window_can_save_a_post_request(self):
        self.client.post(self.window_add_url, data={'title': 'Window 1 title'})
        self.assertEqual(Window.objects.count(), 1)
        new_window = Window.objects.first()
        self.assertEqual(new_window.title, 'Window 1 title')

    def test_add_window_message(self):
        response = self.client.post(self.window_add_url, data={'title': 'Window 1 title'})
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].level_tag, 'success')
        self.assertIn(messages_list[0].message, 'Window was added.')

    def test_add_window_page_redirects_after_POST(self):
        response = self.client.post(self.window_add_url, data={'title': 'Window 1 title'})
        self.assertRedirects(response, '/windows/')

    def test_add_window_print_message(self):
        response = self.client.post(self.window_add_url, data={'title': 'Window 1 title'})
        response_redirected = self.client.get(response.url)
        self.assertIn('Window was added.', response_redirected.rendered_content)

    # TODO: Pass this to tests/test_forms.py
    def test_autogenerate_slug_field(self):
        window = self.save_window_form(title="Some Window Title")
        self.assertEqual(window.slug, 'some-window-title')

    # TODO: Pass this to tests/test_forms.py
    def test_autogenerate_slug_field_must_be_unique(self):
        window_title = "Unique title"

        win1 = self.save_window_form(title=window_title)
        win2 = self.save_window_form(title=window_title)
        self.assertNotEquals(win2.slug, win1.slug)

        win3 = self.save_window_form(title=window_title)
        self.assertNotEquals(win3.slug, win1.slug)
        self.assertNotEquals(win3.slug, win2.slug)

    def save_window_form(self, **window_data):
        """Fill :class:`~window.forms.WindowsForm` with data specified and return instance."""
        window_form = WindowForm(data=window_data)
        return window_form.save()


class WindowListTest(TestCase):
    window_list_url = '/windows/'

    def test_list_url_resolves_to_list_view(self):
        found = resolve(self.window_list_url)
        self.assertEqual(found.func.func_name, 'ListView')

    def test_uses_template(self):
        response = self.client.get(self.window_list_url)
        self.assertTemplateUsed(response, 'windows/window_list.html')

    def test_displays_no_windows_message(self):
        response = self.client.get(self.window_list_url)
        self.assertContains(response, "No window found.")

    def test_displays_all_windows(self):
        Window.objects.create(title="First Window Title", slug="win1")
        Window.objects.create(title="Second Window Title", slug="win2")
        response = self.client.get(self.window_list_url)
        self.assertContains(response, "First Window Title")
        self.assertContains(response, "Second Window Title")


class WindowDetailTest(TestCase):
    def setUp(self):
        self.window = Window.objects.create(title="First Window Title", slug="win1")
        # TODO: Add mimics

    def test_details_returns_correct_html(self):
        request = HttpRequest()
        request.method = 'GET'
        generic_window_view = WindowDetailView()
        generic_window_view.request = request
        generic_window_view.kwargs = {'slug': self.window.slug}
        response = generic_window_view.dispatch(request)
        self.assertEqual(response.status_code, 200)
        now = datetime.now().replace(microsecond=0)
        expected_html = render_to_string('windows/window_detail.html', {
            'window': self.window, 'timestamp': now
        }, context_instance=RequestContext(request))
        self.assertEqual(response.rendered_content.decode(), expected_html)
        # Check last update timestamp format
        self.assertContains(response, now.strftime('%Y-%m-%d @ %H:%M:%S'))

    def test_details_url_resolves_to_details_view(self):
        found = resolve(self.window.get_absolute_url())
        self.assertEqual(found.func.func_name, 'WindowDetailView')

    def test_uses_template(self):
        response = self.client.get(self.window.get_absolute_url())
        self.assertTemplateUsed(response, 'windows/window_detail.html')

    def test_displays_window_data(self):
        response = self.client.get(self.window.get_absolute_url())
        self.assertContains(response, self.window.title)
        # TODO: Check mimics and vars

    def test_context_timestamp(self):
        response = self.client.get(self.window.get_absolute_url())
        now = datetime.now().replace(microsecond=0)
        self.assertDictContainsSubset({'timestamp': now}, response.context_data)
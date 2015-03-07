from django.contrib import messages
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.context import RequestContext
from django.template.loader import render_to_string
from django.test import TestCase
from mimics.forms import MimicManageForm
from mimics.models import Mimic
from mimics.views import MimicManageView
from windows.models import Window


class MimicManagementTest(TestCase):
    maxDiff = None

    def setUp(self):
        # a window is required for a mimic
        self.window, create = Window.objects.get_or_create(slug="win1")
        self.manage_mimic_url = '/windows/%s/mimics/manage/' % self.window.slug

    # TODO: Test add vars in mimic
    # TODO: Test template used

    def test_add_url_resolves_to_create_view(self):
        found = resolve(self.manage_mimic_url)
        self.assertTrue(found.func, MimicManageView)

    def test_manage_mimic_returns_correct_html(self):
        request = HttpRequest()
        request.method = 'GET'
        generic_add_var_view = MimicManageView()
        generic_add_var_view.request = request
        generic_add_var_view.kwargs = {'window': self.window.slug}
        response = generic_add_var_view.dispatch(request)
        self.assertEqual(response.status_code, 200)
        expected_html = render_to_string('mimics/mimic_manage_form.html', {
            'form': MimicManageForm(initial={'window': self.window.pk}),
            'window': self.window
        }, context_instance=RequestContext(request))
        self.assertMultiLineEqual(response.rendered_content.decode(), expected_html)

    def test_add_mimic_can_save_a_post_request(self):
        self.client.post(self.manage_mimic_url, data={'window': self.window.pk})
        self.assertEqual(Mimic.objects.count(), 1)
        self.assertEqual(self.window.mimics.count(), 1)
        new_mimic = Mimic.objects.first()
        self.assertEqual(new_mimic.window, self.window)
        self.assertEqual(self.window.mimics.all()[0], new_mimic)

    def test_add_mimic_page_redirects_after_POST(self):
        response = self.client.post(self.manage_mimic_url, data={'window': self.window.pk})
        self.assertRedirects(response, self.manage_mimic_url)

    def test_add_mimic_message(self):
        response = self.client.post(self.manage_mimic_url, data={'window': self.window.pk})
        messages_list = list(messages.get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].level_tag, 'success')
        self.assertIn(messages_list[0].message, 'Mimic was added.')

    def test_add_mimic_print_message(self):
        response = self.client.post(self.manage_mimic_url, data={'window': self.window.pk})
        response_redirected = self.client.get(response.url)
        self.assertIn('Mimic was added.', response_redirected.rendered_content)

    def test_displays_only_mimics_for_that_windows(self):
        # TODO: Implement this with model_formset
        Mimic.objects.create(name='Mimic 1', window=self.window)
        Mimic.objects.create(name='Mimic 2', window=self.window)
        other_window = Window.objects.create(slug="other-win")
        Mimic.objects.create(name='Mimic 3', window=other_window)
        Mimic.objects.create(name='Mimic 4', window=other_window)
        response = self.client.get(self.manage_mimic_url)
        self.assertContains(response, 'Mimic 1')
        self.assertContains(response, 'Mimic 2')
        self.assertNotContains(response, 'Mimic 3')
        self.assertNotContains(response, 'Mimic 4')


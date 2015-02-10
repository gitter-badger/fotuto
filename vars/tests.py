from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from vars.forms import VarForm
from vars.views import VarCreateView


class AddVarTest(TestCase):
    maxDiff = None

    def test_add_var_returns_correct_html(self):
        request = HttpRequest()
        request.method = 'GET'
        generic_add_var_view = VarCreateView()
        generic_add_var_view.request = request
        response = generic_add_var_view.dispatch(request)
        self.assertEqual(response.status_code, 200)
        expected_html = render_to_string('vars/var_form.html', {'form': VarForm()})  # FIXME: Return var form
        self.assertMultiLineEqual(response.rendered_content.decode(), expected_html)
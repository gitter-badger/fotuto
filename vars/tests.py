from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from vars.forms import VarForm
from vars.models import Device
from vars.views import VarCreateView


class AddVarTest(TestCase):
    maxDiff = None

    def test_add_url_resolves_to_create_view(self):
        found = resolve('/vars/add/')
        self.assertTrue(found.func, VarCreateView)

    def test_add_var_returns_correct_html(self):
        request = HttpRequest()
        request.method = 'GET'
        generic_add_var_view = VarCreateView()
        generic_add_var_view.request = request
        response = generic_add_var_view.dispatch(request)
        self.assertEqual(response.status_code, 200)
        expected_html = render_to_string('vars/var_form.html', {'form': VarForm()})  # FIXME: Return var form
        self.assertMultiLineEqual(response.rendered_content.decode(), expected_html)

    def test_autogenerate_slug_field(self):
        var = self.save_var_form(name="Some Var Name")
        self.assertEqual(var.slug, 'some-var-name')

    def test_autogenerate_slug_field_must_be_unique(self):
        var_name = "Unique name"
        var1 = self.save_var_form(name=var_name)
        var2 = self.save_var_form(name=var_name)
        self.assertEqual(var2.slug, '%s-%s' % (var1.slug, var2.pk - 1))
        var3 = self.save_var_form(name=var_name)
        self.assertEqual(var3.slug, '%s-%s' % (var1.slug, var3.pk - 1))

    def save_var_form(self, **var_data):
        """Fill :class:`~var.forms.VarForm` with data specified and return instance."""
        if 'device' not in var_data:
            d, create = Device.objects.get_or_create(name="Device 1", slug="device-1", model="111", address="123")
            var_data['device'] = d.pk
        var_form = VarForm(data=var_data)
        return var_form.save()
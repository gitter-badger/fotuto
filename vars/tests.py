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
        device = Device(name="Device 1", slug="device-1", model="111", address="123")
        device.save()
        var_form = VarForm(data={
            'name': "Some Var Name",
            'device': device.pk,
        })
        self.assertTrue(var_form.is_valid())
        self.assertEqual(var_form.cleaned_data['slug'], 'some-var-name')

    def test_autogenerate_slug_field_must_be_unique(self):
        device = Device(name="Device 1", slug="device-1", model="111", address="123")
        device.save()
        var_data ={
            'name': "Unique name",
            'device': device.pk,
        }
        var1_form = VarForm(var_data)
        var1 = var1_form.save()
        var2_form = VarForm(var_data)
        var2 = var2_form.save()
        self.assertEqual(var2.slug, '%s-%s' % (var1.slug, var2.pk - 1))
        var3_form = VarForm(var_data)
        var3 = var3_form.save()
        self.assertEqual(var3.slug, '%s-%s' % (var1.slug, var3.pk - 1))
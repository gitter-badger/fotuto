from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from vars.forms import VarForm
from vars.models import Device, Var
from vars.views import VarCreateView


class AddVarTest(TestCase):
    maxDiff = None

    def setUp(self):
        # a device is required for a var
        self.device, create = Device.objects.get_or_create(name="Device 1", slug="device-1", model="111", address="123")

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
        expected_html = render_to_string('vars/var_form.html', {'form': VarForm()})
        self.assertMultiLineEqual(response.rendered_content.decode(), expected_html)

    def test_add_var_can_save_a_post_request(self):
        self.client.post('/vars/add/', data={'name': 'Var 1 name', 'device': self.device.pk})
        self.assertEqual(Var.objects.count(), 1)
        new_var = Var.objects.first()
        self.assertEqual(new_var.name, 'Var 1 name')

    def test_add_var_page_redirects_after_POST(self):
        response = self.client.post('/vars/add/', data={'name': 'Var 1 name', 'device': self.device.pk})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/vars/list/')

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
            var_data['device'] = self.device.pk
        var_form = VarForm(data=var_data)
        return var_form.save()


class VarModelTest(TestCase):

    def setUp(self):
        # Var require a device
        self.device, create = Device.objects.get_or_create(name="Device 1", slug="device-1", model="111", address="123")

    def test_saving_and_retrieving_vars(self):
        Var.objects.create(name="First Var Name", slug="var1", device=self.device)
        Var.objects.create(name="Second Var Name", slug="var2", device=self.device)

        saved_vars = Var.objects.all()
        self.assertEqual(saved_vars.count(), 2)

        first_saved_var = saved_vars[0]
        second_saved_var = saved_vars[1]
        self.assertEqual(first_saved_var.name, "First Var Name")
        self.assertEqual(second_saved_var.name, "Second Var Name")


class DeviceModelTest(TestCase):

    def test_saving_and_retrieving_vars(self):
        Device.objects.create(name="First Device Name", slug="dev1")
        Device.objects.create(name="Second Device Name", slug="dev2")

        saved_device = Device.objects.all()
        self.assertEqual(saved_device.count(), 2)

        first_saved_device = saved_device[0]
        second_saved_device = saved_device[1]
        self.assertEqual(first_saved_device.name, "First Device Name")
        self.assertEqual(second_saved_device.name, "Second Device Name")
